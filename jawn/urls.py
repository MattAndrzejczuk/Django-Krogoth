from filebrowser.sites import site
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from chat.views import UserViewSet, JawnUserViewSet, ImageMessageViewSet, TextMessageViewSet, ChannelViewSet, \
    MessageViewSet, PrivateMessageRelationshipSet, RegionViewSet, LinkMessageViewSet, YouTubeMessageViewSet
from django.contrib import admin
from rest_auth.views import index





router = DefaultRouter()
router.register(r'users', UserViewSet, 'User')
router.register(r'jawn-users', JawnUserViewSet, 'Jawn User')
router.register(r'image-messages', ImageMessageViewSet, 'Image Message')
router.register(r'text-messages', TextMessageViewSet, 'Text Message')
router.register(r'channels', ChannelViewSet, 'Channel')
router.register(r'messages', MessageViewSet, 'Message')
router.register(r'private-message-relationships', PrivateMessageRelationshipSet, 'Private Message')
router.register(r'regions', RegionViewSet, 'Region')
router.register(r'link-messages', LinkMessageViewSet)
router.register(r'youtube-messages', YouTubeMessageViewSet)
router.register(r'youtube', YouTubeMessageViewSet)

from CommunityForum.serializers import AKThreadViewSet, AKThreadCategoryViewSet
router.register(r'AKThreadCategory', AKThreadCategoryViewSet)
router.register(r'AKThread', AKThreadViewSet)

from krogoth_examples.views import FruitViewSet, TextLabelViewSet, ManufacturerViewSet, CarViewSet, \
    ToppingViewSet, PizzaViewSet, HotelViewSet, OccupantViewSet, \
    BasicImageUploadViewSet, BasicFileUploadViewSet
router.register(r'__ExamplesFruit', FruitViewSet, 'Fruit')
router.register(r'__ExamplesTextLabel', TextLabelViewSet, 'TextLabel')
router.register(r'__ExamplesManufacturer', ManufacturerViewSet, 'Manufacturer')
router.register(r'__ExamplesCar', CarViewSet, 'Car')
router.register(r'__ExamplesTopping', ToppingViewSet, 'Topping')
router.register(r'__ExamplesPizza', PizzaViewSet, 'Pizza')
router.register(r'__ExamplesHotel', HotelViewSet, 'Hotel')
router.register(r'__ExamplesOccupant', OccupantViewSet, 'Occupant')
router.register(r'__ExamplesBasicImageUpload', BasicImageUploadViewSet, 'BasicImageUpload')
router.register(r'__ExamplesBasicFileUpload', BasicFileUploadViewSet, 'BasicFileUpload')






from moho_extractor.views import RESTfulProxy_AllBreeds, RESTfulProxy_RandomDogImage, RESTfulProxy_AllDogs, \
    RESTfulProxy_ListImagesForBreed, RESTfulProxy_GetImageForSpecificBreedAndSubBreed, \
    RESTfulProxy_GetListOfSubBreedsUsingBreed, RESTfulProxy_GetRandonImageForBreed, \
    RESTfulProxy_ListImagesForSpecificBreedAndSubBreed






urlpatterns = [


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




    url(r'^api/', include('kbot_lab.urls')),
    url(r'^kbot_lab/', include('kbot_lab.urls')),
    url(r'^admin_a9k/', admin.site.urls),
    url(r'^LazarusIV/', include('LazarusIV.urls')),
    url(r'^LazarusV/', include('LazarusV.urls')),

    url(r'^moho_extractor/', include('moho_extractor.urls')),
    url(r'^krogoth_gantry/', include('krogoth_gantry.urls')),
    # url(r'^Forum/', include('CommunityForum.urls')),


    url(r'^ThirdParty/', include('krogoth_3rdparty_api.urls')),


    # user auth, forgot_password, reset pass, etc..
    url(r'^api/', include(router.urls)),

    # url(r'^api/channel-list/', ChannelList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts/', include('allauth.urls')),

    # Admin stuff
    url(r'^djangular_dashboard/', include('djangular_dashboard.urls')),
    url(r'^admin_a9k/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^$', index),
]
