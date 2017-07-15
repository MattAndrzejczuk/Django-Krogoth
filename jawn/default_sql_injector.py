from dynamic_lazarus_page.models import AngularFuseApplication, NgIncludedHtml


DJANGULAR_ROOT = '/usr/src/app/DjangularStaticFiles'


# Djangular Initializer

# populates database with default js and html files.
from jawn.default_sql_injector import populateDefaultSQL
populateDefaultSQL('')










# Print status if Djangular is starting for the first time:

def printDjangularStatusOnLaunch(first_time_run):
    # GET LAZARUS BUILD VERSION:
    bash_cmd = ['git', 'rev-list', '--count', 'master']
    get_build_cmd = str(subprocess.check_output(bash_cmd))
    current_build_1 = ''
    current_build_2 = ''
    try:
        current_build_1 = ('0.' + str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", "")) + '.'
        current_build_2 = (str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", ""))[1:]
        DjangularVersion = current_build_1[:3] + "." + current_build_2
        print('\033[94mDjangular ' + DjangularVersion + '\033[0m')
        if first_time_run == True:
            print('\033[97m Starting Djangular ' + DjangularVersion + ' for the first time.\033[0m')
    except:
        print('Djangular Initialized')












# Populate default js and html files if the database is fresh:

def populateDefaultSQL(base_dir):

    # Configure Default Djangular View Controllers Here:


    # Default path for js and html files is /DjangularStaticFiles/

    DEFAULT_APPS = [

    ]

    APPLICATION1 = {
        'name': 'News',
        'category': 'Home',
        'js_module': 'newsModule.js',
        'js_controller': 'newsController.js',
        'html_main': 'newsView.html',
        'icon': 'icon-newspaper'
    }


    DEFAULT_APPS.append(APPLICATION1)

    # THIS BREAKS IT, CAN'T QUERY DB FROM SETTINGS.PY
    appsInstalledNow = AngularFuseApplication.objects.all()


    first_time_run = False
    if len(appsInstalledNow) == 0:
        first_time_run = True
        for app in DEFAULT_APPS:

            ctrlfile_path = base_dir + '/' + app['js_controller']
            modfile_path = base_dir + '/' + app['js_module']
            viewfile_path = base_dir + '/' + app['html_main']

            controllerJs_instance = open(ctrlfile_path, 'r', errors='replace')
            moduleJs_instance = open(modfile_path, 'r', errors='replace')
            viewHtml_instance = open(viewfile_path, 'r', errors='replace')

            controllerJs = controllerJs_instance.read()
            moduleJs = moduleJs_instance.read()
            viewHtml = viewHtml_instance.read()

            newDVC = AngularFuseApplication()
            newDVC.name = app['name']
            newDVC.category = app['category']
            newDVC.html_main = viewHtml
            newDVC.js_controller = controllerJs
            newDVC.js_module = moduleJs
            newDVC.icon = app['icon']
    printDjangularStatusOnLaunch(first_time_run)









