from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from krogoth_gantry.views.views_chat import UserViewSet, JawnUserViewSet
from krogoth_gantry.views.index_and_akfoundation import index



router = DefaultRouter()
router.register(r'users', UserViewSet, 'User')
router.register(r'jawn-users', JawnUserViewSet, 'Jawn User')


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
    
    path('admin_a9k/', admin.site.urls),
    path('moho_extractor/', include('krogoth_gantry.routes.urls_akthemes')),
    path('krogoth_gantry/', include('krogoth_gantry.routes.urls_mvc_and_ide')),
    path('krogoth_admin/', include('krogoth_gantry.routes.urls_manager')),
    
    # url(r'^ThirdParty/', include('krogoth_3rdparty_api.urls')),
    path('krogoth_social/', include('krogoth_gantry.routes.urls_forums')),
    
    # user auth, forgot_password, reset pass, etc..
    path('api/', include(router.urls)),
    
    # url(r'^api/channel-list/', ChannelList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    
    # Admin stuff
    path('krogoth_dashboard/', include('krogoth_gantry.routes.resource_dashboard_urls')),


    # generics
    path('generic/', include('krogoth_gantry.routes.urls_generic_features')),

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
