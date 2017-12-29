__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers, exceptions
from chat.models import JawnUser
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.shortcuts import render
from CommunityForum.models import ForumCategory, ForumPost, ForumReply
from rest_framework import viewsets
# Create your views here.

class ForumCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumCategory
        fields = '__all__'
# - - - - - - - - - - - - - - -
class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = '__all__'
    def create(self, validated_data):
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        new = ForumPost.objects.create(title=validated_data['title'],
                                       body=validated_data['body'],
                                       author=jawn_user.base_user,
                                       category=validated_data['category'])
        return new
class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = (AllowAny,)
# - - - - - - - - - - - - - - -
class ForumReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumReply
        fields = '__all__'
    def create(self, validated_data):
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        new = ForumReply.objects.create(post=validated_data['post'],
                                        body=validated_data['body'],
                                        author=jawn_user.base_user,
                                        category=validated_data['category'])
        return new
class ForumReplyViewSet(viewsets.ModelViewSet):
    queryset = ForumReply.objects.all()
    serializer_class = ForumReplySerializer
    permission_classes = (AllowAny,)
# - - - - - - - - - - - - - - -