from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
#    V  -  5

from LazarusV.views import ModProjectViewSet, ModPublicationViewSet, ModBuildViewSet, WargamePackageViewSet, \
    WargameFileViewSet, WargameDataViewSet, UserRatingViewSet, RatingCavedogBaseViewSet, RatingModPublicationViewSet
#    V  -  5
router = DefaultRouter()
router.register(r'ModProject', ModProjectViewSet)
router.register(r'ModPublication', ModPublicationViewSet)
router.register(r'ModBuild', ModBuildViewSet)
router.register(r'WargamePackage', WargamePackageViewSet)
router.register(r'WargameFile', WargameFileViewSet)
router.register(r'WargameData', WargameDataViewSet)
router.register(r'UserRating', UserRatingViewSet)
router.register(r'RatingCavedogBase', RatingCavedogBaseViewSet)
router.register(r'RatingModPublication', RatingModPublicationViewSet)

urlpatterns = [
    url(r'^ModEditor/', include(router.urls)),
]