from django.shortcuts import render

# Create your views here.
# MAIN
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, generics
# from cinicraft_home.serializers import GroupSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from subprocess import Popen, PIPE
import platform
# file listing stuff
import os
from os import walk
from os import listdir
from os.path import isfile, join
from PIL import Image
import json
import re
from rest_framework.permissions import IsAuthenticated, AllowAny
from GeneralWebsiteInfo.models import WebsiteColorTheme
from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF, SoundSetTDF
from django.core import serializers
from LazarusII.FbiData import remove_comments
from rest_framework import status
import codecs

# from lazarus.dependency_data_extractor import WeaponTDFFetch, FeatureTDFFetch, DownloadTDFFetch, SoundTDFFetch




class WeaponTDFFetch():
    def getUsingString(self, strTdf):
        print('BAD TDF FETCH FUNCTION IS BEING CALLED SON! ! ! ')
        return strTdf


    def get(self, file_path):
        tdf_without_comments = ''
        try:
            f3 = codecs.open(file_path, 'r', errors='replace')
            tdf_without_comments = remove_comments(f3.read()).strip().replace('\n', '').replace('\t', '')
        except:
            f3 = open(file_path, 'r', errors='replace')
            tdf_without_comments = remove_comments(f3.read()).strip().replace('\n', '').replace('\t', '')
        # print(tdf_without_comments)
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
                        # print('IS NESTED: ')
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
            # print('PARSING BASE')
            # print(parsed_12)
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
                        # print('GETTING NESTED TYPE')
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
                        pass
                        # print('GETTING BASE TYPE')
                        # print(obj_name.replace('[', ''))
                    return obj_name.replace('[', '')
                    i += 1
        dict_list = []
        _tdf_prep = tdf_without_comments.replace(';}}[', ';}}|[')
        split_tdf = _tdf_prep.split('|')
        for item in split_tdf:
            tdf_without_comments1 = (item)

            nested_obj = parseNested(tdf_without_comments1.replace('\t', ''), getNestedType(tdf_without_comments1))
            base_obj = parseBase(tdf_without_comments1.replace(nested_obj, ''), getBaseType(tdf_without_comments1))

            baseobjectkeyname = getBaseType(tdf_without_comments1)
            dictionary = {}
            try:
                dictionary = json.loads(base_obj)
            except:
                repairattempt1 = base_obj.replace(', " }', ' }')
                dictionary = json.loads(repairattempt1)

            dictionary[getNestedType(tdf_without_comments1)] = json.loads(
                parseBase(nested_obj, getNestedType(tdf_without_comments1)))
            dictionary['_REFERENCE_POINTER'] = baseobjectkeyname
            dict_list.append(dictionary)
            new_weapon_tdf = WeaponTDF()
            new_weapon_tdf._DEV_root_data_path = file_path
            try:
                new_weapon_tdf._OBJECT_KEY_NAME = baseobjectkeyname
                new_weapon_tdf._Lazarus_Identifier = baseobjectkeyname + '_' + dictionary['ID']
            except:
                pass
            try:
                new_weapon_tdf.accuracy = int(dictionary['accuracy'])
            except:
                pass
            try:
                new_weapon_tdf.aimrate = int(dictionary['aimrate'])
            except:
                pass
            try:
                new_weapon_tdf.areaofeffect = int(dictionary['areaofeffect'])
            except:
                pass
            try:
                new_weapon_tdf.ballistic = int(dictionary['ballistic'])
            except:
                pass
            try:
                new_weapon_tdf.beamweapon = int(dictionary['beamweapon'])
            except:
                pass
            try:
                new_weapon_tdf.burnblow = int(dictionary['burnblow'])
            except:
                pass
            try:
                new_weapon_tdf.burst = int(dictionary['burst'])
            except:
                pass
            try:
                new_weapon_tdf.burstrate = float(dictionary['burstrate'])
            except:
                pass
            try:
                new_weapon_tdf.color = int(dictionary['color'])
            except:
                pass
            try:
                new_weapon_tdf.color2 = int(dictionary['color2'])
            except:
                pass
            try:
                new_weapon_tdf.commandfire = int(dictionary['commandfire'])
            except:
                pass
            try:
                new_weapon_tdf.cruise = int(dictionary['cruise'])
            except:
                pass
            try:
                new_weapon_tdf.dropped = int(dictionary['dropped'])
            except:
                pass
            try:
                new_weapon_tdf.duration = float(dictionary['duration'])
            except:
                pass
            try:
                new_weapon_tdf.edgeeffectiveness = float(dictionary['edgeeffectiveness'])
            except:
                pass
            try:
                new_weapon_tdf.endsmoke = int(dictionary['endsmoke'])
            except:
                pass
            try:
                new_weapon_tdf.energy = int(dictionary['energy'])
            except:
                pass
            try:
                new_weapon_tdf.energypershot = int(dictionary['energypershot'])
            except:
                pass
            try:
                new_weapon_tdf.explosionart = int(dictionary['explosionart'])
            except:
                pass
            try:
                new_weapon_tdf.explosiongaf = int(dictionary['explosiongaf'])
            except:
                pass
            try:
                new_weapon_tdf.firestarter = int(dictionary['firestarter'])
            except:
                pass
            try:
                new_weapon_tdf.flighttime = int(dictionary['flighttime'])
            except:
                pass
            try:
                new_weapon_tdf.groundbounce = int(dictionary['groundbounce'])
            except:
                pass
            try:
                new_weapon_tdf.guidance = int(dictionary['guidance'])
            except:
                pass
            try:
                new_weapon_tdf.ID_weapon = int(dictionary['ID'])
            except:
                pass
            try:
                new_weapon_tdf.lavaexplosionart = dictionary['lavaexplosionart']
            except:
                pass
            try:
                new_weapon_tdf.lavaexplosiongaf = dictionary['lavaexplosiongaf']
            except:
                pass
            try:
                new_weapon_tdf.lineofsight = int(dictionary['lineofsight'])
            except:
                pass
            try:
                new_weapon_tdf.metal = int(dictionary['metal'])
            except:
                pass
            try:
                new_weapon_tdf.metalpershot = int(dictionary['metalpershot'])
            except:
                pass
            try:
                new_weapon_tdf.meteor = int(dictionary['meteor'])
            except:
                pass
            try:
                new_weapon_tdf.minbarrelangle = int(dictionary['minbarrelangle'])
            except:
                pass
            try:
                new_weapon_tdf.model = dictionary['model']
            except:
                pass
            try:
                new_weapon_tdf.name = dictionary['name']
            except:
                pass
            try:
                new_weapon_tdf.noautorange = int(dictionary['noautorange'])
            except:
                pass
            try:
                new_weapon_tdf.noexplode = int(dictionary['noexplode'])
            except:
                pass
            try:
                new_weapon_tdf.noradar = int(dictionary['noradar'])
            except:
                pass
            try:
                new_weapon_tdf.paralyzer = int(dictionary['paralyzer'])
            except:
                pass
            try:
                new_weapon_tdf.pitchtolerance = int(dictionary['pitchtolerance'])
            except:
                pass
            try:
                new_weapon_tdf.propeller = int(dictionary['propeller'])
            except:
                pass
            try:
                new_weapon_tdf.randomdecay = int(dictionary['randomdecay'])
            except:
                pass
            try:
                new_weapon_tdf._range = int(dictionary['range'])
            except:
                pass
            try:
                new_weapon_tdf.reloadtime = float(dictionary['reloadtime'])
            except:
                pass
            try:
                new_weapon_tdf.rendertype = int(dictionary['rendertype'])
            except:
                pass
            try:
                new_weapon_tdf.selfprop = int(dictionary['selfprop'])
            except:
                pass
            try:
                new_weapon_tdf.shakeduration = int(dictionary['shakeduration'])
            except:
                pass
            try:
                new_weapon_tdf.shakemagnitudee = int(dictionary['shakemagnitudee'])
            except:
                pass
            try:
                new_weapon_tdf.smokedelay = int(dictionary['smokedelay'])
            except:
                pass
            try:
                new_weapon_tdf.smoketrail = int(dictionary['smoketrail'])
            except:
                pass
            try:
                new_weapon_tdf.soundhit = int(dictionary['soundhit'])
            except:
                pass
            try:
                new_weapon_tdf.soundstart = dictionary['soundstart']
            except:
                pass
            try:
                new_weapon_tdf.soundtrigger = int(dictionary['soundtrigger'])
            except:
                pass
            try:
                new_weapon_tdf.soundwater = dictionary['soundwater']
            except:
                pass
            try:
                new_weapon_tdf.sprayangle = int(dictionary['sprayangle'])
            except:
                pass
            try:
                new_weapon_tdf.startsmoke = int(dictionary['startsmoke'])
            except:
                pass
            try:
                new_weapon_tdf.startvelocity = int(dictionary['startvelocity'])
            except:
                pass
            try:
                new_weapon_tdf.stockpile = int(dictionary['stockpile'])
            except:
                pass
            try:
                new_weapon_tdf.targetable = int(dictionary['targetable'])
            except:
                pass
            try:
                new_weapon_tdf.tolerance = int(dictionary['tolerance'])
            except:
                pass
            try:
                new_weapon_tdf.tracks = int(dictionary['tracks'])
            except:
                pass
            try:
                new_weapon_tdf.turnrate = int(dictionary['turnrate'])
            except:
                pass
            try:
                new_weapon_tdf.turrent = int(dictionary['turrent'])
            except:
                pass
            try:
                new_weapon_tdf.twophase = int(dictionary['twophase'])
            except:
                pass
            try:
                new_weapon_tdf.unitsonly = int(dictionary['unitsonly'])
            except:
                pass
            try:
                new_weapon_tdf.vlaunch = int(dictionary['vlaunch'])
            except:
                pass
            try:
                new_weapon_tdf.waterexplosionart = dictionary['waterexplosionart']
            except:
                pass
            try:
                new_weapon_tdf.waterexplosiongaf = dictionary['waterexplosiongaf']
            except:
                pass
            try:
                new_weapon_tdf.waterweapon = int(dictionary['waterweapon'])
            except:
                pass
            try:
                new_weapon_tdf.weaponacceleration = int(dictionary['weaponacceleration'])
            except:
                pass
            try:
                new_weapon_tdf.weapontimer = float(dictionary['weapontimer'])
            except:
                pass
            try:
                new_weapon_tdf.weapontype2 = dictionary['weapontype2']
            except:
                pass
            try:
                new_weapon_tdf.weaponvelocity = int(dictionary['weaponvelocity'])
            except:
                pass
            try:
                print(dictionary['DAMAGE'])
            except:
                pass

            try:
                new_weapon_tdf.save()
                list_dmg = []
                for key, value in dictionary['DAMAGE'].items():
                    new_damage_obj = Damage(name=key, damage_amount=value)
                    new_damage_obj.weapon_id = new_weapon_tdf.id
                    new_damage_obj.save()
                    list_dmg.append(new_damage_obj)
                for dmg in list_dmg:
                    new_weapon_tdf.damage.add(dmg)
                new_weapon_tdf.save()
            except:
                pass
                # print(bcolors.darkgrey + 'Skipping Add TDF Weapon To SQL' + bcolors.ENDC)
                # return (dict_list)

            # print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')
            # print((dict_list))
            # print('✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ')

        return (dict_list)






