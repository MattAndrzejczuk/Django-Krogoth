from krogoth_gantry.models.gantry_models import KrogothGantryMasterViewController, KrogothGantryDirective, \
    KrogothGantryService, AKGantryMasterViewController, KrogothGantryCategory
import codecs, os
from jawn.settings import BASE_DIR

# MVC BASE COMPONENTS:
TMPL_MODU = 'module.js'
TMPL_CTRL = 'controller.js'
TMPL_VIEW = 'view.html'

# SCAFFOLDING PATHS:
TMPL_LAZY = BASE_DIR + "/static/web/other/lazyReloadableScaffold/"


def create_directory(named: str):
    sys_path = BASE_DIR + "/static/web/app/" + named
    print(sys_path)
    if os.path.isdir(sys_path):
        pass
    else:
        os.makedirs(sys_path)


def create_subdirectory(named: str, within: str):
    sys_path = BASE_DIR + "/static/web/app/" + within + "/" + named
    print(sys_path)
    if os.path.isdir(sys_path):
        pass
    else:
        os.makedirs(sys_path)
    pass


class NewLazyMVC:

    def __init__(self, name: str, main_dir: str, sub_dir: str):

        modu = codecs.open(TMPL_LAZY + TMPL_MODU, 'r').read()
        ctrl = codecs.open(TMPL_LAZY + TMPL_CTRL, 'r').read()
        view = codecs.open(TMPL_LAZY + TMPL_VIEW, 'r').read()


        cat_exist = KrogothGantryCategory.objects.filter(name=main_dir)
        if len(cat_exist) < 1:
            cat_host_obj = KrogothGantryCategory(name=main_dir,
                                                 title=main_dir)
            cat_host_obj.save()
        subcat_exist = KrogothGantryCategory.objects.filter(name=sub_dir)
        if len(subcat_exist) < 1:
            parent = KrogothGantryCategory.objects.get(name=main_dir)
            cat_host_obj = KrogothGantryCategory(name=sub_dir,
                                                 title=sub_dir)
            cat_host_obj.parent = parent
            cat_host_obj.save()

        subcat = KrogothGantryCategory.objects.get(name=sub_dir)
        _mvc = AKGantryMasterViewController.objects.get_or_create(name=name,
                                                                  title=name,
                                                                  category=subcat,
                                                                  is_enabled=True)
        mvc = KrogothGantryMasterViewController.objects.get(name=name)
        mvc.name = name
        mvc.category_id = subcat.id
        mvc.module_js = modu
        mvc.controller_js = ctrl
        mvc.view_html = view
        mvc.save()
        create_directory(main_dir)
        create_subdirectory(sub_dir, main_dir)
