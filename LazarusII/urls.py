from django.conf.urls import url, include
from LazarusII import views

from LazarusII.views import AutoCollectStatic, \
    UserAgentTracker, ExecuteBash_LS_AllCustomModFiles, \
    ReadVanillaTAData, ReadVanillaTASoundData, \
    ReadCoreContingencySoundData, ReadCoreContingencyWeaponData

from LazarusII.viewsets import UnitFBIViewSerialized, WeaponTDFViewSerialized, \
    FeatureTDFViewSerialized, DownloadTDFViewSerialized, SoundTDFViewSerialized


# Pure Python Stuff:
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register(r'FBISerialized', UnitFBIViewSerialized)
router.register(r'WeaponTDF', WeaponTDFViewSerialized)
router.register(r'FeatureTDF', FeatureTDFViewSerialized)
router.register(r'DownloadTDF', DownloadTDFViewSerialized)
router.register(r'SoundTDF', SoundTDFViewSerialized)


urlpatterns = [

    url(r'^serialized/', include(router.urls)),
    url(r'^UserAgentTracker', UserAgentTracker.as_view()),
    url(r'^AutoCollectStatic/', AutoCollectStatic.as_view(), name='AutoCollectStatic'),
    # url(r'^UnitFBIViewset/', include(router.urls)),

    url(r'^ExecuteBash_LS_AllCustomModFiles/', ExecuteBash_LS_AllCustomModFiles.as_view(), name='ExecuteBash_LS_AllCustomModFiles'),

    url(r'^ReadVanillaTAData/', ReadVanillaTAData.as_view(), name='Read Vanilla TA Data'),
    url(r'^ReadVanillaTASoundData/', ReadVanillaTASoundData.as_view(), name='Read Vanilla TA Sound Data'),
    url(r'^ReadCoreContingencyWeaponData/', ReadCoreContingencyWeaponData.as_view(), name='Read TA CC Data'),
    url(r'^ReadCoreContingencySoundData/', ReadCoreContingencySoundData.as_view(), name='Read TA CC Sound Data'),
]