class FeatureTDFFetch():
    def get(self, file_path):
        f3 = open(file_path, 'r', errors='replace')

        # print("OPENING DOWNLOAD TDF... ")
        incoming_tdf = remove_comments(f3.read())
        # print(incoming_tdf)
        # print('TDF Opened Successfully ! ! !')

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

        # print('TDF PREPPED AND READY FOR JSONIFYING: ')
        # print(_tdf_prep)
        # print('______________________________________')

        split_tdf = _tdf_prep.split('|')

        for item in split_tdf:
            nested_obj = parseNested(item, getNestedType(item))
            # print(nested_obj)

        for item in split_tdf:
            nested_type = getNestedType(item)
            # print("NESTED TYPE:  " + nested_type)
            nested_obj = parseNested(item, nested_type)
            # print(nested_obj)
            dictionary = json.loads(nested_obj)
            dictionary['Object_Name'] = nested_type
            dict_list.append(dictionary)

        # print('JSON DUMPS: ')
        # print(json.dumps(dict_list))

        arrayOfNewFeatures = []
        ##### SAVE TO SQL:
        for item in dict_list:
            new_feature = FeatureTDF()
            new_feature._DEV_root_data_path = file_path
            ### 37
            try:
                new_feature.animating = item['animating']
            except:
                pass
            try:
                new_feature.animtrans = item['animtrans']
            except:
                pass
            try:
                new_feature.autoreclaimable = item['autoreclaimable']
            except:
                pass
            try:
                new_feature.burnmax = item['burnmax']
            except:
                pass
            try:
                new_feature.burnmin = item['burnmin']
            except:
                pass
            try:
                new_feature.burnweapon = item['burnweapon']
            except:
                pass
            try:
                new_feature.category = item['category']
            except:
                pass
            try:
                new_feature.description = item['description']
            except:
                pass
            try:
                new_feature.blocking = item['blocking']
            except:
                pass
            try:
                new_feature.damage = item['damage']
            except:
                pass
            try:
                new_feature.energy = item['energy']
            except:
                pass
            try:
                new_feature.featuredead = item['featuredead']
            except:
                pass
            try:
                new_feature.featurereclamate = item['featurereclamate']
            except:
                pass
            try:
                new_feature.filename = item['filename']
            except:
                pass
            try:
                new_feature.flamable = item['flamable']
            except:
                pass
            try:
                new_feature.footprintx = item['footprintx']
            except:
                pass
            try:
                new_feature.footprintz = item['footprintz']
            except:
                pass
            try:
                new_feature.geothermal = item['geothermal']
            except:
                pass
            try:
                new_feature.height = item['height']
            except:
                pass
            try:
                new_feature.hitdensity = item['hitdensity']
            except:
                pass
            try:
                new_feature.indestructible = item['indestructible']
            except:
                pass
            try:
                new_feature.metal = item['metal']
            except:
                pass
            try:
                new_feature.nodisplayinfo = item['nodisplayinfo']
            except:
                pass
            try:
                new_feature._object = item['object']
            except:
                pass
            try:
                new_feature.permanent = item['permanent']
            except:
                pass
            try:
                new_feature.reclaimable = item['reclaimable']
            except:
                pass
            try:
                new_feature.reproduce = item['reproduce']
            except:
                pass
            try:
                new_feature.reproducearea = item['reproducearea']
            except:
                pass
            try:
                new_feature.seqname = item['seqname']
            except:
                pass
            try:
                new_feature.seqnameburn = item['seqnameburn']
            except:
                pass
            try:
                new_feature.seqnamedie = item['seqnamedie']
            except:
                pass
            try:
                new_feature.seqnamereclamate = item['seqnamereclamate']
            except:
                pass
            try:
                new_feature.seqnameshad = item['seqnameshad']
            except:
                pass
            try:
                new_feature.shadtrans = item['shadtrans']
            except:
                pass
            try:
                new_feature.sparktime = item['sparktime']
            except:
                pass
            try:
                new_feature.spreadchance = item['spreadchance']
            except:
                pass
            try:
                new_feature.world = item['world']
            except:
                pass
            try:
                arrayOfNewFeatures.append(new_feature)
                new_feature.save()
                status_code = status.HTTP_201_CREATED
            except:
                pass
        return arrayOfNewFeatures




