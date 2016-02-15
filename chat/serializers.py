from rest_framework import serializers
from chat.models import *
from django.contrib.auth.models import User
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher
import json
from rest_framework.parsers import JSONParser

class UserSerializer(serializers.ModelSerializer):


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

class JawnUserSerializer(serializers.ModelSerializer):
    #base_user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = JawnUser
        fields = ('id', 'url', 'profile_pic', 'about_me', 'follows', 'date_of_birth', 'sex',
                  'base_user',
                  'followers')
        #depth = 2





class ImageMessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = ImageMessage
        fields = ('date_posted', 'channel', 'type', 'image_url', 'caption', 'jawn_user', 'id', 'url')
        #depth = 1

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        c = ImageMessage.objects.create(channel=validated_data['channel'], image_url=validated_data['image_url'], jawn_user=jawn_user, caption=validated_data['caption'])
        message = RedisMessage(str(c.as_json()))
        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return c


class TextMessageSerializer(serializers.ModelSerializer):
    #jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = TextMessage
        fields = ('date_posted', 'channel', 'type', 'text', 'jawn_user', 'id', 'url')
        #depth = 1

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        c = TextMessage.objects.create(channel=validated_data['channel'], text=validated_data['text'], jawn_user=jawn_user)
        print(validated_data['channel'])
        message = RedisMessage(str(c.as_json()))
        RedisPublisher(facility=validated_data['channel'], broadcast=True).publish_message(message)
        return c

    def update(self, instance, validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        print(instance.channel)
        print(instance.as_json())
        message = RedisMessage(str(instance.as_json()))
        RedisPublisher(facility=instance.channel, broadcast=True).publish_message(message)
        return instance



class MessageSerializer(serializers.ModelSerializer):
    jawn_user = JawnUserSerializer(many=False, read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'date_posted', 'channel', 'jawn_user', 'url')
        depth = 1



    def to_representation(self, value):
        if isinstance(value, TextMessage):
            return TextMessageSerializer(value, context=self.context).to_representation(value)
        if isinstance(value, ImageMessage):
            return ImageMessageSerializer(value, context=self.context).to_representation(value)



class ChannelSerializer(serializers.ModelSerializer):
    # messages = MessageSerializer(many=True, read_only=True,)

    messages = serializers.SerializerMethodField('get_messages_ordered')

    def get_messages_ordered(self, channel):
        qset = Message.objects.filter(channel=channel).order_by('-date_posted')
        serialized_data = MessageSerializer(qset, many=True, read_only=True, context=self.context)
        return serialized_data.data


    class Meta:
        model = Channel
        fields = ('id', 'name', 'created', 'creator', 'messages')
        #depth = 1