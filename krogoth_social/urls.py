from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from krogoth_social.views import AKThreadViewSet, AKThreadCategoryViewSet




router = DefaultRouter()
router.register(r'AKThread', AKThreadViewSet, 'AKThreadViewSets')
router.register(r'AKThreadCategory', AKThreadCategoryViewSet, 'AKThreadCategoryViewSet')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
