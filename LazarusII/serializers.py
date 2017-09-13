from LazarusII.models import Damage, WeaponTDF, FeatureTDF, UnitFbiData, DownloadTDF, SoundSetTDF

from rest_framework import serializers, exceptions


class UnitFbiDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitFbiData
        fields = '__all__'
    def update(self, instance, validated_data):
        instance.save()
        return instance


class WeaponTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponTDF
        fields = '__all__'
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(WeaponTDFDataSerializer, self).get_serializer(*args, **kwargs)

class FeatureTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureTDF
        fields = '__all__'
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(FeatureTDFDataSerializer, self).get_serializer(*args, **kwargs)

class DownloadTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadTDF
        fields = '__all__'
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(DownloadTDFDataSerializer, self).get_serializer(*args, **kwargs)

class SoundTDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundSetTDF
        fields = ()
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(SoundTDFDataSerializer, self).get_serializer(*args, **kwargs)



