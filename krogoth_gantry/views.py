from rest_framework.views import APIView
from django.template import loader
from django.http import HttpResponse
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_gantry.models import KrogothGantrySlaveViewController, \
    KrogothGantryIcon, KrogothGantryCategory, KrogothGantryMasterViewController, KrogothGantryDirective, \
    KrogothGantryService, AKGantryMasterViewController
from krogoth_gantry.serializers import AbstractKrogothSerializer, KrogothGantryMasterViewControllerSerializer, \
    KrogothGantryIconSerializer, KrogothGantrySlaveViewControllerSerializer, KrogothGantryCategorySerializer, \
    KrogothGantryDirectiveSerializer, KrogothGantryServiceSerializer
from rest_framework import viewsets, serializers, generics, filters
import subprocess
import django_filters.rest_framework
# from django.core import serializers




import json




class KrogothGantryIconViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = KrogothGantryIcon.objects.all()
    serializer_class = KrogothGantryIconSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('code',)



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class KrogothGantryMasterViewControllerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = KrogothGantryMasterViewController.objects.all()
    serializer_class = KrogothGantryMasterViewControllerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'category', 'id')




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class KrogothGantrySlaveViewControllerViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = KrogothGantrySlaveViewController.objects.all()
    serializer_class = KrogothGantrySlaveViewControllerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')


import os
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class KrogothGantryCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = KrogothGantryCategory.objects.all()
    serializer_class = KrogothGantryCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'parent__id')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class KrogothGantryDirectiveViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = KrogothGantryDirective.objects.all()
    serializer_class = KrogothGantryDirectiveSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class KrogothGantryServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = KrogothGantryService.objects.all()
    serializer_class = KrogothGantryServiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^title')

from krogoth_gantry.krogoth_compiler import master_compiler

class DynamicJavaScriptInjector(APIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = request.GET['name']
        raw_js = master_compiler(username=request.user.username)
        js_response = raw_js.compiled_raw(named=name)
        return HttpResponse(js_response, content_type='application/javascript; charset=utf-8')


class DynamicHTMLInjector(APIView):
    # authentication_classes = (TokenAuthentication,)
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
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        name = request.GET['name']
        application = KrogothGantrySlaveViewController.objects.get(name=name)
        raw_html_response = application.view_html
        master = application.owner.get()
        raw_html_response += '<style>' + master.style_css + master.get_theme_style + '</style>'
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
            if key == 'ImmuneToParalyzer' or key == 'HealTime' or key == 'init_cloaked' or key == 'SelfDestructAs' \
                    or key == 'wsec_badTargetCategory':
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
