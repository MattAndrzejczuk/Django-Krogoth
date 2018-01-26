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

class AKThreadCategorySerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = AKThreadCategory
        fields = ('title', 'ak_threads', 'pub_date', )






class AKThreadCategoryViewSet(viewsets.ModelViewSet):
    queryset = AKThreadCategory.objects.all()
    serializer_class = AKThreadCategorySerializer
    permission_classes = (AllowAny,)



class AKThreadCategorySerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return {
            'title': obj.title
        }
class AKThreadParentSerializer(serializers.ListSerializer):
    def to_representation(self, obj):
        return {
            'parent': obj.parent,
            'title': obj.title
        }


# - - - - - - - - - - - - - - -
class AKThreadSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = AKThread
        category = AKThreadCategorySerializer
        parent = AKThreadParentSerializer
        fields = ('title', 'parent', 'author', 'category', 'pub_date', )

    def create(self, validated_data):

        print(bcolors.blue + " AKThreadSerializer " + bcolors.ENDC)
        print(bcolors.purple)
        print(validated_data)
        print(bcolors.ENDC)

        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        cat = AKThreadCategory.objects.get(id=validated_data['category'].id)
        new = AKThread.objects.create(title=validated_data['title'],
                                      author=jawn_user,
                                      category=cat)
        if validated_data['parent']:
            try:
                new.parent = AKThread.objects.get(title=validated_data['parent'].title)
            except:
                new.parent = AKThread.objects.get(uid=validated_data['parent'].id)
        return new


class AKThreadViewSet(viewsets.ModelViewSet):
    queryset = AKThread.objects.all()
    serializer_class = AKThreadSerializer
    permission_classes = (AllowAny,)
# - - - - - - - - - - - - - - -
# class ForumReplySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ForumReply
#         fields = '__all__'
#     def create(self, validated_data):
#         jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
#         new = ForumReply.objects.create(post=validated_data['post'],
#                                         body=validated_data['body'],
#                                         author=jawn_user.base_user,
#                                         category=validated_data['category'])
#         return new
# class ForumReplyViewSet(viewsets.ModelViewSet):
#     queryset = ForumReply.objects.all()
#     serializer_class = ForumReplySerializer
#     permission_classes = (AllowAny,)
# - - - - - - - - - - - - - - -
