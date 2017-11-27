from rest_framework import serializers, exceptions
from chat.models import JawnUser
from LazarusIV.models import *

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

# models_tdf:
class ModProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModProject
        fields = ('id', )

class CavedogBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CavedogBase
        fields = ('id', )

class LazarusBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusBase
        fields = ('id', )

class DamageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Damage
        fields = ('id', )

class LazarusWeaponTDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusWeaponTDF
        fields = ('id', )

class LazarusFeatureTDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusFeatureTDF
        fields = ('id', )

class LazarusDownloadTDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusDownloadTDF
        fields = ('id', )

class LazarusUnitFBISerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusUnitFBI
        fields = ('id', )
