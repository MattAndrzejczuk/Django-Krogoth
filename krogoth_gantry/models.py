from django.db import models
import codecs
from jawn.settings import BASE_DIR
from polymorphic.models import PolymorphicModel
from django.utils.html import format_html
from krogoth_admin.global_tasks import LogUsage

DEFAULT_CONTROLLER = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/MasterVC/controller.js', 'r').read()
DEFAULT_MODULE = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/MasterVC/module.js', 'r').read()
DEFAULT_MASTERVIEW = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/MasterVC/view.html', 'r').read()
DEFAULT_STYLETHEME = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/MasterVC/themestyle.css', 'r').read()
DEFAULT_SLAVE_CONTROLLER = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/SlaveVC/controller.js',
                                       'r').read()
DEFAULT_SERVICE = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/Services/MiscExampleService.js',
                              'r').read()
DEFAULT_DIRECTIVE = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/Directives/miscDirective.js', 'r').read()


#     ___________________________________
class KrogothGantryService(models.Model):
    name = models.CharField(max_length=52, unique=True)
    title = models.CharField(max_length=55,
                             default='Untitled krogoth_gantry Service',
                             help_text='Cosmetic display name for this service in the primary navigation view')
    service_js = models.TextField(default=DEFAULT_SERVICE)

    def __str__(self):
        LogUsage("krogoth_gantry", "KrogothGantryService", "__str__")
        return self.name

    def save(self, *args, **kwargs):
        LogUsage("krogoth_gantry", "KrogothGantryService", "save")
        self.service_js = self.service_js
        super(KrogothGantryService, self).save(*args, **kwargs)


#     _____________________________________
class KrogothGantryDirective(models.Model):
    name = models.CharField(max_length=51, unique=True)
    title = models.CharField(max_length=55,
                             default='Untitled krogoth_gantry Directive',
                             help_text='Cosmetic display name for this directive in the primary navigation view')
    directive_js = models.TextField(default=DEFAULT_DIRECTIVE)

    def __str__(self):
        LogUsage("krogoth_gantry", "KrogothGantryDirective", "__str__")
        return self.name

    def save(self, *args, **kwargs):
        LogUsage("krogoth_gantry", "KrogothGantryDirective", "save")
        self.directive_js = self.directive_js
        super(KrogothGantryDirective, self).save(*args, **kwargs)


#     _______________________________________________
class KrogothGantrySlaveViewController(models.Model):
    name = models.CharField(max_length=56, unique=True,
                            help_text='MUST BE EXACT NAME OF MASTER VIEW CONTROLLER.')
    title = models.CharField(max_length=55,
                             default='sideNav',
                             help_text='The name for this slave VC.')
    controller_js = models.TextField(default=DEFAULT_SLAVE_CONTROLLER)
    view_html = models.TextField(default=DEFAULT_MASTERVIEW)

    def __str__(self):
        LogUsage("krogoth_gantry", "KrogothGantrySlaveViewController", "__str__")
        return self.name

    def save(self, *args, **kwargs):
        LogUsage("krogoth_gantry", "KrogothGantrySlaveViewController", "save")
        self.controller_js = self.controller_js
        super(KrogothGantrySlaveViewController, self).save(*args, **kwargs)


#     ________________________________
ICON_TYPES = (
    ('FA', 'Font Awesome'),
    ('MDI', 'Material Design Icon'),
    ('ENTYPO', 'Entypo'),
)


# class KrogothGantryIcon(models.Model):
#     code = models.CharField(max_length=75, unique=True)
#     prefix = models.CharField(max_length=75,
#                               default='FA',
#                               choices=ICON_TYPES,
#                               help_text="The icon type, i.e. font awesome, material design, etc...")
#
#     def __str__(self):
#         return self.code
#
#     def save(self, *args, **kwargs):
#         c = self.code.lower()
#         if "mdi " in c:
#             self.prefix = "MDI"
#         elif "fa " in c or "fas " in c or "far " in c or "fab " in c or "fal " in c:
#             self.prefix = "FA"
#         elif "entypo-" in c:
#             self.prefix = "ENTYPO"
#         print('.', end='')
#         super(KrogothGantryIcon, self).save(*args, **kwargs)