class DownloadTDFFetch():
    def get(self, file_path):
        f3 = open(file_path, 'r', errors='replace')

        # print("OPENING DOWNLOAD TDF... ")
        incoming_tdf = remove_comments(f3.read())
        # print(incoming_tdf)
        # print('TDF Opened Successfully ! ! !')

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

        # print('TDF PREPPED AND READY FOR JSONIFYING: ')
        # print(_tdf_prep)
        # print('______________________________________')

        split_tdf = _tdf_prep.split('|')

        for item in split_tdf:
            nested_obj = parseNested(item, getNestedType(item))
            print(nested_obj)

        for item in split_tdf:
            nested_type = getNestedType(item)
            # print("NESTED TYPE:  " + nested_type)
            nested_obj = parseNested(item, nested_type)
            # print(nested_obj)
            dictionary = json.loads(nested_obj)
            dictionary['Object_Name'] = nested_type
            dict_list.append(dictionary)

        # print('JSON DUMPS: ')
        # print(json.dumps(dict_list))

        ## SAVE TO SQL:
        for item in dict_list:
            new_download = DownloadTDF()
            new_download._DEV_root_data_path = file_path
            get_pk_unit = UnitFbiData.objects.filter(UnitName__iexact=item['UNITNAME'])
            new_download.parent_unit = get_pk_unit[0]
            new_download.MENUENTRY = item['Object_Name']
            new_download.BUTTON = item['BUTTON']
            new_download.MENU = item['MENU']
            new_download.UNITMENU = item['UNITMENU']
            new_download.UNITNAME = item['UNITNAME']
            new_download.save()

        return dict_list




