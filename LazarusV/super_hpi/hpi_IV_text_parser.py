import re




def remove_comments(code: str) -> str:
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL)
    def _replacer(match):
        if match.group(2) is not None:
            return ""
        else:
            return match.group(1)
    return regex.sub(_replacer, code)
def cleanTdf(tdfPath: str) -> str:
    file_contents = open(tdfPath, 'r', errors='replace')
    rawTdf = file_contents.read()
    fbi_dump = remove_comments(code=rawTdf)
    p_01 = fbi_dump.replace('\n', '')
    p_02 = p_01.replace('\t', '').replace('  ' ,'').replace('; ' ,';')
    p_03 = p_02.replace(';ExplosionGaf=', ';explosiongaf=').replace(';Explosiongaf=', ';explosiongaf=')
    p_04 = p_03.replace(';Lavaexplosiongaf=', ';lavaexplosiongaf=').replace(';LavaExplosiongaf=', ';lavaexplosiongaf=')
    p_05 = p_04.replace(';WaterExplosiongaf=', ';waterexplosiongaf=').replace(';WaterExplosionGaf=', ';waterexplosiongaf=')
    p_06 = p_05.replace(';LavaExplosionGaf=', ';lavaexplosiongaf=').replace(';FeatureDead=', ';Featuredead=').replace \
        (';featuredead=', ';Featuredead=')
    p_07 = p_06.replace(';Soundhit=', ';soundhit=').replace(';SoundHit=', ';soundhit=')
    p_08 = p_07.replace(';Soundstart=', ';soundstart=').replace(';SoundStart=', ';soundstart=')
    p_09 = p_08.replace(';Soundwater=', ';soundwater=').replace(';SoundWater=', ';soundwater=')
    return p_09.replace(';object=', ';Object=').replace(';model=', ';Model=')
def cleanFbi(fbiPath: str) -> str:
    file_contents = open(fbiPath, 'r', errors='replace')
    rawFbi = file_contents.read()
    fbi_dump = remove_comments(code=rawFbi)
    p_01 = fbi_dump.replace('\n', '')
    p_02 = p_01.replace('\t', '').replace('  ' ,'').replace('; ' ,';').replace(';corpse=', ';Corpse=')
    p_03 = p_02.replace('objectname=', 'Objectname=').replace('ObjectName=', 'Objectname=')
    return p_03
def parseWeaponTDFsSquareBracks(rawTdf: str) -> list:
    pat = r'(?<=\[).+?(?=\])'
    s = rawTdf
    match = re.findall(pat, s)
    new_match = []
    for m in match:
        new_match.append(m.upper())
    return new_match
def parseWeaponTDFs(rawTdf: str) -> list:
    pat = r'(?<=\{).+?(?=\})'
    s = rawTdf
    match = re.findall(pat, s)
    return match
def takeWeaponPropertiesAndDamage(tdf: str) -> list:
    arr = tdf.split('[DAMAGE]{')
    return arr
def toJson(named: str, arr: list) -> dict:
    _json = {}
    _inner = {}
    for kv in arr:
        arr2 = kv.split('=')
        _inner[arr2[0]] = arr2[1]
    _json[named] = _inner
    return _json
def processDownloadTDF(in_obj: dict, _tojson: dict) -> dict:
    out_obj = in_obj
    for key, val in _tojson.items():
        if 'UNITMENU' in val and 'UNITNAME' in val:
            out_obj[val['UNITMENU'] + ' -> ' + val['UNITNAME']] = val
            out_obj[val['UNITMENU'] + ' -> ' + val['UNITNAME']]['menuentry'] = key
            meta_data = 'entry=' + key + '|menu=' + val['MENU'] + '|button=' + val['BUTTON']
            out_obj[val['UNITMENU'] + ' -> ' + val['UNITNAME']]['meta'] = meta_data
    return out_obj