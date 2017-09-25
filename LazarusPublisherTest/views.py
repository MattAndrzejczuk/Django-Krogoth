from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from LazarusDatabase.models import LazarusModProject, LazarusModAsset, LazarusModDependency

import json

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
        return parse_7.replace('[DAMAGE]=', '[DAMAGE] {').replace(';;', '\n    }\n')
    def convertJsonToFeatureTDF(self, _json_str):
        weapon_tdf_json = json.loads(weapon_tdf_str)
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
        return parse_7
    def convertJsonToDownloadTDF(self, _json_str):
        weapon_tdf_json = json.loads(weapon_tdf_str)
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
        return parse_7
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
        parse_7 = parse_6.replace('"', '')
        return parse_7
    def processFiles(self, ass_id):
        hd = ' ══════════════════════════ '
        print('\n\n\033[91m' + '\033[4m' + '\033[44m' + '\033[1m' + hd + ' ASSET: ' +
              str(ass_id) + hd + '\033[0m' + '\033[0m' + '\033[0m' + '\033[0m')
        asset = LazarusModDependency.objects.filter(asset_id=ass_id)

        log_nonedit = 'Non editable dependencies: '
        not_editable_deps = []

        filter_nonedit = ['file.cob', 'file.gaf', 'file.3do', 'file.pcx', 'n/a']

        downloadTDF_ids = []
        unitFBI_id = -1
        weaponTDF_ids = []
        featureTDF_ids = []

        for dep in asset:
            if (dep.model_schema in filter_nonedit) == True:
                not_editable_deps.append(dep)
                log_nonedit += dep.model_schema + ' '
            if dep.model_schema == 'DownloadTDF':
                downloadTDF_ids.append(dep.model_id)
            if dep.model_schema == 'FeatureTDF':
                featureTDF_ids.append(dep.model_id)
            if dep.model_schema == 'WeaponTDF':
                weaponTDF_ids.append(dep.model_id)
            if dep.model_schema == 'UnitFbiData':
                unitFBI_id = dep.model_id

        for weapon in weaponTDF_ids:
            queryset = WeaponTDF.objects.get(id=weapon)
            serializer = WeaponTDFDataSerializer(queryset)
            # print('\033[31m')
            # print(serializer.data)
            # print('\033[0m')

            no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
            no_null_keys.pop('damage')

            dmg_str_val = ''

            for dmg in queryset.damage.all():
                print('\033[33m' + dmg.name + '=' + str(dmg.damage_amount) + '\033[0m; \n')
                dmg_str_val += ('        ' + dmg.name + '=' + str(dmg.damage_amount) + ';')

            no_null_keys['damage'] = dmg_str_val

            asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
            asTDF = self.convertJsonToWeaponTDF(asJSON)

            print('WeaponTDF: \033[34m')
            print(json.dumps(no_null_keys, indent=4, sort_keys=True))
            print('\033[0m\n')
            print(asTDF)

        for download in downloadTDF_ids:
            queryset = DownloadTDF.objects.get(id=download)
            serializer = DownloadTDFDataSerializer(queryset)
            # print('\033[31m')
            # print(serializer.data)
            # print('\033[0m')

            no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
            asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
            asTDF = self.convertJsonToWeaponTDF(asJSON)
            print('DownloadTDF: \033[32m')
            
            print(json.dumps(no_null_keys, indent=4, sort_keys=True))
            print('\033[0m')

        for feature in featureTDF_ids:
            try:
                queryset = FeatureTDF.objects.get(id=feature)
                serializer = FeatureTDFDataSerializer(queryset)
                # print('\033[31m')
                # print(serializer.data)
                # print('\033[0m')
                no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
                asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
                asTDF = self.convertJsonToFeatureTDF(asJSON)
                print('FeatureTDF: \033[36m')
                print(json.dumps(no_null_keys, indent=4, sort_keys=True))
                print('\033[0m')
                print(asTDF)
            except:
                print('\033[31m')
                print('FEATURE TDF FAILED ! ! !')
                print('\033[0m')

        queryset = UnitFbiData.objects.get(id=unitFBI_id)
        serializer = UnitFbiDataSerializer_v2(queryset)
        # print('\033[31m')
        # print(serializer.data)
        # print('\033[0m')
        
        no_null_keys = dict((k, v) for k, v in serializer.data.items() if v)
        asJSON = json.dumps(no_null_keys, indent=4, sort_keys=True)
        asTDF = self.convertJsonToUnitFBI(asJSON)
        
        print('UnitFBI: \033[30m')
        print(json.dumps(no_null_keys, indent=4, sort_keys=True))
        print('\033[0m')
        print(asTDF)

        print('\033[92m')
        print(log_nonedit)
        print('\033[0m')

    def get(self, request, format=None):
        # Process Files For Individual Assets:
        self.processFiles(233)
        self.processFiles(234)
        self.processFiles(235)
        self.processFiles(236)
        self.processFiles(237)
        self.processFiles(238)

        return Response('')




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

