from django.db import models
import jsbeautifier
import xml.dom.minidom
from polymorphic.models import PolymorphicModel
# Create your models here.
from krogoth_gantry.models import KrogothGantryMasterViewController

DEFAULT_CONTROLLER = "(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController); \n\n\tfunction FUSE_APP_NAMEController() \n\t{ \n\t\t\tvar vm = this; \n\t\t\tvm.helloText = 'Welcome to FUSE_APP_NAME';   \n\t} \n})();"
DEFAULT_MODULE = "(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME', ['flow']).config(config); \n\n\tfunction config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) { \n\t$stateProvider.state('app.FUSE_APP_NAME', { \n\t\turl: '/FUSE_APP_NAME', \n\t\tviews: { \n\t\t\t'content@app': { \n\t\t\t\ttemplateUrl: '/moho_extractor/DynamicHTMLInjector/?name=FUSE_APP_NAME', \n\t\t\t\tcontroller: 'FUSE_APP_NAMEController as vm'\n\t\t\t}\n\t\t}, \n\t\tbodyClass: 'file-manager' \n\t}); \n\tmsNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', { \n\t\ttitle: 'FUSE_APP_TITLE', \n\t\ticon: 'FUSE_APP_ICON', \n\t\tstate: 'app.FUSE_APP_NAME', \n\t\tweight: 3 \n\t});    \n\t} \n})();"



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




class VisitorLog(models.Model):
    date_created = models.DateTimeField(auto_created=True)
    remote_addr = models.CharField(max_length=255, blank=True, null=True)
    http_usr = models.CharField(max_length=255, blank=True, null=True)
    http_accept = models.CharField(max_length=255, blank=True, null=True)

class NgIncludedHtml(PolymorphicModel):
    name = models.CharField(max_length=255, unique=True)
    contents = models.TextField(default='<h4> krogoth_gantry Error: There is nothing here yet! </h4>')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='krogoth_gantry will take care of this.')

    def save(self, *args, **kwargs):
        self.url_helper = '/moho_extractor/NgIncludedHtml/?name=' + self.name

        super(NgIncludedHtml, self).save(*args, **kwargs)




class NgIncludedJs(PolymorphicModel):
    name = models.CharField(max_length=255, unique=True)
    contents = models.TextField(default='<h4> krogoth_gantry Error: There is nothing here yet! </h4>')
    url_helper = models.CharField(max_length=255,
                                  default='Dont worry about this text.',
                                  help_text='krogoth_gantry will take care of this.')

    def save(self, *args, **kwargs):
        self.url_helper = '/moho_extractor/NgIncludedJs/?name=' + self.name
        self.contents = jsbeautifier.beautify(self.contents)
        super(NgIncludedJs, self).save(*args, **kwargs)


class IncludedJsMaster(NgIncludedJs):
    master_vc = models.ForeignKey(KrogothGantryMasterViewController,
                                  on_delete=models.CASCADE,
                                  related_name='partial_js')


class IncludedHtmlMaster(NgIncludedHtml):
    sys_path = models.CharField(max_length=256, default='/usr/src/app/')
    master_vc = models.ForeignKey(KrogothGantryMasterViewController, on_delete=models.CASCADE,
                                  related_name='partial_html')