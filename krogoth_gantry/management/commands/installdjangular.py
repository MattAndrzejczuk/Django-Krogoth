from django.core.management.base import BaseCommand, CommandError
from CommunityForum.models import ForumCategory
from moho_extractor.models import NgIncludedHtml
import codecs
import subprocess
from jawn.settings import BASE_DIR
import os
from krogoth_core.models import *
import jsbeautifier
from django.db import IntegrityError
import json

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


def getkrogoth_gantryBuild():
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

        def output_console(msg: str):
            if os.path.isfile(msg) == True:
                # print('dependency loaded... \033[32m' + msg + '\033[0m')
                pass
            else:
                # print('\033[31mNOT FOUND: ' + msg + '\033[0m')
                raise IOError()

        def create_html_view(named: str, at: str):
            try:
                new_ng = NgIncludedHtml(name=named)
                new_ng.contents = codecs.open(at + named + '', 'r').read()
                new_ng.save()
                print(bcolors().OKGREEN + 'CREATED...' + (at + named) + bcolors().ENDC)
                pass
            except:
                print('\033[31mNOT FOUND: ' + named + '\033[0m')

        def get_source_class(kind: str, angular_duty: str, path: str):
            # print(kind)
            # print(angular_duty)
            new_js = AKFoundationAbstract()
            if kind == 'altDate':
                new_js = AKFoundationFilters(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'api-resolver':
                new_js = AKFoundationRESTful(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'toolbar':
                new_js = AKFoundationToolbar(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'basic':
                new_js = AKFoundationFilters(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'chat-tab':
                new_js = AKFoundationQuickPanel(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'config':
                new_js = AKFoundationConfig(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'core':
                new_js = AKFoundationAngularCore(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'filterByIds':
                new_js = AKFoundationFilters(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'filterByPropIds':
                new_js = AKFoundationFilters(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'fuse-config':
                new_js = AKFoundationThemingConfiguration(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'fuse-generator':
                new_js = AKFoundationThemingService(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'fuse-palettes':
                new_js = AKFoundationThemingConstant(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'fuse-themes':
                new_js = AKFoundationThemingConstant(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'fuse-theming':
                new_js = AKFoundationThemingService(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'highlight':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'index':
                new_js = AKFoundationIndex(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'main':
                new_js = AKFoundationMain(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-api':
                new_js = AKFoundationRESTful(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-card':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-datepicker-fix':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-form-wizard':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-info-bar':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-masonry':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-material-color-picker':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-nav':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-navigation':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-random-class':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-responsive-table':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-scroll':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-search-bar':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-shortcuts':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-sidenav-helper':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-splash-screen':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-stepper':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-utils':
                new_js = AKFoundationMain(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-widget':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'ms-timeline':
                new_js = AKFoundationDirectives(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'navigation':
                new_js = AKFoundationNavigation(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'quick-panel':
                new_js = AKFoundationQuickPanel(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'tag':
                new_js = AKFoundationFilters(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            elif kind == 'theme-options':
                new_js = AKFoundationThemingConfiguration(first_name=kind, last_name=angular_duty, ext='.js', path=path)
            else:
                self.stdout.write(BASE_DIR + '/krogoth_core/AKThemes/Pro/' + bcolors().WARNING + (
                        'UNKNOWN...' + kind + '.' + angular_duty) + bcolors().ENDC)

            try:
                if type(new_js) is not AKFoundationAbstract:
                    new_js.is_selected_theme = True
                    new_js.theme = BASE_DIR + '/krogoth_core/AKThemes/Pro/'
                    new_js.code = new_js.as_frontend_response
                    new_js.unique_name = kind + angular_duty + ''  # str(len(AKFoundationAbstract.objects.all())) + 'v1'
                    # print(bcolors.purple + BASE_DIR + '/krogoth_core/AKThemes/Pro/' + new_js.get_filename + new_js.get_file_ext)
                    new_js.save()
                    self.stdout.write(bcolors().OKGREEN + 'CREATED...' + path + (
                            new_js.get_filename + new_js.ext) + bcolors().ENDC)
                else:
                    print(new_js.first_name + '.' + new_js.last_name)
            except IntegrityError:
                self.stdout.write(bcolors().FAIL + path + (
                        'ALREADY EXISTS...' + (new_js.get_filename + new_js.ext)) + bcolors().ENDC)

            # print('dependency saved.')

        name = 'Pro'
        print('Installing AngularJS Frontend Theme: ' + name + '\n')
        path = BASE_DIR + '/krogoth_core/AKThemes/' + name + '/'

        key_paths_js = {
            0: path + 'js/app_core/',
            1: path + 'js/app_navigation/',
            2: path + 'js/app_quick-panel/',
            3: path + 'js/app_toolbar/',
            4: path + 'js/fuse/'
        }
        key_paths_html = {
            0: path + 'html/layouts/',
            1: path + 'html/directives/',
            2: path + 'html/quickpanel/'
        }

        js_files = {}
        for k,v in key_paths_js.items():
            print(bcolors.purple + v + bcolors.ENDC)
            # js_files = os.listdir(v)
            for file in os.listdir(v):
                # print(bcolors.red + file + bcolors.ENDC)
                # print(bcolors.OKGREEN + json.dumps(os.listdir(v), sort_keys=True, indent=2) + bcolors.ENDC)
                count = len(file.split('/'))
                array = file.split('/')
                filename = str(array[count - 1])
                arr = filename.split('.')
                if arr[0] == arr[len(arr) - 2]:
                    if arr[len(arr) - 1] == 'js':
                        # p = path + arr[0] + '\033[36m.' + arr[len(arr) - 1] + '\033[0m'
                        # _msg = path + arr[0] + '.' + arr[len(arr) - 1]
                        # output_console(msg=_msg)
                        js_files[filename] = v
                        get_source_class(kind=str(arr[0]), angular_duty='AK', path=v)

                else:
                    if arr[len(arr) - 1] == 'js':
                        js_files[filename] = v
                        # p = path + arr[0] + '.' + arr[len(arr) - 2] + '.' + arr[len(arr) - 1]
                        # output_console(msg=p)
                        get_source_class(kind=str(arr[0]), angular_duty=str(arr[len(arr) - 2]), path=v)

        html_files = {}
        for k,v in key_paths_html.items():
            # print('analyzing... ' + bcolors.blue + v + bcolors.ENDC)
            for file in os.listdir(v):
                count = len(file.split('/'))
                array = file.split('/')
                create_html_view(named=str(array[count - 1]), at=key_paths_html[k])
                html_files[array[count - 1]] = key_paths_html[k]

        print(bcolors.OKBLUE, end='[html_files]: \n')
        print(json.dumps(
            html_files, sort_keys=True, indent=2).replace('",', '",' + bcolors.green).replace(':', ':' + bcolors.OKBLUE),
              end='')
        print(bcolors.ENDC)

        print(bcolors.green, end='[js_files]: \n')
        print(json.dumps(
            js_files, sort_keys=True, indent=2).replace('",', '",' + bcolors.red).replace(':',
                                                                                              ':' + bcolors.lightgrey),
              end='')
        print(bcolors.ENDC)


