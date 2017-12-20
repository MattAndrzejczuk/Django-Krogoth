# coding=utf-8
__version__ = '0.6.98'
__author__ = 'Matt Andrzejczuk'
from django.db import models
from polymorphic.models import PolymorphicModel
import codecs
from jawn.settings import BASE_DIR

# Create your models here.

class AKFoundationAbstract(PolymorphicModel):
    class Meta:
        abstract = True

    unique_name = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=140,
                                  help_text='EXAMPLES: index. index. toolbar. theming.')
    last_name = models.CharField(max_length=140,
                                 help_text='EXAMPLES: .controller .route .module .service')
    code = models.TextField(default='Not Yet Generated.')
    ext = models.CharField(max_length=24,
                           help_text='EXAMPLES: html css js ')
    theme = models.CharField(max_length=90,
                             default=BASE_DIR + '/krogoth_core/AKThemes/Pro/')
    is_selected_theme = models.BooleanField(default=False)

    @property
    def get_filename(self) -> str:
        if self.first_name is None or self.last_name is None:
            print('AKFoundationAbstract is missing a property.'); raise EnvironmentError()
        return self.first_name + '.' + self.last_name

    @property
    def get_file_ext(self) -> str:
        if self.ext is None:
            print('AKFoundationAbstract is missing a property.'); raise EnvironmentError()
        return self.ext

    # @property
    # def as_frontend_response(self) -> str:
    #     print('retrieving ' + self.get_filename)
    #     return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


def to_js(b: bool) -> str:
    if b == True:
        return 'true'
    else:
        return 'false'


# config.provider.js
class AKFoundationAngularCore(AKFoundationAbstract):
    disableCustomScrollbars = models.BooleanField(default=False)
    disableMdInkRippleOnMobile = models.BooleanField(default=True)
    disableCustomScrollbarsOnMobile = models.BooleanField(default=True)

    @property
    def as_frontend_response(self) -> str:
        if self.first_name == 'config':
            original = codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()
            p1 = original.replace("'|#1#|'", to_js(self.disableCustomScrollbars))
            p2 = p1.replace("'|#2#|'", to_js(self.disableMdInkRippleOnMobile))
            p3 = p2.replace("'|#3#|'", to_js(self.disableCustomScrollbarsOnMobile))
            return p3
        # elif self.first_name == 'core':
        #     if self.last_name == '':



class AKFoundationDirectives(AKFoundationAbstract):
    """ Files from /app/core/directives/

    """

    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationFilters(AKFoundationAbstract):
    """ Files from /app/core/filters/

    """

    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationThemingService(AKFoundationAbstract):
    """ Files from /app/core/theming/
    and from /app/core/theme-options/
    """

    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationThemingConstant(AKFoundationAbstract):
    """ Files from /app/core/theming/
    and from /app/core/theme-options/
    """

    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()

class AKFoundationThemingConfiguration(AKFoundationAbstract):
    """ Files from /app/core/theming/
    and from /app/core/theme-options/
    """
    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationIndex(AKFoundationAbstract):
    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationToolbar(AKFoundationAbstract):
    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationQuickPanel(AKFoundationAbstract):
    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationNavigation(AKFoundationAbstract):
    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKFoundationMain(AKFoundationAbstract):
    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()

class AKFoundationRESTful(AKFoundationAbstract):
    val = models.CharField(max_length=250)
    @property
    def as_frontend_response(self) -> str:
        print('retrieving ' + self.get_filename)
        return codecs.open(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + self.get_filename + self.get_file_ext, 'r').read()


class AKBowerComponent(models.Model):
    package_name = models.CharField(max_length=250)
    package_version = models.CharField(max_length=50)
    url = models.CharField(max_length=251)



class AKCustomDependency(models.Model):
    package_name = models.CharField(max_length=250)
    package_version = models.CharField(max_length=50)
    url = models.CharField(max_length=251)