class SoundTDFFetch():
    def get(self, sounds_str):
        # print("OPENING DOWNLOAD TDF... ")
        incoming_tdf = remove_comments(sounds_str)
        # print(incoming_tdf)
        # print('TDF Opened Successfully ! ! !')

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

        # print('TDF PREPPED AND READY FOR JSONIFYING: ')
        # print(_tdf_prep)
        # print('______________________________________')

        split_tdf = _tdf_prep.split('|')

        for item in split_tdf:
            nested_obj = parseNested(item, getNestedType(item))
            print(nested_obj)

        for item in split_tdf:
            nested_type = getNestedType(item)
            # print("NESTED TYPE:  " + nested_type)
            nested_obj = parseNested(item, nested_type)
            # print(nested_obj)
            dictionary = json.loads(nested_obj)
            dictionary['Object_Name'] = nested_type
            dict_list.append(dictionary)

        print('JSON DUMPS: ')
        print(json.dumps(dict_list))

        ## SAVE TO SQL:
        for item in dict_list:
            new_sound = SoundSetTDF()
            try:
                new_sound.ok1 = item['ok1']
            except:
                pass
            try:
                new_sound.cant1 = item['cant1']
            except:
                pass
            try:
                new_sound.build = item['build']
            except:
                pass
            try:
                new_sound.cloak = item['cloak']
            except:
                pass
            try:
                new_sound.repair = item['repair']
            except:
                pass
            try:
                new_sound.select1 = item['select1']
            except:
                pass
            try:
                new_sound.Capture = item['Capture']
            except:
                pass
            try:
                new_sound.working = item['working']
            except:
                pass
            try:
                new_sound.arrived1 = item['arrived1']
            except:
                pass
            try:
                new_sound.activate = item['activate']
            except:
                pass
            try:
                new_sound.ballistic = item['ballistic']
            except:
                pass
            try:
                new_sound.deactivate = item['deactivate']
            except:
                pass
            try:
                new_sound.underattack = item['underattack']
            except:
                pass
            try:
                new_sound.unitcomplete = item['unitcomplete']
            except:
                pass
            try:
                new_sound.canceldestruct = item['canceldestruct']
            except:
                pass
            try:
                new_sound.count0 = item['count0']
            except:
                pass
            try:
                new_sound.count1 = item['count1']
            except:
                pass
            try:
                new_sound.count2 = item['count2']
            except:
                pass
            try:
                new_sound.count3 = item['count3']
            except:
                pass
            try:
                new_sound.count4 = item['count4']
            except:
                pass
            try:
                new_sound.count5 = item['count5']
            except:
                pass
            try:
                new_sound._OBJECT_KEY_NAME = item['Object_Name']
            except:
                pass
            try:
                new_sound.save()
                print('SAVING: ' + item['Object_Name'])
            except:
                print('SKIPPING: ' + item['Object_Name'])


        return dict_list




class bcolors:
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






    # ok1
    # cant1
    # build
    # cloak
    # repair
    # select1

    # Capture
    # working
    # arrived1
    # activate
    # ballistic

    # deactivate

    # underattack
    # unitcomplete
    # canceldestruct
    # count0
    # count1
    # count2
    # count3
    # count4
    # count5
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif value == '':
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d  # For convenience



