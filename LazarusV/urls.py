from django.conf.urls import url, include
# from LazarusV.views import *
from rest_framework.routers import DefaultRouter
#    V  -  5

router = DefaultRouter()
# router.register(r'Mods', views.TotalAnnihilationModViewset)

urlpatterns = [
    url(r'^LazarusV/', include(router.urls)),
]
