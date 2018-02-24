from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from krogoth_admin.views import UncommitedSQLViewSet

router = DefaultRouter()
router.register(r'UncommitedSQL', UncommitedSQLViewSet)



urlpatterns = [
    url(r'^KrogothAdministration/', include(router.urls))
]


