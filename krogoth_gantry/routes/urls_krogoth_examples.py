
from krogoth_gantry.views.other.generic_contact_form import GenericContactViewCreate, GenericContactViewDetail, \
    GenericContactViewListAll
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from krogoth_gantry.views import forum_views
# AKThreadSocialMediaViewSet
from django.conf.urls import url
from krogoth_gantry.views import resource_dashboard

router_forums = DefaultRouter()

router_forums.register(r'AKThread', forum_views.AKThreadViewSet, 'AKThreadViewSets')
router_forums.register(r'AKThreadCategory', forum_views.AKThreadCategoryViewSet, 'AKThreadCategoryViewSet')
router_forums.register(r'AKThreadSocialMedia', forum_views.AKThreadSocialMediaViewSet, 'AKThreadSocialMediaViewSet')
router_forums.register(r'AKThreadSocialMediaReply', forum_views.AKThreadSocialMediaReplyViewSet, 'AKThreadSocialMediaReply')
router_forums.register(r'ForumThreadCategory', forum_views.ForumThreadCategoryViewSet, 'Forum Thread Category')
router_forums.register(r'ForumThreadOP', forum_views.ForumThreadOPViewSet, 'Forum Thread OP')
router_forums.register(r'ForumThreadReply', forum_views.ForumThreadReplyViewSet, 'Forum Thread Reply')

router_examples = DefaultRouter()
from krogoth_gantry.views.example_views import FruitViewSet, TextLabelViewSet, ManufacturerViewSet, CarViewSet, \
    ToppingViewSet, PizzaViewSet, HotelViewSet, OccupantViewSet, \
    BasicImageUploadViewSet, BasicFileUploadViewSet

router_examples.register(r'__ExamplesFruit', FruitViewSet, 'Fruit')
router_examples.register(r'__ExamplesTextLabel', TextLabelViewSet, 'TextLabel')
router_examples.register(r'__ExamplesManufacturer', ManufacturerViewSet, 'Manufacturer')
router_examples.register(r'__ExamplesCar', CarViewSet, 'Car')
router_examples.register(r'__ExamplesTopping', ToppingViewSet, 'Topping')
router_examples.register(r'__ExamplesPizza', PizzaViewSet, 'Pizza')
router_examples.register(r'__ExamplesHotel', HotelViewSet, 'Hotel')
router_examples.register(r'__ExamplesOccupant', OccupantViewSet, 'Occupant')
router_examples.register(r'__ExamplesBasicImageUpload', BasicImageUploadViewSet, 'BasicImageUpload')
router_examples.register(r'__ExamplesBasicFileUpload', BasicFileUploadViewSet, 'BasicFileUpload')


urlpatterns = [
    # FORUMS
    path('forum_viewsets/', include(router_forums.urls)),
    path('AKThreadListView/', forum_views.AKThreadListView.as_view()),
    path('manual_post_method/', forum_views.manual_post_method.as_view()),
    path('manual_post_reply/', forum_views.manual_post_reply.as_view()),

    # DB SAMPLES
    path('simple_api/', include(router_examples.urls)),

    # CONTACT FORM
    path('contact/create/', GenericContactViewCreate.as_view()),
    path('contact/list/', GenericContactViewListAll.as_view()),
    path('contact/detail/<int:id>/', GenericContactViewDetail.as_view()),

    # RESOURCE MONITORING DASHBOARD
    url(r'^ram/$', resource_dashboard.getRam.as_view(), name='ram'),
    url(r'^processes/$', resource_dashboard.getProcesses.as_view(), name='processes'),
    url(r'^processesDummy/$', resource_dashboard.getProcessesDummy.as_view(), name='processesDummy'),
    url(r'^storage/$', resource_dashboard.getStorage.as_view(), name='processes'),
    url(r'^cpuinfo/$', resource_dashboard.getCPUInfo.as_view(), name='processes'),
    url(r'^uptime/$', resource_dashboard.getUpTime.as_view(), name='processes'),
]
