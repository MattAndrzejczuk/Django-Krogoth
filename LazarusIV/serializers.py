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
        fields = ('id', )
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
        fields = ('id', )
class LazarusUnitFBISerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusUnitDataTA
        fields = '__all__'