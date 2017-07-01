from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair, printKeyValuePair1, printKeyValuePair2, printError, printWarning, printInfo, printLog, printDebug

# For listing units:
from os import walk
import os
from PIL import Image

import time


# Create your views here.
def getUnitFbiUsingId(request):
    printKeyValuePair('hello', 'what the fuck?')
    try:
        mod_name = str(request.GET['mod_name'])
        unit_id = str(request.GET['unit_id'])
        unit_path = '/usr/src/app/static/' + mod_name + '/units/' + unit_id + '.fbi'
        print('unit path: ')
        print(unit_path)
        unitsArray = readFile(unit_path)
        for unit in unitsArray:
            printKeyValuePair('name', unit.Name)
        json_response = {
            "raw_fbi_file": "...." #unitsArray
        }
        print('wtf dude...')
        return Response(json_response)
    except:
        printKeyValuePair('shit', 'is fucked up nigga.')
        json_response = {
            "raw_fbi_file": "...."
        }
        return Response(json_response)


class UnitFbiData(APIView):  # cat cpuinfo
    def get(self, request, format=None):
        printKeyValuePair('views.py','38')
        try:
            printDebug('GET - UnitFbiData', 'entry of try')
            mod_name = str(request.GET['mod_name'])
            printInfo('got "mod_name" GET property')
            unit_id = str(request.GET['unit_id'])
            printInfo('got "unit_id" GET property')
            unit_path = '/usr/src/app/static/' + mod_name + '/units/' + unit_id + '.fbi'

            printLog('unit path: ')
            printInfo(unit_path)

            unitsArray = readFile(unit_path)
            for unit in unitsArray:
                printWarning('OKAY! looping through units array:')
                printKeyValuePair('name', unit)
                printDebug(unit, 'UnitFbiData')

            printLog('finished looping through units array.')
            printInfo('GOING TO JSON DUMPS UNITS ARRAY: ')
            printLog(str(unitsArray))
            printDebug('Unit FBI Data Extracted Successfully! ', 'it always crashed here...')
            return Response(unitsArray)
        except:
            printDebug('GET - UnitFbiData', 'entry of try')
            mod_name = str(request.GET['mod_name'])
            printInfo('got "mod_name" GET property')
            unit_id = str(request.GET['unit_id'])
            printInfo('got "unit_id" GET property')
            unit_path = '/usr/src/app/static/' + mod_name + '/units/' + unit_id + '.FBI'
            printLog('unit path: ')
            printInfo(unit_path)
            unitsArray = readFile(unit_path)
            for unit in unitsArray:
                printWarning('OKAY! looping through units array:')
                printKeyValuePair('name', unit)
                printDebug(unit, 'UnitFbiData')
            printLog('finished looping through units array.')
            printInfo('GOING TO JSON DUMPS UNITS ARRAY: ')
            printLog(str(unitsArray))
            printDebug('Unit FBI Data Extracted Successfully! ', 'it always crashed here...')
            return Response(unitsArray)


class ApiNavigationUrls(APIView):
    def get(self, request, format=None):
        json_response = {
            "list_units_for_mod1": "http://52.27.28.55/LazarusII/LazarusListUnits/?mod_name=totala_files",
            "list_units_for_mod2": "http://52.27.28.55/LazarusII/LazarusListUnits/?mod_name=totala_files2",
            "get 'arach' from mod named: totala_files2": "http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=totala_files2&unit_id=arach",
            "custom toast": "http://52.27.28.55/LazarusII/CustomToast/?msg=hello_world",
            "Execute Bash": "http://52.27.28.55/LazarusII/ExecuteBash/?cmd=ls",
        }
        return Response(json_response)


class CustomToastGenerator(APIView):
    def get(self, request, format=None):
        msg = str(request.GET['msg'])
        html = '<md-toast><span class="md-toast-text" flex>' + msg + '</span><md-button class="md-highlight" ng-click="openMoreInfo($event)">More info</md-button><md-button ng-click="closeToast()">Close</md-button></md-toast>'
        return HttpResponse(html)

