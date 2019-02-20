from django.conf.urls import url

from krogoth_3rdparty_api.views import GenericCallbackURIView
from krogoth_3rdparty_api.twitter_api import UserTimelineTest

from krogoth_3rdparty_api.views import RESTfulProxy_AllBreeds, RESTfulProxy_RandomDogImage, RESTfulProxy_AllDogs, \
    RESTfulProxy_ListImagesForBreed, RESTfulProxy_GetImageForSpecificBreedAndSubBreed, \
    RESTfulProxy_GetListOfSubBreedsUsingBreed, RESTfulProxy_GetRandonImageForBreed, \
    RESTfulProxy_ListImagesForSpecificBreedAndSubBreed




urlpatterns = [
    # UNIVERSAL:
    url(r'^GenericCallbackURI/', GenericCallbackURIView.as_view(), name='Generic Callback URI'),
    # TWITTER:
    url(r'^Twitter/<str:action>/<str:main_param>/', UserTimelineTest.as_view(), name='User Timeline Test'),
    # BLOCKCHAIN:
    url(r'^Blockchain/MakeWallet', UserTimelineTest.as_view(), name='User Timeline Test'),

    # - - - - - - - DOG API - - - - - - - -
    url(r'^api/breeds/list/all/',
        RESTfulProxy_AllDogs.as_view(),
        name='List All Dogs'),
    url(r'^api/breeds/image/random/',
        RESTfulProxy_RandomDogImage.as_view(),
        name='Get Random Dog Image'),
    url(r'^api/breeds/list/',
        RESTfulProxy_AllBreeds.as_view(),
        name='List All Dog Breeds'),
    url(r'^api/breed/type/images/',
        RESTfulProxy_ListImagesForBreed.as_view(),
        name='List All Images For Specified Dog Breed'),
    url(r'^api/breed/type/images/random/',
        RESTfulProxy_GetRandonImageForBreed.as_view(),
        name='Get Random Image For Breed'),
    url(r'^api/breed/type/list/',
        RESTfulProxy_GetListOfSubBreedsUsingBreed.as_view(),
        name='List of SubBreeds'),
    url(r'^api/breed/mastiff/bull/images/',
        RESTfulProxy_ListImagesForSpecificBreedAndSubBreed.as_view(),
        name='Image SubBreeds'),
    url(r'^api/breed/mastiff/bull/images/random/',
        RESTfulProxy_GetImageForSpecificBreedAndSubBreed.as_view(),
        name='Get Image'),
    # - - - - - - - /DOG API - - - - - - -

]