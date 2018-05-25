from rest_framework.views import APIView
from django.template import loader
from django.http import HttpResponse
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_gantry.models import KrogothGantryCategory, KrogothGantryMasterViewController


class master_compiler(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    username = ""

    def __init__(self, username:str, *args, **kwargs):
        self.username = username
        super(master_compiler, self).__init__(*args, **kwargs)



    def compiled_raw(self, named: str) -> str:
        name = named
        application = KrogothGantryMasterViewController.objects.get(name=name)
        raw_js_services_and_directives = ''
        djangular_services = application.djangular_service.all()
        djangular_directives = application.djangular_directive.all()
        compiled_slave = application.compileModuleSlaves
        clean_js_slate = '\n\n\n\n\n\n\t /* ════════════' + application.title + '════════════ */\n\n'
        if name == 'home':
            processed_cats = ''
            for cat in KrogothGantryCategory.objects.all():
                icon = 'folder'
                ipre = 'mdi mdi-'
                parent_icon = 'folder'
                if cat.icon is not None:
                    icon = cat.icon.prefix + cat.icon.code
                if cat.parent is not None:
                    if cat.parent.icon is not None:
                        parent_icon = cat.parent.icon.code
                    p04 = 'msNavigationServiceProvider.saveItem("' + cat.parent.name + '", {\n'
                    p03 = '\ttitle: "' + cat.parent.title + '",\n'
                    p02 = '\ticon: "' + parent_icon + '",\n'
                    p01 = '\tweight: ' + str(cat.parent.weight) + '\n'
                    p0 = '});\n'
                    p1 = 'msNavigationServiceProvider.saveItem("' + cat.parent.name + '.' + cat.name + '", {\n'
                    p2 = '\ttitle: "' + cat.title + '",\n'
                    p3 = '\ticon: "' + ipre + icon + '",\n'
                    p4 = '\tweight: ' + str(cat.weight) + '\n'
                    p5 = '});\n'
                    processed_cats += p04 + p03 + p02 + p01 + p0 + p1 + p2 + p3 + p4 + p5
            cat_contain = compiled_slave['module_with_injected_navigation'].replace('_KROGOTH_CATEGORIES_', processed_cats)
            clean_js_slate += ' \n /* MASTER MODULE */ \n' + cat_contain + \
                              ' \n /* MASTER CONTROLLER */ \n' + application.controller_js
        else:
            clean_js_slate += ' \n /* MASTER MODULE */ \n' + compiled_slave['module_with_injected_navigation'] + \
                              ' \n /* MASTER CONTROLLER */ \n' + application.controller_js
        clean_js_slate += '\n /* SLAVE CONTROLLER */ \n' + compiled_slave['slave_controllers_js']

        for service in djangular_services:
            raw_js_services_and_directives += '\n /* COMPILED SERVICE */ \n' + \
                                              service.service_js.replace('_DJANGULAR_SERVICE_NAME_',
                                                                         service.name).replace(
                                                  '_DJANGULAR_SERVICE_TITLE_', service.title)
            raw_js_services_and_directives += '\n'

        for directive in djangular_directives:
            raw_js_services_and_directives += '\n /* COMPILED DIRECTIVE */ \n' + \
                                              directive.directive_js.replace('_DJANGULAR_DIRECTIVE_NAME_',
                                                                             directive.name).replace(
                                                  "_DJANGULAR_DIRECTIVE_TITLE_", directive.title)
            raw_js_services_and_directives += '\n'
        clean_js_slate += raw_js_services_and_directives
        parsed1 = clean_js_slate.replace('FUSE_APP_NAME', application.name.replace(' ', '_'))
        parsed2 = parsed1.replace('FUSE_APP_TITLE', application.title).replace('FUSE_APP_SLAVE_NAME', application.name + 'Slave')
        parsed3 = parsed2.replace('FUSE_APP_ICON', application.icon.prefix + ' ' + application.icon.code)
        parsed4 = parsed3.replace('NAV_HEADER', application.category.name.replace(' ', '_'))
        try:
            raw_js_response = parsed4.replace('DJANGULAR_USERNAME', self.username)
        except:
            raw_js_response = parsed4
        return raw_js_response