class DependenciesForUnitFBI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        uid = request.GET['uid']
        sampleunit = UnitFbiData.objects.filter(UnitName=uid)
        serialized_obj = serializers.serialize("json", sampleunit)
        json_dict = json.loads(serialized_obj)
        print('SAMPLE UNIT QUERIED: ')
        print(sampleunit)
        ## NEED TO GRAB THE
        dev_root_path = sampleunit[0]._DEV_root_data_path
        last_occurance_of_slash = dev_root_path.rfind("/")
        fbi_file = dev_root_path[last_occurance_of_slash:]
        # THE ROOT PATH OF THE UNIT HPI
        path_without_fbi = dev_root_path.replace(fbi_file, '').replace('/units', '')
        unit_weapon_path = ''
        # WE NEED THIS TO KNOW WHERE TO LOOK FOR ALL DEPENDENCIES.

        # SO NOW WE HAVE THIS:
        # '/usr/src/persistent/media/ta_data/arm_fubar/'
        # BEGIN SCANNING THE FBI FILE TO LOCATE ALL DEPENDENCIES
        #
        # keys used to find dependencies:
        # -------------------------------
        # Objectname        ->  /arm_fubar/objects3d/{ Objectname }
        #                       /arm_fubar/scripts/{ Objectname }
        # UnitName          ->  /arm_fubar/unitpics/{ UnitName }
        #                       /arm_fubar/download/{ UnitName }
        # SoundCategory     -> SOUNDS.txt
        # ExplodeAs         -> UNITS.txt
        # SelfDestructAs    -> UNITS.txt
        # Corpse            -> /arm_fubar/features/corpses/{ UnitName }
        # Weapon1           -> /arm_fubar/weapons/{ UnitName }
        # Weapon2           -> /arm_fubar/weapons/{ UnitName }
        # Weapon3           -> /arm_fubar/weapons/{ UnitName }
        # -------------------------------

        print('\n\n\n\n')

        #   /usr/src/persistent/media/ta_data/arm_fubar : /armdef.fbi
        definer = bcolors.purple + \
                  path_without_fbi + \
                  ' : ' + bcolors.ENDC
        end_val = bcolors.orange + \
                  fbi_file + \
                  bcolors.ENDC
        print(definer + end_val)


        ### DEPENDENCIES CHECKLIST:
        dp_unitpic = False
        dp_3dmodel = False
        dp_script = False
        dp_corpses = False
        dp_allweapons = False
        dp_download = False

        this_unit_has_weapons = False

        print('')
        # UnitName
        definer = bcolors.TEAL + \
                  'UnitName' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '       ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.orange + \
                  sampleunit[0].UnitName + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        unit_pic_path = path_without_fbi + '/unitpics/'
        uname = sampleunit[0].UnitName.lower()
        # /ta_data/UNAME/unitpics/
        dp_unitpic = os.path.exists(unit_pic_path + uname + '.pcx')
        if dp_unitpic == False:
            dp_unitpic = os.path.exists(unit_pic_path + uname.lower() + '.pcx')
        print('unit pic exists : ' + str(dp_unitpic))
        # /ta_data/UNAME/download/
        unit_download_path = path_without_fbi + '/download/' + uname + '.tdf'
        dp_download = os.path.exists(unit_download_path)
        print('unit download exists : ' + str(dp_download))
        # -------------------------------

        # Objectname
        definer = bcolors.TEAL + \
                  'Objectname' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '     ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.orange + \
                  sampleunit[0].Objectname + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # /ta_data/UNAME/objects3d/
        unit_3do_path = path_without_fbi + '/objects3d/'
        uobjname = sampleunit[0].Objectname.lower()
        dp_3dmodel = os.path.exists(unit_3do_path + uobjname + '.3do')
        print('unit 3do exists : ' + str(dp_3dmodel))
        # /ta_data/UNAME/scripts/
        unit_cob_path = path_without_fbi + '/scripts/'
        ucobname = sampleunit[0].Objectname.lower()
        dp_script = os.path.exists(unit_cob_path + ucobname + '.cob')
        print('unit cob exists : ' + str(dp_script))
        # -------------------------------


        # SoundCategory
        definer = bcolors.TEAL + \
                  'SoundCategory' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '  ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].SoundCategory + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # -------------------------------

        # ExplodeAs
        definer = bcolors.TEAL + \
                  'ExplodeAs' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '      ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].ExplodeAs + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # -------------------------------

        # SelfDestructAs
        definer = bcolors.TEAL + \
                  'SelfDestructAs' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  ' ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].SelfDestructAs + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # -------------------------------

        # Corpse
        definer = bcolors.TEAL + \
                  'Corpse' + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '         ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  sampleunit[0].Corpse + \
                  bcolors.ENDC
        print(definer + midchar + end_val)
        # /ta_data/UNAME/features/corpses/
        corpsename = sampleunit[0].Corpse.lower()
        unit_corpse_path = path_without_fbi + '/features/corpses/' + corpsename + '.tdf'
        dp_corpses = os.path.exists(unit_corpse_path)
        print('unit feature corpse exists : ' + str(dp_corpses))
        #FeatureTDFViewset.get()
        # -------------------------------

        all_weapons = []
        try:
            # Weapon1
            if sampleunit[0].Weapon1:
                all_weapons.append(sampleunit[0].Weapon1)

            definer = bcolors.TEAL + \
                      'Weapon1' + \
                      bcolors.ENDC
            midchar = bcolors.lightgreen + \
                      '        ->  ' + \
                      bcolors.ENDC
            end_val = bcolors.lightred + \
                      sampleunit[0].Weapon1 + \
                      bcolors.ENDC
            print(definer + midchar + end_val)
            # /ta_data/UNAME/weapons/
            unit_weapon_path = path_without_fbi + '/weapons/' + uname + '_weapon.tdf'
            dp_allweapons = os.path.exists(unit_weapon_path)
            print('unit weapons exists : ' + str(dp_allweapons))
            this_unit_has_weapons = os.path.exists(unit_weapon_path)
        except:
            print('')
        # -------------------------------

        try:
            # Weapon2
            if sampleunit[0].Weapon2:
                all_weapons.append(sampleunit[0].Weapon2)

            definer = bcolors.TEAL + \
                      'Weapon2' + \
                      bcolors.ENDC
            midchar = bcolors.lightgreen + \
                      '        ->  ' + \
                      bcolors.ENDC
            end_val = bcolors.lightred + \
                      sampleunit[0].Weapon2 + \
                      bcolors.ENDC
            print(definer + midchar + end_val)
        except:
            print('')
        # -------------------------------

        try:
            # Weapon3
            if sampleunit[0].Weapon3:
                all_weapons.append(sampleunit[0].Weapon3)

            definer = bcolors.TEAL + \
                      'Weapon3' + \
                      bcolors.ENDC
            midchar = bcolors.lightgreen + \
                      '        ->  ' + \
                      bcolors.ENDC
            end_val = bcolors.lightred + \
                      sampleunit[0].Weapon3 + \
                      bcolors.ENDC
            print(definer + midchar + end_val)
        except:
            print('')
        # -------------------------------



        # FBI Unit
        try:
            definer = bcolors.blue + \
                      'Unit Object Scanned: ' + \
                      bcolors.ENDC
            midchar = bcolors.orange + \
                      ' -> ' + \
                      bcolors.ENDC
            end_val = bcolors.lightgreen + \
                      str(json_dict[0]['fields']) + \
                      bcolors.ENDC

            fbi_data = json_dict[0]['fields']
            fbijson = json.dumps(del_none(fbi_data), indent=4, sort_keys=True)

            print(bcolors.purple)
            print(fbijson)
            print(bcolors.ENDC)
        except:
            print(bcolors.red + 'Failed to scan FBI Unit ! !' + bcolors.ENDC)
        # TDF Corpse
        corpseTDF = []
        try:
            corpseTDF = FeatureTDFFetch().get(unit_corpse_path)
            definer = bcolors.blue + \
                      'Corpse Objects Scanned: ' + \
                      bcolors.ENDC
            midchar = bcolors.orange + \
                      ' -> ' + \
                      bcolors.ENDC
            end_val = bcolors.lightgreen + \
                      str(corpseTDF) + \
                      bcolors.ENDC
            tdfjson = json.dumps(del_none(corpseTDF), indent=4, sort_keys=True)

            print(bcolors.purple)
            print(tdfjson)
            print(bcolors.ENDC)
            # print(definer + midchar + end_val)
        except:
            print(bcolors.red + 'Failed to scan TDF Feature ! !' + bcolors.ENDC)
        # TDF Download

        downloadTDF = [] 
        try:
            downloadTDF = DownloadTDFFetch().get(unit_download_path)
            definer = bcolors.blue + \
                      'Download Objects Scanned: ' + \
                      bcolors.ENDC
            midchar = bcolors.orange + \
                      ' -> ' + \
                      bcolors.ENDC
            end_val = bcolors.lightgreen + \
                      str(downloadTDF) + \
                      bcolors.ENDC
            print(definer + midchar + end_val)
        except:
            print(bcolors.red + 'Failed to scan TDF Download ! !' + bcolors.ENDC)
        tdf_list = []
        # TDF Weapon
        print('THIS UNIT DOES HAVE WEAPONS ! ! !')
        if os.path.exists(unit_weapon_path):
            print(os.listdir(path_without_fbi + '/weapons/'))
            print(unit_weapon_path)
            weaponTDF = WeaponTDFFetch().get(unit_weapon_path)
            tdf_list = weaponTDF
            definer = bcolors.blue + \
                      'Weapon Objects Scanned: ' + \
                      bcolors.ENDC
            midchar = bcolors.orange + \
                      ' -> ' + \
                      bcolors.ENDC
            end_val = bcolors.lightgreen + \
                      str(weaponTDF) + \
                      bcolors.ENDC
            print(definer + midchar + end_val)
        else:
            # Weapon data with 'UNITNAME_weapon.tdf' does not exist,
            # must scan all weapons in this folder and try to find
            # the weapon that way.
            print('failed to reference weapon using the unit name: ' + path_without_fbi + '/weapons/')
            print('\nweapon TDF files avaliable in /weapons/: ')

            weaponpath = path_without_fbi + '/weapons/'
            listweaponTDFs = os.listdir(weaponpath)
            print('WEAPON PATH: ')
            print(bcolors.cyan + str(weaponpath) + bcolors.ENDC)
            print(bcolors.cyan + str(listweaponTDFs) + bcolors.ENDC)
            # loop through /weapons/ and save all weapons to SQL:
            for weaponTDF in listweaponTDFs:
                weaponpath = path_without_fbi + '/weapons/' + weaponTDF
                unit_weapon_path = weaponpath
                TDF = WeaponTDFFetch().get(weaponpath)
                definer = bcolors.blue + \
                          'Weapon Objects Scanned: ' + \
                          bcolors.ENDC
                # print(definer + bcolors.purple + str(TDF) + bcolors.ENDC)

                for _tdf in TDF:
                    tdfjson = json.dumps(del_none(_tdf), indent=4, sort_keys=True)
                    print(bcolors.blue)
                    print(tdfjson)
                    print(bcolors.ENDC)
                    tdf_list.append(_tdf)


        print('\nAll Detected weapons: ')
        print(all_weapons)
        print('\nAll Detected sound files in /sounds/: ')
        print(os.listdir(path_without_fbi + '/sounds/'))
        allsoundfiles = os.listdir(path_without_fbi + '/sounds/')

        ### DEPENDENCY TODO:
        ## UnitFbiData
        # UnitFbiData.ExplodeAs         --> WeaponTDF._REFERENCE_POINTER
        # UnitFbiData.SelfDestructAs    --> WeaponTDF._REFERENCE_POINTER

        ### DEPENDENCY CHECKLIST:
        ## UnitFbiData
        # UnitFbiData.UnitName
        #                           --> /unitpics/{UnitName}.pcx
        #                           --> /anims/{UnitName}_gadget.gaf
        # UnitFbiData.Objectname    --> /objects3d/{Objectname}.3do
        # UnitFbiData.Corpse        --> /features/corpses/{Corpse}_dead.tdf
        # UnitFbiData.Weapon1       --> /weapons/{UnitName}_weapon.tdf

        ## FeatureTDF
        # FeatureTDF.object        --> /objects3d/{object}.3do

        ## WeaponTDF
        # WeaponTDF.soundstart            --> /sounds/{soundstart}.wav
        # WeaponTDF.soundhit              --> /sounds/{soundhit}.wav
        # WeaponTDF.explosiongaf          --> /anims/{explosiongaf}.gaf
        # WeaponTDF.waterexplosiongaf     --> /anims/{explosiongaf}.gaf
        # WeaponTDF.lavaexplosiongaf      --> /anims/{explosiongaf}.gaf

        ## DownloadTDF
        # DownloadTDF.UnitName      --> UnitFbiData.UnitName
        # DownloadTDF.UnitMenu      --> UnitFbiData.UnitName

        if this_unit_has_weapons == True:
            weapon1primarykey = json_dict[0]['fields']['Weapon1']
            vanillaweaponmatchingpk = WeaponTDF.objects.filter(_OBJECT_KEY_NAME=weapon1primarykey)
            print('Does weapon1 match a Cavedog weapon? ')
            print((len(vanillaweaponmatchingpk) > 0))

        print('\nALL Dependency Keys:')
        print('UnitFbiData.UnitName : \t\t\t' + bcolors.purple + str(json_dict[0]['fields']['UnitName']) + bcolors.ENDC)
        print('UnitFbiData.Objectname : \t\t' + bcolors.purple + str(json_dict[0]['fields']['Objectname']) + bcolors.ENDC)
        print('UnitFbiData.Corpse : \t\t\t' + bcolors.purple + str(json_dict[0]['fields']['Corpse']) + bcolors.ENDC)
        if this_unit_has_weapons == True:
            print('UnitFbiData.Weapon1 : \t\t\t' + bcolors.purple + str(json_dict[0]['fields']['Weapon1']) + bcolors.ENDC)

        for tdf in corpseTDF:
            print('FeatureTDF._object : \t\t\t' + bcolors.purple + str(tdf._object) + bcolors.ENDC)
        for weaponTDF in tdf_list:
            # verify that both sounds exist in the database:
            soundstart_exists_nonCavedog = False
            soundhit_exists_nonCavedog = False
            soundstart_exists_cavedog = False
            soundhit_exists_cavedog = False
            soundstart = 'NIL'
            soundhit = 'NIL'
            try:
                soundstart = weaponTDF['soundstart']
            except:
                pass
            try:
                soundhit = weaponTDF['soundhit']
            except:
                pass
            # loop through all non-Cavedog sounds:
            for sfx in allsoundfiles:
                if soundstart.lower() == sfx.replace('.wav', ''):
                    soundstart_exists_nonCavedog = True
                if soundhit.lower() == sfx.replace('.wav', ''):
                    soundhit_exists_nonCavedog = True
            # loop through official Cavedog sounds:
            if soundstart_exists_nonCavedog == False:
                cavedog_soundstart_matches = SoundSetTDF.objects.filter(_OBJECT_KEY_NAME=soundstart)
                if len(cavedog_soundstart_matches) > 0:
                    print(soundstart + ' is an official Cavedog .wav file. ')
                    soundstart_exists_cavedog = True
            if soundhit_exists_nonCavedog == False:
                cavedog_soundhit_matches = SoundSetTDF.objects.filter(_OBJECT_KEY_NAME=soundhit)
                if len(cavedog_soundhit_matches) > 0:
                    print(soundhit + ' is an official Cavedog .wav file ')
                    soundhit_exists_cavedog = True

            print('')
            print('soundhit_exists_nonCavedog: ')
            print(soundhit_exists_nonCavedog)
            print('soundstart_exists_nonCavedog: ')
            print(soundstart_exists_nonCavedog)
            print('soundstart_exists_cavedog: ')
            print(soundstart_exists_cavedog)
            print('soundhit_exists_cavedog: ')
            print(soundhit_exists_cavedog)
            print('')

            print('WeaponTDF.soundstart : \t\t\t' + bcolors.purple + str(weaponTDF['soundstart']) + bcolors.ENDC)
            print('WeaponTDF.soundhit : \t\t\t' + bcolors.purple + str(weaponTDF['soundhit']) + bcolors.ENDC)
            try:
                print('WeaponTDF.explosiongaf : \t\t' + bcolors.purple + str(weaponTDF['explosiongaf']) + bcolors.ENDC)
            except:
                pass
            try:
                print('WeaponTDF.waterexplosiongaf : \t\t' + bcolors.purple + str(weaponTDF['waterexplosiongaf']) + bcolors.ENDC)
            except:
                pass
            try:
                print('WeaponTDF.lavaexplosiongaf : \t\t' + bcolors.purple + str(weaponTDF['lavaexplosiongaf']) + bcolors.ENDC)
            except:
                pass
        for tdf in downloadTDF:
            print('DownloadTDF.UNITMENU : \t\t\t' + bcolors.purple + str(tdf['UNITMENU']) + bcolors.ENDC)
            print('DownloadTDF.UNITNAME : \t\t\t' + bcolors.purple + str(tdf['UNITNAME']) + bcolors.ENDC)
        print('')





        dep_path_anims = '/anims/' #
        dep_path_download = '/download/' #
        dep_path_features = '/features/corpses/' #
        dep_path_objects3d = '/objects3d/' #
        dep_path_scripts = '/scripts/' #
        dep_path_sounds = '/sounds/'
        dep_path_unitpics =  '/unitpics/' #
        dep_path_units =  '/units/' #
        dep_path_weapons =  '/weapons/' #

        corpsefilename = json_dict[0]['fields']['Corpse']

        ### CHECK TO SEE IF THESE PATHS WORK
        # IF THEY DO, THEY WILL BE THE CHOSEN
        # DEPENDENCIES ASSOCIATED WITH THIS
        # 'UnitModAsset'
        animsGafPath = path_without_fbi + dep_path_anims + uname + '_gadget.gaf'            # anims     GAF
        scriptsCobPath = path_without_fbi + dep_path_scripts + uobjname + '.cob'            # scripts   COB
        unitpicsPcxPath = path_without_fbi + dep_path_unitpics + uname + '.pcx'             # unitpics  PCX
        objects3doPath = path_without_fbi + dep_path_objects3d + uobjname + '.3do'          # objects3d 3DO
        unitFbiPath = path_without_fbi + dep_path_units + uname + '.fbi'                    # units     FBI
        # unit_weapon_path                                                                  # weapons   TDF
        downloadTdfPath = path_without_fbi + dep_path_download + uname + '.tdf'                     # download  TDF
        featuresTdfPath = path_without_fbi + dep_path_features + corpsefilename.lower() + '.tdf'    # features  TDF
        # TODO: SOUNDS.TDF IS STILL INCOMPLETE ! ! !                                        # sounds    TDF

        anims_exists = bcolors.red + ' ✕ ' + bcolors.ENDC
        if os.path.exists(animsGafPath) == True:
            anims_exists = bcolors.green + ' ✓ ' + bcolors.ENDC
        # uobjname uname
        print(path_without_fbi + '' + # anims
              bcolors.green +
              dep_path_anims +
              bcolors.ENDC +
              bcolors.lightred +
              uname + '_gadget' +
              bcolors.ENDC
              + '.gaf' + anims_exists + ' !important ')

        download_exists = bcolors.red + ' ✕ ' + bcolors.ENDC
        if os.path.exists(downloadTdfPath) == True:
            download_exists = bcolors.green + ' ✓ ' + bcolors.ENDC
        print(path_without_fbi + '' +
              bcolors.green +
              dep_path_download +
              bcolors.ENDC +
              bcolors.lightred +
              uname +
              bcolors.ENDC
              + '.tdf' + download_exists)

        features_exist = bcolors.red + ' ✕ ' + bcolors.ENDC
        if os.path.exists(featuresTdfPath) == True:
            features_exist = bcolors.green + ' ✓ ' + bcolors.ENDC
        print(path_without_fbi + '' +
              bcolors.green +
              dep_path_features +
              bcolors.ENDC +
              bcolors.lightred +
              corpsefilename +
              bcolors.ENDC
              + '.tdf' + features_exist)

        objects3d_exists = bcolors.red + ' ✕ ' + bcolors.ENDC
        if os.path.exists(objects3doPath) == True:
            objects3d_exists = bcolors.green + ' ✓ ' + bcolors.ENDC
        print(path_without_fbi + '' +
              bcolors.green +
              dep_path_objects3d +
              bcolors.ENDC +
              bcolors.lightred +
              uobjname +
              bcolors.ENDC
              + '.3do' + objects3d_exists + ' !important ')

        scriptcob_exists = bcolors.red + ' ✕ ' + bcolors.ENDC
        if os.path.exists(scriptsCobPath) == True:
            scriptcob_exists = bcolors.green + ' ✓ ' + bcolors.ENDC
        print(path_without_fbi + '' +
              bcolors.green +
              dep_path_scripts +
              bcolors.ENDC +
              bcolors.lightred +
              uobjname +
              bcolors.ENDC
              + '.cob' + scriptcob_exists + ' !important ')

        sounds_exist = bcolors.red + ' ✕ ' + bcolors.ENDC
        print(path_without_fbi + '' +
              bcolors.green +
              dep_path_sounds +
              bcolors.ENDC +
              bcolors.lightred +
              uname +
              bcolors.ENDC
              + '.wav')

        unitpic_exists = bcolors.red + ' ✕ ' + bcolors.ENDC
        if os.path.exists(unitpicsPcxPath) == True:
            unitpic_exists = bcolors.green + ' ✓ ' + bcolors.ENDC
        print(path_without_fbi + '' +
              bcolors.green +
              dep_path_unitpics +
              bcolors.ENDC +
              bcolors.lightred +
              uname +
              bcolors.ENDC
              + '.pcx' + unitpic_exists + ' !important ')

        units_exist = bcolors.red + ' ✕ ' + bcolors.ENDC
        print(path_without_fbi + '' +
              bcolors.green +
              dep_path_units +
              bcolors.ENDC +
              bcolors.lightred +
              uname +
              bcolors.ENDC
              + '.fbi')


        weapon_exists = bcolors.red + ' ✕ ' + bcolors.ENDC
        if os.path.exists(unit_weapon_path) == True:
            weapon_exists = bcolors.green + ' ✓ ' + bcolors.ENDC
        # print(path_without_fbi + '' +
        #       bcolors.green +
        #       dep_path_weapons +
        #       bcolors.ENDC +
        #       bcolors.lightred +
        #       uname + '_weapon' +
        #       bcolors.ENDC
        #       + '.tdf' + weapon_exists)
        print(unit_weapon_path + weapon_exists)
        print('')


        print('unitpic : ' + bcolors.red + str(dp_unitpic) + bcolors.ENDC)
        print('unit3do : ' + bcolors.red + str(dp_3dmodel) + bcolors.ENDC)
        print('unitcob : ' + bcolors.red + str(dp_script) + bcolors.ENDC)
        print('ucorpse : ' + bcolors.red + str(dp_corpses) + bcolors.ENDC)
        print('hasWeap : ' + bcolors.red + str(this_unit_has_weapons) + bcolors.ENDC)
        print('weapsOk : ' + bcolors.red + str(dp_allweapons) + bcolors.ENDC)
        print('downlod : ' + bcolors.red + str(dp_download) + bcolors.ENDC)


        soundsInSQL = SoundSetTDF.objects.all()
        print(bcolors.purple + 'queried sounds from SQL : ' + bcolors.ENDC + bcolors.lightred + str(soundsInSQL) + bcolors.ENDC)
        print(bcolors.purple + 'total sounds in SQL : ' + bcolors.ENDC + bcolors.lightred + str(len(soundsInSQL)) + bcolors.ENDC)

        return Response(json_dict)




