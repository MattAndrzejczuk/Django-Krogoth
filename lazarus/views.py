from django.shortcuts import render

# Create your views here.
# MAIN
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, generics
# from cinicraft_home.serializers import GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from subprocess import Popen, PIPE
import platform
# file listing stuff
import os
from os import walk
from os import listdir
from os.path import isfile, join
from PIL import Image
import json
import re
from rest_framework.permissions import IsAuthenticated, AllowAny
from GeneralWebsiteInfo.models import WebsiteColorTheme
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF
from django.core import serializers
from LazarusII.FbiData import remove_comments
from rest_framework import status




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





class FeatureTDFFetch():
    def get(self, file_path):
        f3 = open(file_path, 'r', errors='replace')

        # print("OPENING DOWNLOAD TDF... ")
        incoming_tdf = remove_comments(f3.read())
        # print(incoming_tdf)
        # print('TDF Opened Successfully ! ! !')

        status_code = status.HTTP_200_OK

        def parseNested(_tdf, nOBJECT_NAME):
            nparsed_0 = _tdf.replace('[' + nOBJECT_NAME + ']', '')
            nparsed_1 = nparsed_0
            nparsed_2 = nparsed_1.replace('[', '"')
            nparsed_3 = nparsed_2.replace(']', '" :')
            nparsed_4 = nparsed_3.replace('=', '" : "')
            nparsed_5 = nparsed_4.replace(';', '", "')
            nparsed_6 = nparsed_5.replace('{', '{ "')
            nparsed_7 = nparsed_6.replace(', "}', '}')
            nparsed_8 = nparsed_7.replace(', ""', ', "')
            nparsed_9 = nparsed_8.replace('", " }', '"}').replace(' ', '')
            return nparsed_9

        def getNestedType(_tdf):
            try:
                _BrkStart = [m.start() for m in re.finditer('\[', _tdf)]
                _BrkEnd = [m.start() for m in re.finditer('\]', _tdf)]
                return _tdf[int(str(_BrkStart[0])) + 1:int(str(_BrkEnd[0]))]
            except:
                return ''

        dict_list = []
        rmv_tabs_n_spaces0 = incoming_tdf.replace('\t', '')
        rmv_tabs_n_spaces1 = rmv_tabs_n_spaces0.replace('\n', '').strip()
        _tdf_prep = rmv_tabs_n_spaces1.replace(' ', '').replace('} [', '}|[').replace('}[', '}|[')

        # print('TDF PREPPED AND READY FOR JSONIFYING: ')
        # print(_tdf_prep)
        # print('______________________________________')

        split_tdf = _tdf_prep.split('|')

        for item in split_tdf:
            nested_obj = parseNested(item, getNestedType(item))
            # print(nested_obj)

        for item in split_tdf:
            nested_type = getNestedType(item)
            # print("NESTED TYPE:  " + nested_type)
            nested_obj = parseNested(item, nested_type)
            # print(nested_obj)
            dictionary = json.loads(nested_obj)
            dictionary['Object_Name'] = nested_type
            dict_list.append(dictionary)

        # print('JSON DUMPS: ')
        # print(json.dumps(dict_list))

        arrayOfNewFeatures = []
        ##### SAVE TO SQL:
        for item in dict_list:
            new_feature = FeatureTDF()
            new_feature._DEV_root_data_path = file_path
            ### 37
            try:
                new_feature.animating = item['animating']
            except:
                pass
            try:
                new_feature.animtrans = item['animtrans']
            except:
                pass
            try:
                new_feature.autoreclaimable = item['autoreclaimable']
            except:
                pass
            try:
                new_feature.burnmax = item['burnmax']
            except:
                pass
            try:
                new_feature.burnmin = item['burnmin']
            except:
                pass
            try:
                new_feature.burnweapon = item['burnweapon']
            except:
                pass
            try:
                new_feature.category = item['category']
            except:
                pass
            try:
                new_feature.description = item['description']
            except:
                pass
            try:
                new_feature.blocking = item['blocking']
            except:
                pass
            try:
                new_feature.damage = item['damage']
            except:
                pass
            try:
                new_feature.energy = item['energy']
            except:
                pass
            try:
                new_feature.featuredead = item['featuredead']
            except:
                pass
            try:
                new_feature.featurereclamate = item['featurereclamate']
            except:
                pass
            try:
                new_feature.filename = item['filename']
            except:
                pass
            try:
                new_feature.flamable = item['flamable']
            except:
                pass
            try:
                new_feature.footprintx = item['footprintx']
            except:
                pass
            try:
                new_feature.footprintz = item['footprintz']
            except:
                pass
            try:
                new_feature.geothermal = item['geothermal']
            except:
                pass
            try:
                new_feature.height = item['height']
            except:
                pass
            try:
                new_feature.hitdensity = item['hitdensity']
            except:
                pass
            try:
                new_feature.indestructible = item['indestructible']
            except:
                pass
            try:
                new_feature.metal = item['metal']
            except:
                pass
            try:
                new_feature.nodisplayinfo = item['nodisplayinfo']
            except:
                pass
            try:
                new_feature._object = item['object']
            except:
                pass
            try:
                new_feature.permanent = item['permanent']
            except:
                pass
            try:
                new_feature.reclaimable = item['reclaimable']
            except:
                pass
            try:
                new_feature.reproduce = item['reproduce']
            except:
                pass
            try:
                new_feature.reproducearea = item['reproducearea']
            except:
                pass
            try:
                new_feature.seqname = item['seqname']
            except:
                pass
            try:
                new_feature.seqnameburn = item['seqnameburn']
            except:
                pass
            try:
                new_feature.seqnamedie = item['seqnamedie']
            except:
                pass
            try:
                new_feature.seqnamereclamate = item['seqnamereclamate']
            except:
                pass
            try:
                new_feature.seqnameshad = item['seqnameshad']
            except:
                pass
            try:
                new_feature.shadtrans = item['shadtrans']
            except:
                pass
            try:
                new_feature.sparktime = item['sparktime']
            except:
                pass
            try:
                new_feature.spreadchance = item['spreadchance']
            except:
                pass
            try:
                new_feature.world = item['world']
            except:
                pass
            try:
                arrayOfNewFeatures.append(new_feature)
                new_feature.save()
                status_code = status.HTTP_201_CREATED
            except:
                pass
        return arrayOfNewFeatures






