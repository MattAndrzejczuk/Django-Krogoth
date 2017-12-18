# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
from kbot_lab.models import KBNanolatheExampleUpload
from chat.models import JawnUser
from django.contrib.auth.models import AnonymousUser


class KBNanolatheExampleUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = KBNanolatheExampleUpload
        fields = ('kb_path_slug','kb_file','kbc_uploaded_by_user',)

    def create(self, validated_data):
        new_upload = KBNanolatheExampleUpload.nanolathe_upload(named='test_upload')
        # if validated_data['kbc_uploaded_by_user'] is None:
        #     jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        #     new_upload.kbc_uploaded_by_user = jawn_user
        return new_upload