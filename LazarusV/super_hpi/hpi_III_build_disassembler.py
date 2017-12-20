import os, re

from LazarusV.super_hpi.hpi_IV_text_parser import cleanFbi, cleanTdf, parseWeaponTDFs, \
    parseWeaponTDFsSquareBracks, takeWeaponPropertiesAndDamage, toJson, processDownloadTDF


class TotalADisassembler(object):
    def __init__(self, dump_path: str):
        self.working_path = dump_path

        self.filename_dictionary = {}

        self.rawUnitText = ""
        self.rawWeaponText = ""
        self.rawFeatureText = ""
        self.rawDownloadText = ""

        self._3d_model_dependencies = {}
        self._3d_model_dependencies_cavedog = {}
        self._3d_model_dependencies_error = {}
        self._gaf_dependencies = {}
        self._gaf_dependencies_cavedog = {}
        self._gaf_dependencies_error = {}
        self._wav_dependencies = {}
        self._wav_dependencies_cavedog = {}
        self._wav_dependencies_error = {}
        self.VANILLA_PATH = 'hpi_vanilla/'

        super().__init__()
        self.begin_disassembly()

    def begin_disassembly(self):
        units_path = self.working_path + 'units/'
        weapons_path = self.working_path + 'weapons/'
        features_path = self.working_path + 'features/corpses/'
        downloads_path = self.working_path + 'download/'

        if os.path.exists(units_path):
            unitFiles = os.listdir(units_path)
            for fileName in unitFiles:
                _fpath = units_path + fileName
                cleanFBI = cleanFbi(fbiPath=_fpath)
                self.prep_unit_for_sql(using_fbi=cleanFBI, at_location=_fpath)
                self.rawUnitText += cleanFBI
        if os.path.exists(weapons_path):
            weaponfiles = os.listdir(weapons_path)
            for fileName in weaponfiles:
                _fpath = weapons_path + fileName
                clean_tdf = cleanTdf(tdfPath=_fpath)
                weapon_data = self.get_disassembled_weapons(from_text=clean_tdf)
                self.prep_weapon_for_sql(with_data=weapon_data, at_location=_fpath)
                self.rawWeaponText += clean_tdf
        if os.path.exists(features_path):
            featureFiles = os.listdir(features_path)
            for fileName in featureFiles:
                _fpath = features_path + fileName
                if os.path.isfile(_fpath):
                    cleanTDF = cleanTdf(tdfPath=_fpath)
                    _data = self.get_disassembled_generic(from_text=cleanTDF, kind='feature')
                    self.prep_feature_for_sql(with_data=_data, at_location=_fpath)
                    self.rawFeatureText += cleanTDF
        if os.path.exists(downloads_path):
            downloadFiles = os.listdir(downloads_path)
            for fileName in downloadFiles:
                _fpath = downloads_path + fileName
                cleanTDF = cleanTdf(tdfPath=_fpath)
                _data = self.get_disassembled_generic(from_text=cleanTDF, kind='download')
                self.prep_download_for_sql(with_data=_data, at_location=_fpath)
                self.rawDownloadText += cleanTDF

    def prep_unit_for_sql(self, using_fbi: str, at_location: str):
        self.filename_dictionary[at_location] = {}
        self.filename_dictionary[at_location]['kind'] = 'unit'
        self.filename_dictionary[at_location]['key_name'] = 'UNITINFO'
        self.filename_dictionary[at_location]['zdata'] = self.get_disassembled_units(from_text=using_fbi)

    def prep_weapon_for_sql(self, with_data: dict, at_location: str):
        self.filename_dictionary[at_location] = {}
        self.filename_dictionary[at_location]['kind'] = 'weapon'
        self.filename_dictionary[at_location]['key_name'] = '??'
        self.filename_dictionary[at_location]['zdata'] = with_data

    def prep_feature_for_sql(self, with_data: dict, at_location: str):
        self.filename_dictionary[at_location] = {}
        self.filename_dictionary[at_location]['kind'] = 'feature'
        self.filename_dictionary[at_location]['key_name'] = '??'
        self.filename_dictionary[at_location]['zdata'] = with_data

    def prep_download_for_sql(self, with_data: dict, at_location: str):
        self.filename_dictionary[at_location] = {}
        self.filename_dictionary[at_location]['kind'] = 'download'
        self.filename_dictionary[at_location]['key_name'] = '??'
        self.filename_dictionary[at_location]['zdata'] = with_data

    @property
    def unload_text_units(self) -> str:
        return self.rawUnitText

    @property
    def unload_text_weapons(self) -> str:
        return self.rawWeaponText

    @property
    def unload_text_features(self) -> str:
        return self.rawFeatureText

    @property
    def unload_text_downloads(self) -> str:
        return self.rawDownloadText


    def get_disassembled_units(self, from_text: str) -> list:
        tdfList = from_text.split('[UNITINFO]')
        fbiList = []
        if tdfList[0] == '':
            fbiList = tdfList[1:] # first element is blank.
        processed_units = []
        for innerTdf in fbiList:
            unit = self.jsonize_fbi(using_text=innerTdf)

            # arr1 = innerTdf.replace('/', ' ').replace(',', ' ').replace('{', '').replace(';}', ';').split(';')[:-1]
            # for kv in arr1:
            #     if '=' in kv:
            #         prop = kv.split('=')
            #         key = prop[0]
            #         value = prop[1]
            #         if key.upper() == 'OBJECTNAME':
            #             key = 'Objectname'
            #         elif key.upper() == 'WEAPON1':
            #             value = value.upper()
            #         elif key.upper() == 'WEAPON2':
            #             value = value.upper()
            #         elif key.upper() == 'WEAPON3':
            #             value = value.upper()
            #         unit[key] = value

            processed_units.append(unit)
        self.evaluateUnit3DFiles(processed_units)
        return processed_units

    @staticmethod
    def jsonize_fbi(using_text: str) -> dict:
        unit = {}
        arr1 = using_text.replace('/', ' ').replace(',', ' ').replace('{', '').replace(';}', ';').split(';')[:-1]
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
        return unit


    def get_disassembled_weapons(self, from_text: str) -> dict:
        tdfKeyList = parseWeaponTDFsSquareBracks(rawTdf=from_text)
        tdfList = parseWeaponTDFs(rawTdf=from_text)
        count = []
        results = {}
        i = 0
        for innerTdf in tdfList:
            if tdfKeyList[i] == 'DAMAGE':
                i += 1
            unique_key = tdfKeyList[i] #.upper()
            pnd = takeWeaponPropertiesAndDamage(tdf=innerTdf)
            _dmg = pnd[1].split(';')[:-1]
            _weapon = pnd[0].split(';')[:-1]
            asJson = toJson(named=unique_key, arr=_weapon)
            asJson[unique_key]['DAMAGE'] = toJson(named='DAMAGE', arr=_dmg)['DAMAGE']
            count.append(asJson[unique_key])
            results[unique_key] = asJson[unique_key]
            if 'model' in asJson[unique_key]:
                name = asJson[unique_key]['model']
                file_path = self.working_path + 'objects3d/' + asJson[unique_key]['model'] + '.3do'
                self.addModelDependency(file_path, name)
            elif 'Model' in asJson[unique_key]:
                name = asJson[unique_key]['Model']
                file_path = self.working_path + 'objects3d/' + asJson[unique_key]['Model'] + '.3do'
                self.addModelDependency(file_path, name)
            self.findGafDependencies(asJson[unique_key])
            self.findWeaponWavDependencies(asJson[unique_key])
            i += 1
        return results

    def get_disassembled_generic(self, from_text: str, kind: str) -> dict:
        bug_fix_1 = from_text.replace('[MENUENTRY0]{}', '')
        corpseValuesJSON = parseWeaponTDFs(rawTdf=bug_fix_1)
        corpseKeysJSON = parseWeaponTDFsSquareBracks(rawTdf=bug_fix_1)
        # returnArr = []
        returnObj = {}
        n = 0
        for _json in corpseValuesJSON:
            # _tojson = []
            _tojson = toJson(named=corpseKeysJSON[n], arr=_json.split(';')[:-1])
            if kind == 'download':
                returnObj = processDownloadTDF(in_obj=returnObj, _tojson=_tojson)
            else:
                returnObj = self.evaluateFeature3DFiles(in_obj=returnObj, _toJson=_tojson)
            n += 1
        return returnObj

    def evaluateFeature3DFiles(self, in_obj: dict, _toJson: dict) -> dict:
        out_obj = in_obj
        for key, val in _toJson.items():
            file_path = ''
            model_key = 'object'
            if model_key in val:
                file_path = self.working_path + 'objects3d/' + val[model_key] + '.3do'
            else:
                model_key = "Object"
                if 'Object' in val:
                    file_path = self.working_path + 'objects3d/' + val[model_key] + '.3do'

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

    def evaluateUnit3DFiles(self, list_items: list):
        for unit in list_items:
            model_key = 'Objectname'
            file_path = self.working_path + 'objects3d/' + unit[model_key] + '.3do'

            if os.path.isfile(file_path):
                self._3d_model_dependencies[unit[model_key]] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'objects3d/' + model_key + '.3do'):
                    self._3d_model_dependencies_cavedog[unit[model_key]] = file_path
                else:
                    self._3d_model_dependencies_error[unit[model_key]] = file_path
    def findGafDependencies(self, unitObj: dict):
        if 'explosiongaf' in unitObj:
            file_path = self.working_path + 'anims/' + unitObj['explosiongaf'] + '.gaf'
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['explosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['explosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['explosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['explosiongaf']] = file_path
        elif 'Explosiongaf' in unitObj:
            file_path = self.working_path + 'anims/' + unitObj['Explosiongaf'] + '.gaf'
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['Explosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['Explosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['Explosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['Explosiongaf']] = file_path
        if 'waterexplosiongaf' in unitObj:
            file_path = self.working_path + 'anims/' + unitObj['waterexplosiongaf'] + '.gaf'
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['waterexplosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['waterexplosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['waterexplosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['waterexplosiongaf']] = file_path
        if 'lavaexplosiongaf' in unitObj:
            file_path = self.working_path + 'anims/' + unitObj['lavaexplosiongaf'] + '.gaf'
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['lavaexplosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['lavaexplosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['lavaexplosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['lavaexplosiongaf']] = file_path
    def findWeaponWavDependencies(self, weap_obj: dict):
        key1 = 'soundhit'
        key2 = 'soundstart'
        key3 = 'soundwater'
        keys = [key1, key2, key3]
        for k in keys:
            if k in weap_obj:
                file_path = self.working_path + 'sounds/' + weap_obj[k] + '.wav'
                if os.path.isfile(file_path):
                    self._wav_dependencies[weap_obj[k]] = file_path
                else:
                    if os.path.isfile(self.VANILLA_PATH + 'sounds/' + weap_obj[k] + '.wav'):
                        self._wav_dependencies_cavedog[weap_obj[k]] = file_path
                    else:
                        self._wav_dependencies_error[weap_obj[k]] = file_path
    def addModelDependency(self, path: str, name: str):
        if os.path.isfile(path):
            self._3d_model_dependencies[name] = path
        else:
            if os.path.isfile(self.VANILLA_PATH + 'objects3d/' + path + '.3do'):
                self._3d_model_dependencies_cavedog[name] = path
            else:
                self._3d_model_dependencies_error[name] = path

