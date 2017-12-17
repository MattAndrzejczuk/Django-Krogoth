# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from kbot_lab.views import KBNanolatheExampleUploadViewset







router = DefaultRouter()
router.register(r'UploadExample', KBNanolatheExampleUploadViewset)

urlpatterns = [
    url(r'^KBotLab/', include(router.urls)),
]