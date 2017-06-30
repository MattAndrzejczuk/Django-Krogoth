from django.conf.urls import url
from LazarusII import views
from LazarusII.views import UnitFbiData, ApiNavigationUrls, LazarusListUnits
# Pure Python Stuff:
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair

urlpatterns = [
    url(r'^help_api/$', ApiNavigationUrls.as_view()),
    url(r'^unit_fbi/$', views.getUnitFbiUsingId),
    url(r'^UnitFbiData/$', UnitFbiData.as_view(), name='UnitFbiData'),
    url(r'^LazarusListUnits/', LazarusListUnits.as_view(), name='LazarusListUnits'),
]