



# str = 'Hello Python 3.'


# print(str)
# print(str.index('Py'))
# print(str.index('3'))
# print(str[6:14])










import os
import re
import json
import shutil


# codeTDF = "[CORWOLV_GUN]{ID=252;name=Light Plasma Artillery;rendertype=4;ballistic=1;turret=1;range=530;reloadtime=2.65;weaponvelocity=305;areaofeffect=43;soundstart=cannhvy3;soundhit=xplomed2;accuracy=1850;explosiongaf=fx;explosionart=explode3;waterexplosiongaf=fx;waterexplosionart=h2o;lavaexplosiongaf=fx;lavaexplosionart=lavasplash;startsmoke=1;[DAMAGE]{default=85;}}"

def getfile_insensitive(path):
    directory, filename = os.path.split(path)
    directory, filename = (directory or '.'), filename.lower()
    for f in os.listdir(directory):
        newpath = os.path.join(directory, f)
        if os.path.isfile(newpath) and f.lower() == filename:
            return newpath

def isfile_insensitive(path):
    return getfile_insensitive(path) is not None








from cavedog import CAVEDOG_WEAPONS, CAVEDOG_FEATURES, CAVEDOG_SFX, CAVEDOG_3DO, CAVEDOG_GAF, CAVEDOG_UNITS
from json_to_tdf import cavedog_data_generator

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
        self.strict_mode = True
        self.output_dir = '!!!'

        self.cavedog_data_base = cavedog_data_generator(self.strict_mode)
        self.all_readonly_assets = {}
        self.units_with_errors = []

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
        parse_06 = parse_05.replace(';LavaExplosionGaf=', ';lavaexplosiongaf=').replace(';FeatureDead=', ';Featuredead=').replace(';featuredead=', ';Featuredead=')
        parse_07 = parse_06.replace(';Soundhit=', ';soundhit=').replace(';SoundHit=', ';soundhit=')
        parse_08 = parse_07.replace(';Soundstart=', ';soundstart=').replace(';SoundStart=', ';soundstart=')
        parse_09 = parse_08.replace(';Soundwater=', ';soundwater=').replace(';SoundWater=', ';soundwater=')
        return parse_09.replace(';object=', ';Object=').replace(';model=', ';Model=')


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


    def printAllUnitAssets(self, allModFbis, allWeapTdfs, allModFeatures, allDownloads):

        allUsableUnitNames = []
        allUnitsWithErrors = []
        allAssets = {}
        cavedog_data = cavedog_data_generator(self.strict_mode)

        i = 0
        while i < len(allModFbis):
            # print(json.dumps(allModFbis[i], indent=2))
            fbi_unit_name = ''
            is_valid = True

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


            cavedog_data.convertJsonToUnitFBI(allModFbis[i], fbi_unit_name)

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
                    allAssets[pcx] = {}
                    allAssets[pcx]['path'] = self.base_dir + 'unitpics/'
                    allAssets[pcx]['unitname'] = fbi_unit_name
                    break

            possible_gaf_files = os.listdir(self.base_dir + 'anims')
            for gaf in possible_gaf_files:
                if fbi_unit_name.lower() in gaf.lower():
                    print(logpath + 'anims/\033[31m' + gaf)
                    allAssets[gaf] = {}
                    allAssets[gaf]['path'] = self.base_dir + 'anims/'
                    allAssets[gaf]['unitname'] = fbi_unit_name
                    break

            possible_cob_files = os.listdir(self.base_dir + 'scripts')
            for cob in possible_cob_files:
                if fbi_unit_name.lower() in cob.lower():
                    print(logpath + 'scripts/\033[31m' + cob)
                    allAssets[cob] = {}
                    allAssets[cob]['path'] = self.base_dir + 'scripts/'
                    allAssets[cob]['unitname'] = fbi_unit_name
                    break

            print(logpath + '\033[31mobjects3d/' + Objectname + '\033[0m.3do')
            allAssets[Objectname + '.3do'] = {}
            allAssets[Objectname + '.3do']['unitname'] = fbi_unit_name
            allAssets[Objectname + '.3do']['path'] = self.base_dir + 'objects3d/'

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
            inner_corpse_keys = [inner_c1, inner_c2, 'Featuredead']


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
                elif weap_key_1 in allWeapTdfs:
                    cavedog_data.convertJsonToWeaponTDF(allWeapTdfs[weap_key_1], weap_key_1)
                for k in inner_weap_keys:
                    if weap_key_1 in allWeapTdfs:

                        # print('\033[036' + json.dumps(allWeapTdfs[weap_key_1], indent=2) + '\033[0m')
                        if k in allWeapTdfs[weap_key_1]:
                            ext = '.gaf'
                            if 'ound' in k:
                                ext = '.wav'
                                allAssets[allWeapTdfs[weap_key_1][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_1][k] + ext]['path'] = self.base_dir + 'sounds/'
                                allAssets[allWeapTdfs[weap_key_1][k] + ext]['unitname'] = fbi_unit_name
                                # TODO: check  if cavedog asset, is_valid becomes false somewhere around here.
                                # fpath = self.base_dir + 'sounds/' + allAssets[allWeapTdfs[weap_key_1][k] + ext]
                                # fpath += allWeapTdfs[weap_key_1][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_1][k] in CAVEDOG_SFX:
                                #     pass
                                #     print('CAVEDOG ASSET')
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
                            elif 'odel' in k:
                                ext = '.3do'
                                allAssets[allWeapTdfs[weap_key_1][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_1][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_1][k] + ext]['path'] = self.base_dir + 'objects3d/'

                            elif 'xplosiongaf' in k:
                                allAssets[allWeapTdfs[weap_key_1][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_1][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_1][k] + ext]['path'] = self.base_dir + 'anims/'
                                # TODO: check  if cavedog asset, is_valid becomes false somewhere around here.
                                # fpath = self.base_dir + 'objects3d/' + allAssets[allWeapTdfs[weap_key_1][k] + ext]
                                # fpath += allWeapTdfs[weap_key_1][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_1][k] in CAVEDOG_3DO:
                                #     pass
                                #     print('CAVEDOG ASSET')
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
                            # else:
                            #     allAssets[allWeapTdfs[weap_key_1][k] + ext] = self.base_dir + 'anims/'
                                # fpath = self.base_dir + 'anims/' + allAssets[allWeapTdfs[weap_key_1][k] + ext]
                                # fpath += allWeapTdfs[weap_key_1][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_1][k] in CAVEDOG_GAF:
                                #     pass
                                #     print('CAVEDOG ASSET')
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
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
                elif weap_key_2 in CAVEDOG_WEAPONS:
                    cavedog_data.convertJsonToWeaponTDF(allWeapTdfs[weap_key_2], weap_key_2)
                for k in inner_weap_keys:
                    if weap_key_2 in allWeapTdfs:

                        # print('\033[036' + json.dumps(allWeapTdfs[weap_key_2], indent=2) + '\033[0m')
                        if k in allWeapTdfs[weap_key_2]:
                            ext = '.gaf'
                            if 'ound' in k:
                                ext = '.wav'
                                allAssets[allWeapTdfs[weap_key_2][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_2][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_2][k] + ext]['path'] = self.base_dir + 'sounds/'
                                # TODO: check  if cavedog asset, is_valid becomes false somewhere around here.
                                # fpath = self.base_dir + 'sounds/' + allAssets[allWeapTdfs[weap_key_2][k] + ext]
                                # fpath += allWeapTdfs[weap_key_2][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_2][k] in CAVEDOG_SFX:
                                #     pass
                                #     print('CAVEDOG ASSET')
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
                            elif 'odel' in k:
                                ext = '.3do'
                                allAssets[allWeapTdfs[weap_key_2][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_2][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_2][k] + ext]['path'] = self.base_dir + 'objects3d/'

                            elif 'xplosiongaf' in k:
                                allAssets[allWeapTdfs[weap_key_2][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_2][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_2][k] + ext]['path'] = self.base_dir + 'anims/'
                                # TODO: check  if cavedog asset, is_valid becomes false somewhere around here.
                                # fpath = self.base_dir + 'objects3d/' + allAssets[allWeapTdfs[weap_key_2][k] + ext]
                                # fpath += allWeapTdfs[weap_key_2][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_2][k] in CAVEDOG_3DO:
                                #     pass
                                #     print('CAVEDOG ASSET')
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
                            # else:
                            #     allAssets[allWeapTdfs[weap_key_2][k] + ext] = self.base_dir + 'anims/'
                            #     fpath = self.base_dir + 'anims/' + allAssets[allWeapTdfs[weap_key_2][k] + ext]
                            #     fpath += allWeapTdfs[weap_key_2][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_2][k] in CAVEDOG_GAF:
                                #     pass
                                #     print('CAVEDOG ASSET')
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
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
                elif weap_key_3 in CAVEDOG_WEAPONS:
                    cavedog_data.convertJsonToWeaponTDF(allWeapTdfs[weap_key_3], weap_key_3)
                for k in inner_weap_keys:
                    if weap_key_3 in allWeapTdfs:
                        # print('\033[036' + json.dumps(allWeapTdfs[weap_key_3], indent=2) + '\033[0m')
                        if k in allWeapTdfs[weap_key_3]:
                            ext = '.gaf'
                            if 'ound' in k:
                                ext = '.wav'
                                allAssets[allWeapTdfs[weap_key_3][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_3][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_3][k] + ext]['path'] = self.base_dir + 'sounds/'
                                # TODO: check  if cavedog asset, is_valid becomes false somewhere around here.
                                # fpath = self.base_dir + 'sounds/' + allAssets[allWeapTdfs[weap_key_3][k] + ext]
                                # fpath += allWeapTdfs[weap_key_3][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_3][k] in CAVEDOG_SFX:
                                #     pass
                                #     print('CAVEDOG ASSET')
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
                            elif 'odel' in k:
                                ext = '.3do'
                                allAssets[allWeapTdfs[weap_key_3][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_3][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_3][k] + ext]['path'] = self.base_dir + 'objects3d/'

                            elif 'xplosiongaf' in k:
                                allAssets[allWeapTdfs[weap_key_3][k] + ext] = {}
                                allAssets[allWeapTdfs[weap_key_3][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allWeapTdfs[weap_key_3][k] + ext]['path'] = self.base_dir + 'anims/'
                                # TODO: check  if cavedog asset, is_valid becomes false somewhere around here.
                                # fpath = self.base_dir + 'objects3d/' + allAssets[allWeapTdfs[weap_key_3][k] + ext]
                                # fpath += allWeapTdfs[weap_key_3][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_3][k] in CAVEDOG_3DO:
                                #     print('CAVEDOG ASSET')
                                #     pass
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
                                    # self.units_with_errors.append(fbi_unit_name)
                            # else:
                            #     allAssets[allWeapTdfs[weap_key_3][k] + ext] = self.base_dir + 'anims/'
                                # fpath = self.base_dir + 'anims/' + allAssets[allWeapTdfs[weap_key_3][k] + ext]
                                # fpath += allWeapTdfs[weap_key_3][k]
                                # print(fpath)
                                # if allWeapTdfs[weap_key_3][k] in CAVEDOG_GAF:
                                #     print('CAVEDOG ASSET')
                                #     pass
                                # elif os.path.isfile(fpath + ext):
                                #     pass
                                # else:
                                #     print(' 💥 ')
                                #     self.units_with_errors.append(fbi_unit_name)
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
                    cavedog_data.convertJsonToFeatureTDF(allModFeatures[corpse_key], corpse_key)
                    if 'Featuredead' in allModFeatures[corpse_key]:
                        ext = '.3do'
                        heap_key = allModFeatures[corpse_key]['Featuredead']
                        cavedog_data.convertJsonToFeatureTDF(allModFeatures[heap_key.upper()], heap_key.upper())
                        if 'Featuredead' in allModFeatures[heap_key.upper()]:
                            inner_heap_key = allModFeatures[heap_key.upper()]['Featuredead']
                            cavedog_data.convertJsonToFeatureTDF(allModFeatures[inner_heap_key.upper()], inner_heap_key.upper())
                            # print('HEAP WITH A HEAP ALERT!!!')
                            # print(inner_heap_key)
                            try:
                                # print('HOLY SHIT!')
                                # print(allModFeatures[inner_heap_key.upper()]['Object'])
                                if allModFeatures[inner_heap_key.upper()]['Object'] not in CAVEDOG_3DO:
                                    ext = '.3do'
                                    allAssets[allModFeatures[inner_heap_key.upper()]['Object'] + ext] = {}
                                    allAssets[allModFeatures[inner_heap_key.upper()]['Object'] + ext]['unitname'] = fbi_unit_name
                                    allAssets[allModFeatures[inner_heap_key.upper()]['Object'] + ext]['path'] = self.base_dir + 'objects3d/'
                                log = '  ║\033[37m' + allModFeatures[inner_heap_key.upper()][
                                    'Object'] + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                      allModFeatures[inner_heap_key.upper()]['Object'] + '\033[0m' + ext
                                print(log)
                                if 'Featuredead' in allModFeatures[inner_heap_key.upper()]:
                                    # print('AHHHHH')
                                    # print(allModFeatures[inner_heap_key.upper()]['Featuredead'])
                                    deep_key = allModFeatures[inner_heap_key.upper()]['Featuredead']
                                    if allModFeatures[deep_key.upper()]['Object'] not in CAVEDOG_3DO:
                                        ext = '.3do'
                                        allAssets[allModFeatures[deep_key.upper()]['Object'] + ext] = {}
                                        allAssets[allModFeatures[deep_key.upper()]['Object'] + ext][
                                            'unitname'] = fbi_unit_name
                                        allAssets[allModFeatures[deep_key.upper()]['Object'] + ext][
                                            'path'] = self.base_dir + 'objects3d/'
                                    log = '  ║\033[37m' + allModFeatures[deep_key.upper()][
                                        'Object'] + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                          allModFeatures[deep_key.upper()]['Object'] + '\033[0m' + ext
                                    print(log)
                            except:
                                pass
                    for k in inner_corpse_keys:
                        if k in allModFeatures[corpse_key]:
                            if k == 'Featuredead':

                                # heap_key = allModFeatures[corpse_key]['Featuredead']

                                # cavedog_data.convertJsonToFeatureTDF(allModFeatures[heap_key.upper()], heap_key.upper())
                                if allModFeatures[heap_key.upper()]['Object'] not in CAVEDOG_3DO:
                                    ext = '.3do'
                                    allAssets[allModFeatures[heap_key.upper()]['Object'] + ext] = {}
                                    allAssets[allModFeatures[heap_key.upper()]['Object'] + ext]['unitname'] = fbi_unit_name
                                    allAssets[allModFeatures[heap_key.upper()]['Object'] + ext]['path'] = self.base_dir + 'objects3d/'
                                    log = '  ║\033[37m' + allModFeatures[heap_key.upper()]['Object'] + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                          allModFeatures[heap_key.upper()]['Object'] + '\033[0m' + ext
                                    print(log)
                                else:
                                    log = '  ║\033[33m' + 'Featuredead' + '\033[0m \033[94m -> \033[0m\033[31m ' + str(
                                        allModFeatures[heap_key.upper()]['Object']) + ' \033[0m'
                                    ext = '.3do'
                                    log = '  ║\033[37m' + allModFeatures[heap_key.upper()][
                                        'Object'] + '\033[0m \033[94m -> \033[0m\033[31m' + \
                                          allModFeatures[heap_key.upper()]['Object'] + '\033[0m' + ext
                                    print(log)

                            else:
                                ext = '.3do'
                                allAssets[allModFeatures[corpse_key][k] + ext] = {}
                                allAssets[allModFeatures[corpse_key][k] + ext]['unitname'] = fbi_unit_name
                                allAssets[allModFeatures[corpse_key][k] + ext]['path'] = self.base_dir + 'objects3d/'
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
                    print('💣 \033[91m' + weap_key_1 + '\033[0m')
                    print(json.dumps(allWeapTdfs[weap_key_1], indent=2))
                except:
                    pass
                try:
                    print('💣 \033[91m' + weap_key_2 + '\033[0m')
                    print(json.dumps(allWeapTdfs[weap_key_2], indent=2))
                except:
                    pass
                try:
                    print('💣 \033[91m' + weap_key_3 + '\033[0m')
                    print(json.dumps(allWeapTdfs[weap_key_3], indent=2))
                except:
                    pass
                    print('\033[0m')


            if self.strict_mode == False or is_valid == True:
                allUsableUnitNames.append(fbi_unit_name)
                self.cavedog_data_base = cavedog_data
                self.all_readonly_assets = allAssets
            elif is_valid == False:
                allUnitsWithErrors.append(fbi_unit_name)



                # print('╚══╝ ╔══╗ ║ ║ ╠ ╣')
                # print(json.dumps(allWeapTdfs[weap_key_3], indent=2))

            print()


            i += 1

        for k,v in allAssets.items():
            if os.path.isfile(v['path'] + k):
                print('💎 \033[92m' + k[0:13] + '\t' + v['path'] + k + '\033[0m \033[94m ' + v['unitname'] + ' \033[0m')
            else:
                if k[:-4] in CAVEDOG_SFX or k[:-4] in CAVEDOG_3DO or k[:-4] in CAVEDOG_GAF:
                    print('♻️ \033[94m' + k[0:13] + '\tOfficial Cavedog Asset\033[0m')
                else:
                    allUnitsWithErrors.append(v['unitname'])
                    is_valid = False
                    # list_dir = os.listdir(v['path'])
                    # print(k + ' not found, doing hard search: 🔍 ' + v['path'])
                    # print(list_dir)
                    #
                    print('☠️ \033[31m' + k[0:13] + '\tFATAL ERROR - DEPENDENCY NOT FOUND ! \033[0m')

        for dlk, dlv in allDownloads.items():
            valid_dl = False
            u1 = dlk.split(' -> ')[0]
            u2 = dlk.split(' -> ')[1]
            for uname in allUsableUnitNames:
                if u1 == uname or u2 == uname:
                    valid_dl = True
            if valid_dl == True:
                cavedog_data.convertJsonToDownloadTDF(dlv, u1, u2)

        for cu in allUnitsWithErrors:
            if cu not in CAVEDOG_UNITS:
                self.units_with_errors.append(cu)



        # for k,v in CAVEDOG_UNITS.items():
        #     cavedog = False
        #     for cu in allUnitsWithErrors:
        #         if cu == k:
        #             cavedog = True
        #     if cavedog == False:
        #         self.units_with_errors.append(cu)
        print('The following units have dependency errors\n')
        print(self.units_with_errors)





    def saveTdfAndFbi(self):
        print('\n\n\n📁 features - - - - - - - - - - - - - - - - - - - \n')
        for k, v in self.cavedog_data_base.features.items():
            print('📄 \033[91m' + k + '\033[0m')
            path_file = self.output_dir + '/features/corpses/' + k + '.tdf'
            f = open(path_file, 'w')
            f.write(v)
            f.close()
            print(v)
        print('\n\n\n📁 units - - - - - - - - - - - - - - - - - - - \n')
        for k, v in self.cavedog_data_base.units.items():
            print('📄 \033[91m' + k + '\033[0m')
            path_file = self.output_dir + '/units/' + k + '.fbi'
            f = open(path_file, 'w')
            f.write(v)
            f.close()
            print(v)
        print('\n\n\n📁 weapons - - - - - - - - - - - - - - - - - - - \n')
        for k, v in self.cavedog_data_base.weapons.items():
            print('📄 \033[91m' + k + '\033[0m')
            path_file = self.output_dir + '/weapons/' + k + '.tdf'
            f = open(path_file, 'w')
            f.write(v)
            f.close()
            print(v)
        print('\n\n\n📁 download - - - - - - - - - - - - - - - - - - - \n')
        for k, v in self.cavedog_data_base.download.items():
            print('📄 \033[91m' + k + '\033[0m')
            full_file = ''
            for item in v:
                full_file += item
            path_file = self.output_dir + '/download/' + k + '.tdf'
            f = open(path_file, 'w')
            f.write(full_file)
            print(full_file)
            f.close()


    def copyReadOnlyAssets(self):
        wspc = '                             '
        for k,v in self.all_readonly_assets.items():
            if os.path.isfile(v['path'] + k):
                # print('💎 \033[92m' + (k + wspc)[0:23] + '\t' + v['path'] + '\033[0m')
                if k[-3:].upper() == 'GAF':
                    print('from: ' + v['path'] + k)
                    print('to:   ' + self.output_dir + '/anims/' + k)
                    shutil.copyfile(v['path'] + k, self.output_dir + '/anims/' + k)
                elif k[-3:].upper() == 'WAV':
                    print('from: ' + v['path'] + k)
                    print('to:   ' + self.output_dir + '/sounds/' + k)
                    shutil.copyfile(v['path'] + k, self.output_dir + '/sounds/' + k)
                elif k[-3:].upper() == '3DO':
                    print('from: ' + v['path'] + k)
                    print('to:   ' + self.output_dir + '/objects3d/' + k)
                    shutil.copyfile(v['path'] + k, self.output_dir + '/objects3d/' + k)
                elif k[-3:].upper() == 'PCX':
                    print('from: ' + v['path'] + k)
                    print('to:   ' + self.output_dir + '/unitpics/' + k)
                    shutil.copyfile(v['path'] + k, self.output_dir + '/unitpics/' + k)
                elif k[-3:].upper() == 'BOS':
                    print('from: ' + v['path'] + k)
                    print('to:   ' + self.output_dir + '/scripts/' + k)
                    shutil.copyfile(v['path'] + k, self.output_dir + '/scripts/' + k)
                elif k[-3:].upper() == 'COB':
                    print('from: ' + v['path'] + k)
                    print('to:   ' + self.output_dir + '/scripts/' + k)
                    shutil.copyfile(v['path'] + k, self.output_dir + '/scripts/' + k)






            # else:
            #     if k[:-4] in CAVEDOG_SFX or k[:-4] in CAVEDOG_3DO or k[:-4] in CAVEDOG_GAF:
            #         print('♻️ \033[94m' + (k + wspc)[0:23] + '\tOfficial Cavedog Asset\033[0m')
            #     else:
            #         print('☠️ \033[91m' + (k + wspc)[0:23] + '\tFATAL ERROR - DEPENDENCY NOT FOUND ! \033[0m')





#   \033[91m