class DependenciesForUnitFBI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        sampleunit = UnitFbiData.objects.filter(UnitName='ARMDEF')
        serialized_obj = serializers.serialize("json", sampleunit)
        json_dict = json.loads(serialized_obj)

        ## NEED TO GRAB THE
        dev_root_path = '/usr/src/persistent/media/ta_data/arm_fubar/units/armdef.fbi'
        last_occurance_of_slash = dev_root_path.rfind("/")
        fbi_file = dev_root_path[last_occurance_of_slash:]
        # THE ROOT PATH OF THE UNIT HPI
        path_without_fbi = dev_root_path.replace(fbi_file, '').replace('/units', '')
        # WE NEED THIS TO KNOW WHERE TO LOOK FOR ALL DEPENDENCIES.

        # SO NOW WE HAVE THIS:
        # '/usr/src/persistent/media/ta_data/arm_fubar/'
        # BEGIN SCANNING THE FBI FILE TO LOCATE ALL DEPENDENCIES
        #
        # keys used to find dependencies:
        # -------------------------------
        # Objectname        ->  /arm_fubar/objects3d/{ Objectname }
        #                       /arm_fubar/scripts/{ Objectname }
        # UnitName          ->  /arm_fubar/unitpics/{ UnitName }
        #                       /arm_fubar/download/{ UnitName }
        # SoundCategory     -> SOUNDS.txt
        # ExplodeAs         -> UNITS.txt
        # SelfDestructAs    -> UNITS.txt
        # Corpse            -> /arm_fubar/features/corpses/{ UnitName }
        # Weapon1           -> /arm_fubar/weapons/{ UnitName }
        # Weapon2           -> /arm_fubar/weapons/{ UnitName }
        # Weapon3           -> /arm_fubar/weapons/{ UnitName }
        # -------------------------------



        #   /usr/src/persistent/media/ta_data/arm_fubar : /armdef.fbi
        definer = bcolors.purple + \
                  path_without_fbi + \
                  ' : ' + bcolors.ENDC
        end_val = bcolors.orange + \
                  fbi_file + \
                  bcolors.ENDC
        print(definer + end_val)


        ### DEPENDENCIES CHECKLIST:
        dp_unitpic = False
        dp_3dmodel = False
        dp_script = False
        dp_corpses = False
        dp_allweapons = False

        print('')


        # UnitName
        definer = bcolors.TEAL + \
                  'UnitName' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '       ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.orange + \
                  sampleunit[0].UnitName + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        unit_pic_path = path_without_fbi + '/unitpics/'
        uname = sampleunit[0].UnitName.lower()
        # /ta_data/UNAME/unitpics/
        dp_unitpic = os.path.exists(unit_pic_path + uname + '.pcx')
        print('unit pic exists : ' + str(dp_unitpic))
        # -------------------------------

        # Objectname
        definer = bcolors.TEAL + \
                  'Objectname' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '     ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.orange + \
                  sampleunit[0].Objectname + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # /ta_data/UNAME/objects3d/
        unit_3do_path = path_without_fbi + '/objects3d/'
        uobjname = sampleunit[0].Objectname.lower()
        dp_3dmodel = os.path.exists(unit_3do_path + uobjname + '.3do')
        print('unit 3do exists : ' + str(dp_3dmodel))
        # /ta_data/UNAME/scripts/
        unit_cob_path = path_without_fbi + '/scripts/'
        ucobname = sampleunit[0].Objectname.lower()
        dp_script = os.path.exists(unit_cob_path + ucobname + '.cob')
        print('unit cob exists : ' + str(dp_script))
        # -------------------------------


        # SoundCategory
        definer = bcolors.TEAL + \
                  'SoundCategory' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '  ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].SoundCategory + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # -------------------------------

        # ExplodeAs
        definer = bcolors.TEAL + \
                  'ExplodeAs' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '      ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].ExplodeAs + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # -------------------------------

        # SelfDestructAs
        definer = bcolors.TEAL + \
                  'SelfDestructAs' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  ' ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].SelfDestructAs + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # -------------------------------

        # Corpse
        definer = bcolors.TEAL + \
                  'Corpse' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '         ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].Corpse + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # /ta_data/UNAME/features/corpses/
        corpsename = sampleunit[0].Corpse.lower()
        unit_corpse_path = path_without_fbi + '/features/corpses/' + corpsename + '.tdf'
        dp_corpses = os.path.exists(unit_corpse_path)
        print('unit feature corpse exists : ' + str(dp_corpses))
        #FeatureTDFViewset.get()
        # -------------------------------

        # Weapon1
        definer = bcolors.TEAL + \
                  'Weapon1' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '        ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].Weapon1 + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # -------------------------------

        try:
            # Weapon2
            definer = bcolors.TEAL + \
                      'Weapon2' + \
                      bcolors.ENDC
            midchar = bcolors.lightgreen + \
                      '        ->  ' + \
                      bcolors.ENDC
            end_val = bcolors.lightred + \
                      sampleunit[0].Weapon2 + \
                      bcolors.ENDC
            print(definer + midchar + end_val)
        except:
            print('')
        # -------------------------------

        try:
            # Weapon3
            definer = bcolors.TEAL + \
                      'Weapon3' + \
                      bcolors.ENDC
            midchar = bcolors.lightgreen + \
                      '        ->  ' + \
                      bcolors.ENDC
            end_val = bcolors.lightred + \
                      sampleunit[0].Weapon3 + \
                      bcolors.ENDC
            print(definer + midchar + end_val)
        except:
            print('')
        # -------------------------------


        print('unit pic path: ')
        print(os.listdir(unit_pic_path))

        corpseTDF = FeatureTDFFetch().get(unit_corpse_path)
        print(corpseTDF)
        print('')

        return Response(json_dict)




