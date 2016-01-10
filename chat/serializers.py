from rest_framework import serializers
from chat.models import *
from django.contrib.auth.models import User
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher

class UserSerializer(serializers.HyperlinkedModelSerializer):
    jawn_user = serializers.HyperlinkedRelatedField(source='jawn_user.id',
                                                    view_name='jawnuser-detail',
                                                    many=False,
                                                    read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'last_login', 'date_joined', 'password', 'email', 'jawn_user')
        extra_kwargs = {'password': {'write_only': True}}
        #depth = 1

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class JawnUserSerializer(serializers.HyperlinkedModelSerializer):
    base_user = User.objects.all()

    class Meta:
        model = JawnUser
        fields = ('id', 'url', 'profile_pic', 'about_me', 'follows', 'date_of_birth', 'sex', 'base_user', 'followers')
        #depth = 2

    # def create(self, validated_data):
    #     # print validated_data['user']['id']
    #     # print validated_data
    #     jawnuser = JawnUser(
    #         base_user=validated_data['user']['id'],
    #         profile_pic=validated_data['profile_pic'],
    #         about_me=validated_data['about_me'],
    #         date_of_birth=validated_data['date_of_birth'],
    #         sex=validated_data['sex'],
    #     )
    #     jawnuser.save()
    #     return jawnuser



class ImageMessageSerializer(serializers.HyperlinkedModelSerializer):
    #jawn_user = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='jawn_user-detail', source='jawn_user.id')

    class Meta:
        model = ImageMessage
        fields = ('date_posted', 'channel', 'type', 'image_url', 'caption', 'jawn_user', 'id', 'url')
        #depth = 1

    def create(self, validated_data):
        c = ImageMessage.objects.create(**validated_data)
        # print c.as_json()
        message = RedisMessage(str(c.as_json()))
        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return ImageMessage(**validated_data)


class TextMessageSerializer(serializers.HyperlinkedModelSerializer):
    #jawn_user = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='jawn_user-detail', source='jawn_user.id')

    class Meta:
        model = TextMessage
        fields = ('date_posted', 'channel', 'type', 'text', 'jawn_user', 'id', 'url')
        #depth = 1

    def create(self, validated_data):
        c = TextMessage.objects.create(**validated_data)
        # print c.as_json()
        message = RedisMessage(str(c.as_json()))
        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return TextMessage(**validated_data)



class MessageSerializer(serializers.HyperlinkedModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    #channel = serializers.HyperlinkedRelatedField(source='channel.id', view_name='channel-detail', many=False, required=True, queryset=Channel.objects.all())

    class Meta:
        model = Message
        fields = ('date_posted', 'channel', 'jawn_user', 'id', 'url')
        depth = 2

    def to_representation(self, value):
        if isinstance(value, TextMessage):
            return TextMessageSerializer(value, context=self.context).to_representation(value)
        if isinstance(value, ImageMessage):
            return ImageMessageSerializer(value, context=self.context).to_representation(value)

    # def create(self, validated_data):
    #     c = Message.objects.create(**validated_data)
    #     print c.as_json()
    #     message = RedisMessage(str(c.as_json()))
    #     RedisPublisher(facility=validated_data['name'], broadcast=True).publish_message(message)
    #     return Company(**validated_data)

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    messages = MessageSerializer(many=True, read_only=True,)

    class Meta:
        model = Channel
        fields = ('id', 'name', 'created', 'creator', 'messages')
        #depth = 1