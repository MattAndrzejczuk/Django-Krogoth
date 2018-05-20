__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers, exceptions
from chat.models import JawnUser
from chat.serializers import JawnUserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.shortcuts import render
from krogoth_social.models import AKThreadCategory, AKThread
from rest_framework import viewsets

from krogoth_gantry.management.commands.installdjangular import bcolors

# Create your views here.


class AKThreadChildReplySerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    pub_date = serializers.DateTimeField(read_only=True)

class AKThreadListField(serializers.RelatedField):
    def to_representation(self, value):
        ser = AKThreadChildReplySerializer(value)
        return (ser.data)




class AKThreadCategorySerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    ak_threads = AKThreadListField(many=True, read_only=True)
    class Meta:
        model = AKThreadCategory
        fields = ('title', 'ak_threads', 'pub_date', )


class AKThreadParentSerializer(serializers.ListSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    uid = serializers.ReadOnlyField()

    class Meta:
        model = AKThread
        category = AKThreadCategorySerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', 'uid',)



# - - - - - - - - - - - - - - -
class AKThreadSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    uid = serializers.ReadOnlyField()
    broodling = AKThreadListField(many=True, read_only=True)

    class Meta:
        model = AKThread
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', 'uid', 'broodling')

    def create(self, validated_data):
        return AKThread.objects.create(**validated_data)

