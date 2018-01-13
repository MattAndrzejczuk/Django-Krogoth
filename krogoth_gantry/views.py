from rest_framework.views import APIView

from django.template import loader
from django.http import HttpResponse
import json

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from krogoth_gantry.models import KrogothGantrySlaveViewController, \
    KrogothGantryIcon, KrogothGantryCategory, KrogothGantryMasterViewController, KrogothGantryDirective, \
    KrogothGantryService

from rest_framework import viewsets, serializers, generics, filters
import subprocess
# from django.core import serializers
import django_filters.rest_framework


class KrogothGantryMasterViewControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrogothGantryMasterViewController
        fields = '__all__'


class KrogothGantryMasterViewControllerViewSet(viewsets.ModelViewSet):
    queryset = KrogothGantryMasterViewController.objects.all()
    serializer_class = KrogothGantryMasterViewControllerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'category', 'id')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantrySlaveViewControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrogothGantrySlaveViewController
        fields = '__all__'


class KrogothGantrySlaveViewControllerViewSet(viewsets.ModelViewSet):
    queryset = KrogothGantrySlaveViewController.objects.all()
    serializer_class = KrogothGantrySlaveViewControllerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantryIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrogothGantryIcon
        fields = '__all__'


class KrogothGantryIconViewSet(viewsets.ModelViewSet):
    queryset = KrogothGantryIcon.objects.all()
    serializer_class = KrogothGantryIconSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^code',)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = KrogothGantryCategory
        fields = '__all__'


class KrogothGantryCategoryViewSet(viewsets.ModelViewSet):
    queryset = KrogothGantryCategory.objects.all()
    serializer_class = KrogothGantryCategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name',)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantryDirectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrogothGantryDirective
        fields = '__all__'


class KrogothGantryDirectiveViewSet(viewsets.ModelViewSet):
    queryset = KrogothGantryDirective.objects.all()
    serializer_class = KrogothGantryDirectiveSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class KrogothGantryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KrogothGantryService
        fields = '__all__'


class KrogothGantryServiceViewSet(viewsets.ModelViewSet):
    queryset = KrogothGantryService.objects.all()
    serializer_class = KrogothGantryServiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')


