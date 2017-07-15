from LazarusII.models import Damage, WeaponTDF, FeatureTDF, UnitFbiData, DownloadTDF

from rest_framework import serializers, exceptions


class UnitFbiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitFbiData
        fields = '__all__'