class CustomHtmlGenerator(APIView):
    def get(self, request, format=None):
        # msg = str(request.GET['msg'])
        html = '<div> <h1>Some Basic HTML</h1> <p>This is everything.</p> </div>'
        return HttpResponse(html)


class ThemeConstantConfigView(APIView):
    def get(self, request, format=None):
        theme_to_use = 'default : {"primary":{"name":"fuse-paleblue","hues":{"default":"700","hue-1":"500","hue-2":"600","hue-3":"400"}},"accent":{"name":"deep-orange","hues":{"default":"600","hue-1":"400","hue-2":"700","hue-3":"A100"}},"warn":{"name":"fuse-blue","hues":{"default":"500","hue-1":"300","hue-2":"800","hue-3":"A100"}},"background":{"name":"blue-grey","hues":{"default":"50","hue-1":"A100","hue-2":"100","hue-3":"200"}}}'
        pt1_path = '/usr/src/app/DjangularStaticFiles/fuse-themes.constant.pt1.js'
        pt2_path = '/usr/src/app/DjangularStaticFiles/fuse-themes.constant.pt2.js'
        theme_js_pt1 = open(pt1_path, 'r', errors='replace').read()
        theme_js_pt2 = open(pt2_path, 'r', errors='replace').read()
        theme_in_db = WebsiteColorTheme.objects.filter(enabled=True)
        if len(theme_in_db) > 0:
            theme_to_use = theme_in_db[0].replace('"CUSTOM_THEME_NAME"', 'default')
        finalHTML = theme_js_pt1 + theme_to_use + theme_js_pt2
        print(finalHTML)
        return HttpResponse(finalHTML)


####    --------------------------------------------
####    ------------------------------------------------------------------------------------------------------------
####    --------------------------------------------
