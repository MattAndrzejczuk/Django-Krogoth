from django.shortcuts import render
from rest_framework import viewsets, filters, renderers, status, permissions


from LazarusIV.models_tdf import *
from LazarusV.models import *
from LazarusV.serializers import *
from chat.models import JawnUser
# Create your views here.

class ModPublicationViewSet(viewsets.ModelViewSet):
    queryset = ModPublication.objects.all()
    serializer_class = ModPublicationSerializer
    permission_classes = (permissions.AllowAny,)

class ModBuildViewSet(viewsets.ModelViewSet):
    queryset = ModBuild.objects.all()
    serializer_class = ModBuildSerializer
    permission_classes = (permissions.AllowAny,)

class WargamePackageViewSet(viewsets.ModelViewSet):
    queryset = WargamePackage.objects.all()
    serializer_class = WargamePackageSerializer
    permission_classes = (permissions.AllowAny,)

class WargameFileViewSet(viewsets.ModelViewSet):
    queryset = WargameFile.objects.all()
    serializer_class = WargameFileSerializer
    permission_classes = (permissions.AllowAny,)

class WargameDataViewSet(viewsets.ModelViewSet):
    queryset = WargameData.objects.all()
    serializer_class = WargameDataSerializer
    permission_classes = (permissions.AllowAny,)

class UserRatingViewSet(viewsets.ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer
    permission_classes = (permissions.AllowAny,)

class RatingCavedogBaseViewSet(viewsets.ModelViewSet):
    queryset = RatingCavedogBase.objects.all()
    serializer_class = RatingCavedogBaseSerializer
    permission_classes = (permissions.AllowAny,)

class RatingModPublicationViewSet(viewsets.ModelViewSet):
    queryset = RatingModPublication.objects.all()
    serializer_class = RatingModPublicationSerializer
    permission_classes = (permissions.AllowAny,)
