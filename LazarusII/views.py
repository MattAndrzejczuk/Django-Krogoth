from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import detail_route, list_route
from rest_framework import status
import json


from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair, printKeyValuePair1, printKeyValuePair2, \
    printError, printWarning, printInfo, printLog, printDebug



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
from LazarusDatabase.models import SelectedAssetUploadRepository




from LazarusII.models import UnitFbiData, WeaponTDF, Damage, DownloadTDF, FeatureTDF, SoundSetTDF

# from rest_framework import viewsets
import sys
import codecs

from LazarusII.FbiData import remove_comments
from lazarus.views import WeaponTDFFetch, SoundTDFFetch



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



















class ReadVanillaTAData(APIView):
    def get(self, request, format=None):
        # 'SOUND',
        vanillaTaFiles = ['WEAPONS', 'MISSILES', 'ROCKETS', 'CANNONS', 'FIRES', 'METEORS', 'LASERS', 'UNITS', ]
        for filename in vanillaTaFiles:
            txtFile = codecs.open('static/' + filename + '.txt')
            print(filename)
            print('')
            txtFileNoComments = remove_comments(txtFile.read())
            strippedAndMinified = txtFileNoComments.strip().replace('\n', '').replace('\t', '')
            insertedSplitter = strippedAndMinified.replace('}}[', '}}|[')
            arrayOfWeaponObjects = insertedSplitter.split('|')

            for obj in arrayOfWeaponObjects:
                print('')
                weaponTDF = WeaponTDFFetch().getUsingString(obj)
            # '}}['
            print(weaponTDF)
            print('')
        return Response('')


class ReadVanillaTASoundData(APIView):
    def get(self, request, format=None):
        filename = 'SOUND'
        txtFile = codecs.open('static/' + filename + '.txt')
        print(filename)
        print('')
        txtFileNoComments = remove_comments(txtFile.read())
        strippedAndMinified = txtFileNoComments.strip().replace('\n', '').replace('\t', '')
        insertedSplitter = strippedAndMinified.replace('}}[', '}}|[')
        arrayOfWeaponObjects = insertedSplitter.split('|')

        for obj in arrayOfWeaponObjects:
            print('')
            soundTDF = SoundTDFFetch().get(obj)
        # '}}['
        print(soundTDF)
        print('')
        return Response('')


