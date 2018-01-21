from django.conf.urls import url, include
from krogoth_gantry import views
from krogoth_gantry import viewseditor
from rest_framework.routers import DefaultRouter
# from rest_framework.routers import DefaultRouter
router = DefaultRouter()

from krogoth_gantry.views import KrogothGantryMasterViewControllerViewSet, KrogothGantrySlaveViewControllerViewSet, \
    KrogothGantryIconViewSet, \
    KrogothGantryCategoryViewSet, KrogothGantryDirectiveViewSet, KrogothGantryServiceViewSet

from krogoth_core.views import AKFoundationViewSet

router.register(r'MasterViewController',
                KrogothGantryMasterViewControllerViewSet)
router.register(r'SlaveViewController',
                KrogothGantrySlaveViewControllerViewSet)
router.register(r'Icon', KrogothGantryIconViewSet)
router.register(r'Category', KrogothGantryCategoryViewSet)
router.register(r'Directive', KrogothGantryDirectiveViewSet)
router.register(r'Service', KrogothGantryServiceViewSet)



urlpatterns = [
    url(r'^DynamicJavaScriptInjector/',
        views.DynamicJavaScriptInjector.as_view(),
        name='DynamicJavaScriptInjector'),
    url(r'^DynamicHTMLInjector/',
        views.DynamicHTMLInjector.as_view(),
        name='DynamicHTMLInjector'),
    url(r'^DynamicHTMLSlaveInjector/',
        views.DynamicHTMLSlaveInjector.as_view(),
        name='Dynamic HTML Slave Injector'),
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
    url(r'^AKFoundation/',
        viewseditor.AKFoundationViewSet.as_view(),
        name='AKFoundation Editor Detail'),
    url(r'^krogoth_gantryModelForm/',
        views.krogoth_gantryModelForm.as_view(),
        name='krogoth_gantry Model Form'),

    url(r'^viewsets/', include(router.urls)),
]