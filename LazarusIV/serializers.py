from rest_framework import serializers, exceptions
from chat.models import JawnUser

from LazarusIV.models_tdf import LazarusDamageDataTA, LazarusWeaponDataTA, LazarusFeatureDataTA, \
    LazarusDownloadDataTA, LazarusUnitDataTA
from LazarusIV.models import NotificationItem, NotificationCenter, BackgroundWorkerJob, RepositoryFile, \
    UploadRepository, RepositoryDirectory
from LazarusV.models import CavedogBase, LazarusBase

class UploadRepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadRepository
        fields = ('uploader', 'title', 'total_units', 'current_worker_job', 'root_path', 'original_hpi_path', )
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