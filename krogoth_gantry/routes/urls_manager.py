from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from krogoth_gantry.views.manager_tasks import UncommitedSQLViewSet, SaveSQLToFileSystemView, CompileMVCsToStatic, CollectStatic
from krogoth_gantry.views.manager_filesystem import RenameService, CreateService, RenameDirective, \
    CreateDirective, RenameTemplate, CreateTemplate, CreateNewMVCView, RenameJavaScriptTemplate, \
    CreateJavaScriptTemplate


router = DefaultRouter()
router.register(r'UncommitedSQL', UncommitedSQLViewSet)

# SaveSQLToFileSystemView

urlpatterns = [
    path('KrogothAdministration/', include(router.urls)),

    path('SaveSQLToFileSystem/', SaveSQLToFileSystemView.as_view(), name='Save SQL To File System'),
    path('CollectStatic/', CollectStatic.as_view(), name='Collect Static Files'),
    path('Compile/', CompileMVCsToStatic.as_view(), name='Compile All MVCs'),

    path('createNewMasterViewController/', CreateNewMVCView.as_view(), name='Create New MVC View'),

    path('renameAngularJSService/', RenameService.as_view(), name='Rename AngularJS Service'),
    path('createAngularJSService/', CreateService.as_view(), name='Create AngularJS Service'),

    path('renameAngularJSDirective/', RenameDirective.as_view(), name='Rename AngularJS Directive'),
    path('createAngularJSDirective/', CreateDirective.as_view(), name='Create AngularJS Directive'),

    path('renameAngularJSTemplate/', RenameTemplate.as_view(), name='Rename AngularJS Template'),
    path('createAngularJSTemplate/', CreateTemplate.as_view(), name='Create AngularJS Template'),

    path('renameJavaScriptTemplate/', RenameJavaScriptTemplate.as_view(), name='Rename JavaScript Template'),
    path('createJavaScriptTemplate/', CreateJavaScriptTemplate.as_view(), name='Create JavaScript Template'),



]


