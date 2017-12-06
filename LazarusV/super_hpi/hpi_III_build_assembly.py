




class TotalAAssembler(object):
    def __init__(self, strict_mode: bool):
        self.enabled = False
        self.weapons = {}
        self.features = {}
        self.download = {}
        self.units = {}
        self.strict_mode = strict_mode
        self.is_valid = True

    def compileToWeaponTDF(self, weapon_tdf_json: str, jkey: str):
        newtdf = '\n\n[' + jkey + ']\n{\n'
        for k,v in weapon_tdf_json.items():
            if k != 'DAMAGE':
                newtdf += '    ' + k + '=' + v + ';\n'
            elif k == 'DAMAGE':
                newtdf += '    [DAMAGE] {\n'
                for dk, dv in v.items():
                    newtdf += '        ' + dk + '=' + dv + ';\n'
                newtdf += '    }\n'
            else:
                print(k)
        newtdf += '}'
        if self.is_valid == True or self.strict_mode == False:
            self.weapons[jkey] = newtdf

    def compileToFeatureTDF(self, _json: str, jkey: str):
        newtdf = '\n\n[' + jkey + ']\n{\n'
        for k,v in _json.items():
            if k != 'DAMAGE':
                newtdf += '    ' + k + '=' + v + ';\n'
        newtdf += '}'
        if self.is_valid == True or self.strict_mode == False:
            self.features[jkey] = newtdf

    def compileToDownloadTDF(self, _json: str, u1: str, u2: str):
        tdfHeader = ''
        newtdf = ''
        entry = ''
        for k, v in _json.items():
            if k == "menuentry":
                tdfHeader = '\n\n[' + v + ']\n{\n'
            elif k != "meta":
                newtdf += '    ' + k + '=' + v + ';\n'
        newtdf += '}'

        if self.is_valid == True or self.strict_mode == False:
            if u2 not in self.download:
                self.download[u2] = []
            self.download[u2].append(tdfHeader + newtdf)

    def compileToUnitFBI(self, _json: str, unit_name: str):
        newtdf = '\n\n[UNITINFO]\n{\n'
        for k,v in _json.items():
            newtdf += '    ' + k + '=' + v + ';\n'
        newtdf += '}'
        if self.is_valid == True or self.strict_mode == False:
            self.units[unit_name] = newtdf
