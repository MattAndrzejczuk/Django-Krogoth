from django.core.management.base import BaseCommand, CommandError
from moho_extractor.models import NgIncludedJs, NgIncludedHtml
from krogoth_gantry.models import KrogothGantryMasterViewController, KrogothGantryIcon, KrogothGantryCategory, KrogothGantrySlaveViewController
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
        name = 'Pro'
        self.stdout.write(self.style.SUCCESS('Installing AngularJS Frontend Theme: ' + name + '\n'))
        path = '/opt/project/krogoth_core/AKThemes/' + name
        files = os.listdir(theme_path)

        def output_console(msg: str):
            if os.path.isfile(msg) == True:
                print('dependency loaded... \033[32m' + msg + '\033[0m')
            else:
                print('\033[31mNOT FOUND: ' + msg + '\033[0m')
                raise IOError()

        for file in files:
            arr = file.split('.')

            if arr[0] == arr[len(arr) - 2]:
                p = theme_path + arr[0] + '.' + arr[len(arr) - 1]
                output_console(msg=p)
            else:
                p = theme_path + arr[0] + '.' + arr[len(arr) - 2] + '.' + arr[len(arr) - 1]
                output_console(msg=p)


