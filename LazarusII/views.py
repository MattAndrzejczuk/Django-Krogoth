from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair, printError, printWarning, printInfo, printLog, printDebug

# For listing units:
from os import walk
import os
from PIL import Image

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
        }
        return Response(json_response)


class LazarusListUnits(APIView):
    f = []
    d = []
    output_final = open('workfile', 'w')
    root = ''


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
        for (dirpath, dirnames, filenames) in walk(self.root + pathName):
            printLog(dirnames)
            printDebug(filenames, self.root)

            if pathName == 'unitpics':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)
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


        print(bcolors.purple + 'Path: ' + bcolors.ENDC + bcolors.FAIL + dirpath + bcolors.ENDC)
        #print(self.jsonResponse)
        return self.jsonResponse

    def printContents(self, mod_path, mod_name):
        jsonFinal = []
        for (dirpath, dirnames, filenames) in walk(mod_path):
            self.f.extend(filenames)
            self.d.extend(dirnames)
            printLog('printing contents: ' + mod_path)
            for path in dirnames:
                self.printSubContents(path, mod_name)
            break


    def getUnitInfo(self, unitId):
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


    def get(self, request, format=None):
        print(bcolors.lightred + 'GET request: ' + bcolors.ENDC)
        print(bcolors.purple + str(request.GET) + bcolors.ENDC)

        # read GET param 'test' if it exists:
        # try:
        #     print(bcolors.blue + 'test = ' + bcolors.ENDC + bcolors.lightgreen + str(request.GET['test']) + bcolors.ENDC)
        # except:
        #     print('......')

        try:
            printKeyValuePair('Mod Name', str(request.GET['mod_name']))
            self.printContents('/usr/src/app/static/' + str(request.GET['mod_name']) + '/', str(request.GET['mod_name']))
            final_response = {'arm_data': self.jsonResponse}
            return Response(final_response)
        except:
            printError('Mod Failed To Open!')
            unitListPrettyJSON = LazarusListUnits()
            unitListPrettyJSON.printContents('/usr/src/app/static/totala_files2/')
            final_response = {'arm_data': unitListPrettyJSON.jsonResponse}
            return Response(final_response)


"""
/LazarusII/UnitFbiData/?mod_name=totala_files2&unit_id=arach
"""
