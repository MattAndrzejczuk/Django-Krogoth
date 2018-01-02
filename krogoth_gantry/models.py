from django.db import models
import jsbeautifier
import codecs
from jawn.settings import BASE_DIR
from polymorphic.models import PolymorphicModel

DEFAULT_CONTROLLER = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/MasterVC/controller.js', 'r').read()
DEFAULT_MODULE = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/MasterVC/module.js', 'r').read()
DEFAULT_MASTERVIEW = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/MasterVC/view.html', 'r').read()
DEFAULT_SLAVE_CONTROLLER = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/SlaveVC/controller.js', 'r').read()
DEFAULT_SERVICE = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/Services/MiscExampleService.js', 'r').read()
DEFAULT_DIRECTIVE = codecs.open(BASE_DIR + '/krogoth_gantry/DVCManager/MiscDVC/Directives/miscDirective.js', 'r').read()

#     ___________________________________
class KrogothGantryService(models.Model):
    name = models.CharField(max_length=52, unique=True)
    title = models.CharField(max_length=55,
                             default='Untitled krogoth_gantry Service',
                             help_text='Cosmetic display name for this service in the primary navigation view')
    service_js = models.TextField(default=DEFAULT_SERVICE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.service_js = jsbeautifier.beautify(self.service_js)
        super(KrogothGantryService, self).save(*args, **kwargs)

#     _____________________________________
class KrogothGantryDirective(models.Model):
    name = models.CharField(max_length=51, unique=True)
    title = models.CharField(max_length=55,
                             default='Untitled krogoth_gantry Directive',
                             help_text='Cosmetic display name for this directive in the primary navigation view')
    directive_js = models.TextField(default=DEFAULT_DIRECTIVE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.directive_js = jsbeautifier.beautify(self.directive_js)
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
        return self.name

    def save(self, *args, **kwargs):
        self.controller_js = jsbeautifier.beautify(self.controller_js)
        super(KrogothGantrySlaveViewController, self).save(*args, **kwargs)

#     ________________________________
class KrogothGantryIcon(models.Model):
    code = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.code

#     ____________________________________
class KrogothGantryCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

#     ________________________________________________

from django.utils.html import format_html

class KrogothGantryMasterViewController(PolymorphicModel):
    name = models.CharField(max_length=50, unique=True)

    title = models.CharField(max_length=55,
                             default='Untitled krogoth_gantry Application',
                             help_text='Cosmetic display name for this app in the primary navigation view')
    icon = models.ForeignKey(KrogothGantryIcon,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True)
    category = models.ForeignKey(KrogothGantryCategory,
                                 on_delete=models.CASCADE)

    module_js = models.TextField(default=DEFAULT_MODULE)
    controller_js = models.TextField(default=DEFAULT_CONTROLLER)
    view_html = models.TextField(default=DEFAULT_MASTERVIEW)
    style_css = models.TextField(default='')

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

    def icon_as_html(self):
        color = 'style=color:black'
        return format_html('<i {} class="mdi mdi-{}"> </i>', color, self.icon)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.module_js = jsbeautifier.beautify(self.module_js)
        self.controller_js = jsbeautifier.beautify(self.controller_js)
        super(KrogothGantryMasterViewController, self).save(*args, **kwargs)


class AKGantryMasterViewController(KrogothGantryMasterViewController):
    class Meta:
        proxy = True