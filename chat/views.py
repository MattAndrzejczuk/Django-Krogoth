from django.shortcuts import render

# Create your views here.
from chat.models import *
from chat.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

class JawnUserViewSet(viewsets.ModelViewSet):

    queryset = JawnUser.objects.all()
    serializer_class = JawnUserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ImageMessageViewSet(viewsets.ModelViewSet):

    queryset = ImageMessage.objects.all()
    serializer_class = ImageMessageSerializer
    permission_classes = (permissions.IsAuthenticated, )


class TextMessageViewSet(viewsets.ModelViewSet):

    queryset = TextMessage.objects.all()
    serializer_class = TextMessageSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChannelViewSet(viewsets.ModelViewSet):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )

