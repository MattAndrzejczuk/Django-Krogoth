from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from LazarusDatabase.models import LazarusModProject, LazarusModAsset, LazarusModDependency
from chat.models import JawnUser

import json
import os
import re

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


class SuperHPI():
    def __init__(self, usingFbi):
        self.path_to_fbi = usingFbi
        self.allAppendedWeaponTDFs = ""
        self.allAppendedUnitFBIs = ""
        self.allAppendedFeatureTDFs = ""
        self.allAppendedDownloadTDFs = ""

        self.VANILLA_PATH = 'hpi_vanilla/'

        self.logFbiUnitsProcessed = 0

        self._3d_model_dependencies = {}
        self._3d_model_dependencies_cavedog = {}
        self._3d_model_dependencies_error = {}
        self._gaf_dependencies = {}
        self._gaf_dependencies_cavedog = {}
        self._gaf_dependencies_error = {}
        self._wav_dependencies = {}
        self._wav_dependencies_cavedog = {}
        self._wav_dependencies_error = {}

        self.debug_specific_object_mode = False

        subdir_count = len(self.path_to_fbi.split('/'))
        self.base_dir = self.path_to_fbi.replace('units/' + self.path_to_fbi.split('/')[subdir_count - 1], '')

        weaponsPath = self.base_dir + 'weapons/'
        if os.path.exists(weaponsPath):
            weaponfiles = os.listdir(weaponsPath)
            for fileName in weaponfiles:
                self.allAppendedWeaponTDFs += self.cleanTdf(weaponsPath + fileName)


        allFbiFilesPath = self.path_to_fbi.replace(self.path_to_fbi.split('/')[subdir_count - 1], '')
        if os.path.exists(allFbiFilesPath):
            unitFiles = os.listdir(allFbiFilesPath)
            for fileName in unitFiles:
                cleanFBI = self.cleanFbi(allFbiFilesPath + fileName)
                self.allAppendedUnitFBIs += cleanFBI


        featuresPath = self.base_dir + 'features/corpses/'
        if os.path.exists(featuresPath):
            featureFiles = os.listdir(featuresPath)
            for fileName in featureFiles:
                cleanTDF = self.cleanTdf(featuresPath + fileName)
                self.allAppendedFeatureTDFs += cleanTDF


        downloadPath = self.base_dir + 'download/'
        if os.path.exists(downloadPath):
            downloadFiles = os.listdir(downloadPath)
            for fileName in downloadFiles:
                cleanTDF = self.cleanTdf(downloadPath + fileName)
                self.allAppendedDownloadTDFs += cleanTDF


        self.warnings = []
        self.errors = []

    def parseManyUnitFBIs(self, rawTdf):
        # comments need to already have been removed at this point.
        pat = r'(?<=\{).+?(?=\})'
        s = rawTdf
        match = re.findall(pat, s)
        return match

    def parseWeaponTDFsSquareBracks(self, rawTdf):
        pat = r'(?<=\[).+?(?=\])'
        s = rawTdf
        match = re.findall(pat, s)
        new_match = []
        for m in match:
            new_match.append(m.upper())
        # print(new_match)
        return new_match

    def parseWeaponTDFs(self, rawTdf):
        pat = r'(?<=\{).+?(?=\})'
        s = rawTdf
        match = re.findall(pat, s)
        return match

    def parseSingleWeaponTdf(self, rawTdf):
        pat = r'.*\{(.*{.*}.*)}.*'  # See Note at the bottom of the answer
        match = re.search(pat, rawTdf)
        return match

    def parseManyWeaponTDFs(self, rawTdf):
        pat = r'.*\{(.*{.*}.*)}.*'  # See Note at the bottom of the answer
        match = re.findall(pat, rawTdf)
        return match

    def toJson(self, named, arr):
        _json = {}
        _inner = {}
        for kv in arr:
            arr2 = kv.split('=')
            _inner[arr2[0]] = arr2[1]
        _json[named] = _inner
        return _json

    # arr[0] : Properties
    # arr[1] : Damage
    def takeWeaponPropertiesAndDamage(self, tdf):
        arr = tdf.split('[DAMAGE]{')
        return arr

    def remove_comments(self, string):
        pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
        regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
        def _replacer(match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)
        return regex.sub(_replacer, string)

    def cleanTdf(self, tdfPath):
        file_contents = open(tdfPath, 'r', errors='replace')
        rawFbi = file_contents.read()
        fbi_dump = self.remove_comments(rawFbi)
        parse_01 = fbi_dump.replace('\n', '')
        parse_02 = parse_01.replace('\t', '').replace('  ','').replace('; ',';')
        # print('\n')
        # print(parse_02)
        # print('\n')
        parse_03 = parse_02.replace(';ExplosionGaf=', ';explosiongaf=').replace(';Explosiongaf=', ';explosiongaf=')
        parse_04 = parse_03.replace(';Lavaexplosiongaf=', ';lavaexplosiongaf=').replace(';LavaExplosiongaf=', ';lavaexplosiongaf=')
        parse_05 = parse_04.replace(';WaterExplosiongaf=', ';waterexplosiongaf=').replace(';WaterExplosionGaf=', ';waterexplosiongaf=')
        parse_06 = parse_05.replace(';LavaExplosionGaf=', ';lavaexplosiongaf=')
        parse_07 = parse_06.replace(';Soundhit=', ';soundhit=').replace(';SoundHit=', ';soundhit=')
        parse_08 = parse_07.replace(';Soundstart=', ';soundstart=').replace(';SoundStart=', ';soundstart=')
        parse_09 = parse_08.replace(';Soundwater=', ';soundwater=').replace(';SoundWater=', ';soundwater=')
        return parse_09.replace(';Object=', ';object=').replace(';model=', ';Model=')


    def cleanFbi(self, tdfPath):
        file_contents = open(tdfPath, 'r', errors='replace')
        rawFbi = file_contents.read()
        fbi_dump = self.remove_comments(rawFbi)
        parse_01 = fbi_dump.replace('\n', '')
        parse_02 = parse_01.replace('\t', '').replace('  ','').replace('; ',';').replace(';corpse=', ';Corpse=')
        # print('- - - - - - -')
        # print(parse_02)
        parse_03 = parse_02.replace('objectname=', 'Objectname=').replace('ObjectName=', 'Objectname=')
        return parse_03

    def addModelDependency(self, path, name):
        if os.path.isfile(path):
            self._3d_model_dependencies[name] = path
        else:
            if os.path.isfile(self.VANILLA_PATH + 'objects3d/' + path + '.3do'):
                self._3d_model_dependencies_cavedog[name] = path
            else:
                self._3d_model_dependencies_error[name] = path

    def findGafDependencies(self, unitObj):
        if 'explosiongaf' in unitObj:
            file_path = self.base_dir + 'anims/' + unitObj['explosiongaf'] + '.gaf'
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['explosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['explosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['explosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['explosiongaf']] = file_path
        elif 'Explosiongaf' in unitObj:
            file_path = self.base_dir + 'anims/' + unitObj['Explosiongaf'] + '.gaf'
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['Explosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['Explosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['Explosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['Explosiongaf']] = file_path
        if 'waterexplosiongaf' in unitObj:
            file_path = self.base_dir + 'anims/' + unitObj['waterexplosiongaf'] + '.gaf'
            # self._gaf_dependencies[unitObj['waterexplosiongaf']] = file_path
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['waterexplosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['waterexplosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['waterexplosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['waterexplosiongaf']] = file_path
        if 'lavaexplosiongaf' in unitObj:
            file_path = self.base_dir + 'anims/' + unitObj['lavaexplosiongaf'] + '.gaf'
            # self._gaf_dependencies[unitObj['lavaexplosiongaf']] = file_path
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['lavaexplosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['lavaexplosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['lavaexplosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['lavaexplosiongaf']] = file_path

    def findWeaponWavDependencies(self, weap_obj):
        key1 = 'soundhit'
        key2 = 'soundstart'
        key3 = 'soundwater'
        keys = [key1, key2, key3]
        for k in keys:
            if k in weap_obj:
                file_path = self.base_dir + 'sounds/' + weap_obj[k] + '.wav'
                if os.path.isfile(file_path):
                    self._wav_dependencies[weap_obj[k]] = file_path
                else:
                    if os.path.isfile(self.VANILLA_PATH + 'sounds/' + weap_obj[k] + '.wav'):
                        self._wav_dependencies_cavedog[weap_obj[k]] = file_path
                    else:
                        self._wav_dependencies_error[weap_obj[k]] = file_path


    def splitWeaponClusterTDF(self, clusterTDF):
        tdfKeyList = self.parseWeaponTDFsSquareBracks(clusterTDF)
        tdfList = self.parseWeaponTDFs(clusterTDF)
        count = []
        results = {}
        i = 0
        for innerTdf in tdfList:
            if tdfKeyList[i] == 'DAMAGE':
                i += 1
            unique_key = tdfKeyList[i] #.upper()
            pnd = self.takeWeaponPropertiesAndDamage(innerTdf)
            _dmg = pnd[1].split(';')[:-1]
            _weapon = pnd[0].split(';')[:-1]
            asJson = self.toJson(unique_key, _weapon)
            asJson[unique_key]['DAMAGE'] = self.toJson('DAMAGE', _dmg)['DAMAGE']
            count.append(asJson[unique_key])
            results[unique_key] = asJson[unique_key]


            if 'model' in asJson[unique_key]:
                name = asJson[unique_key]['model']
                file_path = self.base_dir + 'objects3d/' + asJson[unique_key]['model'] + '.3do'
                self.addModelDependency(file_path, name)
                # print(asJson[unique_key]['model'])
            elif 'Model' in asJson[unique_key]:
                name = asJson[unique_key]['Model']
                file_path = self.base_dir + 'objects3d/' + asJson[unique_key]['Model'] + '.3do'
                self.addModelDependency(file_path, name)
                # print(asJson[unique_key]['Model'])

            self.findGafDependencies(asJson[unique_key])
            self.findWeaponWavDependencies(asJson[unique_key])

            i += 1
        return results

    def evaluateUnit3DFiles(self, list_items):
        for unit in list_items:
            model_key = 'Objectname'
            file_path = self.base_dir + 'objects3d/' + unit[model_key] + '.3do'

            if os.path.isfile(file_path):
                self._3d_model_dependencies[unit[model_key]] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'objects3d/' + model_key + '.3do'):
                    self._3d_model_dependencies_cavedog[unit[model_key]] = file_path
                else:
                    self._3d_model_dependencies_error[unit[model_key]] = file_path



    def splitUnitClusterFBI(self, clusterFBI):
        # print(clusterFBI.replace('=', '\033[0m\033[91m=\033[0m\033[34m').replace('[UNITINFO]', '\n\n').replace(';','\033[0m;\n\t\033[35m').replace('{','\t{\n\t'))
        tdfList = clusterFBI.split('[UNITINFO]')
        fbiList = []
        if tdfList[0] == '':
            print("FIRST ELEMENT IS BLANK!")
            fbiList = tdfList[1:]
        count = []
        # results = {}
        suc_errors = []
        for innerTdf in fbiList:
            unit = {}
            arr1 = innerTdf.replace('/', ' ').replace(',', ' ').replace('{', '').replace(';}', ';').split(';')[:-1]
            for kv in arr1:
                if '=' in kv:
                    prop = kv.split('=')
                    key = prop[0]
                    value = prop[1]
                    if key.upper() == 'OBJECTNAME':
                        key = 'Objectname'
                    elif key.upper() == 'WEAPON1':
                        value = value.upper()
                    elif key.upper() == 'WEAPON2':
                        value = value.upper()
                    elif key.upper() == 'WEAPON3':
                        value = value.upper()
                    unit[key] = value
                else:
                    self.errors.append('unknown unit FBI ' + str(kv))
            count.append(unit)
        # print('\nFBI processed: ' + str(len(count)) + ' total units,')
        # print('with about: ' + str(len(suc_errors)) + ' errors:')
        self.logFbiUnitsProcessed = len(count)
        # for error in suc_errors:
        #     print(error)
        self.evaluateUnit3DFiles(count)

        return count

    def processDownloadTDF(self, in_obj, _tojson):
        out_obj = in_obj
        for key, val in _tojson.items():
            if 'UNITMENU' in val and 'UNITNAME' in val:
                out_obj[val['UNITMENU'] + ' -> ' + val['UNITNAME']] = val
                out_obj[val['UNITMENU'] + ' -> ' + val['UNITNAME']]['menuentry'] = key
                meta_data = 'entry=' + key + '|menu=' + val['MENU'] + '|button=' + val['BUTTON']
                out_obj[val['UNITMENU'] + ' -> ' + val['UNITNAME']]['meta'] = meta_data
        return out_obj

    def evaluateFeature3DFiles(self, in_obj, _toJson):
        out_obj = in_obj
        for key, val in _toJson.items():
            file_path = ''
            model_key = 'object'
            if model_key in val:
                file_path = self.base_dir + 'objects3d/' + val[model_key] + '.3do'
            else:
                model_key = "Object"
                if 'Object' in val:
                    file_path = self.base_dir + 'objects3d/' + val[model_key] + '.3do'

            if os.path.isfile(file_path):
                self._3d_model_dependencies[val[model_key]] = file_path
            else:
                if model_key in val:
                    if os.path.isfile(self.VANILLA_PATH + 'objects3d/' + val[model_key] + '.3do'):
                        self._3d_model_dependencies_cavedog[val[model_key]] = file_path
                    else:
                        self._3d_model_dependencies_error[val[model_key]] = file_path
            out_obj[key] = val
        return out_obj


    def splitGenericClusterTDF(self, clusterTDF, type):
        bug_fix_1 = clusterTDF.replace('[MENUENTRY0]{}', '')
        corpseValuesJSON = self.parseWeaponTDFs(bug_fix_1)
        corpseKeysJSON = self.parseWeaponTDFsSquareBracks(bug_fix_1)
        returnArr = []
        returnObj = {}
        n = 0
        for _json in corpseValuesJSON:
            _tojson = []
            _tojson = self.toJson(corpseKeysJSON[n], _json.split(';')[:-1])
            if type == 'download':
                returnObj = self.processDownloadTDF(returnObj, _tojson)
            else:
                returnObj = self.evaluateFeature3DFiles(returnObj, _tojson)
            # try:
            #     _tojson = self.toJson(corpseKeysJSON[n], _json.split(';')[:-1])
            #     if type == 'download':
            #         returnObj = self.processDownloadTDF(returnObj, _tojson)
            #     else:
            #         returnObj = self.evaluateFeature3DFiles(returnObj, _tojson)
            # except:
            #     print('Something failed... ' + type)
            #     print(clusterTDF)
                # _tojson = self.toJson(corpseKeysJSON[n], _json.split(';'))
            n += 1
        return returnObj


    def printSpecificUnitAssets(self, ids, allModFbis):
        print(ids)
        mod_fbis = []
        i = 0
        while i < len(ids):
            mod_fbis.append(allModFbis[ids[i]])
            i += 1

        # print(mod_fbis)
        return mod_fbis


    def printAllUnitAssets(self, allModFbis, allWeapTdfs, allModFeatures):
        i = 0
        while i < len(allModFbis):
            # print(json.dumps(allModFbis[i], indent=2))
            fbi_unit_name = ''
            if 'UnitName' in allModFbis[i]:
                fbi_unit_name = allModFbis[i]['UnitName']
            elif 'Unitname' in allModFbis[i]:
                fbi_unit_name = allModFbis[i]['Unitname']
            elif 'unitname' in allModFbis[i]:
                fbi_unit_name = allModFbis[i]['unitname']
            else:
                print('\033[93mTHIS UNIT HAS NO NAME!!!\n')
                print(json.dumps(allModFbis[i], indent=2) + '\033[0m')
                continue
            weap_key_1 = ''
            weap_key_2 = ''
            weap_key_3 = ''
            corpse_key = ''
            Objectname = ''
            print('─────────────────────────────────────────────────────────')
            print(self.base_dir)
            print('\033[35m' + fbi_unit_name + '\033[0m index : ' + str(i))
            logpath = '\033[34m' + self.base_dir + '\033[0m'
            # print(logpath + '\033[31m' + fbi_unit_name + '_gadget' + '\033[0m.gaf')
            if 'Objectname' in allModFbis[i]:
                Objectname = allModFbis[i]['Objectname']
            elif 'objectname' in allModFbis[i]:
                Objectname = allModFbis[i]['objectname']


            possible_pcx_files = os.listdir(self.base_dir + 'unitpics')
            for pcx in possible_pcx_files:
                if fbi_unit_name.lower() in pcx.lower():
                    print(logpath + 'unitpics/\033[31m' + pcx)
                    break

            possible_gaf_files = os.listdir(self.base_dir + 'anims')
            for gaf in possible_gaf_files:
                if fbi_unit_name.lower() in gaf.lower():
                    print(logpath + 'anims/\033[31m' + gaf)
                    break

            possible_cob_files = os.listdir(self.base_dir + 'scripts')
            for cob in possible_cob_files:
                if fbi_unit_name.lower() in cob.lower():
                    print(logpath + 'scripts/\033[31m' + cob)
                    break

            print(logpath + '\033[31mobjects3d/' + Objectname + '\033[0m.3do')
            inner_k1 = 'soundstart'
            inner_k2 = 'soundhit'
            inner_k3 = 'explosiongaf'
            inner_k4 = 'waterexplosiongaf'
            inner_k5 = 'lavaexplosiongaf'
            inner_k7 = 'Model'
            inner_k13 = 'soundwater'
            inner_weap_keys = [inner_k1, inner_k2, inner_k13, inner_k3, inner_k4, inner_k5, inner_k7]

            inner_c1 = 'object'
            inner_c2 = 'Object'
            inner_corpse_keys = [inner_c1, inner_c2]



            print('  ╔═══════════════════════════════════════════════════════╗')
            if 'Weapon1' in allModFbis[i] or 'weapon1' in allModFbis[i]:
                main_key = 'Weapon1'
                if 'Weapon1' not in allModFbis[i]:
                    main_key = 'weapon1'
                weap_key_1 = allModFbis[i][main_key]
                log = '  ║\033[33mWeapon1 : \033[0m \033[32m' + weap_key_1 + '\033[0m'
                print(log)
                if weap_key_1 in CAVEDOG_WEAPONS:
                    print('  ║ \033[36mCavedog Asset\033[0m')

                for k in inner_weap_keys:
                    if weap_key_1 in allWeapTdfs:
                        # print('\033[036' + json.dumps(allWeapTdfs[weap_key_1], indent=2) + '\033[0m')
                        if k in allWeapTdfs[weap_key_1]:
                            ext = '.gaf'
                            if 'ound' in k:
                                ext = '.wav'
                            elif 'odel' in k:
                                ext = '.3do'
                            log = '  ║\033[37m' + k + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                  allWeapTdfs[weap_key_1][k] + '\033[0m' + ext
                            print(log)
                # print(json.dumps(allWeapTdfs[weap_key_1], indent=2))
                print('  ╠═══════════════════════════════════════════════════════╣')
            if 'Weapon2' in allModFbis[i] or 'weapon2' in allModFbis[i]:
                main_key = 'Weapon2'
                if 'Weapon2' not in allModFbis[i]:
                    main_key = 'weapon2'
                weap_key_2 = allModFbis[i][main_key]

                log = '  ║\033[33mWeapon2 :\033[0m \033[32m' + weap_key_2 + '\033[0m'
                print(log)
                if weap_key_2 in CAVEDOG_WEAPONS:
                    print('  ║ \033[36mCavedog Asset\033[0m')

                for k in inner_weap_keys:
                    if weap_key_2 in allWeapTdfs:
                        # print('\033[036' + json.dumps(allWeapTdfs[weap_key_2], indent=2) + '\033[0m')
                        if k in allWeapTdfs[weap_key_2]:
                            ext = '.gaf'
                            if 'ound' in k:
                                ext = '.wav'
                            elif 'odel' in k:
                                ext = '.3do'
                            log = '  ║\033[37m' + k + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                  allWeapTdfs[weap_key_2][k] + '\033[0m' + ext
                            print(log)
                # print(json.dumps(allWeapTdfs[weap_key_2], indent=2))
                print('  ╠═══════════════════════════════════════════════════════╣')
            if 'Weapon3' in allModFbis[i] or 'weapon3' in allModFbis[i]:
                main_key = 'Weapon3'
                if 'Weapon3' not in allModFbis[i]:
                    main_key = 'weapon3'
                weap_key_3 = allModFbis[i][main_key]
                log = '  ║\033[33mWeapon3 : \033[0m \033[32m' + weap_key_3 + '\033[0m'
                print(log)
                if weap_key_3 in CAVEDOG_WEAPONS:
                    print('  ║ \033[36mCavedog Asset\033[0m')

                for k in inner_weap_keys:
                    if weap_key_3 in allWeapTdfs:
                        # print('\033[036' + json.dumps(allWeapTdfs[weap_key_3], indent=2) + '\033[0m')
                        if k in allWeapTdfs[weap_key_3]:
                            ext = '.gaf'
                            if 'ound' in k:
                                ext = '.wav'
                            elif 'odel' in k:
                                ext = '.3do'
                            log = '  ║\033[37m' + k + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                  allWeapTdfs[weap_key_3][k] + '\033[0m' + ext
                            print(log)

                print('  ╠═══════════════════════════════════════════════════════╣')

            if "Corpse" in allModFbis[i] or "corpse" in allModFbis[i]:
                title = 'Corpse'
                if title not in allModFbis[i]:
                    title = 'corpse'
                corpse_key = allModFbis[i][title]

                log = '  ║\033[33mCorpse : \033[0m \033[32m' + allModFbis[i][title] + '\033[0m'
                print(log)

                if corpse_key in CAVEDOG_FEATURES:
                    print('  ║ \033[36mCavedog Feature Asset\033[0m')

                if corpse_key not in allModFeatures:
                    corpse_key = corpse_key.lower()
                    if corpse_key not in allModFeatures:
                        corpse_key = corpse_key.upper()

                if corpse_key in allModFeatures:
                    for k in inner_corpse_keys:
                        if k in allModFeatures[corpse_key]:
                            ext = '.3do'
                            log = '  ║\033[37m' + k + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                allModFeatures[corpse_key][k] + '\033[0m' + ext
                            print(log)

                print('  ╚═══════════════════════════════════════════════════════╝')

            if self.debug_specific_object_mode == True:
                print('\033[94m')
                try:
                    print(json.dumps(allModFeatures[corpse_key], indent=2))
                except:
                    pass


                print('\033[95m')
                try:
                    print('\033[91m' + weap_key_1 + '\033[0m')
                    print(json.dumps(allWeapTdfs[weap_key_1], indent=2))
                except:
                    pass
                try:
                    print('\033[91m' + weap_key_2 + '\033[0m')
                    print(json.dumps(allWeapTdfs[weap_key_2], indent=2))
                except:
                    pass
                try:
                    print('\033[91m' + weap_key_3 + '\033[0m')
                    print(json.dumps(allWeapTdfs[weap_key_3], indent=2))
                except:
                    pass
                    print('\033[0m')




                # print('╚══╝ ╔══╗ ║ ║ ╠ ╣')
                # print(json.dumps(allWeapTdfs[weap_key_3], indent=2))

            print()


            i += 1



class PhaseOneReclaim(APIView):
    def remove_comments(self, string):
        pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
        regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
        def _replacer(match):
            if match.group(2) is not None:
                return ""  
            else:  
                return match.group(1)  
        return regex.sub(_replacer, string)

    def cleanTdf(self, tdfPath):
        file_contents = open(tdfPath, 'r', errors='replace')
        rawFbi = file_contents.read()
        fbi_dump = self.remove_comments(rawFbi)
        parse_01 = fbi_dump.replace('\n', '')
        parse_02 = parse_01.replace('\t', '').replace('  ','').replace('; ',';')
        return parse_02

    def parseWeaponTDFsSquareBracks(self, rawTdf):
        pat = r'(?<=\[).+?(?=\])'
        s = rawTdf
        match = re.findall(pat, s)
        return match

    def parseWeaponTDFs(self, rawTdf):
        pat = r'(?<=\{).+?(?=\})'
        s = rawTdf
        match = re.findall(pat, s)
        return match

    def processTdfBatch(self, rawTDFs):
        tdfKeyList = self.parseWeaponTDFsSquareBracks(rawTDFs)
        tdfList = self.parseWeaponTDFs(rawTDFs)
        i = 0
        for innerTdf in tdfList:
            if tdfKeyList[i] == 'DAMAGE':
                i += 1
            # print(tdfKeyList[i])
            # print(innerTdf)
            # print()
            i += 1

    # def convertToJson(self, giantBatchOfData):


    def get(self, request, format=None):
        parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
        path_to_fbi = '/usr/src/persistent/' + parse_path1 + '.fbi'
        allFbiFilesPath = path_to_fbi.replace(path_to_fbi.split('/')[8], '')

        print('\033[92m')
        print('Starting...')
        print('\033[0m\n')

        dir_extract_request = SuperHPI(allFbiFilesPath)
        """
        allFBIs = dir_extract_request.splitUnitClusterFBI(dir_extract_request.allAppendedUnitFBIs)

        # abel_dict = json.loads(parse_09)
        for fbiUnit in allFBIs:
            if 'Side' in fbiUnit and 'Name' in fbiUnit:
                # print(fbiUnit)
                _json = JSONRenderer().render(fbiUnit)
                stream = BytesIO(_json)
                data = JSONParser().parse(stream)
                fbi_serialized_from_file = UnitFbiDataSerializer_v2(data=data)
                if fbi_serialized_from_file.is_valid() == False:
                    # print('WARNING: ' + fbiUnit['Side'] + ' ' + fbiUnit['Name'] + ' is invalid.')
                    dir_extract_request.warnings.append(fbi_serialized_from_file.errors)
                    dir_extract_request.warnings.append('unable to parse: ' + fbiUnit['Side'] + ' ' + fbiUnit['Name'])
                else:
                    # fbi_serialized_from_file.save()
                    print('SKIPPING: Unit Saved as UnitFbiData_v2')

                # else:
                #     print(fbiUnit['Side'] + ' ' + fbiUnit['Name'] + ' serialized successfully.')


        info = {}
        allFBIs[0] = {}
        allFBIs[0][str(len(dir_extract_request.warnings)) + " warnings: "] = dir_extract_request.warnings
        allFBIs[0][str(len(dir_extract_request.errors)) + " errors: "] = dir_extract_request.errors
        allFBIs[0]["Total FBI units processed successfully: "] = dir_extract_request.logFbiUnitsProcessed
        """

        print('\033[92m')
        print('Starting...')
        print('\033[0m\n')

        allTDFs = dir_extract_request.splitWeaponClusterTDF(dir_extract_request.allAppendedWeaponTDFs)
        print('\033[95m')
        print(json.dumps(allTDFs, indent=2))
        print('\033[0m')

        allFBIs = dir_extract_request.splitUnitClusterFBI(dir_extract_request.allAppendedUnitFBIs)
        print('\033[92m')
        print(json.dumps(allFBIs, indent=2))
        print('\033[0m\n\nFINISHED!')

        allFeatures = dir_extract_request.splitGenericClusterTDF(dir_extract_request.allAppendedFeatureTDFs)
        print('\033[94m')
        print(json.dumps(allFeatures, indent=2))
        print('\033[0m\n\nFINISHED!')

        allDownloads = dir_extract_request.splitGenericClusterTDF(dir_extract_request.allAppendedDownloadTDFs)
        print('\033[91m')
        print(json.dumps(allDownloads, indent=2))
        print('\033[0m\n\nFINISHED!')

        return Response(allFBIs)

""" 
        parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
        path_to_fbi = '/usr/src/persistent/' + parse_path1 + '.fbi'
        file_contents = open(path_to_fbi, 'r', errors='replace')
        rawFbi = file_contents.read()
        fbi_dump = self.remove_comments(rawFbi)
        print('- - - - - - - - -')
        parse_01 = fbi_dump.replace('\n', '')
        parse_02 = parse_01.replace('\t', '').replace('  ','').replace('; ',';')
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
        new_data = {}
        for (key, value) in data.items():
            better_key = key.replace(' ', '')
            new_data[better_key] = value
        fbi_serialized_from_file = UnitFbiDataSerializer_v2(data=new_data)
        print("FBI was serialized successfully: ")
        print(fbi_serialized_from_file.is_valid())
        print(json.dumps(new_data, indent=4, sort_keys=True))
        print('Properties expected: ' + str(fbi_dump.count('=')))
        print('Total properties: ' + str(json.dumps(new_data, indent=4, sort_keys=True).count(':')))
        
        weaponsPath = path_to_fbi.replace('units/' + path_to_fbi.split('/')[8],'') + 'weapons/'
        weaponfiles = os.listdir(weaponsPath)
        allAppendedWeaponTDFs = ""
        for fileName in weaponfiles:
            allAppendedWeaponTDFs += self.cleanTdf(weaponsPath + fileName)

        allFbiFilesPath = path_to_fbi.replace(path_to_fbi.split('/')[8], '')
        unitFiles = os.listdir(allFbiFilesPath)
        allAppendedUnitFBIs = ""
        for fileName in unitFiles:
            allAppendedUnitFBIs += self.cleanTdf(allFbiFilesPath + fileName)

        print(allAppendedWeaponTDFs)
        print('\n\n\n')
        print('Total TDF files harvested: ' + str(len(weaponfiles)))
        print('Total FBI files harvested: ' + str(len(unitFiles)) + '\n')
        return Response(new_data)
"""


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
                print('FeatureTDF: \033[36m')
                print(json.dumps(no_null_keys, indent=4, sort_keys=True))
                print('\033[0m')
                print(asTDF)
                new_feature_tdf_document['name'] = unit_fbi_queryset.Corpse
                new_feature_tdf_document['text_body'] += asTDF + '\n'
            except Exception as inst:
                print('\033[31m')
                print('FEATURE TDF FAILED ! ! !\n')
                print(feature)
                print('')
                print(inst)
                print('\033[0m\n')

        
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
            print(bcolors.orange)
            print('SAVING FBI...')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['units'])
            print(bcolors.ENDC)
            fileoutput_fbi = open(ufbiOut, 'w', errors='replace')
            fileoutput_fbi.write(asset['units']['text_body'])
            fileoutput_fbi.close()
            print(bcolors.green)
            print('FBI SAVED SUCCESSFULLY')
            print(ufbiOut)
            print(bcolors.ENDC)

            # generate weapon tdf:
            wtdfOut = pathToModPublish + '/weapons/' + asset['weapons']['name'] + '_weapons.tdf'
            print(bcolors.orange)
            print('SAVING WEAPON TDF...')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['weapons'])
            print(bcolors.ENDC)
            fileoutput_tdf1 = open(wtdfOut, 'w', errors='replace')
            fileoutput_tdf1.write(asset['weapons']['text_body'])
            fileoutput_tdf1.close()
            print(bcolors.green)
            print('WEAPON TDF SAVED SUCCESSFULLY')
            print(wtdfOut)
            print(bcolors.ENDC)
            # generate download tdf:
            dtdfOut = pathToModPublish + '/download/' + asset['downloads']['name'] + '.tdf'
            print(bcolors.orange)
            print('SAVING DOWNLOAD TDF...')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['downloads'])
            print(bcolors.ENDC)
            fileoutput_tdf2 = open(dtdfOut, 'w', errors='replace')
            fileoutput_tdf2.write(asset['downloads']['text_body'])
            fileoutput_tdf2.close()
            print(bcolors.green)
            print('DOWNLOAD TDF SAVED SUCCESSFULLY')
            print(dtdfOut)
            print(bcolors.ENDC)
            # generate feature tdf:
            ftdfOut = pathToModPublish + '/features/corpses/' + asset['features']['name'] + '.tdf'
            print(bcolors.orange)
            print('SAVING FEATURE TDF...')
            print(bcolors.ENDC)
            print(bcolors.OKBLUE)
            print(asset['features'])
            print(bcolors.ENDC)
            fileoutput_tdf3 = open(ftdfOut, 'w', errors='replace')
            fileoutput_tdf3.write(asset['features']['text_body'])
            fileoutput_tdf3.close()
            print(bcolors.green)
            print('FEATURE TDF SAVED SUCCESSFULLY')
            print(ftdfOut)
            print(bcolors.ENDC)



        ## need to copy non-editable stuff first:
        # cp model.3do /usr/src/persistent/media/ta_data/ArmPrime_1.0_Arm_GorGant/objects3d/

            print('Copying uneditable dependencies... ')
            print(asset)
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
        os.system('zip -r ' + pathToModPublish + '/lazarus_mod.zip ' + pathToModPublish)
        print('zip -r ' + pathToModPublish + '/lazarus_mod.zip ' + pathToModPublish)
        return pathToModPublish.replace('/usr/src/persistent', '') + '/lazarus_mod.zip'

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
            if not os.path.exists(mod_build_path):
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
        else:
            if not os.path.exists(mod_build_path):
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
                print(artists_output_path_for_all_mods + " for artist already exists, \nTotal Builds For:")
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
