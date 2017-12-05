import os, re



class TotalADisassembler():
    def __init__(self, dump_path: str):
        self.working_path = dump_path
        self.rawUnitText = ""
        self.rawWeaponText = ""
        self.rawFeatureText = ""
        self.rawDownloadText = ""
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
        # self.evaluateUnit3DFiles(count) TODO: do we need this?
        return processed_units