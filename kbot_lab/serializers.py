# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers
from kbot_lab.models import KBNanolatheExampleUpload
from chat.models import JawnUser


class KBNanolatheExampleUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = KBNanolatheExampleUpload
        fields = ('kbc_uploaded_by_user','kb_path_slug','kb_file',)

    def create(self, validated_data):
        jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        new_upload = KBNanolatheExampleUpload.nanolathe_upload(named='test_upload')
        new_upload.kbc_uploaded_by_user = jawn_user
        return new_upload