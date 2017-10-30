from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json

from rest_framework.decorators import detail_route, list_route
from rest_framework import status
from rest_framework import viewsets
import re
import codecs
import os
from lazarus.views import WeaponTDFFetch, FeatureTDFFetch, DownloadTDFFetch, SoundTDFFetch
# Create your views here.

from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF, SoundSetTDF
from LazarusDatabase.models import LazarusModProject, LazarusModAsset, LazarusModDependency, LazarusPublicAsset
from chat.models import JawnUser
import copy


emojKill = '💔'
emoj0 = ''  # '🖤'
emoj1 = ''  # emoji.emojize(':blue_heart:')
emoj2 = ''  # emoji.emojize(':green_heart:')
emoj3 = ''  # emoji.emojize(':yellow_heart:')
emoj4 = ''  # ('❤️️')
emoj5 = ''  # emoji.emojize(':purple_heart:')

ej_info1 = '' #emoji.emojize(':zap:')

ej_warn1 = '' #emoji.emojize(':fire:')
ej_warn3 = '' #emoji.emojize(':warning:')
ej_warn2 = '' #emoji.emojize(':boom:')

ej_fbi = '' #emoji.emojize('::package::')
ej_weapon = '' #emoji.emojize(':bomb:')
ej_corpse = '' #emoji.emojize(':skull:')
ej_download = '' #emoji.emojize(':clipboard:')

ej_success1 = '' #emoji.emojize(':white_check_mark:')
ej_success2 = '' #emoji.emojize(':large_blue_circle:')
ej_notfound1 = '' #emoji.emojize('❌')
ej_notfound2 = '' #emoji.emojize('🚫')

ej_none = '⭕️'


class bcolors():
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


class sample(APIView):
    def get(self, request, format=None):
        # 'SOUND',
        return Response('LazarusIII is working properly.')


