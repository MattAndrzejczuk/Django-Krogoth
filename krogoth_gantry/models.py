from django.db import models
import jsbeautifier
import xml.dom.minidom



DEFAULT_CONTROLLER = "(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController); \n\tfunction FUSE_APP_NAMEController() \n\t{ \n\t\t\tvar vm = this; \n\t\t\t vm.viewName = 'FUSE_APP_NAME'; \n\t} \n})();"
DEFAULT_MODULE = "(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME', ['flow']).config(config); \n\n\tfunction config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) { \n\t$stateProvider\n\t.state('app.FUSE_APP_NAME', { \n\t\turl: '/FUSE_APP_NAME', \n\t\tviews: { \n\t\t\t'content@app': { \n\t\t\t\ttemplateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME', \n\t\t\t\tcontroller: 'FUSE_APP_NAMEController as vm'\n\t\t\t}\n\t\t} \n\t})  \n\t_DJANGULAR_SLAVE_VC_INJECTION_POINT_; /* krogoth_gantry Slave VCs automatically injected here. */\n\t_DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_ \n\tmsNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', { \n\t\ttitle: 'FUSE_APP_TITLE', \n\t\ticon: 'FUSE_APP_ICON', \n\t\tstate: 'app.FUSE_APP_NAME', \n\t\tweight: 3 \n\t});  _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_  \n\t} \n})();"
DEFAULT_MASTERVIEW = "<h1>{{ vm.viewName }}</h1>"

DEFAULT_SLAVE_CONTROLLER = "(function () \n{ \n\t'use strict'; \n\tangular.module('app.FUSE_APP_NAME').controller('_SLAVE_NAME_Controller', _SLAVE_NAME_Controller); \n\tfunction _SLAVE_NAME_Controller($stateParams, $log) \n\t{ \n\t\t\tvar vm = this; \n\t\t\t vm.viewName = '_SLAVE_NAME_' + $stateParams.id;  \n\t} \n})();"


DEFAULT_SERVICE = "(function ()\n{\n\t'use strict';\n\tangular\n\t\t.module('app.FUSE_APP_NAME')\n\t\t.factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);\n\t/** @ngInject */\n\tfunction _DJANGULAR_SERVICE_NAME_($log)\n\t{\n\t\t$log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');\n\n\t\tvar service = {\n\t\t\ttestThisService: testThisService\n\t\t};\n\nfunction testThisService()\n\t\t{\n\t\t\t$log.log('_DJANGULAR_SERVICE_NAME_ is working properly.');\n\t\t}\n\t\treturn service;\n\t}\n})();"
DEFAULT_DIRECTIVE = "(function ()\n{\n\t'use strict';\n\tangular\n\t\t.module('app.FUSE_APP_NAME')\n\t\t.directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);\n\t/** @ngInject */\n\tfunction _DJANGULAR_DIRECTIVE_NAME_Directive()\n\t{\n\t\treturn {restrict: 'AE',replace: 'true',template: '_DJANGULAR_DIRECTIVE_TITLE_'};\n\n\t}})\n();"


class krogoth_gantryService(models.Model):
    name = models.CharField(max_length=25, unique=True)
    title = models.CharField(max_length=55, default='Untitled krogoth_gantry Service',
                             help_text='Cosmetic display name for this service in the primary navigation view')
    service_js = models.TextField(default=DEFAULT_SERVICE)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.service_js = jsbeautifier.beautify(self.service_js)
        super(krogoth_gantryService, self).save(*args, **kwargs)



class krogoth_gantryDirective(models.Model):
    name = models.CharField(max_length=25, unique=True)
    title = models.CharField(max_length=55, default='Untitled krogoth_gantry Directive',
                             help_text='Cosmetic display name for this directive in the primary navigation view')
    directive_js = models.TextField(default=DEFAULT_DIRECTIVE)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.directive_js = jsbeautifier.beautify(self.directive_js)
        super(krogoth_gantryDirective, self).save(*args, **kwargs)



class krogoth_gantrySlaveViewController(models.Model):
    name = models.CharField(max_length=25, unique=True, help_text='MUST BE EXACT NAME OF MASTER VIEW CONTROLLER.')
    title = models.CharField(max_length=55, default='sideNav',
                             help_text='The name for this slave VC.')
    controller_js = models.TextField(default=DEFAULT_SLAVE_CONTROLLER)
    view_html = models.TextField(default=DEFAULT_MASTERVIEW)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.controller_js = jsbeautifier.beautify(self.controller_js)
        super(krogoth_gantrySlaveViewController, self).save(*args, **kwargs)




class krogoth_gantryIcon(models.Model):
    name = models.CharField(max_length=25, unique=True)
    code = models.CharField(max_length=75, unique=True)
    def __str__(self):
        return self.name



class krogoth_gantryCategory(models.Model):
    name = models.CharField(max_length=25, unique=True)
    # code = models.CharField(max_length=75, unique=True)
    def __str__(self):
        return self.name



class krogoth_gantryMasterViewController(models.Model):
    name = models.CharField(max_length=25, unique=True)

    title = models.CharField(max_length=55, default='Untitled krogoth_gantry Application',
                             help_text='Cosmetic display name for this app in the primary navigation view')

    icon = models.ForeignKey(krogoth_gantryIcon,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(krogoth_gantryCategory,
                                 on_delete=models.CASCADE)

    module_js = models.TextField(default=DEFAULT_MODULE)
    controller_js = models.TextField(default=DEFAULT_CONTROLLER)
    view_html = models.TextField(default=DEFAULT_MASTERVIEW)

    is_enabled = models.BooleanField(default=True,
                                     help_text='When disabled, this javascript code and html code will not be loaded.')

    djangular_service = models.ManyToManyField(krogoth_gantryService, null=True, blank=True)
    djangular_directive = models.ManyToManyField(krogoth_gantryDirective, null=True, blank=True)
    djangular_slave_vc = models.ManyToManyField(krogoth_gantrySlaveViewController, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.module_js = jsbeautifier.beautify(self.module_js)
        self.controller_js = jsbeautifier.beautify(self.controller_js)

        super(krogoth_gantryMasterViewController, self).save(*args, **kwargs)




class SampleModelOne(models.Model):
    name = models.CharField(max_length=75, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name


