from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

import json
import re
import datetime
import subprocess
import sys
import codecs
from os import walk
import os
from PIL import Image
import time

from LazarusII.FbiData import remove_comments
from DatabaseSandbox.models import TotalAnnihilationUploadedFile
# from LazarusDatabase.models import SelectedAssetUploadRepository
from lazarus.views import WeaponTDFFetch, SoundTDFFetch





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



import os.path



class ExecuteBash_LS_AllCustomModFiles(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        final_obj = {}
        ModFileDesignation = ''
        raw_repo_name = ''
        directory_str = '/usr/src/persistent/media/ta_data'
        try:
            print('')
            ModFileDesignation = str(request.GET['mod_repo']) + '_SelectedAssetUploadRepository'
            raw_repo_name = request.GET['mod_repo']
        except:
            pass
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