class DependenciesForUnitFBI(APIView):
    txtOutput = ''
    ENDPRINT = '<br>'

    HTML_PURPLE = 'purple-A400-fg'
    HTML_ORANGE = 'orange-500-fg'
    HTML_YELLOW = 'yellow-A400-fg'
    HTML_RED = 'red-A400-fg'
    HTML_BLUE = 'blue-A200-fg'
    HTML_GREEN = 'light-green-A700-fg'
    HTML_CYAN = 'cyan-500-fg'
    HTML_TEAL = 'teal-A400-fg'

    HTML_LIME = 'blue-grey-600-fg'

    def printpathwithfile(self, path, filename):
        self.txtOutput += path + filename + self.ENDPRINT
        print(bcolors.lightgrey + path + bcolors.ENDC + bcolors.green + filename + bcolors.ENDC)

    def printpathwithweapon(self, path, filename):
        self.txtOutput += path + filename + self.ENDPRINT
        print(bcolors.TEAL + path + bcolors.ENDC + bcolors.purple + filename + bcolors.ENDC)

    def printkeywithvalue(self, key, value):
        self.txtOutput += key + value + self.ENDPRINT
        definer = bcolors.TEAL + \
                  key + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '  ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  value + \
                  bcolors.ENDC
        print(definer + midchar + end_val)

    def printweaponkeywithvalue(self, weapon, value):
        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str(weapon)
        self.txtOutput += '</span>'
        self.txtOutput += ' -> ' + value + self.ENDPRINT
        definer = bcolors.red + \
                  weapon + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '  ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.purple + \
                  value + \
                  bcolors.ENDC
        print(definer + midchar + end_val)

    def printpurple(self, str_):
        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str_ + self.ENDPRINT
        print(bcolors.purple + str_ + bcolors.ENDC)
        self.txtOutput += '</span>'

    def printblue(self, str_):
        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str_ + self.ENDPRINT
        print(bcolors.blue + str_ + bcolors.ENDC)
        self.txtOutput += '</span>'

    def printred(self, str_):
        self.txtOutput += '<span class="' + self.HTML_RED + '">'
        self.txtOutput += str_ + self.ENDPRINT
        print(bcolors.red + str_ + bcolors.ENDC)
        self.txtOutput += '</span>'

    def printorange(self, str_):
        self.txtOutput += '<span class="' + self.HTML_ORANGE + '">'
        self.txtOutput += str_ + self.ENDPRINT
        print(bcolors.orange + str_ + bcolors.ENDC)
        self.txtOutput += '</span>'

    def printgreen(self, str_):
        self.txtOutput += '<span class="' + self.HTML_GREEN + '">'
        self.txtOutput += str_ + self.ENDPRINT
        print(bcolors.green + str_ + bcolors.ENDC)
        self.txtOutput += '</span>'

    def printbluekeyvalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.purple + key + bcolors.ENDC + bcolors.blue + str(val) + bcolors.ENDC)

    def printbluekeyredvalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_RED + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.blue + key + bcolors.ENDC + bcolors.red + str(val) + bcolors.ENDC)

    def printbluekeyyellowvalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_YELLOW + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.blue + key + bcolors.ENDC + bcolors.orange + str(val) + bcolors.ENDC)

    def printbluekeygreenvalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_GREEN + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.blue + key + bcolors.ENDC + bcolors.green + str(val) + bcolors.ENDC)

    def printbluekeypurplevalue(self, key, val):

        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.blue + key + bcolors.ENDC + bcolors.purple + str(val) + bcolors.ENDC)

    def printyellow_orange_teal(self, str1, str2, str3):
        self.txtOutput += '<span class="' + self.HTML_YELLOW + '">'
        self.txtOutput += str(str1)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_ORANGE + '">'
        self.txtOutput += str(str2)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_CYAN + '">'
        self.txtOutput += str(str3)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.orange + str(str1) + bcolors.ENDC +
              bcolors.lightred + str(str2) + bcolors.ENDC +
              bcolors.TEAL + str(str3) + bcolors.ENDC)

    def printredkeybluevalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_RED + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.red + key + bcolors.ENDC + bcolors.blue + str(val) + bcolors.ENDC)

    def printredkeygreenvalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_RED + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_GREEN + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.red + key + bcolors.ENDC + bcolors.lightgreen + str(val) + bcolors.ENDC)

    def printredkeyyellowvalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_RED + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_ORANGE + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.red + key + bcolors.ENDC + bcolors.lightgreen + str(val) + bcolors.ENDC)

    def printredkeypurplevalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_RED + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.red + key + bcolors.ENDC + bcolors.lightgreen + str(val) + bcolors.ENDC)

    def printyellowkeybluevalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_YELLOW + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_BLUE + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.red + key + bcolors.ENDC + bcolors.blue + str(val) + bcolors.ENDC)

    def printyellowkeygreenvalue(self, key, val):
        self.txtOutput += '<span class="' + self.HTML_YELLOW + '">'
        self.txtOutput += str(key)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_GREEN + '">'
        self.txtOutput += str(val)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        print(bcolors.red + key + bcolors.ENDC + bcolors.lightgreen + str(val) + bcolors.ENDC)

    def print_yellow_purple_green(self, str1, str2, str3):
        self.txtOutput += '<span class="' + self.HTML_ORANGE + '">'
        self.txtOutput += str(str1)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str(str2)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_GREEN + '">'
        self.txtOutput += str(str3)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT

    def print_yellow_purple_teal(self, str1, str2, str3):
        self.txtOutput += '<span class="' + self.HTML_ORANGE + '">'
        self.txtOutput += str(str1)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str(str2)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_TEAL + '">'
        self.txtOutput += str(str3)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT

        # print(bcolors.red + key + bcolors.ENDC + bcolors.lightgreen + str(val) + bcolors.ENDC)

    def print_yellow_purple_red(self, str1, str2, str3):
        self.txtOutput += '<span class="' + self.HTML_ORANGE + '">'
        self.txtOutput += str(str1)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_PURPLE + '">'
        self.txtOutput += str(str2)
        self.txtOutput += '</span>'

        self.txtOutput += '<span class="' + self.HTML_RED + '">'
        self.txtOutput += str(str3)
        self.txtOutput += '</span>'
        self.txtOutput += self.ENDPRINT
        # print(bcolors.red + key + bcolors.ENDC + bcolors.lightgreen + str(val) + bcolors.ENDC)

    def printcyan(self, str_):
        self.txtOutput += '<span class="' + self.HTML_CYAN + '">'
        self.txtOutput += str_ + self.ENDPRINT
        print(bcolors.cyan + str_ + bcolors.ENDC)
        self.txtOutput += '</span>'

    def printgray(self, str_):
        self.txtOutput += str_ + self.ENDPRINT
        print(bcolors.darkgrey + str_ + bcolors.ENDC)

    def printif(self, condition, str_):
        print(bcolors.lightred + 'IF: ' + str_ + bcolors.BOLD + str(condition) + bcolors.ENDC + bcolors.ENDC)

    def printthen(self, results, str_):
        print(bcolors.lightgreen + 'THEN: ' + str_ + bcolors.BOLD + str(results) + bcolors.ENDC + bcolors.ENDC)

    def printelse(self, results, str_):
        print(bcolors.TEAL + 'ELSE: ' + str_ + bcolors.BOLD + str(results) + bcolors.ENDC + bcolors.ENDC)

    def printBOOL(self, name, value):
        self.txtOutput += '<span class="' + self.HTML_LIME + '">'
        self.txtOutput += name
        self.txtOutput += '</span>'
        color = bcolors.green
        if value == False:
            color = bcolors.red
        print(color + name + ' : ' + bcolors.BOLD + str(value) + bcolors.ENDC + bcolors.ENDC)
        # HTML ONLY:
        if value == False:
            self.txtOutput += '<span class="' + self.HTML_RED + '">'
            self.txtOutput += ' : ' + str(value) + self.ENDPRINT
        else:
            self.txtOutput += '<span class="' + self.HTML_GREEN + '">'
            self.txtOutput += ' : ' + str(value) + self.ENDPRINT

        self.txtOutput += '</span>'



    # permission_classes = (AllowAny,)
    def get(self, request, format=None):
        uid = request.GET['uid']

        # CHECK IF THIS DEPENDENCY ALREADY EXISTS:
        try:
            lazarusmodasset = LazarusModAsset.objects.get(name=uid)
            for mod in modprojects:
                if mod.id == lazarusmodasset.project_id:
                    return Response(
                        {'result': 'Aborting, mod asset with UnitName ' + uid + ' already exists for this mod.'})
        except:
            pass

        jawn_user = JawnUser.objects.get(base_user=request.user.id)
        modprojects = LazarusModProject.objects.filter(created_by=jawn_user)
        mod_id = 0

        for mod in modprojects:
            if mod.is_selected == True:
                mod_id = mod.id
        newLazarusModAsset = LazarusModAsset(name=uid, type='UnitFBI', project_id=mod_id, uploader=jawn_user)

        # Get unit with UnitName from database.
        print('Attempting to query FbiData from SQL with filter: ' + uid)
        sampleunit = UnitFbiData.objects.filter(_SNOWFLAKE=(uid))
        newSnowflake = sampleunit[0]._SNOWFLAKE + '|' + str(jawn_user.id)
        self.printbluekeypurplevalue('Preparing To Clone: ', sampleunit[0]._SNOWFLAKE)


        fbiUnitClone = copy.deepcopy(sampleunit[0])
        fbiUnitClone._SNOWFLAKE = newSnowflake
        print(sampleunit[0].id)
        print(sampleunit[0])
        fbiUnitClone.id = sampleunit[0].id + 3000000
        print(fbiUnitClone.id)
        print(fbiUnitClone)
        self.printbluekeygreenvalue('Clone Successful!!! ', fbiUnitClone._SNOWFLAKE)
        fbiUnitClone.save()


        serialized_obj = serializers.serialize("json", sampleunit)
        json_dict = json.loads(serialized_obj)

        try:
            printName = fbiUnitClone.UnitName
            self.txtOutput += '<h1 class="' + self.HTML_TEAL + '">'
            self.txtOutput += str(printName)
            self.txtOutput += '</h1>'
        except:
            printName = uid
            self.txtOutput += '<h1 class="' + self.HTML_TEAL + '">'
            self.txtOutput += str(printName) + ' - failed to get name: fbiUnitClone.UnitName'
            self.txtOutput += '</h1>'

        # Use the unit from SQL and get a path to the root HPI extraction:
        dev_root_path = fbiUnitClone._DEV_root_data_path
        last_occurance_of_slash = dev_root_path.rfind("/")
        fbi_file = dev_root_path[last_occurance_of_slash:]
        path_without_fbi = dev_root_path.replace(fbi_file, '').replace('/units', '')

        # print('\n')
        # print( 'DEPENDENCY SCANNER PHASES:' )
        # self.printcyan(bcolors.HEADER + '[' + emoj5 + ' ] - Atomic Files: PCX, COB, and 3DO' + bcolors.ENDC)
        # self.printcyan(bcolors.HEADER + '[' + emoj4 + ' ] - Scan FBI Key Values, get UnitName Objectname and Corpse' + bcolors.ENDC)
        # self.printcyan(bcolors.HEADER + '[' + emoj3 + ' ] - Scan Weapon Data, verify with unit' + bcolors.ENDC)
        # self.printcyan(bcolors.HEADER + '[' + emoj2 + ' ] - Scan all sound data' + bcolors.ENDC)
        # self.printcyan(bcolors.HEADER + '[' + emoj1 + ' ] - Scan Corpses, verify feature is good' + bcolors.ENDC)
        # self.printcyan(bcolors.HEADER + '[' + emoj0 + ' ] - Display list of all detected file paths' + bcolors.ENDC)
        # print('\n\n\n\n')


        # self.printpurple(path_without_fbi)
        # self.printpathwithfile(path_without_fbi, fbi_file)

        ### STORE ATOMIC DEPENDENCIES IN RAM:
        SYSPATH_unitpic = ''
        SYSPATH_3DModel = ''
        SYSPATH_TDCrpse = ''
        SYSPATH_3DCrpse = ''
        SYSPATH_animGAF = ''
        SYSPATH_scriCOB = ''

        # Global Weapons In RAM:
        weapon1Snowflake = ''
        weapon2Snowflake = ''
        weapon3Snowflake = ''
        weapon1FromSQL = []
        weapon2FromSQL = []
        weapon3FromSQL = []

        # Weapon 3DO File Paths:
        weapon3DOFilePaths = []
        weaponGafs = []

        # All sound data related to TA unit with uid
        sound_assets_evaluation = []

        ### DEPENDENCIES CHECKLIST:
        dp_unitpic = False
        dp_3dmodel = False
        dp_script = False
        dp_corpses = False
        dp_corpsemodel = False
        dp_download = False
        dp_animation = False
        this_unit_has_weapons = False

        # Evaluate paths ahead of time:
        unit_weapon_path = ''
        uname = fbiUnitClone.UnitName.lower()

        # UNIT PIC PATH DETECTOR:
        PCX_filename = uname + '.pcx'
        unit_pic_path = path_without_fbi + '/unitpics/'
        defaultCaseUnitPic = unit_pic_path + PCX_filename
        dp_unitpic = os.path.exists(defaultCaseUnitPic)
        self.printif(' Unit Pic Exists? ', defaultCaseUnitPic)
        if dp_unitpic == False:
            PCX_filename = uname.lower() + '.pcx'
            lowerCaseUnitPic = unit_pic_path + uname.lower() + '.pcx'
            dp_unitpic = os.path.exists(lowerCaseUnitPic)
            self.printthen(lowerCaseUnitPic, 'dp_unitpic not found, trying lowercase')
        self.printBOOL('dp_unitpic', dp_unitpic)
        if dp_unitpic == True:
            SYSPATH_unitpic = unit_pic_path + PCX_filename

        # UNIT DOWNLOAD PATH DETECTOR:
        unit_download_path = path_without_fbi + '/download/' + uname + '.tdf'
        dp_download = os.path.exists(unit_download_path)
        downloadTdfs = []
        if dp_download == True:
            downloadTdf = DownloadTDFFetch().get(unit_download_path)
            for tdf in downloadTdf:
                downloadTdfs.append(tdf)
        self.printBOOL('dp_download', dp_download)

        # 3DO MODEL PATH DETECTOR:
        unit_3do_path = path_without_fbi + '/objects3d/'
        uobjname = fbiUnitClone.Objectname.lower()
        _3DO_filename = uobjname + '.3do'
        dp_3dmodel = os.path.exists(unit_3do_path + _3DO_filename)
        self.printBOOL('dp_3dmodel', dp_3dmodel)
        if dp_3dmodel == True:
            SYSPATH_3DModel = unit_3do_path + _3DO_filename

        # COB SCRIPT PATH DETECTOR:
        unit_cob_path = path_without_fbi + '/scripts/'
        ucobname = fbiUnitClone.Objectname.lower()
        COB_filename = ucobname + '.cob'
        dp_script = os.path.exists(unit_cob_path + COB_filename)
        self.printBOOL('dp_script', dp_script)
        if dp_script == True:
            SYSPATH_scriCOB = unit_cob_path + COB_filename

        # GAF ANIMATION PATH DETECTOR:
        unit_gaf_path = path_without_fbi + '/anims/'
        ugafname = uname + '_gadget'
        GAF_filename = ugafname + '.gaf'
        dp_animation = os.path.exists(unit_gaf_path + GAF_filename)
        self.printBOOL('dp_animation', dp_animation)
        if dp_animation == True:
            SYSPATH_animGAF = unit_gaf_path + GAF_filename

        # make sure the important stuff exists: PCX, COB, and 3DO
        allVitalUnitDependenciesExist = False
        self.printcyan('Checking if the important stuff exists: PCX, COB, and 3DO: ')
        if dp_script == True and dp_unitpic == True and dp_3dmodel == True:
            allVitalUnitDependenciesExist = True
            self.printthen(allVitalUnitDependenciesExist,
                           ' Got all important atomic files except corpse model, carrying on... ')
        else:
            self.printelse(allVitalUnitDependenciesExist, ' This unit is badly broken, vital files are missing: ')

        self.printpurple('\n╔══[' + emoj5 + ' ]: Unit FBI evaluation.')

        # Unit FBI Key Value Dependencies:
        FBIKey_UnitName = ej_notfound2
        FBIKey_Objectname = ej_notfound2
        FBIKey_SoundCategory = ej_notfound2
        FBIKey_ExplodeAs = ej_notfound2
        FBIKey_SelfDestructAs = ej_notfound2
        FBIKey_Corpse = ej_notfound2
        FBIKey_Weapon1 = ej_notfound2
        FBIKey_Weapon2 = ej_notfound2
        FBIKey_Weapon3 = ej_notfound2
        try:
            FBIKey_UnitName = fbiUnitClone.UnitName
        except:
            self.printred('║FAILED TO READ - UnitName')
        try:
            FBIKey_Objectname = fbiUnitClone.Objectname
        except:
            self.printred('║FAILED TO READ - Objectname')
        try:
            FBIKey_SoundCategory = fbiUnitClone.SoundCategory
        except:
            self.printred('║FAILED TO READ - SoundCategory')
        try:
            FBIKey_ExplodeAs = fbiUnitClone.ExplodeAs
        except:
            self.printred('║FAILED TO READ - ExplodeAs')
        try:
            FBIKey_SelfDestructAs = fbiUnitClone.SelfDestructAs
        except:
            self.printred('║FAILED TO READ - SelfDestructAs')
        try:
            FBIKey_Corpse = fbiUnitClone.Corpse
            if FBIKey_Corpse == '' or FBIKey_Corpse == None:
                FBIKey_Corpse = ej_none
        except:
            self.printred('║FAILED TO READ - Corpse')
            FBIKey_Corpse = ej_notfound2
        try:
            FBIKey_Weapon1 = fbiUnitClone.Weapon1
            if FBIKey_Weapon1 == None:
                FBIKey_Weapon1 = ej_none
        except:
            self.printred('║This unit has no weapons')
        try:
            FBIKey_Weapon2 = fbiUnitClone.Weapon2
            if FBIKey_Weapon2 == None:
                FBIKey_Weapon2 = ej_notfound2
        except:
            self.printred('║This unit has no Weapon2')
        try:
            FBIKey_Weapon3 = fbiUnitClone.Weapon3
            if FBIKey_Weapon3 == None:
                FBIKey_Weapon3 = ej_notfound2
        except:
            self.printred('║This unit has no Weapon3')
        self.printbluekeyvalue('║FBIKey_UnitName-->', FBIKey_UnitName)
        self.printbluekeyvalue('║FBIKey_Objectname-->', FBIKey_Objectname)
        self.printbluekeyvalue('║FBIKey_SoundCategory-->', FBIKey_SoundCategory)
        self.printbluekeyvalue('║FBIKey_ExplodeAs-->', FBIKey_ExplodeAs)
        self.printbluekeyvalue('║FBIKey_SelfDestructAs-->', FBIKey_SelfDestructAs)
        self.printbluekeyvalue('║FBIKey_Corpse-->', FBIKey_Corpse)
        self.printbluekeyvalue('║FBIKey_Weapon1-->', FBIKey_Weapon1)
        self.printbluekeyvalue('║FBIKey_Weapon2-->', FBIKey_Weapon2)
        self.printbluekeyvalue('║FBIKey_Weapon3-->', FBIKey_Weapon3)
        self.printpurple('╚════════════════════════════════════════════════════════════════')

        arrayofweaponkeys = []
        # Weapon Evaluation:
        if FBIKey_Weapon1 == ej_none:
            self.printred('\n╔══[' + emoj4 + ' ] - This unit appears to have no weapons.════')
        else:
            # BASIC WEAPON PATH DETECTOR: (based on unit name)
            self.printred('\n╔══[' + emoj4 + ' ] - Weapon evaluation.════')
            unit_weapon_path = path_without_fbi + '/weapons/' + uname + '_weapon.tdf'
            dp_allweapons = os.path.exists(unit_weapon_path)
            self.printBOOL('║dp_allweapons', dp_allweapons)
            self.printred('║basic weapon scanner failed, must scan all weapons avaliable in the path: ')
            self.printpathwithweapon('║' + path_without_fbi, '/weapons/')

            pathToWeaponsDir = path_without_fbi + '/weapons/'
            allWeaponTDFFiles = []
            if os.path.exists(pathToWeaponsDir):
                allWeaponTDFFiles = os.listdir(pathToWeaponsDir)
            self.printkeywithvalue('║ allWeaponTDFFiles ', str(allWeaponTDFFiles))

            self.printred('║ ')
            self.printred('║ Gathering 3rd party weapon models, if they exist.')
            # self.printred('║ missing weapon models result in a crash.')
            # self.printred('║ This portion of the dependency scanner is incomplete,')
            # self.printred('║ it can only verify 3rd party models, it will not check yet for Cavedog models.')
            for tdfFile in allWeaponTDFFiles:
                try:
                    weaponTDF = WeaponTDFFetch().get(path_without_fbi + '/weapons/' + tdfFile)
                    self.printredkeybluevalue('║ Converting TDF to JSON... ', '/weapons/' + tdfFile)
                    self.printred('║ Total weapons detected in this TDF file: ' + str(len(weaponTDF)))
                    print(json.dumps(weaponTDF, indent=2, sort_keys=True))

                    # IDENTIFY WEAPONS BY USING SNOWFLAKES:
                    if weaponTDF[0]['_OBJECT_KEY_NAME'] == FBIKey_Weapon1:
                        weapon1Snowflake = weaponTDF[0]['_SNOWFLAKE']
                        self.printredkeypurplevalue('║ Detected Weapon1 Snowflake: ', weapon1Snowflake)
                    elif weaponTDF[0]['_OBJECT_KEY_NAME'] == FBIKey_Weapon2:
                        weapon1Snowflake = weaponTDF[0]['_SNOWFLAKE']
                        self.printredkeypurplevalue('║ Detected Weapon2 Snowflake: ', weapon1Snowflake)
                    elif weaponTDF[0]['_OBJECT_KEY_NAME'] == FBIKey_Weapon3:
                        weapon1Snowflake = weaponTDF[0]['_SNOWFLAKE']
                        self.printredkeypurplevalue('║ Detected Weapon2 Snowflake: ', weapon1Snowflake)

                    weapon3doPath = path_without_fbi + '/objects3d/' + weaponTDF[0]['model'] + '.3do'
                    self.printredkeyyellowvalue('║ Weapon Model Expected by TDF: ', weaponTDF[0]['model'])
                    self.printredkeybluevalue('║ Weapon Model Path: ', weapon3doPath)

                    self.printredkeyyellowvalue('║ Explosion GAF: ', weaponTDF[0]['explosiongaf'])
                    self.printredkeyyellowvalue('║ Lava GAF: ', weaponTDF[0]['lavaexplosiongaf'])
                    self.printredkeyyellowvalue('║ Water GAF: ', weaponTDF[0]['waterexplosiongaf'])

                    # CHECK FOR 3RD PARTY GAFs:
                    xplosion_ = path_without_fbi + '/anims/' + weaponTDF[0]['explosiongaf'] + '.gaf'
                    xplosion_water = path_without_fbi + '/anims/' + weaponTDF[0]['waterexplosiongaf'] + '.gaf'
                    xplosion_lava = path_without_fbi + '/anims/' + weaponTDF[0]['lavaexplosiongaf'] + '.gaf'

                    if os.path.exists(xplosion_):
                        weaponGafs.append(xplosion_)
                        self.printredkeygreenvalue('║ 3rd Party GAF detected: ', xplosion_)

                    if os.path.exists(xplosion_water):
                        weaponGafs.append(xplosion_water)
                        self.printredkeygreenvalue('║ 3rd Party GAF detected: ', xplosion_water)

                    if os.path.exists(xplosion_lava):
                        weaponGafs.append(xplosion_lava)
                        self.printredkeygreenvalue('║ 3rd Party GAF detected: ', xplosion_lava)

                    modelExists = False
                    if os.path.exists(weapon3doPath) == True:
                        modelExists = True
                        weapon3doWrapper = {}
                        weapon3doWrapper['path'] = weapon3doPath
                        weapon3DOFilePaths.append(weapon3doWrapper)
                        self.printredkeygreenvalue('║ Model File Detected: ', ' SUCCESS ' + weaponTDF[0]['name'] + ' verified.')
                    else:
                        self.printredkeyyellowvalue('║ Model File Detected: ', ' NOT FOUND: ' + weapon3doPath)

                    if modelExists == True:
                        self.printredkeybluevalue('║ ', weapon3doPath + ' Saved Successfully.')
                    else:
                        self.printredkeypurplevalue('║ Warning: ', ' 3do file not found: ' + weaponTDF[0]['model'])
                        self.printredkeypurplevalue('║ ', 'If this is a CaveDog model, this warning can be ignored.')
                except Exception as inst:
                    self.printredkeyyellowvalue('║ FATAL ERROR: ', ' Failed to fetch WeaponTDF from SQL.')
                    self.printorange(inst)

            weapon1FromSQL = WeaponTDF.objects.filter(_OBJECT_KEY_NAME__icontains=FBIKey_Weapon1)
            weapon2FromSQL = WeaponTDF.objects.filter(_OBJECT_KEY_NAME__icontains=FBIKey_Weapon2)
            weapon3FromSQL = WeaponTDF.objects.filter(_OBJECT_KEY_NAME__icontains=FBIKey_Weapon3)
            self.printBOOL('║ Is Weapon1 in SQL? ', (len(weapon1FromSQL) > 0))
            # Grab all sound effect keys from Weapon1:
            # self.printredkeygreenvalue('║ soundhit \t-> \t', weapon1FromSQL[0].soundhit)
            # self.printredkeygreenvalue('║ soundstart \t-> \t', weapon1FromSQL[0].soundstart)
            # self.printredkeygreenvalue('║ soundtrigger \t-> \t', weapon1FromSQL[0].soundtrigger)
            # self.printredkeygreenvalue('║ soundwater \t-> \t', weapon1FromSQL[0].soundwater)
            if FBIKey_Weapon2 != ej_notfound2:
                self.printBOOL('║ Is Weapon2 in SQL? ', (len(weapon2FromSQL) > 0))
                # if len(weapon2FromSQL) > 0:
                # Grab all sound effect keys from Weapon2:
                # self.printredkeygreenvalue('║ soundhit \t-> \t', weapon2FromSQL[0].soundhit)
                # self.printredkeygreenvalue('║ soundstart \t-> \t', weapon2FromSQL[0].soundstart)
                # self.printredkeygreenvalue('║ soundtrigger \t-> \t', weapon2FromSQL[0].soundtrigger)
                # self.printredkeygreenvalue('║ soundwater \t-> \t', weapon2FromSQL[0].soundwater)
            if FBIKey_Weapon3 != ej_notfound2:
                self.printBOOL('║ Is Weapon3 in SQL? ', (len(weapon3FromSQL) > 0))
                # if len(weapon3FromSQL) > 0:
                # Grab all sound effect keys from Weapon2:
                # self.printredkeygreenvalue('║ soundhit \t-> \t', weapon3FromSQL[0].soundhit)
                # self.printredkeygreenvalue('║ soundstart \t-> \t', weapon3FromSQL[0].soundstart)
                # self.printredkeygreenvalue('║ soundtrigger \t-> \t', weapon3FromSQL[0].soundtrigger)
                # self.printredkeygreenvalue('║ soundwater \t-> \t', weapon3FromSQL[0].soundwater)
        self.printred('╚════════════════════════════════════════════════════════════════')

        # Sound Evaluation:
        self.printorange('\n╔══[' + emoj3 + ' ] - Sound evaluation.════')
        sounds_path = path_without_fbi + '/sounds/'
        sounds_dir_exists = os.path.exists(sounds_path)
        allsoundfiles = []
        if sounds_dir_exists == True:
            allsoundfiles = os.listdir(sounds_path)

        cavedogsoundspath = 'static/cavedog_sfx/'

        finalizedSoundPaths = []

        if len(weapon1FromSQL) > 0:
            # Grab all sound effect keys from Weapon1:
            self.printyellowkeygreenvalue('║ Weapon1: ', weapon1FromSQL[0]._OBJECT_KEY_NAME)
            self.printyellowkeybluevalue('║  soundhit \t-> \t', weapon1FromSQL[0].soundhit)
            self.printyellowkeybluevalue('║  soundstart \t-> \t', weapon1FromSQL[0].soundstart)
            self.printyellowkeybluevalue('║  soundtrigger \t-> \t', weapon1FromSQL[0].soundtrigger)
            self.printyellowkeybluevalue('║  soundwater \t-> \t', weapon1FromSQL[0].soundwater)

            sfx1_key = ' N/A '
            sfx2_key = ' N/A '
            sfx3_key = ' N/A '
            sfx4_key = ' N/A '

            if weapon1FromSQL[0].soundhit != None:
                sfx1_key = str(weapon1FromSQL[0].soundhit).replace('.wav', '')
            if weapon1FromSQL[0].soundstart != None:
                sfx2_key = str(weapon1FromSQL[0].soundstart).replace('.wav', '')
            if weapon1FromSQL[0].soundtrigger != None:
                sfx3_key = str(weapon1FromSQL[0].soundtrigger).replace('.wav', '')
            if weapon1FromSQL[0].soundwater != None:
                sfx4_key = str(weapon1FromSQL[0].soundwater).replace('.wav', '')
            sfx1 = SoundSetTDF.objects.filter(_OBJECT_KEY_NAME=sfx1_key)
            sfx2 = SoundSetTDF.objects.filter(_OBJECT_KEY_NAME=sfx2_key)
            sfx3 = SoundSetTDF.objects.filter(_OBJECT_KEY_NAME=sfx3_key)
            sfx4 = SoundSetTDF.objects.filter(_OBJECT_KEY_NAME=sfx4_key)

            if sfx1_key != None and sfx1_key != ' N/A ':
                if os.path.isfile(cavedogsoundspath + sfx1_key + '.wav') > 0:
                    self.print_yellow_purple_green('║ soundhit -> ', sfx1_key, ' Cavedog Asset')
                else:
                    if (sfx1_key.lower() + '.wav') in allsoundfiles:
                        self.print_yellow_purple_teal('║ soundhit -> ', sfx1_key, ' Third Party')
                        finalizedSoundPaths.append(sounds_path + sfx1_key.lower() + '.wav')
                    else:
                        self.print_yellow_purple_red('║ soundhit -> ', sfx1_key, '  WARNING : .wav file not found')

            if sfx2_key != None and sfx2_key != ' N/A ':
                if os.path.isfile(cavedogsoundspath + sfx2_key + '.wav') > 0:
                    self.print_yellow_purple_green('║ soundstart -> ', sfx2_key, ' Cavedog Asset')
                else:
                    if (sfx2_key.lower() + '.wav') in allsoundfiles:
                        self.print_yellow_purple_teal('║ soundhit -> ', sfx2_key, ' Third Party')
                        finalizedSoundPaths.append(sounds_path + sfx2_key.lower() + '.wav')
                    else:
                        self.print_yellow_purple_red('║ soundhit -> ', sfx2_key, '  WARNING : .wav file not found')

            if sfx3_key != None and sfx3_key != ' N/A ':
                if os.path.isfile(cavedogsoundspath + sfx3_key + '.wav') > 0:
                    self.print_yellow_purple_green('║ soundtrigger -> ', sfx3_key, ' Cavedog Asset')
                else:
                    if (sfx3_key.lower() + '.wav') in allsoundfiles:
                        self.print_yellow_purple_teal('║ soundhit -> ', sfx3_key, ' Third Party')
                        finalizedSoundPaths.append(sounds_path + sfx3_key.lower() + '.wav')
                    else:
                        self.print_yellow_purple_red('║ soundhit -> ', sfx3_key, '  WARNING : .wav file not found')

            if sfx4_key != None and sfx4_key != ' N/A ':
                if os.path.isfile(cavedogsoundspath + sfx4_key + '.wav') > 0:
                    self.print_yellow_purple_green('║ soundwater -> ', sfx4_key, ' Cavedog Asset')
                else:
                    if (sfx4_key.lower() + '.wav') in allsoundfiles:
                        self.print_yellow_purple_teal('║ soundhit -> ', sfx4_key, ' Third Party')
                        finalizedSoundPaths.append(sounds_path + sfx4_key.lower() + '.wav')
                    else:
                        self.print_yellow_purple_red('║ soundhit -> ', sfx4_key, '  WARNING : .wav file not found')

        if len(weapon2FromSQL) > 0:
            # Grab all sound effect keys from Weapon2:
            self.printyellowkeygreenvalue('║ Weapon2: ', weapon2FromSQL[0]._OBJECT_KEY_NAME)
            self.printyellowkeybluevalue('║  soundhit \t-> \t', weapon2FromSQL[0].soundhit)
            self.printyellowkeybluevalue('║  soundstart \t-> \t', weapon2FromSQL[0].soundstart)
            self.printyellowkeybluevalue('║  soundtrigger \t-> \t', weapon2FromSQL[0].soundtrigger)
            self.printyellowkeybluevalue('║  soundwater \t-> \t', weapon2FromSQL[0].soundwater)

        if len(weapon3FromSQL) > 0:
            # Grab all sound effect keys from Weapon3:
            self.printyellowkeygreenvalue('║ Weapon3: ', weapon3FromSQL[0]._OBJECT_KEY_NAME)
            self.printyellowkeybluevalue('║  soundhit \t-> \t', weapon3FromSQL[0].soundhit)
            self.printyellowkeybluevalue('║  soundstart \t-> \t', weapon3FromSQL[0].soundstart)
            self.printyellowkeybluevalue('║  soundtrigger \t-> \t', weapon3FromSQL[0].soundtrigger)
            self.printyellowkeybluevalue('║  soundwater \t-> \t', weapon3FromSQL[0].soundwater)

        self.printyellow_orange_teal('║ all sound files', ' -> ', allsoundfiles)
        self.printorange('╚════════════════════════════════════════════════════════════════')

        # Corpse Evaluation:
        if FBIKey_Corpse == ej_notfound2:
            self.printgreen('\n╔══[' + emoj2 + ' ] - No corpse can be found, must scan all corpses avaliable.════')
        elif FBIKey_Corpse == ej_none:
            self.printgreen('\n╔══[' + emoj2 + ' ] - This unit appears to have no corpse.════')
        else:
            # CORPSE FEATURE PATH DETECTOR:
            self.printgreen('\n╔══[' + emoj2 + ' ] - Corpse evaluation.════')
            corpsename = fbiUnitClone.Corpse.lower()
            unit_corpse_path = path_without_fbi + '/features/corpses/' + corpsename + '.tdf'
            corpse_3do_path = path_without_fbi + '/objects3d/' + corpsename + '.3do'
            dp_corpsemodel = os.path.exists(corpse_3do_path)
            dp_corpses = os.path.exists(unit_corpse_path)
            if dp_corpses == True:
                SYSPATH_TDCrpse = unit_corpse_path
            if dp_corpsemodel == True:
                SYSPATH_3DCrpse = corpse_3do_path
            self.printBOOL('║ dp_corpses', dp_corpses)
        self.printgreen('╚════════════════════════════════════════════════════════════════')

        # Final Conclusion Evaluation
        self.printblue('\n╔══[' + emoj1 + ' ] - Final Evaluation.════')

        # SYSPATH_unitpic
        # SYSPATH_3DModel
        # SYSPATH_animGAF
        # SYSPATH_scriCOB
        # SYSPATH_3DCrpse
        # SYSPATH_TDCrpse

        # dp_unitpic
        # dp_3dmodel
        # dp_script
        # dp_corpses
        # dp_download
        # dp_animation


        self.printbluekeypurplevalue('║ SYSPATH_unitpic -> ',
                                     SYSPATH_unitpic.replace('/usr/src/persistent/media/ta_data', ''))
        self.printbluekeypurplevalue('║ SYSPATH_3DModel -> ',
                                     SYSPATH_3DModel.replace('/usr/src/persistent/media/ta_data', ''))
        self.printbluekeypurplevalue('║ SYSPATH_animGAF -> ',
                                     SYSPATH_animGAF.replace('/usr/src/persistent/media/ta_data', ''))
        self.printbluekeypurplevalue('║ SYSPATH_scriCOB -> ',
                                     SYSPATH_scriCOB.replace('/usr/src/persistent/media/ta_data', ''))
        self.printbluekeypurplevalue('║ SYSPATH_3DCrpse -> ',
                                     SYSPATH_3DCrpse.replace('/usr/src/persistent/media/ta_data', ''))
        self.printbluekeypurplevalue('║ SYSPATH_TDCrpse -> ',
                                     SYSPATH_TDCrpse.replace('/usr/src/persistent/media/ta_data', ''))

        for sound in finalizedSoundPaths:
            self.printbluekeypurplevalue('║ SYSPATH_WAVfile -> ',
                                         sound.replace('/usr/src/persistent/media/ta_data', ''))

        # self.printbluekeyredvalue('║ ', ' -> ')
        # self.printbluekeyyellowvalue('║ ', ' -> ')
        # self.printbluekeygreenvalue('║ ', ' -> ')

        self.printblue('║')
        self.printbluekeyyellowvalue('║ ', 'Preparing To Generate A New LazarusModAsset... ')
        self.printblue('║')

        if dp_unitpic == True:
            self.printbluekeygreenvalue('║ Unit Picture Dependency', '[ ✓ ]')
        else:
            self.printbluekeyredvalue('║ Unit Picture Dependency', '[ ✕ ]')

        if dp_3dmodel == True:
            self.printbluekeygreenvalue('║ Unit 3D Model Dependency', '[ ✓ ]')
        else:
            self.printbluekeyredvalue('║ Unit 3D Model Dependency', '[ ✕ ]')

        if dp_script == True:
            self.printbluekeygreenvalue('║ Unit Script Dependency', '[ ✓ ]')
        else:
            self.printbluekeyredvalue('║ Unit Script Dependency', '[ ✕ ]')

        if dp_corpses == True:
            self.printbluekeygreenvalue('║ Unit Corpse Dependency', '[ ✓ ]')
        else:
            self.printbluekeyyellowvalue('║ Unit Corpse Dependency', '[ ! ]')

        if dp_download == True:
            self.printbluekeygreenvalue('║ Unit Download Dependency', '[ ✓ ]')
        else:
            self.printbluekeyyellowvalue('║ Download TDF Not Found', '[ ! ]')
            self.printbluekeyyellowvalue('║ This wont crash the game, but you may not be able to construct this unit.', '')

        if dp_animation == True:
            self.printbluekeygreenvalue('║ Unit Animation Dependency', '[ ✓ ]')
        else:
            self.printbluekeyyellowvalue('║ Unit Animation Dependency', '[ ! ]')

        mod_asset_has_all_dependencies = False

        self.printblue('║')
        # dp_animation == True and dp_download == True and dp_corpses == True
        if dp_script == True and dp_3dmodel == True and dp_unitpic == True:
            mod_asset_has_all_dependencies = True
            self.printbluekeygreenvalue('║ LazarusModAsset Dependencies Scanned & Verified ', 'SUCCESS')
            self.printblue('║')
            self.printblue(
                '║ Creating a new LazarusModAsset <b style="color: #79ff9d">' + uname + '</b> for public distribution... ')
        else:
            self.printbluekeyredvalue('║ LazarusModAsset Dependencies Scanned & Verified ', 'FAILED')
            self.printblue('║')
            self.printbluekeyyellowvalue('║ ',
                                         ' This Total Annihilation UFO/HPI file has missing dependencies, aborting mod asset generation. ')

        self.printblue('╚════════════════════════════════════════════════════════════════')

        if mod_asset_has_all_dependencies == True:
            PNG_filename = uname + '.png'
            unit_pic_path = path_without_fbi + '/unitpics/'
            unitIllustration = unit_pic_path + PNG_filename
            png_unitpic_exists = os.path.exists(unitIllustration)
            if png_unitpic_exists == True:
                newLazarusModAsset.image_thumbnail = unitIllustration
            else:
                newLazarusModAsset.image_thumbnail = '/static/assets/images/logos/ARM_logo.png'
            newLazarusModAsset.save()

            # SYSPATH_3DModel 2
            # SYSPATH_animGAF 3
            # SYSPATH_scriCOB 4
            # SYSPATH_3DCrpse 5
            # SYSPATH_TDCrpse 6

            # Save Asset for Public use:
            publicAsset = LazarusPublicAsset()
            publicAsset.user_uploader = jawn_user
            publicAsset.side = fbiUnitClone.Side
            publicAsset.name = fbiUnitClone.Name
            publicAsset.tags = fbiUnitClone.Category
            publicAsset.description = fbiUnitClone.Description
            publicAsset.unitpic = fbiUnitClone._raw_json_dump
            publicAsset.size = str(fbiUnitClone.FootprintX) + 'x' + str(fbiUnitClone.FootprintZ)
            publicAsset.energyCost = fbiUnitClone.BuildCostEnergy
            publicAsset.metalCost = fbiUnitClone.BuildCostMetal
            publicAsset.fbiSnowflake = fbiUnitClone._SNOWFLAKE
            publicAsset.HP = fbiUnitClone.MaxDamage
            encPath = fbiUnitClone._UPLOAD_DESIGNATION.replace('/usr/src/persistent/', '')
            publicAsset.encoded_path = encPath.replace('/', '_SLSH_') + '_SLSH_units_SLSH_' + fbiUnitClone.UnitName.lower()
            publicAsset.save()
            print('PUBLIC ASSET SAVED:')
            print(publicAsset.id)

            newDependency1 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                  type='unitpic',
                                                  system_path=SYSPATH_unitpic,
                                                  model_id=fbiUnitClone.id,
                                                  model_schema='file.pcx',
                                                  asset_id=newLazarusModAsset.id)
            newDependency1.save()
            self.printyellow_orange_teal('Saved: ', 'unitpic', fbiUnitClone.Name)
            newDependency2 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                  type='objects3d',
                                                  system_path=SYSPATH_3DModel,
                                                  model_id=fbiUnitClone.id,
                                                  model_schema='file.3do',
                                                  asset_id=newLazarusModAsset.id)
            newDependency2.save()

            self.printyellow_orange_teal('Saved: ', 'objects3d (unit)', fbiUnitClone.Name)
            newDependency3 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                  type='anims',
                                                  system_path=SYSPATH_animGAF,
                                                  model_id=fbiUnitClone.id,
                                                  model_schema='file.gaf',
                                                  asset_id=newLazarusModAsset.id)
            newDependency3.save()
            self.printyellow_orange_teal('Saved: ', 'unitpic', fbiUnitClone.Name)

            for gaf in weaponGafs:
                newDependencyGaf = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                        type='anims',
                                                        system_path=gaf,
                                                        model_id=fbiUnitClone.id,
                                                        model_schema='file.gaf',
                                                        asset_id=newLazarusModAsset.id)
                newDependencyGaf.save()
                self.printyellow_orange_teal('Saved: ', 'GAF (weapon): ', gaf)

            for weapon3DO in weapon3DOFilePaths:
                newDependencyWeapon = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id) + '-Weapon',
                                                           type='objects3d',
                                                           system_path=weapon3DO['path'],
                                                           model_id=fbiUnitClone.id,
                                                           model_schema='file.3do',
                                                           asset_id=newLazarusModAsset.id)
                newDependencyWeapon.save()
                self.printyellow_orange_teal('Saved: ', 'objects3d (weapon)', fbiUnitClone.Name)

            self.printyellow_orange_teal('Saved: ', 'anims', fbiUnitClone.Name)
            newDependency4 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                  type='scripts',
                                                  system_path=SYSPATH_scriCOB,
                                                  model_id=fbiUnitClone.id,
                                                  model_schema='file.cob',
                                                  asset_id=newLazarusModAsset.id)
            newDependency4.save()
            self.printyellow_orange_teal('Saved: ', 'scripts', fbiUnitClone.Name)
            newDependency5 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                  type='objects3d.corpse',
                                                  system_path=SYSPATH_3DCrpse,
                                                  model_id=fbiUnitClone.id,
                                                  model_schema='file.3do',
                                                  asset_id=newLazarusModAsset.id)
            newDependency5.save()
            self.printyellow_orange_teal('Saved: ', 'objects3d.corpse', fbiUnitClone.Name)
            if os.path.isfile(SYSPATH_TDCrpse):
                print('SYSPATH_TDCrpse: ' + SYSPATH_TDCrpse)

                corpse = FeatureTDFFetch().get(SYSPATH_TDCrpse, fbiUnitClone.Corpse)
                newDependency6 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                      type='corpse_TDF',
                                                      system_path=SYSPATH_TDCrpse,
                                                      model_id=corpse[0].id,
                                                      model_schema='FeatureTDF',
                                                      asset_id=newLazarusModAsset.id)
                newDependency6.save()
                self.printyellow_orange_teal('Saved: ', 'corpse_TDF', corpse[0].id)
            try:
                ## NOT VERY EFFICIENT HACK FOR GRABING THE DOWNLOAD TDF FROM SQL:
                tdfs = DownloadTDF.objects.filter(_DEV_root_data_path=unit_download_path)
                for tdf in tdfs:
                    str_meta = 'entry=' + tdf.MENUENTRY + '|'
                    str_meta += 'menu=' + str(tdf.MENU) + '|'
                    str_meta += 'button=' + str(tdf.BUTTON)
                    newDependencyX = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                          type=tdf.UNITMENU + ' -> ' + tdf.UNITNAME,
                                                          system_path=unit_download_path,
                                                          model_id=tdf.id,
                                                          model_schema='DownloadTDF',
                                                          meta_data=str_meta,
                                                          asset_id=newLazarusModAsset.id)
                    newDependencyX.save()
                    self.print_yellow_purple_teal('Saved: ', 'DownloadTDF', fbiUnitClone.Name)
            except:
                self.print_yellow_purple_red('Failed To Save: ', 'DownloadTDF', fbiUnitClone.Name)
                pass

            try:
                newDependency8 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                      type='weapon1_TDF',
                                                      system_path=path_without_fbi + '/weapons/' + allWeaponTDFFiles[0],
                                                      model_id=weapon1FromSQL[0].id,
                                                      model_schema='WeaponTDF',
                                                      asset_id=newLazarusModAsset.id)
                newDependency8.save()
                self.print_yellow_purple_green('Saved: ', 'WeaponTDF', weapon1FromSQL[0].name)
            except:
                pass
            try:
                newDependency9 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                      type='weapon2_TDF',
                                                      system_path=path_without_fbi + '/weapons/' + allWeaponTDFFiles[0],
                                                      model_id=weapon2FromSQL[0].id,
                                                      model_schema='WeaponTDF',
                                                      asset_id=newLazarusModAsset.id)
                newDependency9.save()
                self.print_yellow_purple_green('Saved: ', 'WeaponTDF', weapon2FromSQL[0].name)
            except:
                pass
            try:
                newDependency10 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                       type='weapon3_TDF',
                                                       system_path=path_without_fbi + '/weapons/' + allWeaponTDFFiles[0],
                                                       model_id=weapon3FromSQL[0].id,
                                                       model_schema='WeaponTDF',
                                                       asset_id=newLazarusModAsset.id)
                newDependency10.save()
                self.print_yellow_purple_green('Saved: ', 'WeaponTDF', weapon3FromSQL[0].name)
            except:
                pass

            newDependency11 = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                   type='unit_FBI',
                                                   system_path=dev_root_path,
                                                   model_id=fbiUnitClone.id,
                                                   model_schema='UnitFbiData',
                                                   asset_id=newLazarusModAsset.id)
            newDependency11.save()
            self.printredkeybluevalue('Saved UnitFbiData: ', fbiUnitClone.UnitName)

            for sound in finalizedSoundPaths:
                newSoundDp = LazarusModDependency(name=uid + '_' + str(fbiUnitClone.id),
                                                  type='sound_WAV',
                                                  system_path=sound,
                                                  model_id=-1,
                                                  model_schema='n/a',
                                                  asset_id=newLazarusModAsset.id)
                newSoundDp.save()
                self.printredkeygreenvalue('Saved .WAV File: ', sound)





        # ║╚╔╗╝

        # print(self.txtOutput)

        return HttpResponse(self.txtOutput)


class proccessWholeHPIToSQL(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        # 'SOUND',
        # modname = request.GET['modname']
        view_header = '<div style="background-color: #282828">'
        output = [view_header]

        unitFbiPath = '/usr/src/persistent/media/ta_data/armspiderpack_2012/units/armspdr.fbi'
        unitTdfPath_weapon = '/usr/src/persistent/media/ta_data/armspiderpack_2012/weapons/armspdrk_weapon.tdf'
        unitTdfPath_download = '/usr/src/persistent/media/ta_data/armspiderpack_2012/download/armspdr.tdf'
        unitTdfPath_corpse = '/usr/src/persistent/media/ta_data/armspiderpack_2012/features/corpses/armspdr_dead.tdf'

        fbi_file = codecs.open(unitFbiPath)
        fbi_str = '<p style="color: cyan">' + fbi_file.read() + '</p>'
        output.append(fbi_str)
        view_footer = '</div>'
        output.append(view_footer)
        final_output = ''
        for item in output:
            final_output += item

        return HttpResponse(final_output)
