# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.shortcuts import render
from rest_framework import viewsets, filters, renderers, status

from kbot_lab.serializers import KBNanolatheExampleUploadSerializer
from kbot_lab.models import KBNanolatheExampleUpload
# Create your views here.



class KBNanolatheExampleUploadViewset(viewsets.ModelViewSet):
    queryset = KBNanolatheExampleUpload.objects.all()
    serializer_class = KBNanolatheExampleUploadSerializer