from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from krogoth_admin.views import UncommitedSQLViewSet, SaveSQLToFileSystemView, CompileMVCsToStatic
from krogoth_admin.views_filesystem import RenameService, CreateService, RenameDirective, \
    CreateDirective, RenameTemplate, CreateTemplate, CreateNewMVCView, RenameJavaScriptTemplate, \
    CreateJavaScriptTemplate

from krogoth_admin.views_dashboard import getRam, getProcesses, getProcessesDummy, getStorage, getCPUInfo, getUpTime

router = DefaultRouter()
router.register(r'UncommitedSQL', UncommitedSQLViewSet)

# SaveSQLToFileSystemView

urlpatterns = [
    url(r'^KrogothAdministration/', include(router.urls)),

    url(r'^SaveSQLToFileSystem/$', SaveSQLToFileSystemView.as_view(), name='Save SQL To File System'),
    url(r'^Compile/$', CompileMVCsToStatic.as_view(), name='Compile All MVCs'),

    url(r'^createNewMasterViewController/$', CreateNewMVCView.as_view(), name='Create New MVC View'),

    url(r'^renameAngularJSService/$', RenameService.as_view(), name='Rename AngularJS Service'),
    url(r'^createAngularJSService/$', CreateService.as_view(), name='Create AngularJS Service'),

    url(r'^renameAngularJSDirective/$', RenameDirective.as_view(), name='Rename AngularJS Directive'),
    url(r'^createAngularJSDirective/$', CreateDirective.as_view(), name='Create AngularJS Directive'),

    url(r'^renameAngularJSTemplate/$', RenameTemplate.as_view(), name='Rename AngularJS Template'),
    url(r'^createAngularJSTemplate/$', CreateTemplate.as_view(), name='Create AngularJS Template'),

    url(r'^renameJavaScriptTemplate/$', RenameJavaScriptTemplate.as_view(), name='Rename JavaScript Template'),
    url(r'^createJavaScriptTemplate/$', CreateJavaScriptTemplate.as_view(), name='Create JavaScript Template'),


    # DASHBOARD
    url(r'^ram/$', getRam.as_view(), name='ram'),
    url(r'^processes/$', getProcesses.as_view(), name='processes'),
    url(r'^processesDummy/$', getProcessesDummy.as_view(), name='processesDummy'),
    url(r'^storage/$', getStorage.as_view(), name='processes'),
    url(r'^cpuinfo/$', getCPUInfo.as_view(), name='processes'),
    url(r'^uptime/$', getUpTime.as_view(), name='processes'),
]


