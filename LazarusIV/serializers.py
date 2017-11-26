from rest_framework import serializers, exceptions
from chat.models import JawnUser
from LazarusIV.models import UploadRepository, RepositoryDirectory, RepositoryFile, BackgroundWorkerJob, \
    NotificationCenter, NotificationItem

class UploadRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadRepository
        fields = ('id', )

class RepositoryDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryDirectory
        fields = ('id', )

class RepositoryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryFile
        fields = ('id', )

class BackgroundWorkerJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundWorkerJob
        fields = ('id', )

class NotificationCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCenter
        fields = ('id', )

class NotificationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationItem
        fields = ('id', )