from rest_framework import serializers
from chat.models import *
from django.contrib.auth.models import User
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from django.forms import ValidationError
from django.db import connection

class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'date_joined', 'password', 'email', 'jawn_user', )
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('jawn_user',)
        #depth = 1

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError("This email is already used")
        user.set_password(validated_data['password'])
        user.save()
        jawn_user = JawnUser(base_user=user)
        jawn_user.save()
        return user


class JawnUserSerializer(serializers.ModelSerializer):
    base_user = UserSerializer(many=False, read_only=False)

    class Meta:
        model = JawnUser
        fields = ('id', 'profile_pic', 'about_me', 'follows', 'date_of_birth', 'faction',
                  'base_user',
                  'followers')
        #depth = 2

class GetJawnUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = JawnUser
        fields = ('id', 'profile_pic', 'about_me', 'follows', 'date_of_birth', 'faction',
                  'followers')
        #depth = 2

class GetUserSerializer(serializers.ModelSerializer):

    jawn_user = GetJawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'date_joined', 'password', 'email', 'jawn_user', )


class ImageMessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = ImageMessage
        fields = ('id', 'date_posted', 'channel', 'type', 'image_url', 'caption', 'jawn_user', )
        #depth = 1

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        c = ImageMessage.objects.create(channel=validated_data['channel'], image_url=validated_data['image_url'], jawn_user=jawn_user, caption=validated_data['caption'])

        j = ImageMessageSerializer(c, context=self.context)
        json = JSONRenderer().render(j.data)
        message = RedisMessage(json.decode("utf-8"))

        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return c


class TextMessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = TextMessage
        fields = ('id', 'date_posted', 'channel', 'type', 'text', 'jawn_user', )
        #depth = 1

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        c = TextMessage.objects.create(channel=validated_data['channel'], text=validated_data['text'], jawn_user=jawn_user)
        print(validated_data['channel'])

        j = TextMessageSerializer(c, context=self.context)
        json = JSONRenderer().render(j.data)
        message = RedisMessage(json.decode("utf-8"))

        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return c

    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()

        j = TextMessageSerializer(instance, context=self.context)
        json = JSONRenderer().render(j.data)
        message = RedisMessage(json.decode("utf-8"))

        RedisPublisher(facility=instance.channel, broadcast=True).publish_message(message)
        return instance

class LinkMessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = LinkMessage
        fields = ('id',
                  'date_posted',
                  'channel',
                  'type',
                  'text',
                  'image_url',
                  'headline',
                  'organization',
                  'jawn_user',
                  )
        #depth = 1

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        c = LinkMessage.objects.create(channel=validated_data['channel'], text=validated_data['text'], jawn_user=jawn_user, image_url=validated_data['image_url'], headline=validated_data['headline'], organization=validated_data['organization'])
        j = LinkMessageSerializer(c, context=self.context)
        json = JSONRenderer().render(j.data)
        message = RedisMessage(json.decode("utf-8"))
        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return c
        
        
class YouTubeMessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = YouTubeMessage
        fields = ('id',
                  'date_posted',
                  'channel',
                  'type',
                  'text',
                  'name',
                  'youtube_url',
                  'youtube_id',
                  'jawn_user',
                  )
        #depth = 1

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        c = YouTubeMessage.objects.create(channel=validated_data['channel'], text=validated_data['text'], jawn_user=jawn_user, name=validated_data['name'], youtube_url=validated_data['youtube_url'], youtube_id=validated_data['youtube_id'])
        j = YouTubeMessageSerializer(c, context=self.context)
        json = JSONRenderer().render(j.data)
        message = RedisMessage(json.decode("utf-8"))
        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return c


class MessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'date_posted', 'channel', 'jawn_user', )
        depth = 1

    def to_representation(self, value):
        if isinstance(value, TextMessage):
            return TextMessageSerializer(value, context=self.context).to_representation(value)
        if isinstance(value, ImageMessage):
            return ImageMessageSerializer(value, context=self.context).to_representation(value)
        if isinstance(value, LinkMessage):
            return LinkMessageSerializer(value, context=self.context).to_representation(value)
        if isinstance(value, YouTubeMessage):
            return YouTubeMessageSerializer(value, context=self.context).to_representation(value)



class ChannelSerializer(serializers.ModelSerializer):
    # messages = MessageSerializer(many=True, read_only=True,)

    #messages = serializers.SerializerMethodField('get_messages_ordered')

    def get_messages_ordered(self, channel):
        qset = Message.objects.filter(channel=channel).order_by('-date_posted')
        serialized_data = MessageSerializer(qset, many=True, read_only=True, context=self.context)
        return serialized_data.data


    class Meta:
        model = Channel
        fields = ('id', 'name', 'description', 'created', 'creator', )
        #depth = 1



class ChannelListSerializer(serializers.ModelSerializer):



    class Meta:
        model = Channel
        fields =  ('id', 'name', 'description', 'created', 'creator',)
        #depth = 1


class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessageRelationships
        fields = ('id', 'channel', 'user_recipient', 'user_sender', 'channel_name', )



class RegionSerializer(serializers.ModelSerializer):
    total_channels = serializers.SerializerMethodField(read_only=True)
    google_json = JSONSerializerField()

    def get_total_channels(self, data):
        #print(data)
        return None
        #Channel.objects.filter(name_istartswith=)

    def create(self, validated_data):
        instance = Region.objects.create_region(**validated_data)
        print(instance.name)
        return instance

    class Meta:
        model = Region
        fields = ('name', 'coordinates_long', 'coordinates_lat', 'flickr_image', 'flickr_image_large', 'total_channels', 'google_json', )
        read_only_fields = ('total_channels', 'google_json')

class LinkMessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = LinkMessage
        fields = ('id',
                  'date_posted',
                  'channel',
                  'type',
                  'text',
                  'image_url',
                  'headline',
                  'organization',
                  'jawn_user',
                  )
        #depth = 1

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        c = LinkMessage.objects.create(channel=validated_data['channel'], text=validated_data['text'], jawn_user=jawn_user, image_url=validated_data['image_url'], headline=validated_data['headline'], organization=validated_data['organization'])
        j = LinkMessageSerializer(c, context=self.context)
        json = JSONRenderer().render(j.data)
        message = RedisMessage(json.decode("utf-8"))
        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return c