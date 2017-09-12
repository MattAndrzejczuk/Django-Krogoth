from LazarusII.models import Damage, WeaponTDF, FeatureTDF, UnitFbiData, DownloadTDF, SoundSetTDF

from rest_framework import serializers, exceptions


class UnitFbiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitFbiData
        fields = '__all__'

class WeaponTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponTDF
        fields = '__all__'

class FeatureTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureTDF
        fields = '__all__'

class DownloadTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadTDF
        fields = '__all__'

class SoundTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundSetTDF
        fields = '__all__'
