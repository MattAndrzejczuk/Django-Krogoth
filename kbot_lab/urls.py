# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from kbot_lab.views import KBNanolatheExampleUploadViewset, KBNanolatheExamplePlainViewset







router = DefaultRouter()
router.register(r'UploadExample', KBNanolatheExampleUploadViewset)
router.register(r'PlainExample', KBNanolatheExamplePlainViewset)

urlpatterns = [
    url(r'^KBotLab/', include(router.urls)),
]