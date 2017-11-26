from django.conf.urls import url, include
# from LazarusIV.views import *
from rest_framework.routers import DefaultRouter
#    IV  -  4

router = DefaultRouter()
# router.register(r'Mods', views.TotalAnnihilationModViewset)

urlpatterns = [
    url(r'^LazarusIV/', include(router.urls)),
]