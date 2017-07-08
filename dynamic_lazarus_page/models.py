from django.db import models
# Create your models here.
from django.contrib.auth.models import User


DEFAULT_CONTROLLER = "(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController); \n\n\tfunction FUSE_APP_NAMEController() \n\t{ \n\t\t\tvar vm = this; \n\t\t\tvm.helloText = 'Welcome to FUSE_APP_NAME';   \n\t} \n})();"
DEFAULT_MODULE = "(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME', ['flow']).config(config); \n\n\tfunction config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) { \n\t$stateProvider.state('app.FUSE_APP_NAME', { \n\t\turl: '/FUSE_APP_NAME', \n\t\tviews: { \n\t\t\t'content@app': { \n\t\t\t\ttemplateUrl: '/dynamic_lazarus_page/DynamicHTMLInjector/?name=FUSE_APP_NAME', \n\t\t\t\tcontroller: 'FUSE_APP_NAMEController as vm'\n\t\t\t}\n\t\t}, \n\t\tbodyClass: 'file-manager' \n\t}); \n\tmsNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', { \n\t\ttitle: 'FUSE_APP_TITLE', \n\t\ticon: 'FUSE_APP_ICON', \n\t\tstate: 'app.FUSE_APP_NAME', \n\t\tweight: 3 \n\t});    \n\t} \n})();"



ICONS = (
    ('icon-cloud', 'icon-cloud'),
    ('icon-cube', 'icon-cube'),
    ('icon-cube-outline', 'icon-cube-outline'),
    ('icon-cog', 'icon-cog'),
    ('icon-hexagon-outline', 'icon-hexagon-outline'),
    ('icon-hexagon', 'icon-hexagon'),
    ('icon-home', 'icon-home'),
    ('icon-harddisk', 'icon-harddisk'),
    ('icon-view-list', 'icon-view-list'),
    ( 'icon-terrain','Terrain'),
    ( 'icon-dice','Terrain'),
    ( 'icon-help','Question Mark'),
    ('icon-layers','Layers Cube' ),
    ( 'icon-memory','Memory Chip'),
    ( 'icon-package-variant-closed','Package Cube Closed'),
    ( 'icon-package-variant','Package Opened'),

    ('icon-view-agenda','Data Agenda' ),
    ( 'icon-view-array','Data Array'),
    ('icon-view-carousel','Data Carousel' ),
    ( 'icon-view-column','Data Column'),
    ( 'icon-view-dashboard','Data Dashboard'),
    ( 'icon-view-day','Data Day'),
    ( 'icon-view-headline','Data Headline'),
    ( 'icon-view-list','Data List'),
    ( 'icon-view-module','Data Module'),
    ( 'icon-view-quilt','Data Quilt'),
    ( 'icon-view-stream','Data Stream'),
    ('icon-view-week','Data Week' ),
    ('icon-web','Web Globe Atlas' ),

    ('icon-ubuntu', 'icon-ubuntu'),
    ('icon-linux', 'icon-linux'),
    ('icon-apple', 'icon-apple'),
    ('icon-windows', 'icon-windows'),
)


class AngularFuseApplication(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=30, default='Resources')
    js_module = models.TextField(default=DEFAULT_MODULE.replace('; ', '; \n'))
    js_controller = models.TextField(default=DEFAULT_CONTROLLER.replace('; ', '; \n'))
    icon = models.CharField(choices=ICONS, max_length=50, default='icon-hexagon-outline')
    def __str__(self):
        return self.name

class FuseAppComponent(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100) ### .HTML .JS .CSS     etc...
    parent_app = models.ForeignKey(AngularFuseApplication, on_delete=models.CASCADE,)
    contents = models.TextField()
    def __str__(self):
        return self.name

class FuseApplicationComponent(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100) ### .HTML .JS .CSS     etc...
    parent_app = models.ForeignKey(AngularFuseApplication, on_delete=models.CASCADE,)
    contents = models.TextField()


class VisitorLog(models.Model):
    date_created = models.DateTimeField(auto_created=True)
    remote_addr = models.CharField(max_length=255, blank=True, null=True)
    http_usr = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=255, blank=True, null=True)

FACTIONS = (
    ('Arm', 'Arm'),
    ('Core', 'Core'),
)
class LazarusCommanderAccount(models.Model):
    user = models.ForeignKey(User, unique=True)
    is_suspended = models.BooleanField(default=False)
    is_terminated = models.BooleanField(default=False)
    faction = models.CharField(choices=FACTIONS, max_length=25)
    profile_pic = models.CharField(max_length=255)
    about_me = models.CharField(max_length=75)


class LazarusModProject(models.Model):
    unique_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    date_created = models.DateTimeField(auto_created=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(User, unique=True)






















######################
##  USELESS STUFF:  ##
######################
class SuperBasicModel(models.Model):
    basic_string = models.CharField(max_length=100)
    basic_bool = models.BooleanField(default=False)
    basic_int = models.IntegerField()


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')