import subprocess

class ExecuteBash(APIView):

    def get(self, request, format=None):
        cmd = request.GET['cmd']
        result = 'nan'
        final_obj = {}
        if cmd == 'ls':
            result0 = str(subprocess.check_output(['pwd', '.']))
            result1 = str(subprocess.check_output(['ls', 'static/totala_files2']))
            final_obj[str(result0)] = str(result1).split('\\n')
            result2 = str(subprocess.check_output(['ls', 'static/totala_files2/units']))
            final_obj[result0+'static'] = str(result2).split('\\n')
        elif cmd == 'rename_dir':
            # find . -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;
            mod_name = request.GET['cmd']
            rename_files = "find " + mod_name + " -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;"
            os.system(rename_files)
            final_obj['result'] = mod_name + ' should have been set to lower case.'

        context = {'result': final_obj}
        return Response(context)

class LazarusListUnitsOld(APIView):
    f = []
    d = []
    output_final = open('workfile', 'w')
    root = ''
    step = 0

    def __init__(self):
        print(bcolors.cyan + 'Initializing LazarusListUnits' + bcolors.ENDC)
        self.f = []
        self.d = []
        self.output_final = open('workfile', 'w')
        self.jsonResponse = []
        self.root = '/usr/src/app/static/totala_files2/'


    def printSubContents(self, pathName, mod_name):
        #jsonResponse = []
        printInfo(pathName)
        printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
        self.step = self.step + 1
        for (dirpath, dirnames, filenames) in walk(self.root + pathName):
            # printLog(dirnames)
            # printDebug(filenames, self.root)
            printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
            self.step = self.step + 1
            print('DOING SOMETHING IMPORTANT HERE: ')
            printInfo('dirpath : ' + dirpath)
            printLog('dirnames : ' + dirpath)
            printKeyValuePair('filenames : ', filenames)
            printDebug(self.root, 'pathName: ' + pathName)

            if pathName == 'unitpics':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)
                    printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
                    self.step = self.step + 1
            # print(file_extension + "     :     " + filename)
                    #print(self.root + pathName + '/' + file)
                    #print( file_extension.lower())
                    pathToFile = self.root + pathName + '/' + file
                #if file_extension.lower() == '.pcx':
                    try:
                        img = Image.open(pathToFile)
                        imgSaveTo = self.root + pathName + '/' + filename + '.png'
                        img.save(imgSaveTo, format='png')
                        self.jsonResponse.append(
                            {
                                'thumbnail': '/static/' + mod_name + '/unitpics/' + filename + '.png',
                                'object_name': filename,
                                'system_location': imgSaveTo,
                                'fbi_file': '/static/' + mod_name + '/units/' + filename + '.fbi',
                                'RESTful_unit_data': 'http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=' + mod_name + '&unit_id=' + filename
                            }
                        )
                    except:
                        printError('failed to open ' + str(filename) + ' [' + str(file_extension) + ']')

        printKeyValuePair2(bcolors.purple + 'Path: ' + bcolors.ENDC, bcolors.FAIL + dirpath + bcolors.ENDC)
        #print(self.jsonResponse)
        return self.jsonResponse

    def printContents(self, mod_path, mod_name):
        jsonFinal = []
        printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
        self.step = self.step + 1
        for (dirpath, dirnames, filenames) in walk(mod_path):
            self.f.extend(filenames)
            self.d.extend(dirnames)
            print('PRINTING CONTENTS SON: ')
            printInfo('dirpath : ' + dirpath)
            printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
            self.step = self.step + 1
            for path in dirnames:
                printKeyValuePair1('path', path)
                printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
                self.step = self.step + 1
                self.printSubContents(path, mod_name)
            break


    def getUnitInfo(self, unitId):
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


    def get(self, request, format=None):
        print(bcolors.lightred + 'GET request: ' + bcolors.ENDC)
        print(bcolors.purple + str(request.GET) + bcolors.ENDC)

        printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
        self.step = self.step + 1
        # read GET param 'test' if it exists:
        # try:
        #     print(bcolors.blue + 'test = ' + bcolors.ENDC + bcolors.lightgreen + str(request.GET['test']) + bcolors.ENDC)
        # except:
        #     print('......')

        try:
            printKeyValuePair2('⨭   [ ' + str(self.step) + ' ]   ⨮', '✪ STEPPING THROUGH ✪')
            self.step = self.step + 1
            printKeyValuePair('Mod Name', str(request.GET['mod_name']))
            mod_path = '/usr/src/app/static/' + str(request.GET['mod_name']) + '/'
            mod_name = str(request.GET['mod_name'])
            self.printContents(mod_path, mod_name)
            final_response = {'arm_data': self.jsonResponse}
            return Response(final_response)
        except:
            # printKeyValuePair('Mod Name', str(request.GET['mod_name']))
            # mod_path = '/usr/src/app/static/' + str(request.GET['mod_name']) + '/'
            # mod_name = str(request.GET['mod_name'])
            # self.printContents(mod_path, mod_name)
            # final_response = {'arm_data': self.jsonResponse}
            return Response('oh shit')


