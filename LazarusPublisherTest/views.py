from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from LazarusDatabase.models import LazarusModProject, LazarusModAsset, LazarusModDependency
from chat.models import JawnUser

import json
import os

from LazarusII.serializers import *
from LazarusII.models import *
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

from rest_framework.renderers import JSONRenderer
# Create your views here.


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



## new assets can be created here:
## /LazarusII/UnitFBIViewset/?encoded_path=media_SLSH_ta_data_SLSH_mattsAbel_SLSH_units_SLSH_anabel&repo_name=Fresh Repo
class ListDependenciesForAsset(APIView):
    def get(self, request, format=None):
        print('\n\nListDependenciesForAsset\n')


class SerializeFBIFileInPathNoSave(APIView):
    def get(self, request, format=None):
        path_to_fbi = '/usr/src/persistent/media/ta_data/mattsAbel_PMkKp5N/units/anabel.fbi'
        print('Opening .FBI file at: ')
        print(path_to_fbi)
        file_contents = open(path_to_fbi, 'r', errors='replace')
        fbi_dump = file_contents.read()
        parse_01 = fbi_dump.replace('\n', '')
        parse_02 = parse_01.replace('\t', '')
        parse_03 = parse_02.replace(';', '",')
        parse_04 = parse_03.replace('=', ':"')
        parse_05 = parse_04.replace('",}', '"}')
        parse_06 = parse_05.replace('",', '","')
        parse_07 = parse_06.replace(':"', '":"')
        parse_08 = parse_07.replace('[UNITINFO]{', '[UNITINFO]{"')
        parse_09 = parse_08.replace('[UNITINFO]', '')
        abel_dict = json.loads(parse_09)
        abel_json = JSONRenderer().render(abel_dict)
        stream = BytesIO(abel_json)
        data = JSONParser().parse(stream)
        fbi_serialized_from_file = UnitFbiDataSerializer_v2(data=data)
        print("FBI was serialized successfully: ")
        print(fbi_serialized_from_file.is_valid())

        return Response(data)

