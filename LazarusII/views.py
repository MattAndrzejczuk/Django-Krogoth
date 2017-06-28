from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
import json

from LazarusII.DataReaderTA import readFile
from LazarusII.FbiData import LazarusUnit
from LazarusII.PyColors import bcolors, printKeyValuePair


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


class getCPUInfo(APIView):  # cat cpuinfo
    def get(self, request, format=None):
        try:
            mod_name = str(request.GET['mod_name'])
            unit_id = str(request.GET['unit_id'])
            unit_path = '/usr/src/app/static/' + mod_name + '/units/' + unit_id + '.fbi'
            print('unit path: ')
            print(unit_path)
            unitsArray = readFile(unit_path)
            for unit in unitsArray:
                printKeyValuePair('name', unit.Name)
            context = {"test": unitsArray}
            return Response(context)
        except:
            mod_name = 'totala_files2'
            unit_id = 'arach'
            unit_path = '/usr/src/app/static/' + mod_name + '/units/' + unit_id + '.fbi'
            print('unit path: ')
            print(unit_path)
            unitsArray = readFile(unit_path)
            for unit in unitsArray:
                printKeyValuePair('name', unit.Name)
            context = {"test": unitsArray}
            # context = {"error": "something fucked up."}
            return Response(context)
