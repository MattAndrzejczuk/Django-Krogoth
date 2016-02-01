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
import django_filters

class ChannelFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(name="name", lookup_type="startswith")
    region = django_filters.CharFilter(name="name", lookup_type="startswith")

    class Meta:
        model = Channel
        fields = ['created', 'name', 'id', 'creator', 'region']


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

class JawnUserViewSet(viewsets.ModelViewSet):

    queryset = JawnUser.objects.all()
    serializer_class = JawnUserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('base_user', )


class ImageMessageViewSet(viewsets.ModelViewSet):

    queryset = ImageMessage.objects.all()
    serializer_class = ImageMessageSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        serializer_class = ImageMessageSerializer(data=request.DATA, files=request.FILES)
        if serializer_class.is_valid():
           serializer_class.save()
           return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=serializer_class.HTTP_400_BAD_REQUEST)


class TextMessageViewSet(viewsets.ModelViewSet):

    queryset = TextMessage.objects.all()
    serializer_class = TextMessageSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChannelViewSet(viewsets.ModelViewSet):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'id', 'creator',)
    filter_class = ChannelFilter


class MessageViewSet(viewsets.ModelViewSet):

    queryset = Message.objects.all().extra(order_by=['-id'])
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', )

