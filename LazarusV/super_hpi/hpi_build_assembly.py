
class totala_assembler():
    def __init__(self, strict_mode: bool):
        self.enabled = False
        self.weapons = {}
        self.features = {}
        self.download = {}
        self.units = {}
        self.strict_mode = strict_mode
        self.is_valid = True

    def compileToWeaponTDF(self, weapon_tdf_json, jkey):
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

    def compileToFeatureTDF(self, _json, jkey):
        # print('  ⚡️ ⚡️ ⚡️ ⚡️ ⚡️ ⚡️ ⚡️ ⚡️ ⚡️  ')
        # print(jkey)
        # print(_json)
        newtdf = '\n\n[' + jkey + ']\n{\n'
        for k,v in _json.items():
            if k != 'DAMAGE':
                newtdf += '    ' + k + '=' + v + ';\n'
        newtdf += '}'
        if self.is_valid == True or self.strict_mode == False:
            self.features[jkey] = newtdf

    def compileToDownloadTDF(self, _json, u1, u2):
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

    def compileToUnitFBI(self, _json, unit_name):
        newtdf = '\n\n[UNITINFO]\n{\n'
        for k,v in _json.items():
            newtdf += '    ' + k + '=' + v + ';\n'
        newtdf += '}'
        if self.is_valid == True or self.strict_mode == False:
            self.units[unit_name] = newtdf
