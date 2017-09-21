from django.conf.urls import url, include
from DatabaseSandbox.views import BasicUploadExample, UserAgentTracker, UploadDataTA, \
    KubaNetAnalytics, ContactWebAdminFormViewset
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'ContactWebAdminForm', ContactWebAdminFormViewset)

urlpatterns = [
    url(r'^viewsets/', include(router.urls)),
    url(r'^KubaNetAnalytics/', KubaNetAnalytics.as_view(), name='KubaNetAnalytics'),
    url(r'^BasicUploadExample/', BasicUploadExample.as_view(), name='BasicUploadExample'),
    url(r'^UserAgentTracker/', UserAgentTracker.as_view(), name='UserAgentTracker'),
    url(r'^UploadDataTA/', UploadDataTA.as_view(), name='UploadDataTA'),
]

