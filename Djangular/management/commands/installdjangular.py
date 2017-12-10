from django.core.management.base import BaseCommand, CommandError
from dynamic_lazarus_page.models import NgIncludedJs, NgIncludedHtml
from Djangular.models import DjangularMasterViewController, DjangularIcon, DjangularCategory, DjangularSlaveViewController
import codecs
import subprocess





#  READ JS & HTML FILES AS A STRING LIKE SO:
#     f = open('static/app/toolbar/toolbar.controller.js', 'r')
#     f = open('static/app/toolbar/toolbar.module.js', 'r')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEAL = '\033[96m'
    BLACK = '\033[97m'
    GRAY = '\033[90m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'



def getDjangularBuild():
    # GET LAZARUS BUILD VERSION:
    bash_cmd = ['git', 'rev-list', '--count', 'master']
    get_build_cmd = str(subprocess.check_output(bash_cmd))
    current_build_1 = ''
    current_build_2 = ''
    try:
        current_build_1 = ('0.' + str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", "")) + '.'
        current_build_2 = (str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", ""))[1:]
    except:
        print('failed to check version!!!')
    if current_build_2 == '00':
        current_build_2 = '0'
    else:
        current_build_2 = current_build_2.replace('0', '')



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

        icon = DjangularIcon()
        cat = DjangularCategory()
        # get or create a default icon
        try:
            icon = DjangularIcon(name='icon-ubuntu', code='icon-ubuntu')
            icon.save()
        except:
            icon = DjangularIcon.objects.get(name='icon-ubuntu')

        try:
            cat = DjangularCategory(name='Djangular_Admin', code='icon-ubuntu')
            cat.save()
        except:
            cat = DjangularCategory.objects.get(name='Djangular_Admin')


        # loginMasterViewController---------------------------------------------------------
        try:
            str_loginView = codecs.open('Djangular/management/default_templates/login/view.html', 'r').read()
            str_loginModule = codecs.open('Djangular/management/default_templates/login/module.js', 'r').read()
            str_loginController = codecs.open('Djangular/management/default_templates/login/controller.js', 'r').read()
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
            str_view = codecs.open('Djangular/management/default_templates/register/view.html', 'r').read()
            str_module_ = codecs.open('Djangular/management/default_templates/register/module.js', 'r').read()
            str_controller = codecs.open('Djangular/management/default_templates/register/controller.js', 'r').read()
            mvc = DjangularMasterViewController(name='RegisterDjangular', title='Register Djangular Account')
            mvc.view_html = str_view
            mvc.controller_js = str_controller
            mvc.module_js = str_module_
            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... registerMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... registerMasterViewController'))
        # -------------------------------------------------------------------------

        # userprofileMasterViewController---------------------------------------------------------
        try:
            str_view = codecs.open('Djangular/management/default_templates/userprofile/view.html', 'r').read()
            str_module_ = codecs.open('Djangular/management/default_templates/userprofile/module.js', 'r').read()
            str_controller = codecs.open('Djangular/management/default_templates/userprofile/controller.js', 'r').read()
            mvc = DjangularMasterViewController(name='userprofile', title='Djangular User')
            mvc.view_html = str_view
            mvc.controller_js = str_controller
            mvc.module_js = str_module_
            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... userprofileMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... userprofileMasterViewController'))
        # -------------------------------------------------------------------------

        # forumsMasterViewController---------------------------------------------------------
        try:
            str_view = codecs.open('Djangular/management/default_templates/forums/view.html', 'r').read()
            str_module_ = codecs.open('Djangular/management/default_templates/forums/module.js', 'r').read()
            str_controller = codecs.open('Djangular/management/default_templates/forums/controller.js', 'r').read()

            str_ctrl_slave = codecs.open('Djangular/management/default_templates/forums/slavecontroller.js', 'r').read()
            str_view_slave = codecs.open('Djangular/management/default_templates/forums/slaveview.html', 'r').read()
            slave = DjangularSlaveViewController(name='Thread', title="Thread")
            slave.controller_js = str_ctrl_slave
            slave.view_html = str_view_slave
            slave.save()

            mvc = DjangularMasterViewController(name='userprofile', title='Djangular User Profile')
            mvc.view_html = str_view
            mvc.controller_js = str_controller
            mvc.module_js = str_module_

            mvc.category = cat
            mvc.icon = icon
            mvc.djangular_slave_vc.add(slave)
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... forumsMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... forumsMasterViewController'))
        # -------------------------------------------------------------------------

        # mvceditorMasterViewController---------------------------------------------------------
        try:
            str_view = codecs.open('Djangular/management/default_templates/mvc_editor/view.html', 'r').read()
            str_module_ = codecs.open('Djangular/management/default_templates/mvc_editor/module.js', 'r').read()
            str_controller = codecs.open('Djangular/management/default_templates/mvc_editor/controller.js', 'r').read()

            mvc = DjangularMasterViewController(name='mvceditor', title='Master View Controller Editor')
            mvc.view_html = str_view
            mvc.controller_js = str_controller
            mvc.module_js = str_module_

            mvc.category = cat
            mvc.icon = icon
            mvc.save()
            self.stdout.write(self.style.SUCCESS('ADDED... mvceditorMasterViewController'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... mvceditorMasterViewController'))
        # -------------------------------------------------------------------------

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