class many_colors:
    _97 = '\033[97m'
    _96 = '\033[96m'
    _95 = '\033[95m'
    _94 = '\033[94m'
    _93 = '\033[93m'
    _92 = '\033[92m'
    _91 = '\033[91m'
    _90 = '\033[90m'

    _END = '\033[0m'
    _1 = '\033[1m'
    _2 = '\033[2m'
    _3 = '\033[3m'
    _4 = '\033[4m'
    _5 = '\033[5m'
    _6 = '\033[6m'
    _7 = '\033[7m'
    _8 = '\033[8m'
    _9 = '\033[9m'
    _10 = '\033[10m'

    _11 = '\033[11m'
    _12 = '\033[12m'
    _13 = '\033[13m'
    _14 = '\033[14m'
    _15 = '\033[15m'
    _16 = '\033[16m'
    _17 = '\033[17m'
    _18 = '\033[18m'
    _19 = '\033[19m'

    _21 = '\033[21m'
    _22 = '\033[22m'
    _23 = '\033[23m'
    _24 = '\033[24m'
    _25 = '\033[25m'
    _26 = '\033[26m'
    _27 = '\033[27m'
    _28 = '\033[28m'
    _29 = '\033[29m'

    _30 = '\033[30m'
    _31 = '\033[31m'
    _32 = '\033[32m'
    _33 = '\033[33m'
    _34 = '\033[34m'
    _35 = '\033[35m'
    _36 = '\033[36m'
    _37 = '\033[37m'
    _38 = '\033[38m'
    _39 = '\033[39m'


CCD = {
    0: '\033[0m',  # end

    200: '\033[3m',  # italic
    201: '\033[4m',  # underline
    202: '\033[1m',  # bold
    203: '\033[2m',  # darkish

    108: '\033[7m',  # highlight
    107: '\033[107m',  # oj highlight
    106: '\033[106m',  # cyan highlight
    105: '\033[105m',  # magenta highlight
    104: '\033[104m',  # blue highlight
    103: '\033[103m',  # yellow highlight
    102: '\033[102m',  # green highlight
    101: '\033[101m',  # red highlight
    100: '\033[100m',  # purple highlight

    1: '\033[31m',  # dark red
    2: '\033[32m',  # dark green
    3: '\033[33m',  # dark yellow
    4: '\033[34m',  # dark blue
    5: '\033[35m',  # dark magenta
    6: '\033[36m',  # dark cyan
    7: '\033[37m',  # dark yellow

    10: '\033[90m',  # bright purple
    11: '\033[30m',  # purple
    12: '\033[97m',  # oj
    13: '\033[96m',  # cyan
    14: '\033[95m',  # magenta
    15: '\033[94m',  # blue
    16: '\033[93m',  # yellow
    17: '\033[92m',  # green neon
    18: '\033[91m',  # red
}