class ReadCoreContingencySoundData(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        filename = 'SOUND_CC'
        txtFile = codecs.open('static/' + filename + '.txt')
        print(filename)
        print('')
        txtFileNoComments = remove_comments(txtFile.read())
        strippedAndMinified = txtFileNoComments.strip().replace('\n', '').replace('\t', '')
        insertedSplitter = strippedAndMinified.replace('}}[', '}}|[')
        arrayOfWeaponObjects = insertedSplitter.split('|')

        for obj in arrayOfWeaponObjects:
            print('')
            soundTDF = SoundTDFFetch().get(obj)
        # '}}['
        print(soundTDF)
        print('')
        return Response('')

class ReadCoreContingencyWeaponData(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        vanillaTaFiles = ['WEAPONS_CC', ]
        for filename in vanillaTaFiles:
            txtFile = codecs.open('static/' + filename + '.txt')
            print(filename)
            print('')
            txtFileNoComments = remove_comments(txtFile.read())
            strippedAndMinified = txtFileNoComments.strip().replace('\n', '').replace('\t', '')
            insertedSplitter = strippedAndMinified.replace('}}[', '}}|[')
            arrayOfWeaponObjects = insertedSplitter.split('|')

            for obj in arrayOfWeaponObjects:
                print('')
                weaponTDF = WeaponTDFFetch().getUsingString(obj)
            # '}}['
            print(weaponTDF)
            print('')
        return Response('')








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



class ExecuteBash_LS_AllCustomModFiles(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):

        final_obj = {}

        ModFileDesignation = ''
        raw_repo_name = ''
        directory_str = '/usr/src/persistent/media/ta_data'


        # SelectedAssetUploadRepository
        # TotalAnnihilationUploadedFile

        try:
            print('')
            ModFileDesignation = str(request.GET['mod_repo']) + '_SelectedAssetUploadRepository'
            raw_repo_name = request.GET['mod_repo']
        except:
            pass

        # uploadedFilesFilter = []
        # repository = SelectedAssetUploadRepository.objects.get(name=raw_repo_name)
        # taUploadedFileRecords = TotalAnnihilationUploadedFile.objects.filter(designation=ModFileDesignation)
        # for record in taUploadedFileRecords:
        #     uploadedFilesFilter.append(system_path.replace(directory_str + '/', ''))
        # mod_name = request.GET['mod_name']


        # community mods:
        # /usr/src/persistent/media/ta_data/

        mod_paths = []
        uploaded_data_files = TotalAnnihilationUploadedFile.objects.all()
        if ModFileDesignation != '':
            uploaded_data_files = TotalAnnihilationUploadedFile.objects.filter(designation=ModFileDesignation)
            # print('\n\n\n\n\n\n\n\nMOD DESIGNATION FILTER IS WORKING ! ! ! !\n\n\n\n\n')
        else:
            print('\n\n\n\n\n FAIL ! ! ! ' + str(request.GET['mod_repo']) + ' \n\n\n\n\n\n\n')
        for data_file in uploaded_data_files:
            if os.path.isdir(data_file.system_path):
                ls_current_modpath = str(subprocess.check_output(['ls', data_file.system_path]))

                parsed_1 = ls_current_modpath.replace("\\n'","")
                dirs_in_mod = parsed_1.replace("b'","").split('\\n')


                listed_data_files = {
                    'name': data_file.file_name[:-4],
                    'type': data_file.file_name[-4:]
                }

                listed_data_files['directories'] = []
                for mod_item in dirs_in_mod:
                    # listed_data_files[mod_item + '_mod_items'] = {}

                    mod_item_path = data_file.system_path + '/' + mod_item
                    if os.path.isdir(mod_item_path):
                        # print("mod_item : %s" % mod_item)
                        ls_current_submodpath = str(subprocess.check_output(['ls', mod_item_path]))
                        sub_parsed_1 = ls_current_submodpath.replace("\\n'", "")
                        sub_parsed_2 = sub_parsed_1.replace("b'", "")
                        # listed_data_files[mod_item + '_mod_items'] = (sub_parsed_2.split('\\n'))
                        elements_in_dir = (sub_parsed_2.split('\\n'))
                        for raw_data_tdf in elements_in_dir:
                            does_contain_json = True
                            subdirectory_components = 'NIL'
                            parse_moditempath2 = ''
                            if raw_data_tdf[-4:].lower() == '.fbi':
                                parse_moditempath1 = mod_item_path.replace('/usr/src/persistent/', '')
                                parse_moditempath2 = parse_moditempath1.replace('/', '_SLSH_') + '_SLSH_' + raw_data_tdf[:-4]
                                parse_moditempath3 = '/LazarusII/UnitFBIViewset/?encoded_path=' + parse_moditempath2
                            elif raw_data_tdf[-4:].lower() == '.pcx':
                                # LETS MAKE SOME PNGs
                                pcx_path = mod_item_path  #+ raw_data_tdf[-4:]
                                pcxFiles = os.listdir(pcx_path)
                                for pic in pcxFiles:
                                    if pic[-4:] == '.pcx':
                                        try:
                                            # print('reading... ' + pcx_path + '/' + pic)
                                            img = Image.open(pcx_path + '/' + pic)
                                            png = pcx_path + '/' + pic.replace('.pcx', '') + '.png'
                                            if not os.path.isfile(png):
                                                img.save(png, format='png')
                                                print(' saved ✪ %s ' % png)
                                            # else:
                                            #     print('skipping... ' + png)
                                        except Exception as ex:
                                            print(ex)
                                            pass

                            else:
                                parse_moditempath3 = 'nan'
                                does_contain_json = False

                            _type = raw_data_tdf[-4:]
                            # if _type == '.tdf' or _type == '.fbi':
                            #     try:
                            #         logTheAsolutePath = StoredFiles()
                            #         logTheAsolutePath.absolute_path = '/usr/src/persistent/' + raw_data_tdf
                            #         logTheAsolutePath.file_type = raw_data_tdf[-3:]
                            #         logTheAsolutePath.file_name = raw_data_tdf[:-4] + '_' + raw_data_tdf[-3:]
                            #         logTheAsolutePath.save()
                            #     except:
                            #         print('skipping StoredFiles log, file already exists.')

                            if raw_data_tdf[-4:] == ".fbi":
                                pic_url = mod_item_path.replace('/usr/src/persistent', '')\
                                          + '/' + raw_data_tdf[:-4] + '.png'
                                data_file_json = {
                                    'file_type': raw_data_tdf[-4:],
                                    'file_name': raw_data_tdf[:-4],
                                    'mod_path': parse_moditempath3,
                                    'mod_path_slug': parse_moditempath2,
                                    'dir_type': mod_item,
                                    'raw_data_tdf': raw_data_tdf,
                                    'does_contain_json': does_contain_json,
                                    'unit_pic': pic_url.replace('/units/', '/unitpics/')
                                }
                                listed_data_files['directories'].append(data_file_json)
                        # mod_paths[data_file.file_name] = (listed_data_files)
                mod_paths.append(listed_data_files)

        result1 = str(subprocess.check_output(['ls', directory_str]))
        final_obj[directory_str] = str(result1).split('\\n')
        final_obj[directory_str][0] = final_obj[directory_str][0].replace("b'", "")

        context = {'root_items': final_obj, 'mod_paths': mod_paths, 'HPIs': ''}
        return Response(context)



