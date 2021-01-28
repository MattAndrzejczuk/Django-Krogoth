from django.conf.urls import url, include
from krogoth_gantry.views.middleware import viewseditor, front_injector
from rest_framework.routers import DefaultRouter
from krogoth_gantry.views.middleware.viewsets import KrogothGantryMasterViewControllerViewSet, KrogothGantrySlaveViewControllerViewSet, \
    KrogothGantryCategoryViewSet, KrogothGantryDirectiveViewSet, KrogothGantryServiceViewSet
from krogoth_gantry.views import index_and_akfoundation
from krogoth_gantry.views import included_html_js_views

from django.urls import path

from krogoth_gantry.views import manager_filesystem, manager_tasks
#####   THIS WAS FORMALLY URLS_MVC_AND_IDE.PY


router = DefaultRouter()
router.register(r'MasterViewController',
                KrogothGantryMasterViewControllerViewSet)
router.register(r'SlaveViewController',
                KrogothGantrySlaveViewControllerViewSet)
router.register(r'Category', KrogothGantryCategoryViewSet)
router.register(r'Directive', KrogothGantryDirectiveViewSet)
router.register(r'Service', KrogothGantryServiceViewSet)
router.register(r'IncludedHtmlMaster', included_html_js_views.IncludedHtmlMasterViewSet)
router.register(r'IncludedHtmlCore', included_html_js_views.IncludedHtmlCoreViewSet)
router.register(r'IncludedJsMaster', included_html_js_views.IncludedJsMasterViewSet)
router.register(r'AKFoundation', index_and_akfoundation.AKFoundationViewSet)

routerUncommitedSQL = DefaultRouter()
routerUncommitedSQL.register(r'UncommitedSQL', UncommitedSQLViewSet)

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

    path('KrogothAdministration/', include(routerUncommitedSQL.urls)),

    path('SaveSQLToFileSystem/', manager_tasks.SaveSQLToFileSystemView.as_view(), name='Save SQL To File System'),
    path('CollectStatic/', manager_tasks.CollectStatic.as_view(), name='Collect Static Files'),
    path('Compile/', manager_tasks.CompileMVCsToStatic.as_view(), name='Compile All MVCs'),

    path('createNewMasterViewController/', manager_filesystem.CreateNewMVCView.as_view(), name='Create New MVC View'),
    path('renameAngularJSService/', manager_filesystem.RenameService.as_view(), name='Rename AngularJS Service'),
    path('createAngularJSService/', manager_filesystem.CreateService.as_view(), name='Create AngularJS Service'),
    path('renameAngularJSDirective/', manager_filesystem.RenameDirective.as_view(), name='Rename AngularJS Directive'),
    path('createAngularJSDirective/', manager_filesystem.CreateDirective.as_view(), name='Create AngularJS Directive'),
    path('renameAngularJSTemplate/', manager_filesystem.RenameTemplate.as_view(), name='Rename AngularJS Template'),
    path('createAngularJSTemplate/', manager_filesystem.CreateTemplate.as_view(), name='Create AngularJS Template'),
    path('renameJavaScriptTemplate/', manager_filesystem.RenameJavaScriptTemplate.as_view(), name='Rename JavaScript Template'),
    path('createJavaScriptTemplate/', manager_filesystem.CreateJavaScriptTemplate.as_view(), name='Create JavaScript Template'),

]