from django.core.management.base import BaseCommand, CommandError
from dynamic_lazarus_page.models import NgIncludedJs, NgIncludedHtml
from Djangular.models import DjangularMasterViewController, DjangularIcon, DjangularService, \
    DjangularCategory, DjangularSlaveViewController
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

        icon = DjangularIcon()
        try:
            icon = DjangularIcon(name='icon-ubuntu', code='icon-ubuntu')
            icon.save()
        except:
            icon = DjangularIcon.objects.get(name='icon-ubuntu')

        cat = DjangularCategory()
        try:
            cat = DjangularCategory(name='Administration', code='nan')
            cat.save()
        except:
            cat = DjangularCategory.objects.get(name='Administration')





        # loginMasterViewController---------------------------------------------------------
        try:
            mvc = DjangularMasterViewController(name='LoginDjangular', title='Login')
            mvc.view_html = str_loginView
            mvc.controller_js = str_loginController
            mvc.module_js = str_loginModule

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... loginMasterViewController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... loginMasterViewController'))
        #-------------------------------------------------------------------------


        # registerMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('Djangular/management/default_templates/register/view.html', 'r').read()
            str_Module = codecs.open('Djangular/management/default_templates/register/module.js', 'r').read()
            str_Controller = codecs.open('Djangular/management/default_templates/register/controller.js', 'r').read()

            mvc = DjangularMasterViewController(name='RegisterDjangular', title='Register')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... registerMasterViewController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... registerMasterViewController'))
        #-------------------------------------------------------------------------

        # userprofileMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('Djangular/management/default_templates/userprofile/view.html', 'r').read()
            str_Module = codecs.open('Djangular/management/default_templates/userprofile/module.js', 'r').read()
            str_Controller = codecs.open('Djangular/management/default_templates/userprofile/controller.js', 'r').read()

            mvc = DjangularMasterViewController(name='userprofile', title='user profile')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... userprofileMasterViewController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... userprofileMasterViewController'))
        #-------------------------------------------------------------------------

        # mvc_editorMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('Djangular/management/default_templates/mvc_editor/view.html', 'r').read()
            str_Module = codecs.open('Djangular/management/default_templates/mvc_editor/module.js', 'r').read()
            str_Controller = codecs.open('Djangular/management/default_templates/mvc_editor/controller.js', 'r').read()

            mvc = DjangularMasterViewController(name='mvc_editor', title='mvc editor')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... mvc_editorMasterViewController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... mvc_editorMasterViewController'))
        #-------------------------------------------------------------------------

        # dashboardMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('Djangular/management/default_templates/dashboard/view.html', 'r').read()
            str_Module = codecs.open('Djangular/management/default_templates/dashboard/module.js', 'r').read()
            str_Controller = codecs.open('Djangular/management/default_templates/dashboard/controller.js', 'r').read()

            mvc = DjangularMasterViewController(name='dashboard', title='dashboard')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... dashboardMasterViewController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... dashboardMasterViewController'))
        #-------------------------------------------------------------------------


        # forumsMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('Djangular/management/default_templates/forums/view.html', 'r').read()
            str_Module = codecs.open('Djangular/management/default_templates/forums/module.js', 'r').read()
            str_Controller = codecs.open('Djangular/management/default_templates/forums/controller.js', 'r').read()
            str_slaveView = codecs.open('Djangular/management/default_templates/forums/slaveview.html', 'r').read()
            str_slaveController = codecs.open('Djangular/management/default_templates/forums/slavecontroller.js',
                                              'r').read()
            mvc = DjangularMasterViewController(name='forums', title='forums')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            svc = DjangularSlaveViewController(name='Thread', title='Thread')
            svc.view_html = str_slaveView
            svc.controller_js = str_slaveController
            svc.save()

            str_Service = codecs.open('Djangular/management/default_templates/forums/CommunityForumService.js', 'r').read()
            service = DjangularService(name='CommunityForumService', title='Community Forum Service RESTful CRUD')
            service.service_js = str_Service
            service.save()

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            mvc.djangular_service.add(service)
            mvc.djangular_slave_vc.add(svc)
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... forumsMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... forumsMasterViewController'))
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


