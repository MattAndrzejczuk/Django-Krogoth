from django.conf.urls import url, include
from krogoth_gantry.views.middleware import viewseditor, front_injector
from rest_framework.routers import DefaultRouter
from krogoth_gantry.views.middleware.viewsets import KrogothGantryMasterViewControllerViewSet, KrogothGantrySlaveViewControllerViewSet, \
    KrogothGantryCategoryViewSet, KrogothGantryDirectiveViewSet, KrogothGantryServiceViewSet
from krogoth_gantry.views.index_and_akfoundation import AKFoundationViewSet
from krogoth_gantry.views.middleware.included_html_js_views import IncludedHtmlMasterViewSet, IncludedHtmlCoreViewSet, IncludedJsMasterViewSet


router = DefaultRouter()
router.register(r'MasterViewController',
                KrogothGantryMasterViewControllerViewSet)
router.register(r'SlaveViewController',
                KrogothGantrySlaveViewControllerViewSet)
router.register(r'Category', KrogothGantryCategoryViewSet)
router.register(r'Directive', KrogothGantryDirectiveViewSet)
router.register(r'Service', KrogothGantryServiceViewSet)
router.register(r'IncludedHtmlMaster', IncludedHtmlMasterViewSet)
router.register(r'IncludedHtmlCore', IncludedHtmlCoreViewSet)
router.register(r'IncludedJsMaster', IncludedJsMasterViewSet)
router.register(r'AKFoundation', AKFoundationViewSet)


urlpatterns = [
    url(r'^DynamicJavaScriptInjector/',
        front_injector.DynamicJavaScriptInjector.as_view(),
        name='DynamicJavaScriptInjector'),
    url(r'^DynamicHTMLInjector/',
        front_injector.DynamicHTMLInjector.as_view(),
        name='DynamicHTMLInjector'),
    url(r'^DynamicHTMLSlaveInjector/',
        front_injector.DynamicHTMLSlaveInjector.as_view(),
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
