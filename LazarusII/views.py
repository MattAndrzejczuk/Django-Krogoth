from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair, printKeyValuePair1, printKeyValuePair2, printError, printWarning, printInfo, printLog, printDebug

from rest_framework.permissions import IsAuthenticated, AllowAny
import emoji

# For listing units:
from os import walk
import os
from PIL import Image

import time
from LazarusII.FbiData import remove_comments
import re
import datetime
import subprocess

from DatabaseSandbox.models import TotalAnnihilationUploadedFile, LazarusModProjectSB




# Create your views here.
def getUnitFbiUsingId(request):
    printKeyValuePair('hello', 'what the fuck?')
    try:


        mod_name = str(request.GET['mod_name'])
        unit_id = str(request.GET['unit_id'])
        unit_path = '/usr/src/app/static/mods/' + mod_name + '/units/' + unit_id + '.fbi'
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
        # printKeyValuePair('views.py','38')
        try:
            # printDebug('GET - UnitFbiData', 'entry of try')
            mod_name = str(request.GET['mod_name'])
            # printInfo('got "mod_name" GET property')
            unit_id = str(request.GET['unit_id']).lower()
            # printInfo('got "unit_id" GET property')
            unit_path = '/usr/src/app/static/mods/' + mod_name + '/units/' + unit_id + '.fbi'

            try:
                will_show_raw_fbi = str(request.GET['will_show_raw_fbi'])
                fbi_file = open(unit_path, 'r', errors='replace')

                dialog_actions = '<br><br><br><md-button class="md-warn" ng-click="answer(\'close\')">Not Useful</md-button>'

                read_file_str = remove_comments(fbi_file.read())
                if will_show_raw_fbi == 'pretty':
                    read_file_str = read_file_str.replace(';', '; <br>&emsp;')
                    read_file_str = read_file_str.replace('{', '{<br>&emsp;')
                    read_file_str += dialog_actions
                    return HttpResponse(read_file_str)
                else:
                    return HttpResponse(read_file_str)
                # json_response = {'raw_data': fbi_file.read()}


            except:
                unitsArray = readFile(unit_path)
                return Response(unitsArray)
            # for unit in unitsArray:
            #     printWarning('OKAY! looping through units array:')
            #     printKeyValuePair('name', unit)
            #     printDebug(unit, 'UnitFbiData')

            # printLog('finished looping through units array.')
            # printInfo('GOING TO JSON DUMPS UNITS ARRAY: ')
            # printLog(str(unitsArray))
            # printDebug('Unit FBI Data Extracted Successfully! ', 'it always crashed here...')

        except:
            # printDebug('GET - UnitFbiData', 'entry of try')
            # mod_name = str(request.GET['mod_name'])
            # printInfo('got "mod_name" GET property')
            # unit_id = str(request.GET['unit_id'])
            # printInfo('got "unit_id" GET property')
            # unit_path = '/usr/src/app/static/mods/' + mod_name + '/units/' + unit_id + '.FBI'
            # printLog('unit path: ')
            # printInfo(unit_path)
            # unitsArray = readFile(unit_path)
            # for unit in unitsArray:
            #     printWarning('OKAY! looping through units array:')
            #     printKeyValuePair('name', unit)
            #     printDebug(unit, 'UnitFbiData')
            # printLog('finished looping through units array.')
            # printInfo('GOING TO JSON DUMPS UNITS ARRAY: ')
            # printLog(str(unitsArray))
            # printDebug('Unit FBI Data Extracted Successfully! ', 'it always crashed here...')
            return Response('oh shit')

