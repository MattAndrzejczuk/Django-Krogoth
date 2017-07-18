from django.conf.urls import url, include
from Djangular import views



from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'^SampleModelOneView', views.SampleModelOneView)



urlpatterns = [
    url(r'^$', views.index),
    url(r'^DynamicJavaScriptInjector/', views.DynamicJavaScriptInjector.as_view(), name='DynamicJavaScriptInjector'),
    url(r'^DynamicHTMLInjector/', views.DynamicHTMLInjector.as_view(), name='DynamicHTMLInjector'),

    url(r'^DynamicJavaScriptSlaveInjector/(?P<id>[0-9]+)/', views.DynamicJavaScriptSlaveInjector.as_view(),
        name='Dynamic JavaScript Slave Injector'),
    url(r'^DynamicHTMLSlaveInjector/(?P<id>[0-9]+)/', views.DynamicHTMLSlaveInjector.as_view(), name='Dynamic HTML Slave Injector'),

    url(r'^CRUD/', include(router.urls)),
]
