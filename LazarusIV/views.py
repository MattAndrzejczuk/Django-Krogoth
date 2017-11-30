from django.shortcuts import render
from rest_framework import viewsets, filters, renderers, status, permissions


from LazarusIV.models_tdf import LazarusDamageDataTA, LazarusWeaponDataTA, LazarusFeatureDataTA, \
    LazarusDownloadDataTA, LazarusUnitDataTA

from LazarusIV.models import UploadRepository, RepositoryFile, BackgroundWorkerJob, NotificationCenter, \
    RepositoryDirectory, NotificationItem

from LazarusV.models import CavedogBase, LazarusBase

from LazarusIV.serializers import UploadRepositorySerializer, RepositoryDirectorySerializer, \
    RepositoryFileSerializer, BackgroundWorkerJobSerializer, NotificationCenterSerializer, \
    NotificationItemSerializer, CavedogBaseSerializer, LazarusBaseSerializer, DamageSerializer, \
    LazarusWeaponTDFSerializer, LazarusFeatureTDFSerializer, LazarusDownloadTDFSerializer, LazarusUnitFBISerializer

#    IV  -  4

class UploadRepositoryViewSet(viewsets.ModelViewSet):
    queryset = UploadRepository.objects.all()
    serializer_class = UploadRepositorySerializer
    permission_classes = (permissions.AllowAny,)

class RepositoryDirectoryViewSet(viewsets.ModelViewSet):
    queryset = RepositoryDirectory.objects.all()
    serializer_class = RepositoryDirectorySerializer
    permission_classes = (permissions.AllowAny,)

class RepositoryFileViewSet(viewsets.ModelViewSet):
    queryset = RepositoryFile.objects.all()
    serializer_class = RepositoryFileSerializer
    permission_classes = (permissions.AllowAny,)

class BackgroundWorkerJobViewSet(viewsets.ModelViewSet):
    queryset = BackgroundWorkerJob.objects.all()
    serializer_class = BackgroundWorkerJobSerializer
    permission_classes = (permissions.AllowAny,)

class KickThatMuleLee(viewsets.ModelViewSet):
    """
    list:
    Dispatches the next worker to begin job, if available and worker limit not reached.
    """
    queryset = BackgroundWorkerJob.objects.filter(is_working=True)
    serializer_class = BackgroundWorkerJobSerializer
    permission_classes = (permissions.IsAdminUser,)

class NotificationCenterViewSet(viewsets.ModelViewSet):
    queryset = NotificationCenter.objects.all()
    serializer_class = NotificationCenterSerializer
    permission_classes = (permissions.AllowAny,)

class NotificationItemViewSet(viewsets.ModelViewSet):
    queryset = NotificationItem.objects.all()
    serializer_class = NotificationItemSerializer
    permission_classes = (permissions.AllowAny,)




class CavedogBaseViewSet(viewsets.ModelViewSet):
    queryset = CavedogBase.objects.all()
    serializer_class = CavedogBaseSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusBaseViewSet(viewsets.ModelViewSet):
    queryset = LazarusBase.objects.all()
    serializer_class = LazarusBaseSerializer
    permission_classes = (permissions.AllowAny,)

class DamageViewSet(viewsets.ModelViewSet):
    queryset = LazarusDamageDataTA.objects.all()
    serializer_class = DamageSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusWeaponTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusWeaponDataTA.objects.all()
    serializer_class = LazarusWeaponTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusFeatureTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusFeatureDataTA.objects.all()
    serializer_class = LazarusFeatureTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusDownloadTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusDownloadDataTA.objects.all()
    serializer_class = LazarusDownloadTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusUnitFBIViewSet(viewsets.ModelViewSet):
    queryset = LazarusUnitDataTA.objects.all()
    serializer_class = LazarusUnitFBISerializer
    permission_classes = (permissions.AllowAny,)