# abel asset id is: 233
class GatherDependenciesForModAssetTestAbel(APIView):

    permission_classes = (IsAuthenticated,)

    def convertJsonToWeaponTDF(self, _json_str):
        weapon_tdf_json = json.loads(_json_str)
        ### REMOVE NON CAVEDOG KEY-VALUE PAIRS:
        weapon_tdf_json.pop('_SNOWFLAKE', None)
        weapon_tdf_json.pop('id', None)
        weapon_tdf_json.pop('_Lazarus_Identifier', None)
        weapon_tdf_json.pop('_DEV_root_data_path', None)
        className = '[' + weapon_tdf_json.pop('_OBJECT_KEY_NAME', None) + ']'
        # print(className)
        pretty = json.dumps(weapon_tdf_json, indent=4, sort_keys=True)
        parse_4 = pretty.replace('": ', '=').replace('\n}', ';\n}').replace(',', ';').replace('ID_weapon', 'ID')
        parse_5 = parse_4.replace('"damage', '[DAMAGE]').replace('_range', 'range')
        parse_7 = parse_5.replace('];', '}').replace('=[', '{').replace('', '').replace('"', '')
        return className + parse_7.replace('[DAMAGE]=', '[DAMAGE] {').replace(';;', ';\n    }\n').replace('=true', '=1').replace('=false', '=0')
    def convertJsonToFeatureTDF(self, _json_str):
        weapon_tdf_json = json.loads(_json_str)
        ### REMOVE NON CAVEDOG KEY-VALUE PAIRS:
        weapon_tdf_json.pop('_SNOWFLAKE', None)
        weapon_tdf_json.pop('id', None)
        weapon_tdf_json.pop('_Lazarus_Identifier', None)
        weapon_tdf_json.pop('_DEV_root_data_path', None)
        className = '[' + weapon_tdf_json.pop('_OBJECT_KEY_NAME', None) + ']'
        pretty = json.dumps(weapon_tdf_json, indent=4, sort_keys=True)
        parse_2 = pretty.replace('": ', '=').replace('\n}', ';\n}')
        parse_6 = parse_2.replace(',', ';').replace('];', '}').replace('=[', '{')
        parse_7 = parse_6.replace('"', '').replace('_object=', 'object=')
        return className + parse_7.replace('=true', '=1').replace('=false', '=0')
    def convertJsonToDownloadTDF(self, _json_str):
        weapon_tdf_json = json.loads(_json_str)
        ### REMOVE NON CAVEDOG KEY-VALUE PAIRS:
        weapon_tdf_json.pop('_SNOWFLAKE', None)
        weapon_tdf_json.pop('id', None)
        weapon_tdf_json.pop('_Lazarus_Identifier', None)
        weapon_tdf_json.pop('_DEV_root_data_path', None)
        weapon_tdf_json.pop('parent_unit', None)
        className = '[' + weapon_tdf_json.pop('MENUENTRY', None) + ']'
        pretty = json.dumps(weapon_tdf_json, indent=4, sort_keys=True)
        parse_4 = pretty.replace('": ', '=').replace('\n}', ';\n}').replace(',', ';')
        parse_7 = parse_4.replace('];', '}').replace('=[', '{').replace('', '').replace('"', '')
        return className + parse_7
    def convertJsonToUnitFBI(self, _json_str):
        weapon_tdf_json = json.loads(_json_str)
        ### REMOVE NON CAVEDOG KEY-VALUE PAIRS:
        weapon_tdf_json.pop('id', None)
        className = '[UNITINFO]'
        pretty = json.dumps(weapon_tdf_json, indent=4, sort_keys=True)
        parse_1 = pretty.replace('": ', '=')
        parse_2 = parse_1.replace('\n}', ';\n}')
        parse_3 = parse_2.replace(',', ';')
        parse_4 = parse_3.replace('ID_weapon', 'ID')
        parse_5 = parse_4.replace('"damage', '[DAMAGE]').replace('_range', 'range')
        parse_6 = parse_5.replace('];', '}').replace('=[', '{').replace('', '')
        parse_7 = parse_6.replace('"', '').replace('=true', '=1').replace('=false', '=0')
        return className + parse_7
    def processFiles(self, ass_id):
        hd = ' ══════════════════════════ '
        print('\n\n\033[91m' + '\033[4m' + '\033[44m' + '\033[1m' + hd + ' ASSET: ' +
              str(ass_id) + hd + '\033[0m' + '\033[0m' + '\033[0m' + '\033[0m')
        asset = LazarusModDependency.objects.filter(asset_id=ass_id)
        

        log_nonedit = 'Non editable dependencies: '
        not_editable_deps = []

        filter_nonedit = ['file.cob', 'file.gaf', 'file.3do', 'file.pcx', 'n/a', 'file.wav']

        downloadTDF_ids = []
        unitFBI_id = -1
        weaponTDF_ids = []
        featureTDF_ids = []

        new_weapon_tdf_document = {"text_body":"", "name":"nan"}
        new_download_tdf_document = {"text_body":"", "name":"nan"}
        new_feature_tdf_document = {"text_body":"", "name":"nan"}
        new_unit_fbi_document = {"text_body":"", "name":"nan"}

        data_ball = {}

        data_ball['weapons'] = {}
        data_ball['units'] = {}
        data_ball['features'] = {}
        data_ball['downloads'] = {}
        # These hold arrays of string system paths
        data_ball['bitmaps'] = []
        data_ball['anims'] = []
        data_ball['objects3d'] = []
        data_ball['scripts'] = []
        data_ball['sounds'] = []
        data_ball['unitpics'] = []
