from django.core.management.base import BaseCommand, CommandError
from moho_extractor.models import NgIncludedJs, NgIncludedHtml
from krogoth_gantry.models import krogoth_gantryMasterViewController, krogoth_gantryIcon, krogoth_gantryService, \
    krogoth_gantryCategory, krogoth_gantrySlaveViewController
from CommunityForum.models import ForumCategory
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

        ctrl = open('krogoth_gantry/management/default_templates/toolbarCtrl.js', 'r')
        module = open('static/app/toolbar/toolbar.module.js', 'r')

        jsLayout = codecs.open('krogoth_gantry/management/default_templates/mainHtmlLayout.js', 'r')
        jsColorThemesConstants = codecs.open('krogoth_gantry/management/default_templates/colorThemesConstants.js', 'r')

        htmlMain = codecs.open('krogoth_gantry/management/default_templates/layoutMain.html', 'r')
        htmlNav = codecs.open('krogoth_gantry/management/default_templates/layoutNavigation.html', 'r')
        htmlToolbar = codecs.open('krogoth_gantry/management/default_templates/layoutToolbar.html', 'r')

        str_ctrl = ctrl.read()
        str_module = module.read()

        str_jsColorThemesConstants = jsColorThemesConstants.read()
        str_jsLayout = jsLayout.read()

        str_htmlMain = htmlMain.read()
        str_htmlNav = htmlNav.read()
        str_htmlToolbar = htmlToolbar.read()

        str_loginView = codecs.open('krogoth_gantry/management/default_templates/login/view.html', 'r').read()
        str_loginModule = codecs.open('krogoth_gantry/management/default_templates/login/module.js', 'r').read()
        str_loginController = codecs.open('krogoth_gantry/management/default_templates/login/controller.js', 'r').read()

        icon = krogoth_gantryIcon()
        try:
            icon = krogoth_gantryIcon(name='icon-ubuntu')
            icon.save()
        except:
            icon = krogoth_gantryIcon.objects.get(name='icon-ubuntu')

        cat = krogoth_gantryCategory()
        try:
            cat = krogoth_gantryCategory(name='Administration')
            cat.save()
        except:
            cat = krogoth_gantryCategory.objects.get(name='Administration')


        # homeLandingPage---------------------------------------------------------
        try:
            str_View = codecs.open('krogoth_gantry/management/default_templates/base_view.html', 'r').read()
            str_Module = codecs.open('krogoth_gantry/management/default_templates/base_module.js', 'r').read()
            str_Controller = codecs.open('krogoth_gantry/management/default_templates/base_controller.js', 'r').read()

            mvc = krogoth_gantryMasterViewController(name='home', title='It Works!')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... homeMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... homeMasterViewController'))
        # -------------------------------------------------------------------------


        # loginMasterViewController---------------------------------------------------------
        try:
            mvc = krogoth_gantryMasterViewController(name='Loginkrogoth_gantry', title='Login')
            mvc.view_html = str_loginView
            mvc.controller_js = str_loginController
            mvc.module_js = str_loginModule

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... loginMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... loginMasterViewController'))
        # -------------------------------------------------------------------------


        # registerMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('krogoth_gantry/management/default_templates/register/view.html', 'r').read()
            str_Module = codecs.open('krogoth_gantry/management/default_templates/register/module.js', 'r').read()
            str_Controller = codecs.open('krogoth_gantry/management/default_templates/register/controller.js', 'r').read()

            mvc = krogoth_gantryMasterViewController(name='Registerkrogoth_gantry', title='Register')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... registerMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... registerMasterViewController'))
        # -------------------------------------------------------------------------

        # userprofileMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('krogoth_gantry/management/default_templates/userprofile/view.html', 'r').read()
            str_Module = codecs.open('krogoth_gantry/management/default_templates/userprofile/module.js', 'r').read()
            str_Controller = codecs.open('krogoth_gantry/management/default_templates/userprofile/controller.js', 'r').read()

            mvc = krogoth_gantryMasterViewController(name='userprofile', title='user profile')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... userprofileMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... userprofileMasterViewController'))
        # -------------------------------------------------------------------------

        # mvc_editorMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('krogoth_gantry/management/default_templates/mvc_editor/view.html', 'r').read()
            str_Module = codecs.open('krogoth_gantry/management/default_templates/mvc_editor/module.js', 'r').read()
            str_Controller = codecs.open('krogoth_gantry/management/default_templates/mvc_editor/controller.js', 'r').read()

            mvc = krogoth_gantryMasterViewController(name='AngularEditor', title='Angular Editor')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... AngularEditorMasterViewController'))

            str_Service = codecs.open('krogoth_gantry/management/default_templates/mvc_editor/krogoth_gantryEditorRESTful.js',
                                      'r').read()
            try:
                service = krogoth_gantryService(name='krogoth_gantryEditorRESTful', title='Community Forum Service RESTful CRUD')
                service.service_js = str_Service
                service.save()
                try:
                    mvc.djangular_service.add(service)
                    mvc.save()
                except:
                    self.stdout.write(self.style.SUCCESS('FAIL... AngularEditor.add -> krogoth_gantryEditorRESTful'))
            except:
                mvc.delete()
                self.stdout.write(self.style.SUCCESS('FAIL... krogoth_gantryEditorRESTful.save()'))

        except:
            self.stdout.write(self.style.WARNING('SKIPPING... AngularEditorMasterViewController'))
        # -------------------------------------------------------------------------

        # dashboardMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('krogoth_gantry/management/default_templates/dashboard/view.html', 'r').read()
            str_Module = codecs.open('krogoth_gantry/management/default_templates/dashboard/module.js', 'r').read()
            str_Controller = codecs.open('krogoth_gantry/management/default_templates/dashboard/controller.js', 'r').read()

            mvc = krogoth_gantryMasterViewController(name='dashboard', title='dashboard')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... dashboardMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... dashboardMasterViewController'))
        # -------------------------------------------------------------------------


        # forumsMasterViewController---------------------------------------------------------
        try:
            str_View = codecs.open('krogoth_gantry/management/default_templates/forums/view.html', 'r').read()
            str_Module = codecs.open('krogoth_gantry/management/default_templates/forums/module.js', 'r').read()
            str_Controller = codecs.open('krogoth_gantry/management/default_templates/forums/controller.js', 'r').read()
            str_slaveView = codecs.open('krogoth_gantry/management/default_templates/forums/slaveview.html', 'r').read()
            str_slaveController = codecs.open('krogoth_gantry/management/default_templates/forums/slavecontroller.js',
                                              'r').read()
            mvc = krogoth_gantryMasterViewController(name='General', title='Forums')
            mvc.view_html = str_View
            mvc.controller_js = str_Controller
            mvc.module_js = str_Module

            svc = krogoth_gantrySlaveViewController(name='Thread', title='Thread')
            try:
                svc.view_html = str_slaveView
                svc.controller_js = str_slaveController
                svc.save()
            except:
                self.stdout.write(self.style.SUCCESS('FAIL... krogoth_gantrySlaveViewController.save()'))

            str_Service = codecs.open('krogoth_gantry/management/default_templates/forums/CommunityForumService.js',
                                      'r').read()
            service = krogoth_gantryService(name='CommunityForumService', title='Community Forum Service RESTful CRUD')
            try:
                service.service_js = str_Service
                service.save()
            except:
                self.stdout.write(self.style.SUCCESS('FAIL... krogoth_gantryService.save()'))

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            try:
                mvc.djangular_service.add(service)
            except:
                self.stdout.write(self.style.SUCCESS('FAIL... forums.add -> krogoth_gantryService'))
            try:
                mvc.djangular_slave_vc.add(svc)
                mvc.save()
            except:
                self.stdout.write(self.style.SUCCESS('FAIL... forums.add -> krogoth_gantrySlaveViewController'))
                mvc.delete()

            general_forum = ForumCategory.objects.get_or_create(title='General', is_deleted=False)
            self.stdout.write(self.style.SUCCESS('ADDED... forumsMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... forumsMasterViewController'))
        # -------------------------------------------------------------------------



        # toolbarController
        try:
            sqlCtrl = NgIncludedJs(name='toolbarController')
            sqlCtrl.contents = str_ctrl
            sqlCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... toolbarController'))
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
