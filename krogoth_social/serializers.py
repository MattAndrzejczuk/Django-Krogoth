__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers, exceptions
from chat.models import JawnUser
from chat.serializers import JawnUserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.shortcuts import render
from krogoth_social.models import AKThreadCategory, AKThread, AKThreadSocialMedia, \
    ForumThreadCategory, ForumThreadOP, ForumThreadReply
from rest_framework import viewsets
from datetime import datetime
from krogoth_gantry.management.commands.installdjangular import bcolors

# Create your views here.


class ForumThreadCategorySerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField()

    class Meta:
        model = ForumThreadCategory
        fields = ('uid', 'weight', 'description', 'title', 'total_threads', 'img_url')

class ForumThreadOPSerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField()
    author = JawnUserSerializer(read_only=True)

    class Meta:
        model = ForumThreadOP
        fields = ('uid', 'title', 'author', 'pub_date', 'date_modified', 'not_deleted', 'category', 'content',
                  'total_likes', 'total_replies','pub_date',)

    def create(self, validated_data):
        validated_data['pub_date'] = datetime.now()
        validated_data['author'] = JawnUser.objects.get(id=self.context['request'].user.id)
        cat = ForumThreadCategory.objects.get(uid=validated_data['category'].uid)
        validated_data['uid'] = cat.uid + "_THREAD_" + str(cat.total_threads)
        cat.total_threads += 1
        cat.save()
        validated_data['date_modified'] = datetime.now()
        return ForumThreadOP.objects.create(**validated_data)


class ForumThreadReplySerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField()
    author = JawnUserSerializer(read_only=True)

    class Meta:
        model = ForumThreadReply
        fields = ('uid', 'author', 'parent', 'pub_date', 'date_modified', 'not_deleted', 'content', 'total_likes',)

    def create(self, validated_data):
        validated_data['pub_date'] = datetime.now()
        validated_data['author'] = JawnUser.objects.get(id=self.context['request'].user.id)
        _op = ForumThreadOP.objects.get(uid=validated_data['parent'].uid)
        validated_data['uid'] = _op.uid + "_REPLY_" + str(_op.total_replies)
        _op.total_replies += 1
        _op.date_modified = datetime.now()
        _op.save()
        new = ForumThreadReply.objects.create(**validated_data)
        return new

class AKThreadChildReplySerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    pub_date = serializers.DateTimeField(read_only=True)
    content = serializers.CharField(read_only=True)

class AKThreadListField(serializers.RelatedField):
    def to_representation(self, value):
        ser = AKThreadChildReplySerializer(value)
        return (ser.data)

class AKThreadCategorySerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    ak_threads = AKThreadListField(many=True, read_only=True)
    class Meta:
        model = AKThreadCategory
        fields = ('uid', 'description', 'title', 'ak_threads', 'pub_date', )

class AKThreadParentSerializer(serializers.ListSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    uid = serializers.ReadOnlyField()

    class Meta:
        model = AKThread
        category = AKThreadCategorySerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', 'uid', 'date_modified', 'author_name',)

# - - - - - - - - - - - - - - -
class AKThreadSerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField()
    broodling = AKThreadListField(many=True, read_only=True)

    class Meta:
        model = AKThread
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', 'date_modified', 'uid', 'broodling', 'is_reply', 'content', 'author_name',)


class AKThreadSocialMediaSerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField()
    
    class Meta:
        model = AKThreadSocialMedia
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'author', 'category', 'content', 'uid', 'author_name', 'pub_date',)
        
    def create(self, validated_data):
        validated_data['pub_date'] = datetime.now()
        newuid = ''.join(e for e in validated_data['title'] if e.isalnum())
        finalize = newuid + "_" + str(datetime.now())[0:10]
        new = AKThread.objects.create(title=validated_data['title'],author=validated_data['author'],category=validated_data['category'],content=validated_data['content'],uid=finalize,pub_date=datetime.now(),)
        return new

class AKThreadReplySocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AKThreadSocialMedia
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', 'content', 'likes', 'type')