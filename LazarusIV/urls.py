
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from LazarusIV.views import UploadRepositoryViewSet, RepositoryDirectoryViewSet, RepositoryFileViewSet, \
    BackgroundWorkerJobViewSet, NotificationCenterViewSet, NotificationItemViewSet, CavedogBaseViewSet, \
    LazarusBaseViewSet, DamageViewSet, LazarusWeaponTDFViewSet, LazarusFeatureTDFViewSet, LazarusDownloadTDFViewSet, \
    LazarusUnitFBIViewSet
#    IV  -  4
router = DefaultRouter()
router.register(r'UploadRepository', UploadRepositoryViewSet)
router.register(r'RepositoryDirectory', RepositoryDirectoryViewSet)
router.register(r'RepositoryFileViewSet', RepositoryFileViewSet)
router.register(r'BackgroundWorkerJobViewSet', BackgroundWorkerJobViewSet)
# router.register(r'KickThatMuleLee', KickThatMuleLee)
router.register(r'NotificationCenterViewSet', NotificationCenterViewSet)
router.register(r'NotificationItemViewSet', NotificationItemViewSet)
# models_tdf:
router.register(r'CavedogBaseViewSet', CavedogBaseViewSet)
router.register(r'LazarusBaseViewSet', LazarusBaseViewSet)
router.register(r'DamageViewSet', DamageViewSet)
router.register(r'LazarusWeaponTDFViewSet', LazarusWeaponTDFViewSet)
router.register(r'LazarusFeatureTDFViewSet', LazarusFeatureTDFViewSet)
router.register(r'LazarusDownloadTDFViewSet', LazarusDownloadTDFViewSet)
router.register(r'LazarusUnitFBIViewSet', LazarusUnitFBIViewSet)

urlpatterns = [
    url(r'^ContentSubmission/', include(router.urls)),
]

