# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.db import models
from polymorphic.models import PolymorphicModel
import codecs

# Create your models here.

class AKFoundationAbstract(PolymorphicModel):
    class Meta:
        abstract = True

    name = models.CharField(max_length=140,
                            help_text='EXAMPLES: index.controller index.route toolbar.module theming.service')
    code = models.TextField(default='Not Yet Generated.')
    ext = models.CharField(max_length=24,
                           help_text='EXAMPLES: html css js ')
    theme = models.CharField(max_length=90,
                                  default='krogoth_core/AKThemes/Pro/')
    is_selected_theme = models.BooleanField(default=False)

    @property
    def get_filename(self) -> str:
        return self.name

    @property
    def get_file_ext(self) -> str:
        return self.ext

    @property
    def as_frontend_response(self) -> str:
        return codecs.open('krogoth_core/AKThemes/Pro/' + self.get_filename + '.' + self.get_file_ext, 'r')



def to_js(b: bool) -> str:
    if b == True:
        return 'true'
    else:
        return 'false'



# config.provider.js
class AKFoundationCoreConfig(AKFoundationAbstract):
    disableCustomScrollbars = models.BooleanField(default=False)
    disableMdInkRippleOnMobile = models.BooleanField(default=True)
    disableCustomScrollbarsOnMobile = models.BooleanField(default=True)

    @property
    def as_frontend_response(self) -> str:
        original = codecs.open('krogoth_core/AKThemes/Pro/' + self.get_filename + '.' + self.get_file_ext, 'r').read()
        p1 = original.replace("'|#1#|'", to_js(self.disableCustomScrollbars))
        p2 = p1.replace("'|#2#|'", to_js(self.disableMdInkRippleOnMobile))
        p3 = p2.replace("'|#3#|'", to_js(self.disableCustomScrollbarsOnMobile))
        return p3


class AKFoundationCoreDirectives(AKFoundationAbstract):
    """ Files from /app/core/directives/

    """

    val = models.CharField(max_length=250)


class AKFoundationCoreFilters(AKFoundationAbstract):
    """ Files from /app/core/filters/

    """

    val = models.CharField(max_length=250)


class AKFoundationCoreLayouts(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationCoreServices(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationCoreThemeOptions(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationCoreTheming(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationIndex(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationToolbar(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationQuickPanel(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationNavigation(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKFoundationMain(AKFoundationAbstract):
    val = models.CharField(max_length=250)


class AKBowerComponent(models.Model):
    package_name = models.CharField(max_length=250)
    package_version = models.CharField(max_length=50)
    index_header = models.CharField(max_length=251)
