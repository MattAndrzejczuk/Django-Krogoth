from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from krogoth_admin.views import UncommitedSQLViewSet
from krogoth_admin.views_filesystem import RenameService, CreateService, RenameDirective, RenameTemplate


router = DefaultRouter()
router.register(r'UncommitedSQL', UncommitedSQLViewSet)



# from rest_auth.views import (
#     LoginView, LogoutView, UserDetailsView, PasswordChangeView,
#     PasswordResetView, PasswordResetConfirmView, RegisterUserBasic
# )


urlpatterns = [
    url(r'^KrogothAdministration/', include(router.urls)),
    url(r'^renameAngularJSService/$', RenameService.as_view(), name='Rename AngularJS Module'),
    url(r'^createAngularJSService/$', CreateService.as_view(), name='Create AngularJS Service'),
]