#     ____________________________________
class KrogothGantryCategory(PolymorphicModel):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=55,
                             default='Untitled krogoth_gantry Application',
                             help_text='Cosmetic display name for this app in the primary navigation view')
    weight = models.IntegerField(default=3)
    parent = models.ForeignKey('KrogothGantryCategory', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        LogUsage("krogoth_gantry", "KrogothGantryCategory", "__str__")
        return self.name

    @classmethod
    def get_or_create_catagory(cls, named: str, titled: str):
        LogUsage("krogoth_gantry", "KrogothGantryCategory", "get_or_create_catagory")
        catagory_exists = cls.objects.filter(name=named, title=titled)
        if len(catagory_exists) > 0:
            return catagory_exists.first()
        else:
            cat = cls.objects.create(name=named.replace('.', ''), title=titled)
            cat.save()
            return cat


#     ________________________________________________


class KrogothGantryMasterViewController(PolymorphicModel):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=55,
                             default='Untitled krogoth_gantry Application',
                             help_text='Cosmetic display name for this app in the primary navigation view')
    category = models.ForeignKey(KrogothGantryCategory,
                                 on_delete=models.CASCADE)
    module_js = models.TextField(default=DEFAULT_MODULE)
    controller_js = models.TextField(default=DEFAULT_CONTROLLER)
    view_html = models.TextField(default=DEFAULT_MASTERVIEW)
    style_css = models.TextField(default='/**/')
    themestyle_is_enabled = models.BooleanField(default=True)
    themestyle = models.TextField(default=DEFAULT_STYLETHEME)
    is_enabled = models.BooleanField(default=True,
                                     help_text='When disabled, this javascript code and html code will not be loaded.')
    djangular_service = models.ManyToManyField(KrogothGantryService,
                                               null=True,
                                               blank=True,
                                               related_name='provider')
    djangular_directive = models.ManyToManyField(KrogothGantryDirective,
                                                 null=True,
                                                 blank=True,
                                                 related_name='displayer')
    djangular_slave_vc = models.ManyToManyField(KrogothGantrySlaveViewController,
                                                null=True,
                                                blank=True,
                                                related_name='owner')

    path_to_static = models.CharField(default='NOT_SET', max_length=125)
    is_lazy = models.BooleanField(default=False,
                                  help_text='If lazy, this master view controller will not load until accessed.')

    @property
    def get_theme_style(self):
        LogUsage("krogoth_gantry", "KrogothGantryMasterViewController", "get_theme_style")
        if self.themestyle_is_enabled == True:
            return self.themestyle
        else:
            return '/*THEMESTYLE_DISABLED*/'

    def icon_as_html(self):
        LogUsage("krogoth_gantry", "KrogothGantryMasterViewController", "icon_as_html")
        color = 'style=color:black'
        return format_html('<i {} class="mdi mdi-{}"> </i>', color, self.icon)

    def __str__(self):
        LogUsage("krogoth_gantry", "KrogothGantryMasterViewController", "__str__")
        return self.title

    def get_module_js_compiled(self, old_module: str):
        LogUsage("krogoth_gantry", "KrogothGantryMasterViewController", "get_module_js_compiled")
        subcat = ''
        cat = ''
        if self.category is not None:
            if self.category.parent is not None:
                cat = self.category.parent.name
            subcat = self.category.name

        # if cat == "NO_CAT":
        #     cat_set = old_module.replace('AK_NAVCAT_KROGOTH.', "")
        # else:
        #     cat_set = old_module.replace('AK_NAVCAT_KROGOTH', cat)
        # if subcat == "NO_SUBCAT":
        #     subcat_set = cat_set.replace('AK_SUBCATAGORY_KROGOTH.', "")
        # else:
        #     subcat_set = cat_set.replace('AK_SUBCATAGORY_KROGOTH', subcat)

        cat_set = old_module.replace('AK_NAVCAT_KROGOTH', cat)
        subcat_set = cat_set.replace('AK_SUBCATAGORY_KROGOTH', subcat)
        return subcat_set

    @property
    def compileModuleSlaves(self):
        LogUsage("krogoth_gantry", "KrogothGantryMasterViewController", "compileModuleSlaves")
        djangular_slaves = self.djangular_slave_vc.all()
        slave_controllers_js = ''
        slave__states = []
        msApiProviders = []
        for slave in djangular_slaves:
            CRUD_MODEL = 'SampleModelOneView'
            # slave.name = self.name
            STATE_IDENTIFIER = 'FUSE_APP_NAME.' + slave.name
            STATE_URI = slave.name
            print('dude... wtf...')
            slave_identifier = slave.name + '.' + slave.name  # FUSE_APP_NAME._SLAVE_NAME_
            state_pt_1 = ".state('app." + self.name + "." + slave.name + "', {url: '/" + STATE_URI + "/:id', views: { "
            state_pt_2 = "'content@app': { templateUrl: '/krogoth_gantry/DynamicHTMLSlaveInjector/?name=" + str(
                slave.name) + "', "
            state_pt_3 = " controller: '" + slave.name + "Controller as vm' } "
            state_pt_4 = "  }, resolve: { Model" + slave.name + ": function (msApi) { "
            state_pt_5 = " return msApi.resolve('app." + STATE_IDENTIFIER + "REST@get' "
            state_pt_6 = " ); } } })  "
            msApiStateItem = state_pt_1 + state_pt_2 + state_pt_3 + state_pt_4 + state_pt_5 + state_pt_6
            msApiProvider = "msApiProvider.register('app." + STATE_IDENTIFIER + "REST', ['"
            msApiProvider += "/krogoth_gantry/CRUD/" + CRUD_MODEL + "/:id']);\n"
            slave__states.append(msApiStateItem)
            msApiProviders.append(msApiProvider)
            slave_controllers_js += slave.controller_js.replace('_SLAVE_NAME_', slave.name).replace('FUSE_APP_NAME',
                                                                                                    self.name)
            slave_controllers_js += '\n'

        statesAsString = ''
        providersAsString = ''
        for state in slave__states:
            statesAsString += state

        for provider in msApiProviders:
            providersAsString += provider

        module_with_injected_msApi = self.module_js.replace('_DJANGULAR_SLAVE_VC_INJECTION_POINT_', statesAsString)
        module_with_injected_msApi_2 = module_with_injected_msApi.replace('_DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_',
                                                                          providersAsString)

        newMsNavSrv = ''
        for slave in djangular_slaves:
            parse_1 = "msNavigationServiceProvider.saveItem('FUSE_APP_NAME." + slave.name + "', { "
            parse_2 = "	title: '" + slave.title + "', "
            parse_3 = " icon: 'icon-bullet', "
            parse_4 = " state: 'app.FUSE_APP_NAME." + slave.name + "', "
            parse_5 = " weight: 3 }); "
            newMsNavSrv += parse_1 + parse_2 + parse_3 + parse_4 + parse_5
            newMsNavSrv += '\n'
            print(newMsNavSrv)

        module_with_injected_navigation = module_with_injected_msApi_2.replace(
            '_DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_', newMsNavSrv)
        return_obj = {}
        return_obj['slave_controllers_js'] = slave_controllers_js
        return_obj['module_with_injected_navigation'] = self.get_module_js_compiled(
            old_module=module_with_injected_navigation)
        return return_obj

    def save(self, *args, **kwargs):
        # self.module_js = self.module_js
        # self.controller_js = self.controller_js
        LogUsage("krogoth_gantry", "KrogothGantryMasterViewController", "save")
        super(KrogothGantryMasterViewController, self).save(*args, **kwargs)


class AKGantryMasterViewController(KrogothGantryMasterViewController):
    class Meta:
        proxy = True
