from django.db import models
import jsbeautifier
# Create your models here.

from LazarusII.PyColors import printError, printInfo, printWarning, printLog, printDebug

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
    name = models.CharField(max_length=255, help_text='please use "_" instead of spaces!')
    category = models.CharField(max_length=30, default='Resources')
    js_module = models.TextField(default=DEFAULT_MODULE.replace('; ', '; \n'))
    js_controller = models.TextField(default=DEFAULT_CONTROLLER.replace('; ', '; \n'))
    html_main = models.TextField(default='<h1>Djangular Lazarus</h1>')
    icon = models.CharField(choices=ICONS, max_length=50, default='icon-hexagon-outline')
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        print('Saving AngularFuseApplication')
        print(self.name)
        self.name = self.name.replace(' ', '_')
        self.js_module = jsbeautifier.beautify(self.js_module)
        self.js_controller = jsbeautifier.beautify(self.js_controller)
        super(AngularFuseApplication, self).save(*args, **kwargs)



class FuseAppComponent(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100) ### .HTML .JS .CSS     etc...
    parent_app = models.ForeignKey(AngularFuseApplication, on_delete=models.CASCADE,)
    contents = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print('Saving FuseAppComponent')
        print(self.name)
        self.contents = jsbeautifier.beautify(self.contents)
        super(AngularFuseApplication, self).save(*args, **kwargs)




class VisitorLog(models.Model):
    date_created = models.DateTimeField(auto_created=True)
    remote_addr = models.CharField(max_length=255, blank=True, null=True)
    http_usr = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=255, blank=True, null=True)




class NgIncludedHtml(models.Model):
    name = models.CharField(max_length=255)
    contents = models.TextField(default='<h4> Djangular Error: There is nothing here yet! </h4>')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='Djangular will take care of this.')

    def save(self, *args, **kwargs):
        self.url_helper = '/dynamic_lazarus_page/NgIncludedHtml/?name=' + self.name
        super(NgIncludedHtml, self).save(*args, **kwargs)