class DynamicJavaScriptInjector(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        name = request.GET['name']
        print('️💛💛💛💛💛💛💛💛💛💛')
        application = KrogothGantryMasterViewController.objects.get(name=name)

        raw_js_services_and_directives = ''
        djangular_services = application.djangular_service.all()

        # raw_js_services_and_directives += '\n\n'
        djangular_directives = application.djangular_directive.all()

        #     raw_js_services_and_directives = raw_js_services_and_directives.replace('_DJANGULAR_DIRECTIVE_TITLE_', directive.title)
        # raw_js_services_and_directives += '\n\n'

        compiled_slave = application.compileModuleSlaves

        # print('WHAT')
        clean_js_slate = '\n\n\n\n\n\n\t /* ════════════' + application.title + '════════════ */\n\n'

        if name == 'home':
            processed_cats = ''
            for cat in KrogothGantryCategory.objects.all():
                icon = 'folder'
                if cat.icon is not None:
                    icon = cat.icon.code
                p1 = 'msNavigationServiceProvider.saveItem("' + cat.name + '", {\n'
                p2 = '\ttitle: "' + cat.title + '",\n'
                p3 = '\ticon: "mdi mdi-' + icon + '",\n'
                p4 = '\tweight: 3\n'
                p5 = '});\n'
                processed_cats += p1 + p2 + p3 + p4 + p5
            cat_contain = compiled_slave['module_with_injected_navigation'].replace('_KROGOTH_CATEGORIES_', processed_cats)
            clean_js_slate += ' \n /* MASTER MODULE */ \n' + cat_contain + \
                              ' \n /* MASTER CONTROLLER */ \n' + application.controller_js
        else:
            clean_js_slate += ' \n /* MASTER MODULE */ \n' + compiled_slave['module_with_injected_navigation'] + \
                              ' \n /* MASTER CONTROLLER */ \n' + application.controller_js
        clean_js_slate += '\n /* SLAVE CONTROLLER */ \n' + compiled_slave['slave_controllers_js']

        # clean_js_slate += application.controller_js.replace('_DJANGULAR_SLAVE_VC_INJECTION_POINT_', '') + \
        #                  ' ' + application.controller_js

        for service in djangular_services:
            raw_js_services_and_directives += '\n /* COMPILED SERVICE */ \n' + \
                                              service.service_js.replace('_DJANGULAR_SERVICE_NAME_',
                                                                         service.name).replace(
                                                  '_DJANGULAR_SERVICE_TITLE_', service.title)
            raw_js_services_and_directives += '\n'
            # raw_js_services_and_directives = raw_js_services_and_directives.replace('_DJANGULAR_SERVICE_TITLE_', service.title)

        # print('THE')
        for directive in djangular_directives:
            raw_js_services_and_directives += '\n /* COMPILED DIRECTIVE */ \n' + \
                                              directive.directive_js.replace('_DJANGULAR_DIRECTIVE_NAME_',
                                                                             directive.name).replace(
                                                  "_DJANGULAR_DIRECTIVE_TITLE_", directive.title)
            raw_js_services_and_directives += '\n'
            # raw_js_services_and_directives = raw_js_services_and_directives

        clean_js_slate += raw_js_services_and_directives

        parsed1 = clean_js_slate.replace('FUSE_APP_NAME', application.name.replace(' ', '_'))
        parsed2 = parsed1.replace('FUSE_APP_TITLE', application.title).replace('FUSE_APP_SLAVE_NAME', application.name + 'Slave')
        parsed3 = parsed2.replace('FUSE_APP_ICON', 'mdi mdi-' + application.icon.code)
        parsed4 = parsed3.replace('NAV_HEADER', application.category.name.replace(' ', '_'))
        try:
            raw_js_response = parsed4.replace('DJANGULAR_USERNAME', request.user.username)
        except:
            raw_js_response = parsed4

        return HttpResponse(raw_js_response, content_type='application/javascript; charset=utf-8')


class DynamicHTMLInjector(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        print('🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡️')
        name = request.GET['name']
        application = KrogothGantryMasterViewController.objects.get(name=name)

        raw_html_response = application.view_html
        raw_html_response += '<style>' + application.style_css + application.get_theme_style + '</style>'

        if raw_html_response == '':
            raw_html_response += '<div layout="column" layout-padding layout-margin>'
            raw_html_response += '<h1>' + application.name.replace('_', ' ') + '</h1>'
            raw_html_response += '<h3>No Fuse App HTML Component</h3>'
            info = "You're seeing this message because no Fuse App HTML component with the type: HTML has not been " + \
                   "added to this Angular Fuse Application named " + application.name
            raw_html_response += "<p>" + info + "</p>"
            raw_html_response += '</div>'
        return HttpResponse(raw_html_response, content_type='text/html; charset=utf-8')


class DynamicHTMLSlaveInjector(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        name = request.GET['name']

        application = KrogothGantrySlaveViewController.objects.get(name=name)
        raw_html_response = application.view_html

        if raw_html_response == '':
            raw_html_response += '<div layout="column" layout-padding layout-margin>'
            raw_html_response += '<h1>' + application.name.replace('_', ' ') + '</h1>'
            raw_html_response += '<h3>No Fuse App HTML Component</h3>'
            info = "You're seeing this message because no Fuse App HTML component with the type: HTML has not been " + \
                   "added to this Angular Fuse Application named " + application.name
            raw_html_response += "<p>" + info + "</p>"
            raw_html_response += '</div>'
        return HttpResponse(raw_html_response, content_type='text/html; charset=utf-8')


class krogoth_gantryModelForm(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        app = 'LazarusII' + '.models'
        model_name = request.GET['model_name']
        model_id = request.GET['model_id']
        module = __import__(app)
        djclass = getattr(module, 'models')
        djmodel = getattr(djclass, model_name)
        queryset = djmodel.objects.filter(id=model_id)
        serialized_obj = django.core.serializers.serialize("json", queryset)
        json_dict = json.loads(serialized_obj)
        finalResponse = ''
        i = 0
        print('️💚💚💚💚💚💚💚💚💚💚')
        for key, value in json_dict[0]['fields'].items():

            filterCategory = 'ng-hide="filter.cbOther === false"'

            # FILTER COMBAT CHECKBOX
            if key == 'Weapon1' or key == 'Weapon2' or key == 'Weapon3' or key == 'canattack' or key == 'SightDistance':
                filterCategory = 'ng-hide="filter.cbCombat === false"'
            if key == 'ImmuneToParalyzer' or key == 'HealTime' or key == 'init_cloaked' or key == 'SelfDestructAs' or key == 'wsec_badTargetCategory':
                filterCategory = 'ng-hide="filter.cbCombat === false"'
            if key == 'NoAutoFire' or key == 'attackrunlength' or key == 'CanDgun' or key == 'BadTargetCategory':
                filterCategory = 'ng-hide="filter.cbCombat === false"'
            if key == 'Stealth' or key == 'antiweapons' or key == 'kamikaze' or key == 'SonarDistance' or key == 'MaxDamage':
                filterCategory = 'ng-hide="filter.cbCombat === false"'
            if key == 'ExplodeAs' or key == 'DamageModifier' or key == 'kamikazedistance' or key == 'RadarDistance':
                filterCategory = 'ng-hide="filter.cbCombat === false"'

            # FILTER NAME INFO CHECKBOX
            if key == 'Name' or key == 'ItalianName' or key == 'ItalianDescription' or key == 'Copyright':
                filterCategory = 'ng-hide="filter.cbNameInfo === false"'
            if key == 'SpanishName' or key == 'SpanishDescription' or key == 'ItalianDescription' or key == 'JapaneseName':
                filterCategory = 'ng-hide="filter.cbNameInfo === false"'
            if key == 'Description' or key == 'FrenchDescription' or key == 'GermanDescription' or key == 'JapanesDescription':
                filterCategory = 'ng-hide="filter.cbNameInfo === false"'
            if key == 'GermanName' or key == 'FrenchName' or key == 'PigLatinDescription' or key == 'Category':
                filterCategory = 'ng-hide="filter.cbNameInfo === false"'
            if key == 'Description' or key == 'PigLatinName' or key == 'Objectname' or key == 'UnitName':
                filterCategory = 'ng-hide="filter.cbNameInfo === false"'

            # FILTER PATHFINDER CHECKBOX
            if key == 'FootprintX' or key == 'MaxVelocity' or key == 'teleporter' or key == 'canhover':
                filterCategory = 'ng-hide="filter.cbPathfinder === false"'
            if key == 'cantbetransported' or key == 'TurnRate' or key == 'MoveRate1' or key == 'DefaultMissionType':
                filterCategory = 'ng-hide="filter.cbPathfinder === false"'
            if key == 'MovementClass' or key == 'canguard' or key == 'Canfly' or key == 'canpatrol':
                filterCategory = 'ng-hide="filter.cbPathfinder === false"'
            if key == 'FootprintZ' or key == 'transportsize' or key == 'canmove' or key == 'Acceleration':
                filterCategory = 'ng-hide="filter.cbPathfinder === false"'
            if key == 'NoChaseCategory' or key == 'maneuverleashlength' or key == 'BrakeRate' or key == 'canstop':
                filterCategory = 'ng-hide="filter.cbPathfinder === false"'

            # FILTER RESOURCES CHECKBOX
            if key == 'BuildCostMetal' or key == 'MetalMake' or key == 'EnergyStorage' or key == 'EnergyMake':
                filterCategory = 'ng-hide="filter.cbResources === false"'
            if key == 'MetalStorage' or key == 'TidalGenerator' or key == 'EnergyUse' or key == 'ExtractsMetal':
                filterCategory = 'ng-hide="filter.cbResources === false"'
            if key == 'WindGenerator' or key == 'BuildCostEnergy' or key == 'MakesMetal' or key == 'CloakCostMoving':
                filterCategory = 'ng-hide="filter.cbResources === false"'

            # FILTER CONSTRUCTION CHECKBOX
            if key == 'BuildTime' or key == 'WorkerTime' or key == 'ActiveWhenBuild' or key == 'Builder':
                filterCategory = 'ng-hide="filter.cbConstruction === false"'
            if key == 'IsAirBase' or key == 'CanReclamate' or key == 'Builddistance' or key == 'CanCapture':
                filterCategory = 'ng-hide="filter.cbConstruction === false"'
            if key == 'BuildAngle' or key == 'istargetingupgrade':
                filterCategory = 'ng-hide="filter.cbConstruction === false"'

            if value != None and value != '':
                type = 'text'
                # if i % 5 == 0:
                #     finalResponse += '<div layout="row">'      cbConstruction
                finalResponse += '<md-input-container ' + filterCategory + ' >'
                finalResponse += '<label class="md-primary-fg md-hue-3">' + str(key) + '</label>' + \
                                 '<input class="md-accent-fg" ng-model="djangularForm.' + str(key) + '" type="' + str(
                    type) + '" ' + \
                                 'value="' + str(value) + '">'
                finalResponse += '</md-input-container>'
                # if i % 5 == 0:
                #     finalResponse += '</div>'
                # i += 1
        return HttpResponse(finalResponse)
