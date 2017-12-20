# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.shortcuts import render
from rest_framework import viewsets, filters, renderers, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from kbot_lab.serializers import KBNanolatheExampleUploadSerializer, KBNanolatheExamplePlainSerializer
from kbot_lab.models import KBNanolatheExampleUpload, KBNanolatheExamplePlain
# Create your views here.



class KBNanolatheExampleUploadViewset(viewsets.ModelViewSet):
    queryset = KBNanolatheExampleUpload.objects.all()
    serializer_class = KBNanolatheExampleUploadSerializer

class KBNanolatheExamplePlainViewset(viewsets.ModelViewSet):
    queryset = KBNanolatheExamplePlain.objects.all()
    serializer_class = KBNanolatheExamplePlainSerializer