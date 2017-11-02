from rest_framework import viewsets

from LazarusII.serializers import UnitFbiDataSerializer_v2, WeaponTDFDataSerializer, \
    FeatureTDFDataSerializer, DownloadTDFDataSerializer, SoundTDFDataSerializer

from LazarusII import models


class UnitFBIViewSerialized(viewsets.ModelViewSet):
    serializer_class = UnitFbiDataSerializer_v2
    queryset = models.UnitFbiData_v2.objects.all()

class WeaponTDFViewSerialized(viewsets.ModelViewSet):
    serializer_class = WeaponTDFDataSerializer
    queryset = models.WeaponTDF.objects.all()

class FeatureTDFViewSerialized(viewsets.ModelViewSet):
    serializer_class = FeatureTDFDataSerializer
    queryset = models.FeatureTDF.objects.all()

class DownloadTDFViewSerialized(viewsets.ModelViewSet):
    serializer_class = DownloadTDFDataSerializer
    queryset = models.DownloadTDF.objects.all()

class SoundTDFViewSerialized(viewsets.ModelViewSet):
    serializer_class = SoundTDFDataSerializer
    queryset = models.SoundSetTDF.objects.all()