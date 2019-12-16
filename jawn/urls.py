from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from krogoth_gantry.views.views_chat import UserViewSet, JawnUserViewSet, ImageMessageViewSet, TextMessageViewSet, ChannelViewSet, \
    MessageViewSet, PrivateMessageRelationshipSet, RegionViewSet, LinkMessageViewSet, YouTubeMessageViewSet
from krogoth_gantry.views.index_and_akfoundation import index



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

from krogoth_gantry.views.example_views import FruitViewSet, TextLabelViewSet, ManufacturerViewSet, CarViewSet, \
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


urlpatterns = []

registered = [
    

    url(r'^api/', include('kbot_lab.urls')),
    url(r'^kbot_lab/', include('kbot_lab.urls')),
    
    url(r'^admin_a9k/', admin.site.urls),
    # url(r'^djadmin/', include('djadmin.urls')),
    
    url(r'^moho_extractor/', include('krogoth_gantry.routes.urls_akthemes')),
    url(r'^krogoth_gantry/', include('krogoth_gantry.routes.urls_mvc_and_ide')),
    url(r'^krogoth_admin/', include('krogoth_gantry.routes.urls_manager')),
    
    url(r'^ThirdParty/', include('krogoth_3rdparty_api.urls')),
    url(r'^krogoth_social/', include('krogoth_gantry.routes.urls_forums')),
    
    # user auth, forgot_password, reset pass, etc..
    url(r'^api/', include(router.urls)),
    
    # url(r'^api/channel-list/', ChannelList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts/', include('allauth.urls')),
    
    # Admin stuff
    url(r'^krogoth_dashboard/', include('krogoth_gantry.routes.resource_dashboard_urls')),
    
    url(r'^$', index),
]

for url in registered:
    num = 0
    try:
        urlpatterns.append(url)
    except:
        print("❌ URLS FAIL AT INDEX: ", end="")
        print(num)
    num += 1
