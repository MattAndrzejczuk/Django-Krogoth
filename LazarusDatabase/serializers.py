from LazarusDatabase.models import TotalAnnihilationMod, LazarusModProject, LazarusModAsset, LazarusModDependency
from rest_framework import serializers, exceptions




class TotalAnnihilationModSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalAnnihilationMod
        fields = '__all__'


class LazarusModProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModProject
        fields = '__all__'


class LazarusModAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModAsset
        fields = '__all__'


class LazarusModDependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = LazarusModDependency
        fields = '__all__'
