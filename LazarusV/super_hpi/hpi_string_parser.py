import os, re



class TotalADisassembler():
    def __init__(self, dump_path: str):
        self.working_path = dump_path
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
        features_path = self.working_path + 'features/'
        downloads_path = self.working_path + 'downloads/'

        if os.path.exists(units_path):
            unitFiles = os.listdir(units_path)
            for fileName in unitFiles:
                _fpath = units_path + fileName
                cleanFBI = self.cleanFbi(fbiPath=_fpath)
                self.rawUnitText += cleanFBI
        if os.path.exists(weapons_path):
            weaponfiles = os.listdir(weapons_path)
            for fileName in weaponfiles:
                _fpath = weapons_path + fileName
                self.rawWeaponText += self.cleanTdf(tdfPath=_fpath)
        if os.path.exists(features_path):
            featureFiles = os.listdir(features_path)
            for fileName in featureFiles:
                _fpath = features_path + fileName
                cleanTDF = self.cleanTdf(tdfPath=_fpath)
                self.rawFeatureText += cleanTDF
        if os.path.exists(downloads_path):
            downloadFiles = os.listdir(downloads_path)
            for fileName in downloadFiles:
                _fpath = downloads_path + fileName
                cleanTDF = self.cleanTdf(tdfPath=_fpath)
                self.rawDownloadText += cleanTDF

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



    def get_disassembled_units(self, units_as_raw_text: str) -> list:
        tdfList = units_as_raw_text.split('[UNITINFO]')
        fbiList = []
        if tdfList[0] == '':
            fbiList = tdfList[1:] # first element is blank.
        processed_units = []
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
            processed_units.append(unit)
        self.evaluateUnit3DFiles(processed_units)
        return processed_units

    def get_disassembled_weapons(self, weapons_as_raw_text: str) -> dict:
        tdfKeyList = self.parseWeaponTDFsSquareBracks(weapons_as_raw_text)
        tdfList = self.parseWeaponTDFs(weapons_as_raw_text)
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


















    def remove_comments(self, code: str) -> str:
        pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
        regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
        def _replacer(match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)
        return regex.sub(_replacer, code)
    def cleanTdf(self, tdfPath: str) -> str:
        file_contents = open(tdfPath, 'r', errors='replace')
        rawTdf = file_contents.read()
        fbi_dump = self.remove_comments(code=rawTdf)
        parse_01 = fbi_dump.replace('\n', '')
        parse_02 = parse_01.replace('\t', '').replace('  ','').replace('; ',';')
        parse_03 = parse_02.replace(';ExplosionGaf=', ';explosiongaf=').replace(';Explosiongaf=', ';explosiongaf=')
        parse_04 = parse_03.replace(';Lavaexplosiongaf=', ';lavaexplosiongaf=').replace(';LavaExplosiongaf=', ';lavaexplosiongaf=')
        parse_05 = parse_04.replace(';WaterExplosiongaf=', ';waterexplosiongaf=').replace(';WaterExplosionGaf=', ';waterexplosiongaf=')
        parse_06 = parse_05.replace(';LavaExplosionGaf=', ';lavaexplosiongaf=').replace(';FeatureDead=', ';Featuredead=').replace(';featuredead=', ';Featuredead=')
        parse_07 = parse_06.replace(';Soundhit=', ';soundhit=').replace(';SoundHit=', ';soundhit=')
        parse_08 = parse_07.replace(';Soundstart=', ';soundstart=').replace(';SoundStart=', ';soundstart=')
        parse_09 = parse_08.replace(';Soundwater=', ';soundwater=').replace(';SoundWater=', ';soundwater=')
        return parse_09.replace(';object=', ';Object=').replace(';model=', ';Model=')
    def cleanFbi(self, fbiPath: str) -> str:
        file_contents = open(fbiPath, 'r', errors='replace')
        rawFbi = file_contents.read()
        fbi_dump = self.remove_comments(code=rawFbi)
        parse_01 = fbi_dump.replace('\n', '')
        parse_02 = parse_01.replace('\t', '').replace('  ','').replace('; ',';').replace(';corpse=', ';Corpse=')
        parse_03 = parse_02.replace('objectname=', 'Objectname=').replace('ObjectName=', 'Objectname=')
        return parse_03
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
    def evaluateUnit3DFiles(self, list_items):
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
    def findGafDependencies(self, unitObj):
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
            # self._gaf_dependencies[unitObj['waterexplosiongaf']] = file_path
            if os.path.isfile(file_path):
                self._gaf_dependencies[unitObj['waterexplosiongaf']] = file_path
            else:
                if os.path.isfile(self.VANILLA_PATH + 'anims/' + unitObj['waterexplosiongaf'] + '.gaf'):
                    self._gaf_dependencies_cavedog[unitObj['waterexplosiongaf']] = file_path
                else:
                    self._gaf_dependencies_error[unitObj['waterexplosiongaf']] = file_path
        if 'lavaexplosiongaf' in unitObj:
            file_path = self.working_path + 'anims/' + unitObj['lavaexplosiongaf'] + '.gaf'
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
                file_path = self.working_path + 'sounds/' + weap_obj[k] + '.wav'
                if os.path.isfile(file_path):
                    self._wav_dependencies[weap_obj[k]] = file_path
                else:
                    if os.path.isfile(self.VANILLA_PATH + 'sounds/' + weap_obj[k] + '.wav'):
                        self._wav_dependencies_cavedog[weap_obj[k]] = file_path
                    else:
                        self._wav_dependencies_error[weap_obj[k]] = file_path
    def addModelDependency(self, path, name):
        if os.path.isfile(path):
            self._3d_model_dependencies[name] = path
        else:
            if os.path.isfile(self.VANILLA_PATH + 'objects3d/' + path + '.3do'):
                self._3d_model_dependencies_cavedog[name] = path
            else:
                self._3d_model_dependencies_error[name] = path
    def takeWeaponPropertiesAndDamage(self, tdf):
        arr = tdf.split('[DAMAGE]{')
        return arr
    def toJson(self, named, arr):
        _json = {}
        _inner = {}
        for kv in arr:
            arr2 = kv.split('=')
            _inner[arr2[0]] = arr2[1]
        _json[named] = _inner
        return _json