from django.shortcuts import render
from rest_framework import viewsets, filters, renderers, status, permissions

from LazarusIV.models_tdf import *
from LazarusIV.models import *
from LazarusIV.serializers import *
from chat.models import JawnUser
# Create your views here.

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
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusWeaponTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusWeaponTDF.objects.all()
    serializer_class = LazarusWeaponTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusFeatureTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusFeatureTDF.objects.all()
    serializer_class = LazarusFeatureTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusDownloadTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusDownloadTDF.objects.all()
    serializer_class = LazarusDownloadTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusUnitFBIViewSet(viewsets.ModelViewSet):
    queryset = LazarusUnitFBI.objects.all()
    serializer_class = LazarusUnitFBISerializer
    permission_classes = (permissions.AllowAny,)
