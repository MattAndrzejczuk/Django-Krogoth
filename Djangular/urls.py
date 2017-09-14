from django.conf.urls import url, include
from Djangular import views
from Djangular import viewseditor


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

    url(r'^MasterViewControllerEditorList/',
        viewseditor.MasterViewControllerEditorListView.as_view(),
        name='Master View Controller Editor List'),
    url(r'^MasterViewControllerEditorDetail/',
        viewseditor.MasterViewControllerEditorDetailView.as_view(),
        name='Master View Controller Editor Detail'),

    url(r'^SlaveViewControllerEditorList/',
        viewseditor.SlaveViewControllerEditorListView.as_view(),
        name='Slave View Controller Editor List'),
    url(r'^SlaveViewControllerEditorDetail/',
        viewseditor.SlaveViewControllerEditorDetailView.as_view(),
        name='Slave View Controller Editor Detail'),

    url(r'^DjangularModelForm/',
        views.DjangularModelForm.as_view(),
        name='Djangular Model Form'),
]
