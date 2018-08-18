__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers, exceptions
from chat.models import JawnUser
from chat.serializers import JawnUserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.shortcuts import render
from krogoth_social.models import AKThreadCategory, AKThread, AKThreadSocialMedia
from rest_framework import viewsets

from krogoth_gantry.management.commands.installdjangular import bcolors

# Create your views here.


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
    pub_date = serializers.DateTimeField(read_only=True)
    uid = serializers.ReadOnlyField()
    broodling = AKThreadListField(many=True, read_only=True)

    class Meta:
        model = AKThread
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', 'date_modified', 'uid', 'broodling', 'is_reply', 'content', 'author_name',)

    def create(self, validated_data):
        return AKThread.objects.create(**validated_data)

class AKThreadSocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AKThreadSocialMedia
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'parent', 'author', 'uid', 'category', 'pub_date', 'broodling', 'content', 'likes', 'type')

class AKThreadReplySocialMediaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AKThreadSocialMedia
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', 'content', 'likes', 'type')
