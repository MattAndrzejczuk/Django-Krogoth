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



class ModProject(viewsets.ModelViewSet):
    queryset = ModProject.objects.all()
    serializer_class = ModProjectSerializer
    permission_classes = (permissions.AllowAny,)

class CavedogBase(viewsets.ModelViewSet):
    queryset = CavedogBase.objects.all()
    serializer_class = CavedogBaseSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusBase(viewsets.ModelViewSet):
    queryset = LazarusBase.objects.all()
    serializer_class = LazarusBaseSerializer
    permission_classes = (permissions.AllowAny,)

class Damage(viewsets.ModelViewSet):
    queryset = Damage.objects.all()
    serializer_class = DamageSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusWeaponTDF(viewsets.ModelViewSet):
    queryset = LazarusWeaponTDF.objects.all()
    serializer_class = LazarusWeaponTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusFeatureTDF(viewsets.ModelViewSet):
    queryset = LazarusFeatureTDF.objects.all()
    serializer_class = LazarusFeatureTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusDownloadTDF(viewsets.ModelViewSet):
    queryset = LazarusDownloadTDF.objects.all()
    serializer_class = LazarusDownloadTDFSerializer
    permission_classes = (permissions.AllowAny,)

class LazarusUnitFBI(viewsets.ModelViewSet):
    queryset = LazarusUnitFBI.objects.all()
    serializer_class = LazarusUnitFBISerializer
    permission_classes = (permissions.AllowAny,)