# AutoCollectStatic
class ApiNavigationUrls(APIView):
    def get(self, request, format=None):
        json_response = {
            "list_units_for_mod1": "http://52.27.28.55/LazarusII/LazarusListUnits/?mod_name=totala_files",
            "list_units_for_mod2": "http://52.27.28.55/LazarusII/LazarusListUnits/?mod_name=totala_files2",
            "get 'arach' from mod named: totala_files2": "http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=totala_files2&unit_id=arach",
            "custom toast": "http://52.27.28.55/LazarusII/CustomToast/?msg=hello_world",
            "Execute Bash ls": "http://52.27.28.55/LazarusII/ExecuteBash/?cmd=ls&mod_name=totala_files2&dir=units",
            "Execute Bash rename mods to lowercase": "http://52.27.28.55/LazarusII/ExecuteBash/?cmd=rename_dir&mod_name=totala_files2",
            "AutoCollectStatic": "http://52.27.28.55/LazarusII/AutoCollectStatic/",
        }
        final_json = {}
        final_json['old_stuff'] = json_response

        tdf_data = {
            "coradon_weapon": "http://52.27.28.55/LazarusII/OpenTotalAnnihilationTDFFile/?mod_name=mod_hoverattack&file_name=coradon_weapon&directory_name=weapons",
            "corhunt_weapon": "http://52.27.28.55/LazarusII/OpenTotalAnnihilationTDFFile/?mod_name=totala_files&file_name=corhunt_weapon&directory_name=weapons",
            "corkrog_weapon": "http://52.27.28.55/LazarusII/OpenTotalAnnihilationTDFFile/?mod_name=totala_files&file_name=corkrog_weapon&directory_name=weapons",
            "cormort_weapon": "http://52.27.28.55/LazarusII/OpenTotalAnnihilationTDFFile/?mod_name=totala_files&file_name=cormort_weapon&directory_name=weapons",
            "corsh_weapon": "http://52.27.28.55/LazarusII/OpenTotalAnnihilationTDFFile/?mod_name=totala_files&file_name=corsh_weapon&directory_name=weapons",
            "armmine1_weapon": "http://52.27.28.55/LazarusII/OpenTotalAnnihilationTDFFile/?mod_name=totala_files&file_name=armmine1_weapon&directory_name=weapons",
            "armmine3_weapon": "http://52.27.28.55/LazarusII/OpenTotalAnnihilationTDFFile/?mod_name=totala_files&file_name=armmine3_weapon&directory_name=weapons"
        }

        final_json['TDF_Examples'] = tdf_data

        return Response(final_json)



class UserAgentTracker(APIView):
    def get(self, request, format=None):
        REMOTE_ADDR = str(request.META['REMOTE_ADDR'])
        HTTP_USER_AGENT = str(request.META['HTTP_USER_AGENT'])
        HTTP_ACCEPT_LANGUAGE = str(request.META['HTTP_ACCEPT_LANGUAGE'])
        _date = datetime.date
        _time = datetime.time


        html = '<div>' + \
               '<h1> User Visitor Tracking </h1>' + \
               '<h3> REMOTE_ADDR </h3>' + \
               '<p>' + str(REMOTE_ADDR) + '</p>' + \
               '<h3> HTTP_USER_AGENT </h3>' + \
               '<p>' + str(HTTP_USER_AGENT) + '</p>' + \
               '<h3> HTTP_ACCEPT_LANGUAGE </h3>' + \
               '<p>' + str(HTTP_ACCEPT_LANGUAGE) + '</p>' + \
               '<h4> date </h4>' + \
               '<p>' + str(_date.today()) + '</p>' + \
               '<h5> username </h5>' + \
               '<p>' + str(request.user) + '</p>' + \
               '</div>'
        return HttpResponse(html)


class CustomToastGenerator(APIView):
    def get(self, request, format=None):
        msg = str(request.GET['msg'])
        html = '<md-toast><span class="md-toast-text" flex>' + msg + '</span><md-button class="md-highlight" ng-click="openMoreInfo($event)">More info</md-button><md-button ng-click="closeToast()">Close</md-button></md-toast>'
        return HttpResponse(html)



class ExecuteBash(APIView):
    def get(self, request, format=None):
        cmd = request.GET['cmd']
        result = 'nan'
        key_name = 'nan'
        final_obj = {}
        if cmd == 'ls':
            mod_name = request.GET['mod_name']
            dir = request.GET['dir']
            result0 = str(subprocess.check_output(['pwd', '.'])).replace("b'","").replace("\\n'","/")
            result1 = str(subprocess.check_output(['ls', 'static/mods']))
            final_obj[str(result0)] = str(result1).split('\\n')
            result2 = str(subprocess.check_output(['ls', 'static/mods/' + mod_name + '/' + dir ]))
            key_name = result0+'static/mods/'+mod_name+'/'+dir
            final_obj[key_name] = str(result2).split('\\n')
            final_obj[key_name][0] = final_obj[key_name][0].replace("b'", "")
        elif cmd == 'rename_dir':
            # find . -depth -exec rename 's/(.*)\/([^\/]*)/$1\/\L$2/' {} \;
            result0 = str(subprocess.check_output(['ls', '.'])).replace("b'", "").replace("\\n'", "/")
            mod_name = request.GET['mod_name']
            rename_files_bash = "bash bashRenameStuffToLowerInDirectory.sh " + mod_name
            os.system(rename_files_bash)
            final_obj['info'] = 'bash script executed from ' + result0
            final_obj['result'] = mod_name + ' should have been set to lower case.'

        context = {'result': final_obj}
        return Response(context)