class LazarusListUnits(APIView):
    f = []
    d = []
    root = ''
    step = 0

    def printColored(self, text, color_id):
        print(CCD[color_id] + text + CCD[0])

    def printColoredFile(self, filename, ext, color_id1, color_id2):
        print(CCD[color_id1] + filename + CCD[0] + CCD[color_id2] + ext + CCD[0])

    def logCurrentObjectState(self):
        print('')

    def getUnitFbiUsingId(self, unit_id, mod_name):
        printColored('getting unit fbi', 3)
        try:
            unit_path = '/usr/src/app/static/' + mod_name + '/units/' + unit_id + '.fbi'
            printColored('unit path: ', 6)
            printColored(unit_path, 5)
            unitsArray = readFile(unit_path)
            for unit in unitsArray:
                printKeyValuePair('name', unit.Name)
            json_response = {
                "raw_fbi_file": "...."  # unitsArray
            }
            print('wtf dude...')
            return Response(json_response)
        except:
            printKeyValuePair('shit', 'is fucked up nigga.')
            json_response = {
                "raw_fbi_file": "...."
            }
            return Response(json_response)

    def __init__(self):
        self.printColored('Initializing LazarusListUnits', 15)
        self.f = []
        self.d = []
        self.jsonResponse = []
        self.root = '/usr/src/app/static/totala_files2/'
        self.printColored('init completed!', 12)

    def printSubContents(self, pathName, mod_name):
        for (dirpath, dirnames, filenames) in walk(self.root + pathName):
            if pathName.lower() == 'unitpics':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)
                    self.printColoredFile(filename.lower(), file_extension.lower(), 17, 6)
                    pathToFile = self.root + pathName + '/' + file
                    try:
                        img = Image.open(pathToFile)
                        imgSaveTo = self.root + pathName + '/' + filename + '.png'
                        img.save(imgSaveTo, format='png')
                        self.jsonResponse.append(
                            {
                                'thumbnail': '/static/' + mod_name + '/unitpics/' + filename + '.png',
                                'object_name': filename,
                                'system_location': imgSaveTo,
                                'fbi_file': '/static/' + mod_name + '/units/' + filename + '.fbi',
                                'RESTful_unit_data': 'http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=' + mod_name + '&unit_id=' + filename
                            }
                        )
                    except:
                        printError('failed to open ' + str(filename) + ' [' + str(file_extension) + ']')
            elif pathName.lower() == 'units':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)
                    self.printColoredFile(filename.lower(), file_extension.lower(), 18, 6)
            elif pathName.lower() == 'weapons':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)
                    self.printColoredFile(filename.lower(), file_extension.lower(), 10, 6)
        return self.jsonResponse

    def printContents(self, mod_path, mod_name):
        self.printColored('will now loop through this "walk(mod_path)" ' + str(walk(mod_path)), 102)
        for (dirpath, dirnames, filenames) in walk(mod_path):
            self.printColored('self.f before extend: ', 105)
            self.printColored(str(self.f), 15)
            self.f.extend(filenames)
            self.printColored('self.f after extend: ', 102)
            self.printColored(str(self.f), 15)
            self.printColored('self.d before extend: ', 106)
            self.printColored(str(self.d), 16)
            self.d.extend(dirnames)
            self.printColored('self.d after extend: ', 103)
            self.printColored(str(self.d), 16)
            self.printColored(' for (dirpath, dirnames, filenames) ', 101)
            self.printColored(str(dirpath) + ' ' + str(dirnames) + ' ' + str(filenames), 14)
            for path in dirnames:
                self.printColored(str(path), 13)
                self.printSubContents(path, mod_name)
            break


    def getUnitInfo(self, unitId):
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


    def get(self, request, format=None):
        try:
            mod_path = '/usr/src/app/static/' + str(request.GET['mod_name']) + '/'
            mod_name = str(request.GET['mod_name'])
            self.printColored('Will now print the contents of ' + mod_path, 1)
            time.sleep(2)
            self.printContents(mod_path, mod_name)
            final_response = {'arm_data': self.jsonResponse}
            return Response(final_response)
        except:
            return Response('oh shit')

"""
/LazarusII/UnitFbiData/?mod_name=totala_files2&unit_id=arach
"""
