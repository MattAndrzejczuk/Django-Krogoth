from django.conf.urls import url
from LazarusII import views
from LazarusII.views import getCPUInfo

# Pure Python Stuff:
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair


urlpatterns = [
    url(r'^unit_fbi/$', views.getUnitFbiUsingId),
    url(r'^cpuinfo/$', getCPUInfo.as_view(), name='cpuinfo'),
]


