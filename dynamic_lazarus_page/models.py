from django.db import models
# Create your models here.
from django.contrib.auth.models import User

DEFAULT_MODULE = '(function(){"use strict";function a(a,t,e,_){a.state("app.FUSE_APP_NAME",{url:"/FUSE_APP_NAME",views:{"content@app":{templateUrl:"/dynamic_lazarus_page/DynamicHTMLInjector/?name=FUSE_APP_NAME",controller:"FUSE_APP_NAMEController as vm"}},bodyClass:"file-manager"}),_.saveItem("apps.FUSE_APP_NAME",{title:"FUSE_APP_TITLE",icon:"icon-star",state:"app.FUSE_APP_NAME",weight:5})}angular.module("app.FUSE_APP_NAME",["flow"]).config(a)}();'
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
    ('icon-terrain', 'icon-terrain'),
    ('icon-dice', 'icon-dice'),
    ('icon-help', 'icon-help'),
    ('icon-ubuntu', 'icon-ubuntu'),
    ('icon-linux', 'icon-linux'),
    ('icon-apple', 'icon-apple'),
    ('icon-windows', 'icon-windows'),
)

class SuperBasicModel(models.Model):
    basic_string = models.CharField(max_length=100)
    basic_bool = models.BooleanField(default=False)
    basic_int = models.IntegerField()


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')


class AngularFuseApplication(models.Model):
    # def __str__(self):
    #     return self.name
    name = models.CharField(max_length=255)
    js_module = models.TextField(default=DEFAULT_MODULE)
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