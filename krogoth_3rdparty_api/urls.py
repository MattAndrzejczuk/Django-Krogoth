from django.conf.urls import url

from krogoth_3rdparty_api.views import GenericCallbackURIView
from krogoth_3rdparty_api.twitter_api import UserTimelineTest

urlpatterns = [
    # UNIVERSAL:
    url(r'^GenericCallbackURI/', GenericCallbackURIView.as_view(), name='Generic Callback URI'),
    # TWITTER:
    url(r'^Twitter/<str:action>/<str:main_param>/', UserTimelineTest.as_view(), name='User Timeline Test'),
    # BLOCKCHAIN:
    url(r'^Blockchain/MakeWallet', UserTimelineTest.as_view(), name='User Timeline Test'),
]