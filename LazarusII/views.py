from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair, printKeyValuePair1, printKeyValuePair2, \
    printError, printWarning, printInfo, printLog, printDebug

from rest_framework.permissions import IsAuthenticated, AllowAny

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


# from LazarusII.serializers import UnitFbiDataSerializer
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF

# from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route

from rest_framework import status






class FeatureTDFViewset(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):



        return Response(dict_list)






class WeaponTDFViewset(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        # mod_name = str(request.GET['mod_name'])
        # print('1 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        # file_name = str(request.GET['file_name'])
        # print('2 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        # directory_name = 'weapons'
        # print('3 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        # # media/ta_data/dictator/weapons
        # file_path = '/usr/src/persistent/media/ta_data/' + mod_name + '/' + directory_name + '/' + file_name + '.tdf'
        # print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ %s ' % file_path)
        parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
        file_path = '/usr/src/persistent/' + parse_path1 + '.tdf'

        f3 = open(file_path, 'r', errors='replace')
        print('5 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ')

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

        dict_list = []
        _tdf_prep = tdf_without_comments.replace(';}}[', ';}}|[')
        split_tdf = _tdf_prep.split('|')

        print('❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆')
        print(tdf_without_comments)
        print('❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆ ❆')

        try:
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
                # getBaseType(item)
                dict_list.append(dictionary)
                print('☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ dictionary ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
                print(dictionary)
                print('☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
                new_weapon_tdf = WeaponTDF()
                try:
                    new_weapon_tdf.accuracy = int(dictionary['accuracy'])
                except:
                    print('SKIPPING... accuracy ')
                try:
                    new_weapon_tdf.aimrate = int(dictionary['aimrate'])
                except:
                    print('SKIPPING... aimrate ')
                try:
                    new_weapon_tdf.areaofeffect = int(dictionary['areaofeffect'])
                except:
                    print('SKIPPING... areaofeffect ')
                try:
                    new_weapon_tdf.ballistic = int(dictionary['ballistic'])
                except:
                    print('SKIPPING... ballistic ')
                try:
                    new_weapon_tdf.beamweapon = int(dictionary['beamweapon'])
                except:
                    print('SKIPPING... beamweapon ')
                try:
                    new_weapon_tdf.burnblow = int(dictionary['burnblow'])
                except:
                    print('SKIPPING... burnblow ')
                try:
                    new_weapon_tdf.burst = int(dictionary['burst'])
                except:
                    print('SKIPPING... burst ')
                try:
                    new_weapon_tdf.burstrate = float(dictionary['burstrate'])
                except:
                    print('SKIPPING... burstrate ')
                try:
                    new_weapon_tdf.color = int(dictionary['color'])
                except:
                    print('SKIPPING... color ')
                try:
                    new_weapon_tdf.color2 = int(dictionary['color2'])
                except:
                    print('SKIPPING... color2 ')
                try:
                    new_weapon_tdf.commandfire = int(dictionary['commandfire'])
                except:
                    print('SKIPPING... commandfire ')
                try:
                    new_weapon_tdf.cruise = int(dictionary['cruise'])
                except:
                    print('SKIPPING... cruise ')
                try:
                    new_weapon_tdf.dropped = int(dictionary['dropped'])
                except:
                    print('SKIPPING... dropped ')
                try:
                    new_weapon_tdf.duration = float(dictionary['duration'])
                except:
                    print('SKIPPING... duration ')
                try:
                    new_weapon_tdf.edgeeffectiveness = float(dictionary['edgeeffectiveness'])
                except:
                    print('SKIPPING... edgeeffectiveness ')
                try:
                    new_weapon_tdf.endsmoke = int(dictionary['endsmoke'])
                except:
                    print('SKIPPING... endsmoke ')
                try:
                    new_weapon_tdf.energy = int(dictionary['energy'])
                except:
                    print('SKIPPING... energy ')
                try:
                    new_weapon_tdf.energypershot = int(dictionary['energypershot'])
                except:
                    print('SKIPPING... energypershot ')
                try:
                    new_weapon_tdf.explosionart = int(dictionary['explosionart'])
                except:
                    print('SKIPPING... explosionart ')
                try:
                    new_weapon_tdf.explosiongaf = int(dictionary['explosiongaf'])
                except:
                    print('SKIPPING... explosiongaf ')
                try:
                    new_weapon_tdf.firestarter = int(dictionary['firestarter'])
                except:
                    print('SKIPPING... firestarter ')
                try:
                    new_weapon_tdf.flighttime = int(dictionary['flighttime'])
                except:
                    print('SKIPPING... flighttime ')
                try:
                    new_weapon_tdf.groundbounce = int(dictionary['groundbounce'])
                except:
                    print('SKIPPING... groundbounce ')
                try:
                    new_weapon_tdf.guidance = int(dictionary['guidance'])
                except:
                    print('SKIPPING... guidance ')
                try:
                    new_weapon_tdf.ID_weapon = int(dictionary['ID'])
                except:
                    print('SKIPPING... ID ')
                try:
                    new_weapon_tdf.lavaexplosionart = dictionary['lavaexplosionart']
                except:
                    print('SKIPPING... lavaexplosionart ')
                try:
                    new_weapon_tdf.lavaexplosiongaf = dictionary['lavaexplosiongaf']
                except:
                    print('SKIPPING... lavaexplosiongaf ')
                try:
                    new_weapon_tdf.lineofsight = int(dictionary['lineofsight'])
                except:
                    print('SKIPPING... lineofsight ')
                try:
                    new_weapon_tdf.metal = int(dictionary['metal'])
                except:
                    print('SKIPPING... metal ')
                try:
                    new_weapon_tdf.metalpershot = int(dictionary['metalpershot'])
                except:
                    print('SKIPPING... metalpershot ')
                try:
                    new_weapon_tdf.meteor = int(dictionary['meteor'])
                except:
                    print('SKIPPING... meteor ')
                try:
                    new_weapon_tdf.minbarrelangle = int(dictionary['minbarrelangle'])
                except:
                    print('SKIPPING... minbarrelangle ')
                try:
                    new_weapon_tdf.model = dictionary['model']
                except:
                    print('SKIPPING... model ')
                try:
                    new_weapon_tdf.name = dictionary['name']
                except:
                    print('SKIPPING... name ')
                try:
                    new_weapon_tdf.noautorange = int(dictionary['noautorange'])
                except:
                    print('SKIPPING... noautorange ')
                try:
                    new_weapon_tdf.noexplode = int(dictionary['noexplode'])
                except:
                    print('SKIPPING... noexplode ')
                try:
                    new_weapon_tdf.noradar = int(dictionary['noradar'])
                except:
                    print('SKIPPING... noradar ')
                try:
                    new_weapon_tdf.paralyzer = int(dictionary['paralyzer'])
                except:
                    print('SKIPPING... paralyzer ')
                try:
                    new_weapon_tdf.pitchtolerance = int(dictionary['pitchtolerance'])
                except:
                    print('SKIPPING... pitchtolerance ')
                try:
                    new_weapon_tdf.propeller = int(dictionary['propeller'])
                except:
                    print('SKIPPING... propeller ')
                try:
                    new_weapon_tdf.randomdecay = int(dictionary['randomdecay'])
                except:
                    print('SKIPPING... randomdecay ')
                try:
                    new_weapon_tdf._range = int(dictionary['range'])
                except:
                    print('SKIPPING... range ')
                try:
                    new_weapon_tdf.reloadtime = float(dictionary['reloadtime'])
                except:
                    print('SKIPPING... reloadtime ')
                try:
                    new_weapon_tdf.rendertype = int(dictionary['rendertype'])
                except:
                    print('SKIPPING... rendertype ')
                try:
                    new_weapon_tdf.selfprop = int(dictionary['selfprop'])
                except:
                    print('SKIPPING... selfprop ')
                try:
                    new_weapon_tdf.shakeduration = int(dictionary['shakeduration'])
                except:
                    print('SKIPPING... shakeduration ')
                try:
                    new_weapon_tdf.shakemagnitudee = int(dictionary['shakemagnitudee'])
                except:
                    print('SKIPPING... shakemagnitudee ')
                try:
                    new_weapon_tdf.smokedelay = int(dictionary['smokedelay'])
                except:
                    print('SKIPPING... smokedelay ')
                try:
                    new_weapon_tdf.smoketrail = int(dictionary['smoketrail'])
                except:
                    print('SKIPPING... smoketrail ')
                try:
                    new_weapon_tdf.soundhit = int(dictionary['soundhit'])
                except:
                    print('SKIPPING... soundhit ')
                try:
                    new_weapon_tdf.soundstart = dictionary['soundstart']
                except:
                    print('SKIPPING... soundstart ')
                try:
                    new_weapon_tdf.soundtrigger = int(dictionary['soundtrigger'])
                except:
                    print('SKIPPING... soundtrigger ')
                try:
                    new_weapon_tdf.soundwater = dictionary['soundwater']
                except:
                    print('SKIPPING... soundwater ')
                try:
                    new_weapon_tdf.sprayangle = int(dictionary['sprayangle'])
                except:
                    print('SKIPPING... sprayangle ')
                try:
                    new_weapon_tdf.startsmoke = int(dictionary['startsmoke'])
                except:
                    print('SKIPPING... startsmoke ')
                try:
                    new_weapon_tdf.startvelocity = int(dictionary['startvelocity'])
                except:
                    print('SKIPPING... startvelocity ')
                try:
                    new_weapon_tdf.stockpile = int(dictionary['stockpile'])
                except:
                    print('SKIPPING... stockpile ')
                try:
                    new_weapon_tdf.targetable = int(dictionary['targetable'])
                except:
                    print('SKIPPING... targetable ')
                try:
                    new_weapon_tdf.tolerance = int(dictionary['tolerance'])
                except:
                    print('SKIPPING... tolerance ')
                try:
                    new_weapon_tdf.tracks = int(dictionary['tracks'])
                except:
                    print('SKIPPING... tracks ')
                try:
                    new_weapon_tdf.turnrate = int(dictionary['turnrate'])
                except:
                    print('SKIPPING... turnrate ')
                try:
                    new_weapon_tdf.turrent = int(dictionary['turrent'])
                except:
                    print('SKIPPING... turrent ')
                try:
                    new_weapon_tdf.twophase = int(dictionary['twophase'])
                except:
                    print('SKIPPING... twophase ')
                try:
                    new_weapon_tdf.unitsonly = int(dictionary['unitsonly'])
                except:
                    print('SKIPPING... unitsonly ')
                try:
                    new_weapon_tdf.vlaunch = int(dictionary['vlaunch'])
                except:
                    print('SKIPPING... vlaunch ')
                try:
                    new_weapon_tdf.waterexplosionart = dictionary['waterexplosionart']
                except:
                    print('SKIPPING... waterexplosionart ')
                try:
                    new_weapon_tdf.waterexplosiongaf = dictionary['waterexplosiongaf']
                except:
                    print('SKIPPING... waterexplosiongaf ')
                try:
                    new_weapon_tdf.waterweapon = int(dictionary['waterweapon'])
                except:
                    print('SKIPPING... waterweapon ')
                try:
                    new_weapon_tdf.weaponacceleration = int(dictionary['weaponacceleration'])
                except:
                    print('SKIPPING... weaponacceleration ')
                try:
                    new_weapon_tdf.weapontimer = float(dictionary['weapontimer'])
                except:
                    print('SKIPPING... weapontimer ')
                try:
                    new_weapon_tdf.weapontype2 = dictionary['weapontype2']
                except:
                    print('SKIPPING... weapontype2 ')
                try:
                    new_weapon_tdf.weaponvelocity = int(dictionary['weaponvelocity'])
                except:
                    print('SKIPPING... weaponvelocity ')
                try:
                    new_damage_obj = Damage()
                    new_weapon_tdf.damage = Damage.objects.get(id=1)
                except:
                    print('SKIPPING... Damage Obj ')
                try:
                    new_weapon_tdf.save()
                except:
                    print('FAIL . . .')
                    return Response(dict_list)

                print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')
                print(json.dumps(dict_list))
                print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')

                return Response(dict_list)
        except:
            print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')
            print(json.dumps(dict_list))
            print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')

            return Response(dict_list)


class ExecuteBash_LS_AllCustomModFiles(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):

        final_obj = {}

        # mod_name = request.GET['mod_name']
        directory_str = '/usr/src/persistent/media/ta_data'

        # community mods:
        # /usr/src/persistent/media/ta_data/

        mod_paths = []
        uploaded_data_files = TotalAnnihilationUploadedFile.objects.all()
        for data_file in uploaded_data_files:
            print("data_file %s" % data_file)
            if os.path.isdir(data_file.system_path):
                ls_current_modpath = str(subprocess.check_output(['ls', data_file.system_path]))

                parsed_1 = ls_current_modpath.replace("\\n'","")
                dirs_in_mod = parsed_1.replace("b'","").split('\\n')

                print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ')
                print("parsed_1 %s" % parsed_1)
                print("dirs_in_mod : ")
                listed_data_files = {
                    'name': data_file.file_name[:-4],
                    'type': data_file.file_name[-4:]
                }

                listed_data_files['directories'] = []
                for mod_item in dirs_in_mod:
                    # listed_data_files[mod_item + '_mod_items'] = {}

                    mod_item_path = data_file.system_path + '/' + mod_item
                    if os.path.isdir(mod_item_path):
                        print("mod_item : %s" % mod_item)
                        ls_current_submodpath = str(subprocess.check_output(['ls', mod_item_path]))
                        sub_parsed_1 = ls_current_submodpath.replace("\\n'", "")
                        sub_parsed_2 = sub_parsed_1.replace("b'", "")
                        # listed_data_files[mod_item + '_mod_items'] = (sub_parsed_2.split('\\n'))
                        elements_in_dir = (sub_parsed_2.split('\\n'))
                        for raw_data_tdf in elements_in_dir:
                            does_contain_json = True
                            subdirectory_components = 'NIL'
                            parse_moditempath2 = ''
                            if raw_data_tdf[-4:] == '.fbi':
                                parse_moditempath1 = mod_item_path.replace('/usr/src/persistent/', '')
                                parse_moditempath2 = parse_moditempath1.replace('/', '_SLSH_') + '_SLSH_' + raw_data_tdf[:-4]
                                parse_moditempath3 = '/LazarusII/UnitFBIViewset/?encoded_path=' + parse_moditempath2
                            elif raw_data_tdf[-4:] == '.tdf':
                                parse_moditempath1 = mod_item_path.replace('/usr/src/persistent/', '')
                                parse_moditempath2 = parse_moditempath1.replace('/',
                                                                                '_SLSH_') + '_SLSH_' + raw_data_tdf[:-4]
                                if mod_item == 'weapons':
                                    parse_moditempath3 = '/LazarusII/WeaponTDFViewset/?encoded_path=' + parse_moditempath2
                                elif mod_item == 'download':
                                    parse_moditempath3 = '/LazarusII/DownloadTDFViewset/?encoded_path=' + parse_moditempath2
                                elif mod_item == 'units':
                                    parse_moditempath3 = '/LazarusII/UnitFBIViewset/?encoded_path=' + parse_moditempath2
                                else:
                                    parse_moditempath1 = mod_item_path.replace('/usr/src/persistent/', '')
                                    parse_moditempath2 = parse_moditempath1.replace('/',
                                                                                    '_SLSH_') + '_SLSH_' + raw_data_tdf[
                                                                                                           :-4]
                                    parse_moditempath3 = 'nan'
                                    does_contain_json = False
                            elif raw_data_tdf[-4:] == 'pses': # CORPSE FEATURE DETECTED! #      7/14/2017
                                # subdirectory_components = mod_item_path  #'THIS IS A CORPSE ! ! !'
                                corpses_dir = mod_item_path + '/corpses'
                                ls_cmd_features_dir = str(subprocess.check_output(['ls', corpses_dir]))
                                corpses_parsed_1 = ls_cmd_features_dir.replace("\\n'", "")
                                corpses_parsed_2 = corpses_parsed_1.replace("b'", "")
                                replace_me_str = '\\' + 'n'
                                replace_regex1 = corpses_parsed_2.replace(replace_me_str, '_NL_')
                                subdirectory_components = replace_regex1.split('_NL_')
                                for feat in subdirectory_components:
                                    parse_moditempath1 = mod_item_path.replace('/usr/src/persistent/', '')
                                    parse_moditempath2 = parse_moditempath1.replace('/',
                                                                                '_SLSH_') + '_SLSH_' + raw_data_tdf + '_SLSH_'
                                raw_data_tdf = 'CORPSES_dir'

                            else:
                                parse_moditempath3 = 'nan'
                                does_contain_json = False

                            _type = raw_data_tdf[-4:]
                            if _type == '.tdf' or _type == '.fbi':
                                try:
                                    logTheAsolutePath = StoredFiles()
                                    logTheAsolutePath.absolute_path = '/usr/src/persistent/' + raw_data_tdf
                                    logTheAsolutePath.file_type = raw_data_tdf[-3:]
                                    logTheAsolutePath.file_name = raw_data_tdf[:-4] + '_' + raw_data_tdf[-3:]
                                    logTheAsolutePath.save()
                                except:
                                    print('skipping StoredFiles log, file already exists.')

                            data_file_json = {
                                'file_type': raw_data_tdf[-4:],
                                'file_name': raw_data_tdf[:-4],
                                'mod_path': parse_moditempath3,
                                'mod_path_slug': parse_moditempath2,
                                'dir_type': mod_item,
                                'raw_data_tdf': raw_data_tdf,
                                'does_contain_json': does_contain_json,
                                'subdirectory_components': subdirectory_components
                            }

                            listed_data_files['directories'].append(data_file_json)
                        # mod_paths[data_file.file_name] = (listed_data_files)
                mod_paths.append(listed_data_files)

        result1 = str(subprocess.check_output(['ls', directory_str]))
        final_obj[directory_str] = str(result1).split('\\n')
        final_obj[directory_str][0] = final_obj[directory_str][0].replace("b'", "")

        context = {'root_items': final_obj, 'mod_paths': mod_paths, 'HPIs': ''}
        return Response(context)


class DownloadTDFViewset(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
        file_path = '/usr/src/persistent/' + parse_path1 + '.tdf'
        f3 = open(file_path, 'r', errors='replace')

        print("OPENING DOWNLOAD TDF... ")
        incoming_tdf = remove_comments(f3.read())
        print(incoming_tdf)
        print('TDF Opened Successfully ! ! !')

        def parseNested(_tdf, nOBJECT_NAME):
            nparsed_0 = _tdf.replace('[' + nOBJECT_NAME + ']', '')
            nparsed_1 = nparsed_0
            nparsed_2 = nparsed_1.replace('[', '"')
            nparsed_3 = nparsed_2.replace(']', '" :')
            nparsed_4 = nparsed_3.replace('=', '" : "')
            nparsed_5 = nparsed_4.replace(';', '", "')
            nparsed_6 = nparsed_5.replace('{', '{ "')
            nparsed_7 = nparsed_6.replace(', "}', '}')
            nparsed_8 = nparsed_7.replace(', ""', ', "')
            nparsed_9 = nparsed_8.replace('", " }', '"}').replace(' ', '')
            return nparsed_9

        def getNestedType(_tdf):
            try:
                _BrkStart = [m.start() for m in re.finditer('\[', _tdf)]
                _BrkEnd = [m.start() for m in re.finditer('\]', _tdf)]
                return _tdf[int(str(_BrkStart[0])) + 1:int(str(_BrkEnd[0]))]
            except:
                return ''

        dict_list = []
        rmv_tabs_n_spaces0 = incoming_tdf.replace('\t', '')
        rmv_tabs_n_spaces1 = rmv_tabs_n_spaces0.replace('\n', '').strip()
        _tdf_prep = rmv_tabs_n_spaces1.replace(' ', '').replace('} [', '}|[').replace('}[', '}|[')

        print('TDF PREPPED AND READY FOR JSONIFYING: ')
        print(_tdf_prep)
        print('______________________________________')

        split_tdf = _tdf_prep.split('|')

        for item in split_tdf:
            nested_obj = parseNested(item, getNestedType(item))
            print(nested_obj)

        for item in split_tdf:
            nested_type = getNestedType(item)
            print("NESTED TYPE:  " + nested_type)
            nested_obj = parseNested(item, nested_type)
            print(nested_obj)
            dictionary = json.loads(nested_obj)
            dictionary['Object_Name'] = nested_type
            dict_list.append(dictionary)

        print('JSON DUMPS: ')
        print(json.dumps(dict_list))

        ## SAVE TO SQL:
        for item in dict_list:
            new_download = DownloadTDF()
            get_pk_unit = UnitFbiData.objects.filter(UnitName__iexact=item['UNITNAME'])
            new_download.parent_unit = get_pk_unit[0]

            new_download.MENUENTRY = item['Object_Name']
            new_download.BUTTON = item['BUTTON']
            new_download.MENU = item['MENU']
            new_download.UNITMENU = item['UNITMENU']
            new_download.UNITNAME = item['UNITNAME']
            new_download.save()

        return Response(dict_list)


class FeatureTDFViewset(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
        file_path = '/usr/src/persistent/' + parse_path1 + '.tdf'
        f3 = open(file_path, 'r', errors='replace')

        print("OPENING DOWNLOAD TDF... ")
        incoming_tdf = remove_comments(f3.read())
        print(incoming_tdf)
        print('TDF Opened Successfully ! ! !')

        status_code = status.HTTP_200_OK

        def parseNested(_tdf, nOBJECT_NAME):
            nparsed_0 = _tdf.replace('[' + nOBJECT_NAME + ']', '')
            nparsed_1 = nparsed_0
            nparsed_2 = nparsed_1.replace('[', '"')
            nparsed_3 = nparsed_2.replace(']', '" :')
            nparsed_4 = nparsed_3.replace('=', '" : "')
            nparsed_5 = nparsed_4.replace(';', '", "')
            nparsed_6 = nparsed_5.replace('{', '{ "')
            nparsed_7 = nparsed_6.replace(', "}', '}')
            nparsed_8 = nparsed_7.replace(', ""', ', "')
            nparsed_9 = nparsed_8.replace('", " }', '"}').replace(' ', '')
            return nparsed_9

        def getNestedType(_tdf):
            try:
                _BrkStart = [m.start() for m in re.finditer('\[', _tdf)]
                _BrkEnd = [m.start() for m in re.finditer('\]', _tdf)]
                return _tdf[int(str(_BrkStart[0])) + 1:int(str(_BrkEnd[0]))]
            except:
                return ''

        dict_list = []
        rmv_tabs_n_spaces0 = incoming_tdf.replace('\t', '')
        rmv_tabs_n_spaces1 = rmv_tabs_n_spaces0.replace('\n', '').strip()
        _tdf_prep = rmv_tabs_n_spaces1.replace(' ', '').replace('} [', '}|[').replace('}[', '}|[')

        print('TDF PREPPED AND READY FOR JSONIFYING: ')
        print(_tdf_prep)
        print('______________________________________')

        split_tdf = _tdf_prep.split('|')

        for item in split_tdf:
            nested_obj = parseNested(item, getNestedType(item))
            print(nested_obj)

        for item in split_tdf:
            nested_type = getNestedType(item)
            print("NESTED TYPE:  " + nested_type)
            nested_obj = parseNested(item, nested_type)
            print(nested_obj)
            dictionary = json.loads(nested_obj)
            dictionary['Object_Name'] = nested_type
            dict_list.append(dictionary)

        print('JSON DUMPS: ')
        print(json.dumps(dict_list))

        ##### SAVE TO SQL:
        for item in dict_list:
            new_feature = FeatureTDF()
            ### 37
            try:
                new_feature.animating = item['animating']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.animtrans = item['animtrans']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.autoreclaimable = item['autoreclaimable']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.burnmax = item['burnmax']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.burnmin = item['burnmin']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.burnweapon = item['burnweapon']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.category = item['category']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.description = item['description']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.blocking = item['blocking']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.damage = item['damage']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.energy = item['energy']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.featuredead = item['featuredead']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.featurereclamate = item['featurereclamate']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.filename = item['filename']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.flamable = item['flamable']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.footprintx = item['footprintx']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.footprintz = item['footprintz']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.geothermal = item['geothermal']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.height = item['height']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.hitdensity = item['hitdensity']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.indestructible = item['indestructible']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.metal = item['metal']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.nodisplayinfo = item['nodisplayinfo']
            except:
                print('SKIPPING    animating')
            try:
                new_feature._object = item['object']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.permanent = item['permanent']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.reclaimable = item['reclaimable']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.reproduce = item['reproduce']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.reproducearea = item['reproducearea']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.seqname = item['seqname']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.seqnameburn = item['seqnameburn']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.seqnamedie = item['seqnamedie']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.seqnamereclamate = item['seqnamereclamate']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.seqnameshad = item['seqnameshad']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.shadtrans = item['shadtrans']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.sparktime = item['sparktime']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.spreadchance = item['spreadchance']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.world = item['world']
            except:
                print('SKIPPING    animating')
            try:
                new_feature.save()
                status_code = status.HTTP_201_CREATED
            except:
                print('no new content.')

        return Response(dict_list, status=status_code)



# animating
# animtrans
# autoreclaimable
# burnmax
# burnmin
# burnweapon
# category
# description
# blocking
# damage
# energy
# featuredead
# featurereclamate
# filename
# flamable
# footprintx
# footprintz
# geothermal
# height
# hitdensity
# indestructible
# metal
# nodisplayinfo
# _object
# permanent
# reclaimable
# reproduce
# reproducearea
# seqname
# seqnameburn
# seqnamedie
# seqnamereclamate
# seqnameshad
# shadtrans
# sparktime
# spreadchance
# world





class UnitFBIViewset(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
        file_path = '/usr/src/persistent/' + parse_path1 + '.fbi'

        try:
            parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
            file_path = '/usr/src/persistent/' + parse_path1 + '.fbi'
            print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ %s ' % file_path)
            print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ %s ' % file_path)
            print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ %s ' % file_path)
        except:
            print('falling back to old API...')

        f3 = open(file_path, 'r', errors='replace')

        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ THE FILE DID OPEN ! ! ! ! ')

        OBJECT_NAME = 'UNITINFO'

        tdf_without_comments = remove_comments(f3.read().strip().replace('\n', '').replace('\t', ''))

        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪  ! ! ! ! ')
        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪  ! ! ! ! ')
        print(tdf_without_comments)
        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪  ! ! ! ! ')
        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪  ! ! ! ! ')

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
        parsed_13 = parsed_12.replace('", "]', '"}]')
        # print(parsed_12)


        print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')
        print(parsed_13)
        print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')
        dictionary = json.loads(parsed_13)
        print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')
        print(dictionary)
        print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')

        print(dictionary[0])

        try:

            for weapon in dictionary:
                weapon['OBJ_NAME'] = OBJECT_NAME

            new_unit_fbi = UnitFbiData()
            new_unit_fbi._raw_json_dump = '...'  # json.dumps(dictionary[0])

            try:
                new_unit_fbi.Acceleration = float(dictionary[0]['Acceleration'])
            except:
                print('SKIPPING...' + str('Acceleration'))
            try:
                new_unit_fbi.ActiveWhenBuild = int(dictionary[0]['ActiveWhenBuild'])
            except:
                print('SKIPPING...' + str('ActiveWhenBuild'))
            try:
                new_unit_fbi.ai_limit = dictionary[0]['ai_limit']
            except:
                print('SKIPPING...' + str('ai_limit'))
            try:
                new_unit_fbi.ai_weight = dictionary[0]['ai_weight']
            except:
                print('SKIPPING...' + str('ai_weight'))
            try:
                new_unit_fbi.altfromsealevel = int(dictionary[0]['altfromsealevel'])
            except:
                print('SKIPPING...' + str('altfromsealevel'))
            try:
                new_unit_fbi.amphibious = int(dictionary[0]['amphibious'])
            except:
                print('SKIPPING...' + str('amphibious'))
            try:
                new_unit_fbi.antiweapons = int(dictionary[0]['antiweapons'])
            except:
                print('SKIPPING...' + str('antiweapons'))
            try:
                new_unit_fbi.attackrunlength = int(dictionary[0]['attackrunlength'])
            except:
                print('SKIPPING...' + str('attackrunlength'))
            try:
                new_unit_fbi.BMcode = int(dictionary[0]['BMcode'])
            except:
                print('SKIPPING...' + str('BMcode'))
            try:
                new_unit_fbi.BadTargetCategory = dictionary[0]['BadTargetCategory']
            except:
                print('SKIPPING...' + str('BadTargetCategory'))
            try:
                new_unit_fbi.BankScale = int(dictionary[0]['BankScale']) ### START
            except:
                print('SKIPPING...' + str('BankScale'))
            try:
                new_unit_fbi.BrakeRate = int(dictionary[0]['BrakeRate'])
            except:
                print('SKIPPING...' + str('BrakeRate'))
            try:
                new_unit_fbi.BuildAngle = int(dictionary[0]['BuildAngle'])
            except:
                print('SKIPPING...' + str('BuildAngle'))
            try:
                new_unit_fbi.BuildCostEnergy = int(dictionary[0]['BuildCostEnergy'])
            except:
                print('SKIPPING...' + str('BuildCostEnergy'))
            try:
                new_unit_fbi.BuildCostMetal = int(dictionary[0]['BuildCostMetal'])
            except:
                print('SKIPPING...' + str('BuildCostMetal'))
            try:
                new_unit_fbi.BuildTime = int(dictionary[0]['BuildTime'])
            except:
                print('SKIPPING...' + str('BuildTime'))
            try:
                new_unit_fbi.Builddistance = int(dictionary[0]['Builddistance'])
            except:
                print('SKIPPING...' + str('Builddistance'))
            try:
                new_unit_fbi.Builder = int(dictionary[0]['Builder'])
            except:
                new_unit_fbi.Builder = False
                print('SKIPPING...' + str('Builder'))
            try:
                new_unit_fbi.canattack = int(dictionary[0]['canattack'])
            except:
                print('SKIPPING...' + str('canattack'))
            try:
                new_unit_fbi.CanCapture = int(dictionary[0]['CanCapture'])
            except:
                print('SKIPPING...' + str('CanCapture'))
            try:
                new_unit_fbi.CanDgun = int(dictionary[0]['CanDgun'])
            except:
                print('SKIPPING...' + str('CanDgun'))
            try:
                new_unit_fbi.Canfly = int(dictionary[0]['Canfly'])
            except:
                print('SKIPPING...' + str('Canfly'))
            try:
                new_unit_fbi.canguard = int(dictionary[0]['canguard'])
            except:
                print('SKIPPING...' + str('canguard'))
            try:
                new_unit_fbi.canhover = int(dictionary[0]['canhover'])
            except:
                print('SKIPPING...' + str('canhover'))
            try:
                new_unit_fbi.canload = int(dictionary[0]['canload'])
            except:
                print('SKIPPING...' + str('canload'))
            try:
                new_unit_fbi.canmove = int(dictionary[0]['canmove'])
            except:
                print('SKIPPING...' + str('canmove'))
            try:
                new_unit_fbi.canpatrol = int(dictionary[0]['canpatrol'])
            except:
                print('SKIPPING...' + str('canpatrol'))
            try:
                new_unit_fbi.CanReclamate = int(dictionary[0]['CanReclamate'])
            except:
                print('SKIPPING...' + str('CanReclamate'))
            try:
                new_unit_fbi.canstop = int(dictionary[0]['canstop'])
            except:
                print('SKIPPING...' + str('canstop'))
            try:
                new_unit_fbi.cantbetransported = int(dictionary[0]['cantbetransported'])  ### END
            except:
                print('SKIPPING...' + str('cantbetransported'))
            try:
                new_unit_fbi.Category = dictionary[0]['Category']
            except:
                print('SKIPPING...' + str('Category'))
            try:
                new_unit_fbi.CloakCost = int(dictionary[0]['CloakCost'])
            except:
                print('SKIPPING...' + str('CloakCost'))
            try:
                new_unit_fbi.CloakCostMoving = int(dictionary[0]['CloakCostMoving'])
            except:
                print('SKIPPING...' + str('CloakCostMoving'))
            try:
                new_unit_fbi.Commander = int(dictionary[0]['Commander'])
            except:
                print('SKIPPING...' + str('Commander'))
            try:
                new_unit_fbi.Copyright = dictionary[0]['Copyright']
            except:
                print('SKIPPING...' + str('Copyright'))
            try:
                new_unit_fbi.Corpse = dictionary[0]['Corpse']
            except:
                print('SKIPPING...' + str('Corpse'))
            try:
                new_unit_fbi.cruisealt = int(dictionary[0]['cruisealt'])
            except:
                print('SKIPPING...' + str('cruisealt'))
            try:
                new_unit_fbi.DamageModifier = float(dictionary[0]['DamageModifier'])
            except:
                print('SKIPPING...' + str('DamageModifier'))
            try:
                new_unit_fbi.DefaultMissionType = dictionary[0]['DefaultMissionType']
            except:
                print('SKIPPING...' + str('DefaultMissionType'))
            try:
                new_unit_fbi.Description = dictionary[0]['Description']
            except:
                print('SKIPPING...' + str('Description'))
            try:
                new_unit_fbi.Designation = dictionary[0]['Designation']
            except:
                print('SKIPPING...' + str('Designation'))
            try:
                new_unit_fbi.digger = int(dictionary[0]['digger']) # BEGIN
            except:
                print('SKIPPING...' + str('digger'))
            try:
                new_unit_fbi.Downloadable = int(dictionary[0]['Downloadable'])
            except:
                print('SKIPPING...' + str('Downloadable'))
            try:
                new_unit_fbi.EnergyMake = int(dictionary[0]['EnergyMake'])
            except:
                print('SKIPPING...' + str('EnergyMake'))
            try:
                new_unit_fbi.EnergyStorage = int(dictionary[0]['EnergyStorage'])
            except:
                print('SKIPPING...' + str('EnergyStorage'))
            try:
                new_unit_fbi.EnergyUse = int(dictionary[0]['EnergyUse'])  # END
            except:
                print('SKIPPING...' + str('EnergyUse'))
            try:
                new_unit_fbi.ExplodeAs = dictionary[0]['ExplodeAs']
            except:
                print('SKIPPING...' + str('ExplodeAs'))
            try:
                new_unit_fbi.ExtractsMetal = float(dictionary[0]['ExtractsMetal']) # FLOAT__
            except:
                print('SKIPPING...' + str('ExtractsMetal'))
            try:
                new_unit_fbi.firestandorders = int(dictionary[0]['firestandorders'])  # BEGIN INT
            except:
                print('SKIPPING...' + str('firestandorders'))
            try:
                new_unit_fbi.Floater = int(dictionary[0]['Floater'])
            except:
                print('SKIPPING...' + str('Floater'))
            try:
                new_unit_fbi.FootprintX = int(dictionary[0]['FootprintX'])
            except:
                print('SKIPPING...' + str('FootprintX'))
            try:
                new_unit_fbi.FootprintZ = int(dictionary[0]['FootprintZ'])  # END INT
            except:
                print('SKIPPING...' + str('FootprintZ'))
            try:
                new_unit_fbi.FrenchDescription = dictionary[0]['FrenchDescription']
            except:
                print('SKIPPING...' + str('FrenchDescription'))
            try:
                new_unit_fbi.FrenchName = dictionary[0]['FrenchName']
            except:
                print('SKIPPING...' + str('FrenchName'))
            try:
                new_unit_fbi.GermanDescription = dictionary[0]['GermanDescription']
            except:
                print('SKIPPING...' + str('GermanDescription'))
            try:
                new_unit_fbi.GermanName = dictionary[0]['GermanName']
            except:
                print('SKIPPING...' + str('GermanName'))
            try:
                new_unit_fbi.HealTime = int(dictionary[0]['HealTime'])  # BEGIN INT
            except:
                print('SKIPPING...' + str('HealTime'))
            try:
                new_unit_fbi.HideDamage = int(dictionary[0]['HideDamage'])
            except:
                print('SKIPPING...' + str('HideDamage'))
            try:
                new_unit_fbi.HoverAttack = int(dictionary[0]['HoverAttack'])
            except:
                print('SKIPPING...' + str('HoverAttack'))
            try:
                new_unit_fbi.ImmuneToParalyzer = int(dictionary[0]['ImmuneToParalyzer'])
            except:
                print('SKIPPING...' + str('ImmuneToParalyzer'))
            try:
                new_unit_fbi.init_cloaked = int(dictionary[0]['init_cloaked'])
            except:
                print('SKIPPING...' + str('init_cloaked'))
            try:
                new_unit_fbi.IsAirBase = int(dictionary[0]['IsAirBase'])
            except:
                print('SKIPPING...' + str('IsAirBase'))
            try:
                new_unit_fbi.IsFeature = int(dictionary[0]['IsFeature'])
            except:
                print('SKIPPING...' + str('IsFeature'))
            try:
                new_unit_fbi.istargetingupgrade = int(dictionary[0]['istargetingupgrade'])  # END INT
            except:
                print('SKIPPING...' + str('istargetingupgrade'))
            try:
                new_unit_fbi.ItalianDescription = dictionary[0]['ItalianDescription']
            except:
                print('SKIPPING...' + str('ItalianDescription'))
            try:
                new_unit_fbi.ItalianName = dictionary[0]['ItalianName']
            except:
                print('SKIPPING...' + str('ItalianName'))
            try:
                new_unit_fbi.JapanesDescription = dictionary[0]['JapanesDescription']
            except:
                print('SKIPPING...' + str('JapanesDescription'))
            try:
                new_unit_fbi.JapaneseName = dictionary[0]['JapaneseName']
            except:
                print('SKIPPING...' + str('JapaneseName'))
            try:
                new_unit_fbi.kamikaze = int(dictionary[0]['kamikaze'])  # BEGIN INT
            except:
                print('SKIPPING...' + str('kamikaze'))
            try:
                new_unit_fbi.kamikazedistance = int(dictionary[0]['kamikazedistance'])
            except:
                print('SKIPPING...' + str('kamikazedistance'))
            try:
                new_unit_fbi.MakesMetal = int(dictionary[0]['MakesMetal'])
            except:
                print('SKIPPING...' + str('MakesMetal'))
            try:
                new_unit_fbi.maneuverleashlength = int(dictionary[0]['maneuverleashlength'])
            except:
                print('SKIPPING...' + str('maneuverleashlength'))
            try:
                new_unit_fbi.MaxDamage = int(dictionary[0]['MaxDamage'])
            except:
                print('SKIPPING...' + str('MaxDamage'))
            try:
                new_unit_fbi.MaxSlope = int(dictionary[0]['MaxSlope'])
            except:
                print('SKIPPING...' + str('MaxSlope'))
            try:
                new_unit_fbi.MaxVelocity = int(dictionary[0]['MaxVelocity'])
            except:
                print('SKIPPING...' + str('MaxVelocity'))
            try:
                new_unit_fbi.MaxWaterDepth = int(dictionary[0]['MaxWaterDepth'])
            except:
                print('SKIPPING...' + str('MaxWaterDepth'))
            try:
                new_unit_fbi.MetalMake = int(dictionary[0]['MetalMake'])
            except:
                print('SKIPPING...' + str('MetalMake'))
            try:
                new_unit_fbi.MetalStorage = int(dictionary[0]['MetalStorage'])
            except:
                print('SKIPPING...' + str('MetalStorage'))
            try:
                new_unit_fbi.mincloakdistance = int(dictionary[0]['mincloakdistance'])
            except:
                print('SKIPPING...' + str('mincloakdistance'))
            try:
                new_unit_fbi.MinWaterDepth = int(dictionary[0]['MinWaterDepth'])
            except:
                print('SKIPPING...' + str('MinWaterDepth'))
            try:
                new_unit_fbi.MobileStandOrders = int(dictionary[0]['MobileStandOrders'])
            except:
                print('SKIPPING...' + str('MobileStandOrders'))
            try:
                new_unit_fbi.MoveRate1 = int(dictionary[0]['MoveRate1'])  # END INT
            except:
                print('SKIPPING...' + str('MoveRate1'))
            try:
                new_unit_fbi.MovementClass = dictionary[0]['MovementClass']
            except:
                print('SKIPPING...' + str('MovementClass'))
            try:
                new_unit_fbi.Name = dictionary[0]['Name']
            except:
                print('SKIPPING...' + str('Name'))
            try:
                new_unit_fbi.NoAutoFire = int(dictionary[0]['NoAutoFire'])
            except:
                print('SKIPPING...' + str('NoAutoFire'))
            try:
                new_unit_fbi.NoChaseCategory = dictionary[0]['NoChaseCategory']
            except:
                print('SKIPPING...' + str('NoChaseCategory'))
            try:
                new_unit_fbi.norestrict = int(dictionary[0]['norestrict'])
            except:
                print('SKIPPING...' + str('norestrict'))
            try:
                new_unit_fbi.NoShadow = int(dictionary[0]['NoShadow'])
            except:
                print('SKIPPING...' + str('NoShadow'))
            try:
                new_unit_fbi.Objectname = dictionary[0]['Objectname']
            except:
                print('SKIPPING...' + str('Objectname'))
            try:
                new_unit_fbi.onoffable = int(dictionary[0]['onoffable'])
            except:
                print('SKIPPING...' + str('onoffable'))
            try:
                new_unit_fbi.Ovradjust = int(dictionary[0]['Ovradjust'])
            except:
                print('SKIPPING...' + str('Ovradjust'))
            try:
                new_unit_fbi.PigLatinDescription = dictionary[0]['PigLatinDescription']
            except:
                print('SKIPPING...' + str('PigLatinDescription'))
            try:
                new_unit_fbi.PigLatinName = dictionary[0]['PigLatinName']
            except:
                print('SKIPPING...' + str('PigLatinName'))
            try:
                new_unit_fbi.PitchScale = int(dictionary[0]['PitchScale'])  # BEGIN INT
            except:
                print('SKIPPING...' + str('PitchScale'))
            try:
                new_unit_fbi.RadarDistance = int(dictionary[0]['RadarDistance'])
            except:
                print('SKIPPING...' + str('RadarDistance'))
            try:
                new_unit_fbi.RadarDistanceJam = int(dictionary[0]['RadarDistanceJam'])
            except:
                print('SKIPPING...' + str('RadarDistanceJam'))
            try:
                new_unit_fbi.Scale = int(dictionary[0]['Scale'])  # END INT
            except:
                print('SKIPPING...' + str('Scale'))
            try:
                new_unit_fbi.SelfDestructAs = dictionary[0]['SelfDestructAs']
            except:
                print('SKIPPING...' + str('SelfDestructAs'))
            try:
                new_unit_fbi.selfdestructcountdown = int(dictionary[0]['selfdestructcountdown'])   # INT_()
            except:
                print('SKIPPING...' + str('selfdestructcountdown'))
            try:
                new_unit_fbi.ShootMe = int(dictionary[0]['ShootMe'])   # INT_()
            except:
                print('SKIPPING...' + str('ShootMe'))
            try:
                new_unit_fbi.ShowPlayerName = int(dictionary[0]['ShowPlayerName'])   # INT_()
            except:
                print('SKIPPING...' + str('ShowPlayerName'))
            try:
                new_unit_fbi.Side = dictionary[0]['Side']
            except:
                print('SKIPPING...' + str('Side'))
            try:
                new_unit_fbi.SightDistance = int(dictionary[0]['SightDistance'])   # INT_()
            except:
                print('SKIPPING...' + str('SightDistance'))
            try:
                new_unit_fbi.SonarDistance = int(dictionary[0]['SonarDistance'])   # INT_()
            except:
                print('SKIPPING...' + str('SonarDistance'))
            try:
                new_unit_fbi.SonarDistanceJam = int(dictionary[0]['SonarDistanceJam'])   # INT_()
            except:
                print('SKIPPING...' + str('SonarDistanceJam'))
            try:
                new_unit_fbi.sortbias = int(dictionary[0]['sortbias'])   # INT_()
            except:
                print('SKIPPING...' + str('sortbias'))
            try:
                new_unit_fbi.SoundCategory = dictionary[0]['SoundCategory']
            except:
                print('SKIPPING...' + str('SoundCategory'))
            try:
                new_unit_fbi.SpanishDescription = dictionary[0]['SpanishDescription']
            except:
                print('SKIPPING...' + str('SpanishDescription'))
            try:
                new_unit_fbi.SpanishName = dictionary[0]['SpanishName']
            except:
                print('SKIPPING...' + str('SpanishName'))
            try:
                new_unit_fbi.StandingFireOrder = int(dictionary[0]['StandingFireOrder'])   # INT_()
            except:
                print('SKIPPING...' + str('StandingFireOrder'))
            try:
                new_unit_fbi.StandingMoveOrder = int(dictionary[0]['StandingMoveOrder'])   # INT_()
            except:
                print('SKIPPING...' + str('StandingMoveOrder'))
            try:
                new_unit_fbi.Stealth = int(dictionary[0]['Stealth'])   # INT_()
            except:
                print('SKIPPING...' + str('Stealth'))
            try:
                new_unit_fbi.SteeringMode = int(dictionary[0]['SteeringMode'])   # INT_()
            except:
                print('SKIPPING...' + str('SteeringMode'))
            try:
                new_unit_fbi.TEDClass = dictionary[0]['TEDClass']
            except:
                print('SKIPPING...' + str('TEDClass'))
            try:
                new_unit_fbi.teleporter = int(ictionary[0]['teleporter'])   # INT_()
            except:
                print('SKIPPING...' + str('teleporter'))
            try:
                new_unit_fbi.ThreeD = int(dictionary[0]['ThreeD'])   # INT_()
            except:
                print('SKIPPING...' + str('ThreeD'))
            try:
                new_unit_fbi.TidalGenerator = int(dictionary[0]['TidalGenerator'])   # INT_()
            except:
                print('SKIPPING...' + str('TidalGenerator'))
            try:
                new_unit_fbi.TransMaxUnits = int(dictionary[0]['TransMaxUnits'])   # INT_()
            except:
                print('SKIPPING...' + str('TransMaxUnits'))
            try:
                new_unit_fbi.transportcapacity = int(dictionary[0]['transportcapacity'])   # INT_()
            except:
                print('SKIPPING...' + str('transportcapacity'))
            try:
                new_unit_fbi.transportsize = int(dictionary[0]['transportsize'])   # INT_()
            except:
                print('SKIPPING...' + str('transportsize'))
            try:
                new_unit_fbi.TurnRate = int(dictionary[0]['TurnRate'])   # INT_()
            except:
                print('SKIPPING...' + str('TurnRate'))
            try:
                new_unit_fbi.UnitName = dictionary[0]['UnitName']
            except:
                print('SKIPPING...' + str('UnitName'))
            try:
                new_unit_fbi.UnitNumber = int(dictionary[0]['UnitNumber'])
            except:
                print('SKIPPING...' + str('UnitNumber'))
            try:
                new_unit_fbi.Upright = dictionary[0]['Upright']
            except:
                print('SKIPPING...' + str('Upright'))
            try:
                new_unit_fbi.Version = float(dictionary[0]['Version'])
            except:
                print('SKIPPING...' + str('Version'))
            try:
                new_unit_fbi.WaterLine = int(dictionary[0]['WaterLine'])   # INT_()
            except:
                print('SKIPPING...' + str('WaterLine'))
            # try:
            #     new_unit_fbi.Weapon_One = dictionary[0]['Weapon1']
            # except:
            #     print('SKIPPING...' + str('Weapon1'))
            # try:
            #     new_unit_fbi.Name_Weapon_Two = dictionary[0]['Weapon2']
            # except:
            #     print('SKIPPING...' + str('Weapon2'))
            # try:
            #     new_unit_fbi.Name_Weapon_Three = dictionary[0]['Weapon3']
            # except:
            #     print('SKIPPING...' + str('Weapon3'))
            try:
                new_unit_fbi.WindGenerator = int(dictionary[0]['WindGenerator'])   # INT_()
            except:
                print('SKIPPING...' + str('WindGenerator'))
            try:
                new_unit_fbi.WorkerTime = int(dictionary[0]['WorkerTime'])   # INT_()
            except:
                print('SKIPPING...' + str('WorkerTime'))
            try:
                new_unit_fbi.wpri_badTargetCategory = dictionary[0]['wpri_badTargetCategory']
            except:
                print('SKIPPING...' + str('wpri_badTargetCategory'))
            try:
                new_unit_fbi.wsec_badTargetCategory = dictionary[0]['wsec_badTargetCategory']
            except:
                print('SKIPPING...' + str('wsec_badTargetCategory'))
            try:
                new_unit_fbi.YardMap = dictionary[0]['YardMap']
            except:
                print('SKIPPING...' + str('YardMap'))
            # 135

            print('new_unit_fbi : ')
            print(new_unit_fbi)

            new_unit_fbi.save()

            return Response(dictionary)


        except:
            return Response(dictionary)

    def post(self, request, *args, **kwargs):
        raw_json = request.POST.dict()  # ['raw_json']

        # obj_1 = json.loads(raw_json)
        # print(json.dumps(raw_json))
        print(raw_json)
        print(request.POST)
        return Response(raw_json)




"""
        new_unit_fbi = UnitFbiData()
        new_unit_fbi._raw_json_dump = raw_json

        new_unit_fbi.Acceleration
        new_unit_fbi.ActiveWhenBuild
        new_unit_fbi.ai_limit
        new_unit_fbi.ai_weight
        new_unit_fbi.altfromsealevel
        new_unit_fbi.amphibious
        new_unit_fbi.antiweapons
        new_unit_fbi.attackrunlength
        new_unit_fbi.BMcode
        new_unit_fbi.BadTargetCategory

        new_unit_fbi.BankScale
        new_unit_fbi.BrakeRate
        new_unit_fbi.BuildAngle
        new_unit_fbi.BuildCostEnergy
        new_unit_fbi.BuildCostMetal
        new_unit_fbi.BuildTime
        new_unit_fbi.Builddistance
        new_unit_fbi.Builder
        new_unit_fbi.canattack
        new_unit_fbi.CanCapture

        new_unit_fbi.CanDgun
        new_unit_fbi.Canfly
        new_unit_fbi.canguard
        new_unit_fbi.canhover
        new_unit_fbi.canload
        new_unit_fbi.canmove
        new_unit_fbi.canpatrol
        new_unit_fbi.CanReclamate
        new_unit_fbi.canstop
        new_unit_fbi.cantbetransported

        new_unit_fbi.Category
        new_unit_fbi.CloakCost
        new_unit_fbi.CloakCostMoving
        new_unit_fbi.Commander
        new_unit_fbi.Copyright
        new_unit_fbi.Corpse
        new_unit_fbi.cruisealt
        new_unit_fbi.DamageModifier
        new_unit_fbi.DefaultMissionType
        new_unit_fbi.Description

        new_unit_fbi.Designation
        new_unit_fbi.digger
        new_unit_fbi.Downloadable
        new_unit_fbi.EnergyMake
        new_unit_fbi.EnergyStorage
        new_unit_fbi.EnergyUse
        new_unit_fbi.ExplodeAs
        new_unit_fbi.ExtractsMetal
        new_unit_fbi.firestandorders
        new_unit_fbi.Floater
        # 50

        new_unit_fbi.FootprintX
        new_unit_fbi.FootprintZ
        new_unit_fbi.FrenchDescription
        new_unit_fbi.FrenchName
        new_unit_fbi.GermanDescription
        new_unit_fbi.GermanName
        new_unit_fbi.HealTime
        new_unit_fbi.HideDamage
        new_unit_fbi.HoverAttack
        new_unit_fbi.ImmuneToParalyzer

        new_unit_fbi.init_cloaked
        new_unit_fbi.IsAirBase
        new_unit_fbi.IsFeature
        new_unit_fbi.istargetingupgrade
        new_unit_fbi.ItalianDescription
        new_unit_fbi.ItalianName
        new_unit_fbi.JapanesDescription
        new_unit_fbi.JapaneseName
        new_unit_fbi.kamikaze
        new_unit_fbi.kamikazedistance

        new_unit_fbi.MakesMetal
        new_unit_fbi.maneuverleashlength
        new_unit_fbi.MaxDamage
        new_unit_fbi.MaxSlope
        new_unit_fbi.MaxVelocity
        new_unit_fbi.MaxWaterDepth
        new_unit_fbi.MetalMake
        new_unit_fbi.MetalStorage
        new_unit_fbi.mincloakdistance
        new_unit_fbi.MinWaterDepth

        new_unit_fbi.MobileStandOrders
        new_unit_fbi.MoveRate1
        new_unit_fbi.MovementClass
        new_unit_fbi.Name
        new_unit_fbi.NoAutoFire
        new_unit_fbi.NoChaseCategory
        new_unit_fbi.norestrict
        new_unit_fbi.NoShadow
        new_unit_fbi.Objectname
        new_unit_fbi.onoffable

        new_unit_fbi.Ovradjust
        new_unit_fbi.PigLatinDescription
        new_unit_fbi.PigLatinName
        new_unit_fbi.PitchScale
        new_unit_fbi.RadarDistance
        new_unit_fbi.RadarDistanceJam
        new_unit_fbi.Scale
        new_unit_fbi.SelfDestructAs
        new_unit_fbi.selfdestructcountdown
        new_unit_fbi.ShootMe
        # 100

        new_unit_fbi.ShowPlayerName
        new_unit_fbi.Side
        new_unit_fbi.SightDistance
        new_unit_fbi.SonarDistance
        new_unit_fbi.SonarDistanceJam
        new_unit_fbi.sortbias
        new_unit_fbi.SoundCategory
        new_unit_fbi.SpanishDescription
        new_unit_fbi.SpanishName
        new_unit_fbi.StandingFireOrder

        new_unit_fbi.StandingMoveOrder
        new_unit_fbi.Stealth
        new_unit_fbi.SteeringMode
        new_unit_fbi.TEDClass
        new_unit_fbi.teleporter
        new_unit_fbi.ThreeD
        new_unit_fbi.TidalGenerator
        new_unit_fbi.TransMaxUnits
        new_unit_fbi.transportcapacity
        new_unit_fbi.transportsize

        new_unit_fbi.TurnRate
        new_unit_fbi.UnitName
        new_unit_fbi.Upright
        new_unit_fbi.Version
        new_unit_fbi.WaterLine

        new_unit_fbi.Weapon_One
        new_unit_fbi.Name_Weapon_Two
        new_unit_fbi.Name_Weapon_Three
        new_unit_fbi.WindGenerator
        new_unit_fbi.WorkerTime
        new_unit_fbi.wpri_badTargetCategory
        new_unit_fbi.wsec_badTargetCategory
        new_unit_fbi.YardMap
        # 135

"""










# Create your views here.
def getUnitFbiUsingId(request):
    permission_classes = (AllowAny,)
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
        printKeyValuePair('oh shit', 'an error has occured.')
        json_response = {
            "raw_fbi_file": "...."
        }
        return Response(json_response)

"""

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

"""






# AutoCollectStatic
class ApiNavigationUrls(APIView):
    permission_classes = (AllowAny,)
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
    permission_classes = (AllowAny,)
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
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        msg = str(request.GET['msg'])
        html = '<md-toast><span class="md-toast-text" flex>' + msg + '</span><md-button class="md-highlight" ng-click="openMoreInfo($event)">More info</md-button><md-button ng-click="closeToast()">Close</md-button></md-toast>'
        return HttpResponse(html)



class ExecuteBash(APIView):
    permission_classes = (AllowAny,)
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





class OpenTotalAnnihilationFBIFileII(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        mod_name = str(request.GET['mod_name'])
        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ')
        file_name = str(request.GET['file_name'])
        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪')
        directory_name = 'units'
        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ')
        file_path = '/usr/src/persistent/media/ta_data/' + mod_name + '/' + directory_name + '/' + file_name + '.fbi'
        print(' ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ %s ' % file_path)
        f3 = open(file_path, 'r', errors='replace')
        print('5 ✪ ✪ ✪ ✪ ✪ ✪ ✪ ✪ ')
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


"""
class ExecuteBash_LS_AllCustomModFilesOld(APIView):
    def get(self, request, format=None):

        final_obj = {}

        # mod_name = request.GET['mod_name']
        directory_str = '/usr/src/persistent/media/ta_data'

        # community mods:
        # /usr/src/persistent/media/ta_data/

        mod_paths = {}
        uploaded_data_files = TotalAnnihilationUploadedFile.objects.all()
        for data_file in uploaded_data_files:
            print("data_file %s" % data_file)
            if os.path.isdir(data_file.system_path):
                ls_current_modpath = str(subprocess.check_output(['ls', data_file.system_path]))

                parsed_1 = ls_current_modpath.replace("\\n'","")
                dirs_in_mod = parsed_1.replace("b'","").split('\\n')

                print("parsed_1 %s" % parsed_1)
                print("dirs_in_mod : ")
                mod_paths['system_path'] = data_file.system_path
                listed_data_files = {}
                # listed_data_files['system_path'] = data_file.system_path
                for mod_item in dirs_in_mod:
                    listed_data_files[mod_item] = []
                    print("mod_item : %s" % mod_item)
                    mod_item_path = data_file.system_path + '/' + mod_item
                    if os.path.isdir(mod_item_path):
                        ls_current_submodpath = str(subprocess.check_output(['ls', mod_item_path]))
                        sub_parsed_1 = ls_current_submodpath.replace("\\n'", "")
                        sub_parsed_2 = sub_parsed_1.replace("b'", "")
                        listed_data_files[mod_item].append(sub_parsed_2.split('\\n'))

                mod_paths[data_file.system_path] = listed_data_files #parsed_2.split('\\n')
            # mod_paths.append(data_file.system_path)


        result1 = str(subprocess.check_output(['ls', directory_str]))
        final_obj[directory_str] = str(result1).split('\\n')
        final_obj[directory_str][0] = final_obj[directory_str][0].replace("b'", "")

        context = {'root_items': final_obj, 'mod_paths': mod_paths}
        return Response(context)




class ExecuteBash_LS_AllCustomModFilesII(APIView):
    def get(self, request, format=None):

        final_obj = {}

        # mod_name = request.GET['mod_name']
        directory_str = '/usr/src/persistent/media/ta_data'

        # community mods:
        # /usr/src/persistent/media/ta_data/

        mod_paths = {}
        uploaded_data_files = TotalAnnihilationUploadedFile.objects.all()
        i = 0
        for data_file in uploaded_data_files:
            print("data_file %s" % data_file)
            if os.path.isdir(data_file.system_path):
                ls_current_modpath = str(subprocess.check_output(['ls', data_file.system_path]))

                parsed_1 = ls_current_modpath.replace("\\n'","")
                dirs_in_mod = parsed_1.replace("b'","").split('\\n')

                print("parsed_1 %s" % parsed_1)
                print("dirs_in_mod : ")
                mod_paths['system_path'] = data_file.system_path
                listed_data_files = {}
                # listed_data_files['system_path'] = data_file.system_path
                for mod_item in dirs_in_mod:
                    listed_data_files[mod_item] = []
                    print("mod_item : %s" % mod_item)
                    mod_item_path = data_file.system_path + '/' + mod_item
                    if os.path.isdir(mod_item_path):
                        ls_current_submodpath = str(subprocess.check_output(['ls', mod_item_path]))
                        sub_parsed_1 = ls_current_submodpath.replace("\\n'", "")
                        sub_parsed_2 = sub_parsed_1.replace("b'", "")
                        listed_data_files[mod_item].append(sub_parsed_2.split('\\n'))

                # mod_paths[data_file.system_path] = listed_data_files #parsed_2.split('\\n')
                try:
                    mod_paths['data_file_'+str(i)] = listed_data_files
                except:
                    print('damn...')
                i += 1
            # mod_paths.append(data_file.system_path)


        result1 = str(subprocess.check_output(['ls', directory_str]))
        final_obj[directory_str] = str(result1).split('\\n')
        final_obj[directory_str][0] = final_obj[directory_str][0].replace("b'", "")

        list_of_items_in_root = []
        for item in final_obj:
            if item != "'":
                list_of_items_in_root.append(item)

        context = {'root_items': list_of_items_in_root, 'mod_paths': mod_paths}
        return Response(context)
"""


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

    permission_classes = (AllowAny,)

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

    permission_classes = (AllowAny,)

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

    permission_classes = (AllowAny,)

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

        subcontents_to_print = '/usr/src/persistent/media/ta_data/' + mod_name
        # self.printColored(subcontents_to_print, 14)

        print('printSubContents')
        print('printSubContents')
        print('printSubContents')
        print(subcontents_to_print)
        print(subcontents_to_print)
        print(subcontents_to_print)

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
                    pathToFile = '/usr/src/persistent/media/ta_data/' + mod_name + '/unitpics' + '/' + filename + '.pcx'

                    # self.printColored('GOING TO GET CONTENTS OF: ', 11)
                    # self.printColoredFile(mod_name, filename, 15, 3)
                    unit_fbi = ReadUnitFbi().get(mod_name, filename)

                    print('filename')
                    print(filename)

                    try:
                        img = Image.open(pathToFile)
                        imgSaveTo = '/usr/src/persistent/media/ta_data/' + mod_name + '/unitpics' + '/' + filename + '.png'
                        img.save(imgSaveTo, format='png')

                        self.jsonResponse.append(
                            {
                                'thumbnail': '/media/ta_data/' + mod_name + '/unitpics/' + filename + '.png',
                                'object_name': filename,
                                'system_location': imgSaveTo,
                                'fbi_file': '/media/ta_data/' + mod_name + '/units/' + filename + '.fbi',
                                'unit_data': unit_fbi,
                                'RESTful_unit_data': 'http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=' + mod_name + '&unit_id=' + filename
                            }
                        )

                        print('JSON Response So Far...')
                        print(self.unit_fbi_final)

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
        print('printContents')
        print('printContents')
        print('printContents')
        print(mod_path)
        print(mod_path)
        print(mod_path)
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
            print('dirnames')
            print(dirnames)
            for path in dirnames:
            #     self.printColored(str(path), 13)
                self.printSubContents(path, mod_name)
            break


    def getUnitInfo(self, unitId):
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


    def get(self, request, format=None):

        return Response('greetings!')
        # try:
            # try:
            #     should_get_user_content = str(request.GET['should_get_user_content'])
            #     mod_path = '/usr/src/persistent/media/ta_data/' + str(request.GET['mod_name']) + '/'
            #     mod_name = str(request.GET['mod_name'])
            #     self.printContents(mod_path, mod_name)
            #     print('☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
            #     print(mod_path)
      