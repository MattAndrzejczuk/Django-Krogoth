from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from krogoth_gantry.models.gantry_models import KrogothGantryCategory, KrogothGantryMasterViewController
from colors import ink


class master_compiler(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    username = ""

    def __init__(self, username:str, *args, **kwargs):
        self.username = username
        super(master_compiler, self).__init__(*args, **kwargs)



    def compiled_raw(self, named) -> str:

        lazy_token = ""
        if isinstance(named, list):
            name = named[0]
            lazy_token = named[1]
            print("NAME: " + name)
            print("LAZY TOKEN: " + lazy_token)
        else:
            name = named
        application = KrogothGantryMasterViewController.objects.get(name=name)
        raw_js_services_and_directives = ''
        djangular_services = application.djangular_service.all()
        djangular_directives = application.djangular_directive.all()
        compiled_slave = application.compileModuleSlaves
        clean_js_slate = '\n\n\n\n\n\n\t /* ════════════' + application.title + '════════════ */\n\n'


        ink.pyellow("COMPILING SOMETHING NOW...")
        app_ctrl = application.controller_js
        for js in application.partial_js.all():
            no_ext = js.name.replace(".js", "")
            ink.pgreen(application.name + ":")
            ink.pblue(no_ext + "\n")

            ink.pcyan("\n⚙️\n#KG" + no_ext + "\n")
            app_ctrl = app_ctrl.replace("#KG" + no_ext, "\n/*~ ~ ~ ~ ~ ~" + no_ext + "~ ~ ~ ~ ~ ~*/\n" +
                                        js.contents + "\n/*~/~/~/~/~/~" + no_ext + "~/~/~/~/~/~*/\n" + "\n")

        if name == 'home':
            processed_cats = ''
            for cat in KrogothGantryCategory.objects.all():
                icon = 'folder'
                ipre = 'mdi mdi-'
                parent_icon = 'folder'
                if cat.parent is not None:
                    p04 = 'msNavigationServiceProvider.saveItem("' + cat.parent.name + '", {\n'
                    p03 = '\ttitle: "' + cat.parent.title + '",\n'
                    p02 = '\ticon: "mdi mdi-circle",\n'
                    p01 = '\tweight: ' + str(cat.parent.weight) + '\n'
                    p0 = '});\n'
                    p1 = 'msNavigationServiceProvider.saveItem("' + cat.parent.name + '.' + cat.name + '", {\n'
                    p2 = '\ttitle: "' + cat.title + '",\n'
                    p3 = '\ticon: "mdi mdi-circle",\n'
                    p4 = '\tweight: ' + str(cat.weight) + '\n'
                    p5 = '});\n'
                    processed_cats += p04 + p03 + p02 + p01 + p0 + p1 + p2 + p3 + p4 + p5
            cat_contain = compiled_slave['module_with_injected_navigation'].replace('_KROGOTH_CATEGORIES_', processed_cats)
            clean_js_slate += ' \n /* MASTER MODULE */ \n' + cat_contain + \
                              ' \n /* MASTER CONTROLLER */ \n' + app_ctrl
        else:
            clean_js_slate += ' \n /* ┈┈┈┈┈┈┈┈┈ MASTER MODULE ┈┈┈┈┈┈┈┈┈ */ \n' + \
                              compiled_slave['module_with_injected_navigation'] + \
                              ' \n /* ┈┈┈┈┈┈┈┈┈ MASTER CONTROLLER ┈┈┈┈┈┈┈┈┈ */ \n' + app_ctrl
        clean_js_slate += '\n /* SLAVE CONTROLLER */ \n' + compiled_slave['slave_controllers_js']

        for service in djangular_services:
            raw_js_services_and_directives += '\n /* ┈┈┈┈┈┈┈┈┈ COMPILED SERVICE ┈┈┈┈┈┈┈┈┈ */ \n' + \
                                              service.service_js.replace('_DJANGULAR_SERVICE_NAME_',
                                                                         service.name+lazy_token).replace(
                                                  '_DJANGULAR_SERVICE_TITLE_', service.title)
            raw_js_services_and_directives += '\n'
            clean_js_slate = clean_js_slate.replace(service.name, service.name+lazy_token)

        for directive in djangular_directives:
            raw_js_services_and_directives += '\n /* ┈┈┈┈┈┈┈┈┈ COMPILED DIRECTIVE  ┈┈┈┈┈┈┈┈┈ */ \n' + \
                                              directive.directive_js.replace('_DJANGULAR_DIRECTIVE_NAME_',
                                                                             directive.name+lazy_token).replace(
                                                  "_DJANGULAR_DIRECTIVE_TITLE_", directive.title)
            raw_js_services_and_directives += '\n'
            clean_js_slate = clean_js_slate.replace(directive.name, directive.name + lazy_token)
        clean_js_slate += raw_js_services_and_directives
        fuse_app_name = application.name.replace(' ', '_') + lazy_token
        parsed1 = clean_js_slate.replace('FUSE_APP_NAME', fuse_app_name)
        if len(lazy_token) > 0:
            base_uri = '/krogoth_gantry/DynamicHTMLInjector/?name='
            mvc_view = base_uri + fuse_app_name
            mvc_view_fixed = base_uri + application.name.replace(' ', '_') + "&tmpl=" + lazy_token + ".HTML"
            parsed1 = parsed1.replace(mvc_view, mvc_view_fixed)
        parsed2 = parsed1.replace('FUSE_APP_TITLE', application.title).replace('FUSE_APP_SLAVE_NAME', application.name
                                                                               + 'Slave')
        parsed3 = parsed2.replace('FUSE_APP_ICON', ' mdi mdi-circle')
        parsed4 = parsed3.replace('NAV_HEADER', application.category.name.replace(' ', '_'))
        try:
            raw_js_response = parsed4.replace('DJANGULAR_USERNAME', self.username)
        except:
            raw_js_response = parsed4
        return raw_js_response
