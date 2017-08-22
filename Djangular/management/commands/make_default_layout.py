from django.core.management.base import BaseCommand, CommandError
from dynamic_lazarus_page.models import NgIncludedJs, NgIncludedHtml
from Djangular.models import DjangularMasterViewController, DjangularIcon, DjangularCategory
import codecs





#  READ JS & HTML FILES AS A STRING LIKE SO:
#     f = open('static/app/toolbar/toolbar.controller.js', 'r')
#     f = open('static/app/toolbar/toolbar.module.js', 'r')






class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'

    # def add_arguments(self, parser):
    #     parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(''))

        ctrl = open('Djangular/management/default_templates/toolbarCtrl.js', 'r')
        module = open('static/app/toolbar/toolbar.module.js', 'r')

        jsLayout = codecs.open('Djangular/management/default_templates/mainHtmlLayout.js', 'r')
        jsColorThemesConstants = codecs.open('Djangular/management/default_templates/colorThemesConstants.js', 'r')

        htmlMain = codecs.open('Djangular/management/default_templates/layoutMain.html', 'r')
        htmlNav = codecs.open('Djangular/management/default_templates/layoutNavigation.html', 'r')
        htmlToolbar = codecs.open('Djangular/management/default_templates/layoutToolbar.html', 'r')

        str_ctrl = ctrl.read()
        str_module = module.read()

        str_jsColorThemesConstants = jsColorThemesConstants.read()
        str_jsLayout = jsLayout.read()
        str_htmlMain = htmlMain.read()
        str_htmlNav = htmlNav.read()
        str_htmlToolbar = htmlToolbar.read()

        str_loginView = codecs.open('Djangular/management/default_templates/login/view.html', 'r').read()
        str_loginModule = codecs.open('Djangular/management/default_templates/login/module.js', 'r').read()
        str_loginController = codecs.open('Djangular/management/default_templates/login/controller.js', 'r').read()



        # loginMasterViewController---------------------------------------------------------
        try:
            mvc = DjangularMasterViewController(name='LoginDjangular', title='Login')
            mvc.view_html = str_loginView
            mvc.controller_js = str_loginController
            mvc.module_js = str_loginModule

            cat = DjangularCategory(name='Authentication', code='Authentication')
            cat.save()

            icon = DjangularIcon(name='icon-ubuntu', code='icon-ubuntu')
            icon.save()

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... loginMasterViewController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... loginMasterViewController'))
        #-------------------------------------------------------------------------



        # toolbarController
        try:
            sqlCtrl = NgIncludedJs(name='toolbarController')
            sqlCtrl.contents = str_ctrl
            sqlCtrl.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... toolbarController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... toolbarController'))

        # toolbarModule
        try:
            modCtrl = NgIncludedJs(name='toolbarModule')
            modCtrl.contents = str_module
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... toolbarModule'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... toolbarModule'))

        # jsLayout
        try:
            modCtrl = NgIncludedJs(name='mainHtmlLayout')
            modCtrl.contents = str_jsLayout
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... mainHtmlLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... mainHtmlLayout'))

        # colorThemesConstants
        try:
            colorThemesConstants = NgIncludedJs(name='colorThemesConstants')
            colorThemesConstants.contents = str_jsColorThemesConstants
            colorThemesConstants.save()
            self.stdout.write(self.style.SUCCESS('ADDED... colorThemesConstants'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... colorThemesConstants'))

        # htmlMainLayout
        try:
            modCtrl = NgIncludedHtml(name='htmlMainLayout')
            modCtrl.contents = str_htmlMain
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... htmlMainLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... htmlMainLayout'))

        # htmlNavLayout
        try:
            modCtrl = NgIncludedHtml(name='htmlNavLayout')
            modCtrl.contents = str_htmlNav
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... htmlNavLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... htmlNavLayout'))

        # htmlToolbarLayout
        try:
            modCtrl = NgIncludedHtml(name='htmlToolbarLayout')
            modCtrl.contents = str_htmlToolbar
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... htmlToolbarLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... htmlToolbarLayout'))