#file.3do
        for dep in asset:
            if (dep.model_schema in filter_nonedit) == True:
                not_editable_deps.append(dep)
                log_nonedit += dep.model_schema + ' '
                if dep.model_schema == 'file.pcx':
                    data_ball['unitpics'].append(dep.system_path)
                elif dep.model_schema == 'file.3do':
                    data_ball['objects3d'].append(dep.system_path)
                elif dep.model_schema == 'file.cob':
                    data_ball['scripts'].append(dep.system_path)
                elif dep.model_schema == 'file.gaf':
                    data_ball['anims'].append(dep.system_path)
                elif dep.model_schema == 'file.wav' or dep.model_schema == 'n/a':
                    print(bcolors.WARNING + 
                    'Warning - Lazarus still defines .wav dependencies as n/a. This might break things.' + 
                    bcolors.ENDC)
                    data_ball['sounds'].append(dep.system_path)
            if dep.model_schema == 'DownloadTDF':
                downloadTDF_ids.append(dep.model_id)
            if dep.model_schema == 'FeatureTDF':
                featureTDF_ids.append(dep.model_id)
            if dep.model_schema == 'WeaponTDF':
                weaponTDF_ids.append(dep.model_id)
            if dep.model_schema == 'UnitFbiData':
                unitFBI_id = dep.model_id

        unit_fbi_queryset = UnitFbiData.objects.get(id=unitFBI_id)
        
        for weapon in weaponTDF_ids:
            queryset = WeaponTDF.objects.get(id=weapon)
            serializer = WeaponTDFDataSerializer(queryset)

            no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
            no_null_keys.pop('damage')

            dmg_str_val = ''

            for dmg in queryset.damage.all():
                print('\033[33m' + dmg.name + '=' + str(dmg.damage_amount) + '\033[0m; \n')
                dmg_str_val += ('        ' + dmg.name + '=' + str(dmg.damage_amount) + ';')

            no_null_keys['damage'] = dmg_str_val

            asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
            asTDF = self.convertJsonToWeaponTDF(asJSON)

            # print('WeaponTDF: \033[34m')
            # print(json.dumps(no_null_keys, indent=4, sort_keys=True))
            # print('\033[0m\n')
            # print(asTDF)
            new_weapon_tdf_document['name'] = unit_fbi_queryset.UnitName
            new_weapon_tdf_document['text_body'] += asTDF + '\n'


        
        for download in downloadTDF_ids:
            queryset = DownloadTDF.objects.get(id=download)
            serializer = DownloadTDFDataSerializer(queryset)

            no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
            asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
            asTDF = self.convertJsonToDownloadTDF(asJSON)
            # print('DownloadTDF: \033[32m')
            # print(json.dumps(no_null_keys, indent=4, sort_keys=True))
            # print('\033[0m')
            # print(asTDF)
            new_download_tdf_document['name'] = unit_fbi_queryset.UnitName
            new_download_tdf_document['text_body'] += asTDF + '\n'

        
        for feature in featureTDF_ids:
            try:
                queryset = FeatureTDF.objects.get(id=feature)
                serializer = FeatureTDFDataSerializer(queryset)
                no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
                asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
                asTDF = self.convertJsonToFeatureTDF(asJSON)
                # print('FeatureTDF: \033[36m')
                # print(json.dumps(no_null_keys, indent=4, sort_keys=True))
                # print('\033[0m')
                # print(asTDF)
                new_feature_tdf_document['name'] = unit_fbi_queryset.corpse
                new_feature_tdf_document['text_body'] += asTDF + '\n'
            except:
                print('\033[31m')
                print('FEATURE TDF FAILED ! ! !')
                print('\033[0m')

        
        serializer = UnitFbiDataSerializer_v2(unit_fbi_queryset)
        
        no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
        asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
        asTDF = self.convertJsonToUnitFBI(asJSON)
        new_unit_fbi_document['name'] = unit_fbi_queryset.UnitName
        new_unit_fbi_document['text_body'] = asTDF
        # print('UnitFBI: \033[30m')
        # print(json.dumps(no_null_keys, indent=4, sort_keys=True))
        # print('\033[0m')
        # print(asTDF)

        print('\033[92m')
        print(log_nonedit)
        print('\033[0m')

        print(bcolors.lightgreen)
        print(new_download_tdf_document['text_body'])
        print(bcolors.ENDC)

        print(bcolors.purple)
        print(new_weapon_tdf_document['text_body'])
        print(bcolors.ENDC)
        
        print(bcolors.TEAL)
        print(new_feature_tdf_document['text_body'])
        print(bcolors.ENDC)
        
        print(bcolors.OKBLUE)
        print(new_unit_fbi_document['text_body'])
        print(bcolors.ENDC)

        data_ball['weapons'] = new_weapon_tdf_document
        data_ball['units'] = new_unit_fbi_document
        data_ball['features'] = new_feature_tdf_document
        data_ball['downloads'] = new_download_tdf_document
        

        return data_ball

    def copyFilesToPublishModBuildDestination(self, pathToModPublish, modData):
        print('Building Mod: ' + pathToModPublish)
        #pathToModPublish = '/usr/src/app/static/PublishedModsDebug'
        #print('DEBUG OVVERRIDE, PUBLISHING TO: ' + pathToModPublish)
        # fOut = pathToModPublish + '/test.txt'
        # fileoutput_fbi = open(fOut, 'w', errors='replace')
        # fileoutput_fbi.write(str(modData))
        # fileoutput_fbi.close()

        # We need to create all the root HPI directories
        path_bitmaps = pathToModPublish + '/bitmaps'
        path_anims = pathToModPublish + '/anims'
        path_download = pathToModPublish + '/download'
        path_features = pathToModPublish + '/features/corpses'

        path_objects3d = pathToModPublish + '/objects3d'
        path_scripts = pathToModPublish + '/scripts'
        path_sounds = pathToModPublish + '/sounds'
        path_unitpics = pathToModPublish + '/unitpics'
        path_units = pathToModPublish + '/units'
        path_weapons = pathToModPublish + '/weapons'

        print('Moving custom mod art into position...')
        print(path_bitmaps)

        os.makedirs(path_bitmaps)
        os.makedirs(path_anims)
        os.makedirs(path_download)
        os.makedirs(path_features)
        os.makedirs(path_objects3d)
        os.makedirs(path_scripts)
        os.makedirs(path_sounds)
        os.makedirs(path_unitpics)
        os.makedirs(path_units)
        os.makedirs(path_weapons)

        for asset in modData:               
            print(bcolors.cyan)
            print('building assets...')
            print(bcolors.ENDC)
            print(bcolors.green)
            print('weapons')
            print(bcolors.ENDC)
            print(bcolors.orange)
            print(asset['weapons'])
            print(bcolors.ENDC)
            print(bcolors.green)
            print('units')
            print(bcolors.ENDC)
            print(bcolors.orange)
            print(asset['units'])
            print(bcolors.ENDC)
            print(bcolors.green)
            print('features')
            print(bcolors.ENDC)
            print(bcolors.orange)
            print(asset['features'])
            print(bcolors.ENDC)
            print(bcolors.green)
            print('downloads')
            print(bcolors.ENDC)
            print(bcolors.orange)
            print(asset['downloads'])
            print(bcolors.ENDC)

            # data_ball['bitmaps'] = []
            # data_ball['anims'] = []
            # data_ball['objects3d'] = []
            # data_ball['scripts'] = []
            # data_ball['sounds'] = []
            # data_ball['unitpics'] = []

            print(bcolors.red)
            print('anims')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['anims'])
            print(bcolors.ENDC)
            print(bcolors.red)
            print('objects3d')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['objects3d'])
            print(bcolors.ENDC)
            print(bcolors.red)
            print('scripts')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['scripts'])
            print(bcolors.ENDC)
            print(bcolors.red)
            print('sounds')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['sounds'])
            print(bcolors.ENDC)
            print('unitpics')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['unitpics'])
            print(bcolors.ENDC)
            print('bitmaps')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['bitmaps'])
            print(bcolors.ENDC)
            
            # generate unit fbi:
            ufbiOut = pathToModPublish + '/units/' + asset['units']['name'] + '.fbi'
            fileoutput_fbi = open(ufbiOut, 'w', errors='replace')
            fileoutput_fbi.write(asset['units']['text_body'])
            fileoutput_fbi.close()

            # generate weapon tdf:
            wtdfOut = pathToModPublish + '/weapons/' + asset['weapons']['name'] + '.tdf'
            fileoutput_tdf1 = open(wtdfOut, 'w', errors='replace')
            fileoutput_tdf1.write(asset['weapons']['text_body'])
            fileoutput_tdf1.close()
            # generate download tdf:
            dtdfOut = pathToModPublish + '/download/' + asset['downloads']['name'] + '.tdf'
            fileoutput_tdf2 = open(dtdfOut, 'w', errors='replace')
            fileoutput_tdf2.write(asset['downloads']['text_body'])
            fileoutput_tdf2.close()
            # generate feature tdf:
            ftdfOut = pathToModPublish + '/features/' + asset['features']['name'] + '.tdf'
            fileoutput_tdf3 = open(ftdfOut, 'w', errors='replace')
            fileoutput_tdf3.write(asset['features']['text_body'])
            fileoutput_tdf3.close()



        ## need to copy non-editable stuff first:
        # cp model.3do /usr/src/persistent/media/ta_data/ArmPrime_1.0_Arm_GorGant/objects3d/

        print('Copying uneditable dependencies... ')
        # I have no clue how in the hell this isnt crashing...
        # asset here is undefined...
        for model in asset['objects3d']:
            file_name = model.split('/')[len(model.split('/')) - 1]
            cmd_ = 'cp ' + model + ' ' + path_objects3d + '/' + file_name
            print(bcolors.OKGREEN + cmd_ + bcolors.ENDC)
            os.system(cmd_)
        for model in asset['scripts']:
            file_name = model.split('/')[len(model.split('/')) - 1]
            cmd_ = 'cp ' + model + ' ' + path_scripts + '/' + file_name
            print(bcolors.OKGREEN + cmd_ + bcolors.ENDC)
            os.system(cmd_)
        for model in asset['sounds']:
            file_name = model.split('/')[len(model.split('/')) - 1]
            cmd_ = 'cp ' + model + ' ' + path_sounds + '/' + file_name
            print(bcolors.OKGREEN + cmd_ + bcolors.ENDC)
            os.system(cmd_)
        for model in asset['unitpics']:
            file_name = model.split('/')[len(model.split('/')) - 1]
            cmd_ = 'cp ' + model + ' ' + path_unitpics + '/' + file_name
            print(bcolors.OKGREEN + cmd_ + bcolors.ENDC)
            os.system(cmd_)
        for model in asset['anims']:
            file_name = model.split('/')[len(model.split('/')) - 1]
            cmd_ = 'cp ' + model + ' ' + path_anims + '/' + file_name
            print(bcolors.OKGREEN + cmd_ + bcolors.ENDC)
            os.system(cmd_)
        #print('Saved File: ' + fOut)
        
        # weapon.tdf file:
        # text_body

        print('\n\n\nOKAY, NOW THE MOD WILL BE PACKED INTO A UFO: ')
        # pathToModPublish
        # HPIPack [-d DirectoryToPack] [-f HPIFileName] [auto]
        # /usr/src/app/static/HPI_Tools/HPIPack.exe
        exe = '/usr/src/app/static/HPI_Tools/HPIPack.exe'
        cmd_compress = "DISPLAY=:0 wine " + exe + " -d '" + pathToModPublish + "' -f '" + pathToModPublish + "/lazarus_mod.ufo' auto"
        # cmd_compress = "bash compressTA_Mod.sh " + pathToModPublish + " " + pathToModPublish + '/lazarus_mod.ufo'
        # os.system(cmd_compress)
        os.system('zip -r ' + pathToModPublish + 'lazarus_mod.ufo ' + pathToModPublish)
        print('zip -r ' + pathToModPublish + 'lazarus_mod ' + pathToModPublish)
        return pathToModPublish + 'lazarus_mod.ufo'

    def get(self, request, format=None):
        # Process Files For Individual Assets:
        # self.processFiles(233)
        # self.processFiles(234)
        # self.processFiles(235)
        # self.processFiles(236)
        # self.processFiles(237)

        artist_id = request.user.id
        artist_name = request.user.username
        # all_mods = LazarusModProject.objects.filter(created_by=request.user.id)

        jawn_user = JawnUser.objects.get(base_user=request.user)
        all_mods = LazarusModProject.objects.filter(created_by=jawn_user)

        selectedModName = ''
        selectedModId = -1
        print('looping through all mods: ')
        for mod in all_mods:
            print(mod)
            if mod.is_selected == True:
                selectedModName = mod.name
                selectedModId = mod.id

        data_of_units = []
        assetsForProject = LazarusModAsset.objects.filter(project_id=selectedModId)
        for asset in assetsForProject:
            unit_data = self.processFiles(asset.id)
            data_of_units.append(unit_data)


        artists_selected_mod_name = selectedModName.replace(' ', '_').replace('#', '_').replace('!', '_')
        artists_output_path_for_all_mods = '/usr/src/persistent/media/published_mods_v1/' + artist_name + '_' + str(artist_id)
        mod_build_path = artists_output_path_for_all_mods + '/' + artists_selected_mod_name

        print('checking if artists mod collection exists: ')
        print(artists_output_path_for_all_mods)

        # rare case it fails to get mod id
        if selectedModId == -1:
            return Response('Critical Error, couldn\'t find the selected mod for user making this request.')

        if not os.path.exists(artists_output_path_for_all_mods):
            print("Creating Root Mod Build Directory:")
            print(mod_build_path)
            os.makedirs(mod_build_path)
            total_builds = 0
            new_mod_build_path = mod_build_path + '/' + artists_selected_mod_name + '_v1.' + str(total_builds)
            safe_mod_build_path = new_mod_build_path.replace(' ', '_').replace('#', '_').replace('!', '_')
            os.makedirs(safe_mod_build_path)
            print('\nPath for new mod build created: ' + new_mod_build_path)
            # TODO: Now, copy all files to this directory!
            link = self.copyFilesToPublishModBuildDestination(new_mod_build_path, data_of_units)
            return Response(link)
        else:
            print(mod_build_path + " already exists, \nTotal Builds For:")
            print(mod_build_path)
            total_builds = len(os.listdir(mod_build_path))
            print(total_builds)
            new_mod_build_path = mod_build_path + '/' + artists_selected_mod_name + '_v1.' + str(total_builds)
            safe_mod_build_path = new_mod_build_path.replace(' ', '_').replace('#', '_').replace('!', '_')
            os.makedirs(safe_mod_build_path)
            print('\nPath for new mod build created: ' + new_mod_build_path)
            # TODO: Now, copy all files to this directory!
            link = self.copyFilesToPublishModBuildDestination(new_mod_build_path, data_of_units)
            return Response(link)
        return Response(data_of_units)




