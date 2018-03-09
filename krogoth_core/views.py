from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from krogoth_core.models import AKFoundationAbstract
from krogoth_core.serializers import AKFoundationSerializer


class AKFoundationViewSet(viewsets.ModelViewSet):
    queryset = AKFoundationAbstract.objects.all()
    serializer_class = AKFoundationSerializer
    permission_classes = (AllowAny, )
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('unique_name', 'first_name', 'last_name', 'ext', )