class ExecuteBash_LS_AllCustomModFiles(APIView):
    def get(self, request, format=None):

        final_obj = {}

        # mod_name = request.GET['mod_name']
        directory_str = '/usr/src/persistent/media/ta_data'

        # community mods:
        # /usr/src/persistent/media/ta_data/

        mod_paths = {}
        uploaded_data_files = TotalAnnihilationUploadedFile.objects.all()
        for data_file in uploaded_data_files:
            if os.path.isdir(data_file.system_path):
                ls_current_modpath = str(subprocess.check_output(['ls', data_file.system_path]))

                parsed_1 = ls_current_modpath.replace("\\n'","")
                parsed_2 = parsed_1.replace("b'","")

                mod_paths[data_file.system_path] = parsed_2.split('\\n')
            # mod_paths.append(data_file.system_path)


        result1 = str(subprocess.check_output(['ls', directory_str]))
        final_obj[directory_str] = str(result1).split('\\n')
        final_obj[directory_str][0] = final_obj[directory_str][0].replace("b'", "")

        context = {'result': final_obj, 'mod_paths': mod_paths}
        return Response(context)



class AutoCollectStatic(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        command = 'python3 manage.py collectstatic --no-input'
        os.system(command)
        html = '<div> <h1>Collect Static</h1> <p>should be completed.</p> </div>'
        return HttpResponse(html)



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

import os.path

class ReadUnitFbi:  # cat cpuinfo
    def get(self, mod_name, unit_id):
        # printKeyValuePair('views.py','38')
        # print('')

        # print('')
        try:
            # printInfo('got "unit_id" GET property')
            unit_path = ''
            if os.path.isfile('/usr/src/app/static/mods/' + mod_name + '/units/' + unit_id + '.fbi'):
                unit_path = '/usr/src/app/static/mods/' + mod_name + '/units/' + unit_id + '.fbi'
            else:
                unit_path = '/usr/src/persistent/media/ta_data/' + mod_name + '/units/' + unit_id + '.fbi'
            # printLog('unit path: ')
            # printInfo(unit_path)
            unitsArray = readFile(unit_path)
            # for unit in unitsArray:
            #     printWarning('OKAY! looping through units array:')
            #     printKeyValuePair('name', unit)
            #     printDebug(unit, 'UnitFbiData')

            # printLog('finished looping through units array.')
            # printInfo('GOING TO JSON DUMPS UNITS ARRAY: ')
            # printLog(str(unitsArray))
            # printDebug('Unit FBI Data Extracted Successfully! ', 'it always crashed here...')
            return unitsArray
        except:
            print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
            print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
            print('✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
            print('✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
            print('✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')

            unit_path = '/usr/src/persistent/media/ta_data/' + mod_name + '/units/' + unit_id + '.fbi'
            unitsArray = readFile(unit_path)
            return unitsArray



class OpenTotalAnnihilationFBIFile(APIView):
    def get(self, request, format=None):
        mod_name = str(request.GET['mod_name'])
        print('1 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        file_name = str(request.GET['file_name'])
        print('2 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        directory_name = 'units'
        print('3 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        file_path = '/usr/src/app/static/mods/' + mod_name + '/' + directory_name + '/' + file_name + '.fbi'
        print('4 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        f3 = open(file_path, 'r', errors='replace')

        print('5 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        OBJECT_NAME = 'UNITINFO'

        tdf_without_comments = remove_comments(f3.read().strip().replace('\n', '').replace('\t', ''))

        parsed_0 = tdf_without_comments.replace('[' + OBJECT_NAME + ']', '')
        parsed_1 = parsed_0.replace('', '')
        parsed_2 = parsed_1.replace('[', '"')
        parsed_3 = parsed_2.replace(']', '" :')
        parsed_4 = parsed_3.replace('=', '" : "')
        parsed_5 = parsed_4.replace(';', '", "')
        parsed_6 = parsed_5.replace('{', '{ "')
        parsed_7 = parsed_6.replace(', "}', '}')
        parsed_8 = parsed_7.replace(', ""', ', "')
        total_weapons = [m.start() for m in re.finditer('[' + OBJECT_NAME + ']', tdf_without_comments)]
        parsed_9 = parsed_8.replace('}{', '}, {', len(total_weapons) - 1)
        parsed_10 = '[' + parsed_9 + ']'

        tab_str = '	'
        parsed_11 = parsed_10.replace('\t', '')
        parsed_12 = parsed_11.replace('", "}', '"}')
        print(parsed_12)

        dictionary = json.loads(parsed_12)

        for weapon in dictionary:
            weapon['OBJ_NAME'] = OBJECT_NAME

        return Response(dictionary)



class OpenTotalAnnihilationTDFFile(APIView):

    def get(self, request, format=None):
        mod_name = str(request.GET['mod_name'])
        file_name = str(request.GET['file_name'])
        directory_name = str(request.GET['directory_name'])
        file_path = '/usr/src/app/static/mods/' + mod_name + '/' + directory_name + '/' + file_name + '.tdf'
        f3 = open(file_path, 'r', errors='replace')

        print('5 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        # OBJECT_NAME = 'UNITINFO'

        tdf_without_comments = remove_comments(f3.read().strip().replace('\n', '').replace('\t', ''))

        def parseNested(_tdf, nOBJECT_NAME):
            # nOBJECT_NAME = 'DAMAGE'
            nparsed_0 = _tdf.replace('[' + nOBJECT_NAME + ']', '')
            nparsed_1 = nparsed_0.replace('', '')
            nparsed_2 = nparsed_1.replace('[', '"')
            nparsed_3 = nparsed_2.replace(']', '" :')
            nparsed_4 = nparsed_3.replace('=', '" : "')
            nparsed_5 = nparsed_4.replace(';', '", "')
            nparsed_6 = nparsed_5.replace('{', '{ "')
            nparsed_7 = nparsed_6.replace(', "}', '}')
            nparsed_8 = nparsed_7.replace(', ""', ', "')
            total_weapons = [m.start() for m in re.finditer('[' + nOBJECT_NAME + ']', _tdf)]
            nparsed_9 = nparsed_8.replace('}{', '}, {', len(total_weapons) - 1)
            nparsed_10 = '[' + nparsed_9 + ']'
            tab_str = '	'
            nparsed_11 = nparsed_10.replace('\t', '')
            nparsed_12 = nparsed_11.replace('", "}', '"}')

            _BrkStart = [m.start() for m in re.finditer('\[', _tdf)]
            _BrkEnd = [m.start() for m in re.finditer('\}', _tdf)]
            if len(_BrkStart) == len(_BrkEnd):
                i = 0
                for obj in _BrkStart:
                    obj_name = _tdf[_BrkStart[i]:_BrkEnd[i]]
                    is_nested = (_tdf[_BrkStart[i] - 1:_BrkStart[i] + 1])
                    if is_nested:
                        # print(obj_name)
                        return obj_name
                    i += 1

        def parseBase(_tdf, bOBJECT_NAME):
            # bOBJECT_NAME = 'Hellfire_LASER'
            tdf_without_comments = remove_comments(_tdf)
            parsed_0 = tdf_without_comments.replace('[' + bOBJECT_NAME + ']', '')
            parsed_1 = parsed_0.replace('', '')
            parsed_2 = parsed_1.replace('[', '"')
            parsed_3 = parsed_2.replace(']', '" :')
            parsed_4 = parsed_3.replace('=', '" : "')
            parsed_5 = parsed_4.replace(';', '", "')
            parsed_6 = parsed_5.replace('{', '{ "')
            parsed_7 = parsed_6.replace(', "}', '}')
            parsed_8 = parsed_7.replace(', ""', ', "')
            total_weapons = [m.start() for m in re.finditer('[' + bOBJECT_NAME + ']', _tdf)]
            parsed_9 = parsed_8.replace('}{', '}, {', len(total_weapons) - 1)
            parsed_10 = parsed_9  # '[' + parsed_9 + ']'
            tab_str = '	'
            parsed_11 = parsed_10.replace('\t', '')
            parsed_12 = parsed_11.replace('", "}', '"}')
            return parsed_12

        def getNestedType(_tdf):
            _BrkStart = [m.start() for m in re.finditer('\[', _tdf)]
            _BrkEnd = [m.start() for m in re.finditer('\]', _tdf)]
            if len(_BrkStart) == len(_BrkEnd):
                i = 0
                for obj in _BrkStart:
                    obj_name = _tdf[_BrkStart[i]:_BrkEnd[i]]
                    is_nested = (_tdf[_BrkStart[i] - 1:_BrkStart[i] + 1])
                    if is_nested:
                        # print('...')
                        # print(obj_name.replace('[', ''))
                        return obj_name.replace('[', '')
                    i += 1

        def getBaseType(_tdf):
            _BrkStart = [m.start() for m in re.finditer('\[', _tdf)]
            _BrkEnd = [m.start() for m in re.finditer('\]', _tdf)]
            if len(_BrkStart) == len(_BrkEnd):
                i = 0
                for obj in _BrkStart:
                    obj_name = _tdf[_BrkStart[i]:_BrkEnd[i]]
                    is_nested = (_tdf[_BrkStart[i] - 1:_BrkStart[i] + 1])
                    if is_nested:
                        print('...')
                        print(obj_name.replace('[', ''))
                    return obj_name.replace('[', '')
                    i += 1

        # _ERR = emoji.emojize(' :collision: ', use_aliases=True)
        # _checkForParseErrors = [m.start() for m in re.finditer("\;\}\}\[", tdf_without_comments)]


        # if len(_checkForParseErrors) <= 0:
        #     print(_ERR + _ERR + _ERR + _ERR + _ERR + _ERR + _ERR + _ERR)
        #     print('CRITICAL PARSE ERROR, FAILED TO SPLIT THE PAYLOAD.')
        #     print(_ERR + _ERR + _ERR + _ERR + _ERR + _ERR + _ERR + _ERR)
        #     print(tdf_without_comments)
        #     print(_ERR + _ERR + _ERR + _ERR + _ERR + _ERR + _ERR + _ERR)


        dict_list = []
        _tdf_prep = tdf_without_comments.replace(';}}[', ';}}|[')
        split_tdf = _tdf_prep.split('|')

        print('❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆')
        print(tdf_without_comments)
        print('❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆')


        for item in split_tdf:
            print('☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
            print(item)
            print('☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
            tdf_without_comments1 = remove_comments(item)
            nested_obj = parseNested(tdf_without_comments1.replace('\t', ''), getNestedType(tdf_without_comments1))
            base_obj = parseBase(tdf_without_comments1.replace(nested_obj, ''), getBaseType(tdf_without_comments1))
            dictionary = json.loads(base_obj)
            dictionary[getNestedType(tdf_without_comments1)] = json.loads(
                parseBase(nested_obj, getNestedType(tdf_without_comments1)))
            getBaseType(item)
            dict_list.append(dictionary)

        print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')
        print(json.dumps(dict_list))
        print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')

        return Response(dict_list)


"""
    def get(self, request, format=None):
        mod_name = str(request.GET['mod_name'])
        file_name = str(request.GET['file_name'])
        directory_name = str(request.GET['directory_name'])
        file_path = '/usr/src/app/static/mods/' + mod_name + '/' + directory_name + '/' + file_name + '.tdf'
        f3 = open(file_path, 'r', errors='replace')

        arrayOfDetectedObjects = []

        tdf_without_comments = remove_comments(f3.read())
        # sampleObj1 = '[SMALL_BUILDING]s sddf..d..fsdfdsfdfds [DAMAGE] [HUGE_BUILDING] ....... [SMALL_BUILDING],,, [DAMAGE] '
        _BrkStart = [m.start() for m in re.finditer('\[', tdf_without_comments)]
        _BrkEnd = [m.start() for m in re.finditer('\]', tdf_without_comments)]
        if len(_BrkStart) == len(_BrkEnd):
            i = 0
            for obj in _BrkStart:
                obj_name = tdf_without_comments[_BrkStart[i]:_BrkEnd[i]]
                if 'DAMAGE' != obj_name:
                    arrayOfDetectedObjects.append(obj_name)
                    print(obj_name)
                i += 1



        # TODO: must parse multiple OBJECT_NAME from file before we begin doing anything.
        OBJECT_NAME = 'UNITINFO'
        weapon_parse_helper = 'DAMAGE'

        parsed_0 = tdf_without_comments

        # for detectedObject in arrayOfDetectedObjects:
        #     print('⦿ ⦿ ⦿ ⦿ ⦿ ⦿ ⦿ ⦿')
        #     print(detectedObject)
        #     print('⦿ ⦿ ⦿ ⦿ ⦿ ⦿ ⦿ ⦿')
        #     parsed_0 = parsed_0.replace(detectedObject + ']', '')

        # parsed_0 = tdf_without_comments.replace('[' + OBJECT_NAME + ']', '')
        parsed_1 = parsed_0#.replace('","}}{', '}}{')
        parsed_2 = parsed_1#.replace('   ', '"')
        parsed_3 = parsed_2#.replace(']', '" :')
        parsed_4 = parsed_3#.replace('=', '" : "')
        parsed_5 = parsed_4#.replace(';', '", "')
        parsed_6 = parsed_5#.replace('{', '{ "')
        parsed_7 = parsed_6#.replace(', "}', '}')
        parsed_8 = parsed_7#.replace('","}}{', '}}{')
        total_weapons = [m.start() for m in re.finditer('[' + weapon_parse_helper + ']', tdf_without_comments)]
        parsed_9 = parsed_8#.replace('}{', '}, {', len(total_weapons) - 1)
        parsed_10 = '' #  '[' + parsed_9 + ']'
        print('✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        tab_str = '	'
        parsed_11 = parsed_10.replace(tab_str, '')
        parsed_12 = parsed_11.replace('\n', '')
        parsed_13 = parsed_12#.replace('", "}}]', '}}]')
        print(parsed_13.split('}}['))
        print(parsed_13)
        print('✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        dictionary = json.loads(parsed_13)

        for weapon in dictionary:
            weapon['OBJ_NAME'] = OBJECT_NAME

        return Response(dictionary)
"""




class LazarusListUnits(APIView):

    permission_classes = (AllowAny,)  # IsAuthenticated
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
        # printColored('getting unit fbi', 3)
        try:
            unit_path = '/usr/src/app/static/mods/' + mod_name + '/units/' + unit_id + '.fbi'
            # printColored('unit path: ', 6)
            # printColored(unit_path, 5)
            unitsArray = readFile(unit_path)
            for unit in unitsArray:
                printKeyValuePair('name', unit.Name)
            json_response = {
                "raw_fbi_file": "...."  # unitsArray
            }
            # print('wtf dude...')
            return Response(json_response)
        except:
            # printKeyValuePair('shit', 'is fucked up nigga.')
            json_response = {
                "raw_fbi_file": "...."
            }
            return Response(json_response)

    def __init__(self):
        self.printColored('Initializing LazarusListUnits', 15)
        self.f = []
        self.d = []
        self.jsonResponse = []
        self.unit_fbi_final = []
        self.root = '/✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪/'
        # self.printColored('init completed!', 12)

    def printSubContents(self, pathName, mod_name):

        subcontents_to_print = '/usr/src/app/static/mods/' + mod_name
        # self.printColored(subcontents_to_print, 14)

        for (dirpath, dirnames, filenames) in walk(subcontents_to_print):
            # if pathName.lower() == 'unitpics':
            #     for file in filenames:
            #         filename, file_extension = os.path.splitext(file)
            #         self.printColoredFile(filename.lower(), file_extension.lower(), 17, 6)
            #         pathToFile = self.root + pathName + '/' + file
            #         try:
            #             img = Image.open(pathToFile)
            #             imgSaveTo = self.root + pathName + '/' + filename + '.png'
            #             img.save(imgSaveTo, format='png')
            #             self.jsonResponse.append(
            #                 {
            #                     'thumbnail': '/static/' + mod_name + '/unitpics/' + filename + '.png',
            #                     'object_name': filename,
            #                     'system_location': imgSaveTo,
            #                     'fbi_file': '/static/' + mod_name + '/units/' + filename + '.fbi',
            #                     'RESTful_unit_data': 'http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=' + mod_name + '&unit_id=' + filename
            #                 }
            #             )
            #         except:
            #             printError('failed to open ' + str(filename) + ' [' + str(file_extension) + ']')
            if pathName.lower() == 'units':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)

                    filename = filename.lower()
                    file_extension = file_extension.lower()

                    # self.printColoredFile(filename.lower(), file_extension.lower(), 18, 6)
                    pathToFile = '/usr/src/app/static/mods/' + mod_name + '/unitpics' + '/' + filename + '.pcx'

                    # self.printColored('GOING TO GET CONTENTS OF: ', 11)
                    # self.printColoredFile(mod_name, filename, 15, 3)
                    unit_fbi = ReadUnitFbi().get(mod_name, filename)

                    try:
                        img = Image.open(pathToFile)
                        imgSaveTo = '/usr/src/app/static/mods/' + mod_name + '/unitpics' + '/' + filename + '.png'
                        img.save(imgSaveTo, format='png')

                        self.jsonResponse.append(
                            {
                                'thumbnail': '/static/mods/' + mod_name + '/unitpics/' + filename + '.png',
                                'object_name': filename,
                                'system_location': imgSaveTo,
                                'fbi_file': '/static/mods/' + mod_name + '/units/' + filename + '.fbi',
                                'unit_data': unit_fbi,
                                'RESTful_unit_data': 'http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=' + mod_name + '&unit_id=' + filename
                            }
                        )

                        is_unique = True
                        # remove duplicates:
                        for item in self.unit_fbi_final:
                            if item['UnitName'] == unit_fbi[0]['UnitName']:
                                is_unique = False

                        if is_unique == True:
                            self.unit_fbi_final.append(unit_fbi[0])
                    except:
                        printError('failed to open ' + str(filename) + ' [' + str(file_extension) + ']')
            elif pathName.lower() == 'weapons':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)
                    # self.printColoredFile(filename.lower(), file_extension.lower(), 10, 6)
        return self.jsonResponse

    def printContents(self, mod_path, mod_name):
        # self.printColored('will now loop through this "walk(mod_path)" ' + str(walk(mod_path)), 102)
        for (dirpath, dirnames, filenames) in walk(mod_path):
            # self.printColored('self.f before extend: ', 105)
            # self.printColored(str(self.f), 15)
            self.f.extend(filenames)
            # self.printColored('self.f after extend: ', 102)
            # self.printColored(str(self.f), 15)
            # self.printColored('self.d before extend: ', 106)
            # self.printColored(str(self.d), 16)
            self.d.extend(dirnames)
            # self.printColored('self.d after extend: ', 103)
            # self.printColored(str(self.d), 16)
            # self.printColored(' for (dirpath, dirnames, filenames) ', 101)
            # self.printColored(str(dirpath) + ' ' + str(dirnames) + ' ' + str(filenames), 14)
            for path in dirnames:
            #     self.printColored(str(path), 13)
                self.printSubContents(path, mod_name)
            break


    def getUnitInfo(self, unitId):
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


    def get(self, request, format=None):
        try:
            # try:
            #     should_get_user_content = str(request.GET['should_get_user_content'])
            #     mod_path = '/usr/src/persistent/media/ta_data/' + str(request.GET['mod_name']) + '/'
            #     mod_name = str(request.GET['mod_name'])
            #     self.printContents(mod_path, mod_name)
            #     print('☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
            #     print(mod_path)
            #     print('☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
            #     return Response(self.unit_fbi_final)
            # except:
            mod_path = '/usr/src/app/static/mods/' + str(request.GET['mod_name']) + '/'
            mod_name = str(request.GET['mod_name'])
            self.printContents(mod_path, mod_name)
            return Response(self.unit_fbi_final)
        except:
            return Response('oh shit')

"""
/LazarusII/UnitFbiData/?mod_name=totala_files2&unit_id=arach
"""

