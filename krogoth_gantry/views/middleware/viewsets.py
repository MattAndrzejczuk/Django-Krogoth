

from krogoth_gantry.models.gantry_models import KrogothGantryCategory, \
    KrogothGantryDirective, KrogothGantryService
from krogoth_gantry.functions.edit_mvc import KrogothGantryMasterViewControllerSerializer, \
    KrogothGantrySlaveViewControllerSerializer, \
    KrogothGantryCategorySerializer, KrogothGantryMasterViewController, \
    KrogothGantryDirectiveSerializer, KrogothGantryServiceSerializer, \
    KrogothGantrySlaveViewController
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantryMasterViewControllerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = KrogothGantryMasterViewController.objects.all().order_by('name')
    serializer_class = KrogothGantryMasterViewControllerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'category', 'id')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantrySlaveViewControllerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = KrogothGantrySlaveViewController.objects.all().order_by('name')
    serializer_class = KrogothGantrySlaveViewControllerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantryCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = KrogothGantryCategory.objects.all().order_by('name')
    serializer_class = KrogothGantryCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'parent__id')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantryDirectiveViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = KrogothGantryDirective.objects.all().order_by('name')
    serializer_class = KrogothGantryDirectiveSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class KrogothGantryServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = KrogothGantryService.objects.all().order_by('name')
    serializer_class = KrogothGantryServiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')
