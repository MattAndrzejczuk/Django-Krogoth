from django.conf.urls import url, include
from krogoth_gantry import views
from krogoth_gantry import viewseditor
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

from krogoth_gantry.viewsets import KrogothGantryMasterViewControllerViewSet, KrogothGantrySlaveViewControllerViewSet, \
    KrogothGantryIconViewSet, \
    KrogothGantryCategoryViewSet, KrogothGantryDirectiveViewSet, KrogothGantryServiceViewSet

from krogoth_core.views import AKFoundationViewSet

from moho_extractor.views import IncludedHtmlMasterViewSet, IncludedHtmlCoreViewSet, IncludedJsMasterViewSet

router.register(r'MasterViewController',
                KrogothGantryMasterViewControllerViewSet)
router.register(r'SlaveViewController',
                KrogothGantrySlaveViewControllerViewSet)
router.register(r'Icon', KrogothGantryIconViewSet)
router.register(r'Category', KrogothGantryCategoryViewSet)
router.register(r'Directive', KrogothGantryDirectiveViewSet)
router.register(r'Service', KrogothGantryServiceViewSet)

router.register(r'IncludedHtmlMaster', IncludedHtmlMasterViewSet)
router.register(r'IncludedHtmlCore', IncludedHtmlCoreViewSet)
router.register(r'IncludedJsMaster', IncludedJsMasterViewSet)

router.register(r'AKFoundation', AKFoundationViewSet)


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


    url(r'^viewsets/', include(router.urls)),
]