class CustomHtmlGenerator(APIView):
    def get(self, request, format=None):
        # msg = str(request.GET['msg'])
        html = '<div> <h1>Some Basic HTML</h1> <p>This is everything.</p> </div>'
        return HttpResponse(html)


class ThemeConstantConfigView(APIView):
    def get(self, request, format=None):
        theme_to_use = 'default : {"primary":{"name":"fuse-paleblue","hues":{"default":"700","hue-1":"500","hue-2":"600","hue-3":"400"}},"accent":{"name":"deep-orange","hues":{"default":"600","hue-1":"400","hue-2":"700","hue-3":"A100"}},"warn":{"name":"fuse-blue","hues":{"default":"500","hue-1":"300","hue-2":"800","hue-3":"A100"}},"background":{"name":"blue-grey","hues":{"default":"50","hue-1":"A100","hue-2":"100","hue-3":"200"}}}'
        pt1_path = '/usr/src/app/DjangularStaticFiles/fuse-themes.constant.pt1.js'
        pt2_path = '/usr/src/app/DjangularStaticFiles/fuse-themes.constant.pt2.js'
        theme_js_pt1 = open(pt1_path, 'r', errors='replace').read()
        theme_js_pt2 = open(pt2_path, 'r', errors='replace').read()
        theme_in_db = WebsiteColorTheme.objects.filter(enabled=True)
        if len(theme_in_db) > 0:
            theme_to_use = theme_in_db[0].replace('"CUSTOM_THEME_NAME"', 'default')
        finalHTML = theme_js_pt1 + theme_to_use + theme_js_pt2
        print(finalHTML)
        return HttpResponse(finalHTML)


####    --------------------------------------------
####    ------------------------------------------------------------------------------------------------------------
####    --------------------------------------------
