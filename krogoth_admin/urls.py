from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from krogoth_admin.views import UncommitedSQLViewSet, SaveSQLToFileSystemView
from krogoth_admin.views_filesystem import RenameService, CreateService, RenameDirective, \
    CreateDirective, RenameTemplate, CreateTemplate


router = DefaultRouter()
router.register(r'UncommitedSQL', UncommitedSQLViewSet)

# SaveSQLToFileSystemView

urlpatterns = [
    url(r'^KrogothAdministration/', include(router.urls)),

    url(r'^SaveSQLToFileSystem/$', SaveSQLToFileSystemView.as_view(), name='Save SQL To File System'),

    url(r'^renameAngularJSService/$', RenameService.as_view(), name='Rename AngularJS Service'),
    url(r'^createAngularJSService/$', CreateService.as_view(), name='Create AngularJS Service'),

    url(r'^renameAngularJSDirective/$', RenameDirective.as_view(), name='Rename AngularJS Directive'),
    url(r'^createAngularJSDirective/$', CreateDirective.as_view(), name='Create AngularJS Directive'),

    url(r'^renameAngularJSTemplate/$', RenameTemplate.as_view(), name='Rename AngularJS Template'),
    url(r'^createAngularJSTemplate/$', CreateTemplate.as_view(), name='Create AngularJS Template'),
]
