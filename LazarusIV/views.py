
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from django.shortcuts import render
from rest_framework import viewsets, filters, renderers, status, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import detail_route, list_route, authentication_classes

from LazarusIV.armprime_dispatcher.jobs import Worker

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
    permission_classes = (AllowAny,)
    throttle_scope = 'uploads'

class RepositoryDirectoryViewSet(viewsets.ModelViewSet):
    queryset = RepositoryDirectory.objects.all()
    serializer_class = RepositoryDirectorySerializer
    permission_classes = (AllowAny,)

class RepositoryFileViewSet(viewsets.ModelViewSet):
    queryset = RepositoryFile.objects.all()
    serializer_class = RepositoryFileSerializer
    permission_classes = (AllowAny,)

class BackgroundWorkerJobViewSet(viewsets.ModelViewSet):
    queryset = BackgroundWorkerJob.objects.filter(is_finished=False)
    serializer_class = BackgroundWorkerJobSerializer
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'manual_worker'

    @detail_route(methods=['post'])
    @authentication_classes(IsAdminUser, )
    def kick_post(self, request, format=None):
        workr = Worker()
        workr.kickThatMuleLee()
        return Response('Mule was kicked!')



# class KickThatMuleLee(APIView):
    """
    list:
    Dispatches the next worker to begin job, if available and worker limit not reached.
    """
    # def get(self, request, format=None):
    #     workr = Worker()
    #     workr.kickThatMuleLee()
    #     return Response('Mule was kicked!')

class NotificationCenterViewSet(viewsets.ModelViewSet):
    queryset = NotificationCenter.objects.all()
    serializer_class = NotificationCenterSerializer
    permission_classes = (AllowAny,)

class NotificationItemViewSet(viewsets.ModelViewSet):
    queryset = NotificationItem.objects.all()
    serializer_class = NotificationItemSerializer
    permission_classes = (AllowAny,)


class CavedogBaseViewSet(viewsets.ModelViewSet):
    queryset = CavedogBase.objects.all()
    serializer_class = CavedogBaseSerializer
    permission_classes = (AllowAny,)

class LazarusBaseViewSet(viewsets.ModelViewSet):
    queryset = LazarusBase.objects.all()
    serializer_class = LazarusBaseSerializer
    permission_classes = (AllowAny,)

class DamageViewSet(viewsets.ModelViewSet):
    queryset = LazarusDamageDataTA.objects.all()
    serializer_class = DamageSerializer
    permission_classes = (AllowAny,)

class LazarusWeaponTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusWeaponDataTA.objects.all()
    serializer_class = LazarusWeaponTDFSerializer
    permission_classes = (AllowAny,)

class LazarusFeatureTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusFeatureDataTA.objects.all()
    serializer_class = LazarusFeatureTDFSerializer
    permission_classes = (AllowAny,)

class LazarusDownloadTDFViewSet(viewsets.ModelViewSet):
    queryset = LazarusDownloadDataTA.objects.all()
    serializer_class = LazarusDownloadTDFSerializer
    permission_classes = (AllowAny,)

class LazarusUnitFBIViewSet(viewsets.ModelViewSet):
    queryset = LazarusUnitDataTA.objects.all()
    serializer_class = LazarusUnitFBISerializer
    permission_classes = (AllowAny,)
