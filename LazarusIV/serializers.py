
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from rest_framework import serializers, exceptions
from chat.models import JawnUser

from LazarusIII.models import LazarusDamageDataTA, LazarusWeaponDataTA, LazarusFeatureDataTA, \
    LazarusDownloadDataTA, LazarusUnitDataTA
from LazarusIV.models import NotificationItem, NotificationCenter, BackgroundWorkerJob, RepositoryFile, \
    UploadRepository, RepositoryDirectory
from LazarusV.models import CavedogBase, LazarusBase
import os

class UploadRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadRepository
        fields = ('uploader', 'hpi_file', 'title', 'total_files', 'current_worker_job',
                  'root_path', 'original_hpi_path', )
        read_only_fields = ('title', 'root_path', 'original_hpi_path', 'uploader')

    def create(self, validated_data):
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.context['request'].user.username)
        # jawn_user = JawnUser.objects.get(base_user=self.context['request'].user)
        new_repo = UploadRepository.objects.create(uploader=jawn_user,
                                                   hpi_file=validated_data['hpi_file'],
                                                   title=validated_data['hpi_file'].name,
                                                   total_files=0,
                                                   current_worker_job=0,
                                                   root_path='',
                                                   original_hpi_path='')
        print(' 📦 ', end='')
        new_repo.set_file_paths()
        worker = BackgroundWorkerJob()
        worker.enqueue_job(on_repo=new_repo, to_do='I')
        return new_repo

class RepositoryDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryDirectory
        fields = ('dir_repository', 'dir_name', 'dir_path', 'dir_total_files', )
class RepositoryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryFile
        fields = ('repo_dir', 'file_name', 'file_path', 'file_kind', 'file_thumbnail', )
class BackgroundWorkerJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundWorkerJob
        fields = ('job_name', 'dispatched_by_repo', 'is_finished', 'is_working', )
class NotificationCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCenter
        fields = ('parent_user', 'unread_private', )
class NotificationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationItem
        fields = ('center', 'is_private', 'kind', 'image_url', 'sfx_chime', 'title', 'body', 'date', 'unread', )


class CavedogBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CavedogBase
        fields = '__all__'
class LazarusBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusBase
        fields = '__all__'
class DamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusDamageDataTA
        fields = '__all__'
class LazarusWeaponTDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusWeaponDataTA
        fields = '__all__'
class LazarusFeatureTDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusFeatureDataTA
        fields = '__all__'
class LazarusDownloadTDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusDownloadDataTA
        fields = '__all__'
class LazarusUnitFBISerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusUnitDataTA
        fields = '__all__'