# Try instead with new UnitFbiDataSerializer_v2
"""
>>> from LazarusII.serializers import *
>>> from LazarusII.models import *
>>>
>>> ## UnitFbiDataSerializer
>>> ## UnitFbiData
>>>
>>> from django.utils.six import BytesIO
>>> from rest_framework.parsers import JSONParser
>>>



>>> fbi_abel = UnitFbiData.objects.get(id=899)
>>> fbi_serializer = UnitFbiDataSerializer(fbi_abel)
>>> fbi_serializer.data


>>> path_to_fbi = '/usr/src/persistent/media/ta_data/mattsAbel_PMkKp5N/units/anabel.fbi'
>>> import codecs

>>> file_contents = open(path_to_fbi, 'r', errors='replace')
>>> fbi_dump = f3.read()

>>> parse_01 = fbi_dump.replace('\n', '')
>>> parse_02 = parse_01.replace('\t', '')
>>> parse_03 = parse_02.replace(';', '",')
>>> parse_04 = parse_03.replace('=', ':"')
>>> parse_05 = parse_04.replace('",}', '"}')
>>> parse_06 = parse_05.replace('",', '","')
>>> parse_07 = parse_06.replace(':"', '":"')
>>> parse_08 = parse_07.replace('[UNITINFO]{', '[UNITINFO]{"')
>>> parse_09 = parse_08.replace('[UNITINFO]', '')

>>> ## import json
>>> abel_dict = json.loads(parse_09)

>>> from rest_framework.renderers import JSONRenderer
>>> abel_json = JSONRenderer().render(fbi_serializer.data)
>>> stream = BytesIO(abel_json)
>>> data = JSONParser().parse(stream)
>>> fbi_serialized_from_file = UnitFbiDataSerializer(data=data)
>>> print(fbi_serialized_from_file.is_valid())
False
>>> fbi_serialized_from_file.validated_data
{}
"""
