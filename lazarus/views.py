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



class LazarusListUnits:
    f = []
    d = []
    output_final = open('workfile', 'w')
    jsonResponse = []
    root = ''

    outputConsole = ''
    outputConsole_unit = ''
    outputConsole_errors = ''

    def __init__(self, unitName):
        self.f = []
        self.d = []
        self.output_final = open('workfile', 'w')
        self.jsonResponse = []
        print('')
        print('LOOK RIGHT HERE: ')
        print(unitName)
        self.root = unitName

        self.outputConsole_errors = ''
        self.outputConsole = ''
        self.outputConsole_unit = ''

    def printSubContents(self, pathName):
        for (dirpath, dirnames, filenames) in walk(self.root + pathName):
            self.outputConsole += bcolors.lightgreen + ' ' + '⚒ ⚒ ⚒' + '\n' + bcolors.ENDC
            self.outputConsole += (pathName)

            print(bcolors.pink + self.root + pathName + ' ⚔ ' + dirpath + bcolors.ENDC)
            if pathName == 'unitpics':
                for file in filenames:
                    self.outputConsole += bcolors.lightgreen + ' ' + '♧' + ' ' + bcolors.ENDC
                    filename, file_extension = os.path.splitext(file)
                    self.outputConsole += bcolors.OKBLUE + str(self.root + pathName + '/' + file) + bcolors.ENDC
                    self.outputConsole += bcolors.OKGREEN + str( file_extension.lower()) + bcolors.ENDC
                    pathToFile = self.root + pathName + '/' + file
                    try:
                        img = Image.open(pathToFile)
                        imgSaveTo = self.root + pathName + '/' + filename + '.png'
                        img.save(imgSaveTo, format='png')
                        self.jsonResponse.append({'thumbnail': imgSaveTo, 'object_name':filename})
                    except:
                        print('OHHHH SHIT!!!')
                break
            elif pathName == 'units':
                for unitFile in filenames:
                    #file_object = open('test', 'r')
                    #print(file_object.read())
                    print(bcolors.pink + ' ⚙ ' + unitFile + ' ⚙ ' + bcolors.ENDC)
                    filename, file_extension = os.path.splitext(unitFile)
                    if file_extension == '.fbi':
                        try:
                            self.outputConsole += bcolors.lightcyan + ' ☾' + str(self.root + pathName + '/' + unitFile) + '☽ ' + bcolors.ENDC
                            file_object = open(self.root + pathName + '/' + unitFile, 'r')

                            # self.outputConsole_unit += bcolors.pink + '⚛ ' + filename + '' + bcolors.ENDC
                            # self.outputConsole_unit += bcolors.blue + '' + file_extension + ' ▼' + bcolors.ENDC
                            self.outputConsole_unit += '\n' + file_object.read() + '\n'
                        except:
                            self.outputConsole_errors += bcolors.red + '\n' + 'failed to load file: ' + filename + bcolors.ENDC
                    else:
                        self.outputConsole += bcolors.darkgrey + ' ☾' + str(self.root + pathName + '/' + unitFile) + '☽ ' + bcolors.ENDC



    def printContents(self):

        self.outputConsole += bcolors.lightgreen + ' ' + '✩ ✩ ✩ ✩ ✩' + ' ' + bcolors.ENDC

        for (dirpath, dirnames, filenames) in walk(self.root):
            self.outputConsole += '\n'
            self.f.extend(filenames)
            self.d.extend(dirnames)
            self.outputConsole += bcolors.HEADER + 'dirpath' + str(dirpath) + bcolors.ENDC
            self.outputConsole += bcolors.BOLD + 'dirnames' + str(dirnames) + bcolors.ENDC

            self.outputConsole += bcolors.lightgreen + ' ' + '☭ ☭ ☭' + ' ' + bcolors.ENDC
            for path in dirnames:
                self.outputConsole += bcolors.WARNING + ' ✦ \t ' + path + ", " + bcolors.ENDC
                self.printSubContents(path)
            break

    def printUnitFBI(self):
        return

    def getUnitInfo(self, unitId):
        return


class LazarusUnit:

    def __str__(self):
        return 'Name: ' + self.Name + ', Info: ' + self.Description + ', HP: ' + self.MaxDamage + '.'

    def getJsonRepresentation(self):
        the_json = {'Name':self.Name,
                    'Description':self.Description,
                    'Class':self.TEDClass, 'HP':self.MaxDamage,
                    'BuildCostEnergy':self.BuildCostEnergy,
                    'BuildCostMetal':self.BuildCostMetal,
                    'picture': '/static/totala_files2/unitpics/' + self.Objectname + '.png'}
        return json.dumps(the_json)


    def __init__(self):
        self.UnitName = ''
        self.Version = ''
        self.Side = ''
        self.Objectname = ''
        self.Designation = ''
        self.Name = ''
        self.Description = ''
        self.FrenchDescription = ''
        self.GermanDescription = ''
        self.FootprintX = 3
        self.FootprintZ = 3
        self.BuildCostEnergy = 15000
        self.BuildCostMetal = 1500
        self.MaxDamage = 2500
        self.MaxWaterDepth = 35
        self.MaxSlope = 14
        self.EnergyUse = 1
        self.BuildTime = 100
        self.WorkerTime = 0
        self.BMcode = 1
        self.Builder = 0
        self.ThreeD = 1
        self.ZBuffer = 1
        self.NoAutoFire = 0
        self.SightDistance = 300
        self.RadarDistance = 0
        self.SoundCategory = ''
        self.EnergyStorage = 10
        self.MetalStorage = 10
        self.ExplodeAs = ''
        self.SelfDestructAs = ''
        self.Category = ''
        self.TEDClass = ''
        self.Copyright = ''
        self.Corpse = ''
        self.UnitNumber = 21
        self.firestandorders = 1
        self.StandingFireOrder = 2
        self.mobilestandorders = 1
        self.StandingMoveOrder = 1
        self.canmove = 1
        self.canpatrol = 1
        self.canstop = 1
        self.canguard = 1
        self.MaxVelocity = 1
        self.BrakeRate = 0.15
        self.Acceleration = 0.1
        self.TurnRate = 500
        self.SteeringMode = 2
        self.ShootMe = 1
        self.EnergyMake = 2
        self.DefaultMissionType = ''
        self.maneuverleashlength = 500
        self.MovementClass = ''
        self.Upright = 1
        self.Weapon1 = ''
        self.Weapon2 = ''
        self.Weapon3 = ''
        self.wpri_badTargetCategory = ''
        self.BadTargetCategory = ''
        self.canattack = 1
        self.NoChaseCategory = ''



def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)


def get_unit_instances(the_selection):

    allUnitInstances = []
    #the_path = '/usr/src/app/static/'
    the_path = '/usr/src/volatile/static/'
    #the_selection = 'totala_files2/units/'
    the_mod = the_path + the_selection
    #the_file = 'CORCRASH.FBI'
    print('Yo what the fuck???')
    print(the_mod )
    file_object = open(the_mod, 'r', encoding='utf-8', errors='ignore')
    unit_object_rawstr = file_object.read()
    print(unit_object_rawstr)
    unitObj_parsed = unit_object_rawstr.split('[UNITINFO]')
    total_units_in_file = 1 #len(unitObj_parsed) - 1
    print('why is this shit fucked up?')
    f2 = open(the_mod, 'r', encoding='utf-8', errors='ignore')
    f3 = open(the_mod, 'r', encoding='utf-8', errors='ignore')
    print('heres f2')
    print(f2)
    print('SDFGSGSDFGDFGHDFGHDFGH')
    print(f3)
    i = sum(1 for line in f2)
    u = LazarusUnit()

    while i > 0:
        thisLine = remove_comments(f3.readline())
        if '{' in thisLine:
            u = LazarusUnit()
        elif '}' in thisLine:
            allUnitInstances.append(u)
        elif '=' in thisLine:
            keyVal = thisLine.split('=')
            keyVal[1] = keyVal[1].replace(';', '')

            if 'UnitName' in keyVal[0]:
                u.UnitName = keyVal[1].replace('\n', '')
            elif 'Version' in keyVal[0]:
                u.Version = keyVal[1].replace('\n', '')
            elif 'Side' in keyVal[0]:
                u.Side = keyVal[1].replace('\n', '')
            elif 'Objectname' in keyVal[0]:
                u.Objectname = keyVal[1].replace('\n', '')
            elif 'Designation' in keyVal[0]:
                u.Designation = keyVal[1].replace('\n', '')
            elif 'Name' in keyVal[0]:
                u.Name = keyVal[1].replace('\n', '')
            elif 'Description' in keyVal[0]:
                u.Description = keyVal[1].replace('\n', '')
            elif 'FrenchDescription' in keyVal[0]:
                u.FrenchDescription = keyVal[1].replace('\n', '')
            elif 'GermanDescription' in keyVal[0]:
                u.GermanDescription = keyVal[1]
            elif 'FootprintX' in keyVal[0]:
                u.FootprintX = keyVal[1].replace('\n', '')
            elif 'FootprintZ' in keyVal[0]:
                u.FootprintZ = keyVal[1].replace('\n', '')
            elif 'BuildCostEnergy' in keyVal[0]:
                u.BuildCostEnergy = keyVal[1].replace('\n', '')
            elif 'BuildCostMetal' in keyVal[0]:
                u.BuildCostMetal = keyVal[1].replace('\n', '')
            elif 'MaxDamage' in keyVal[0]:
                u.MaxDamage = keyVal[1].replace('\n', '')
            elif 'MaxWaterDepth' in keyVal[0]:
                u.MaxWaterDepth = keyVal[1].replace('\n', '')
            elif 'MaxSlope' in keyVal[0]:
                u.MaxSlope = keyVal[1].replace('\n', '')
            elif 'EnergyUse' in keyVal[0]:
                u.EnergyUse = keyVal[1].replace('\n', '')
            elif 'BuildTime' in keyVal[0]:
                u.BuildTime = keyVal[1].replace('\n', '')
            elif 'WorkerTime' in keyVal[0]:
                u.WorkerTime = keyVal[1].replace('\n', '')
            elif 'BMcode' in keyVal[0]:
                u.BMcode = keyVal[1].replace('\n', '')
            elif 'ThreeD' in keyVal[0]:
                u.ThreeD = keyVal[1].replace('\n', '')
            elif 'ZBuffer' in keyVal[0]:
                u.ZBuffer = keyVal[1].replace('\n', '')
            elif 'NoAutoFire' in keyVal[0]:
                u.NoAutoFire = keyVal[1].replace('\n', '')
            elif 'SightDistance' in keyVal[0]:
                u.SightDistance = keyVal[1].replace('\n', '')
            elif 'RadarDistance' in keyVal[0]:
                u.RadarDistance = keyVal[1].replace('\n', '')
            elif 'SoundCategory' in keyVal[0]:
                u.SoundCategory = keyVal[1].replace('\n', '')
            elif 'EnergyStorage' in keyVal[0]:
                u.EnergyStorage = keyVal[1].replace('\n', '')
            elif 'MetalStorage' in keyVal[0]:
                u.MetalStorage = keyVal[1].replace('\n', '')
            elif 'ExplodeAs' in keyVal[0]:
                u.ExplodeAs = keyVal[1].replace('\n', '')
            elif 'SelfDestructAs' in keyVal[0]:
                u.SelfDestructAs = keyVal[1].replace('\n', '')
            elif 'Category' in keyVal[0]:
                u.Category = keyVal[1].replace('\n', '')
            elif 'TEDClass' in keyVal[0]:
                u.TEDClass = keyVal[1].replace('\n', '')
            elif 'Copyright' in keyVal[0]:
                u.Copyright = keyVal[1].replace('\n', '')
            elif 'Corpse' in keyVal[0]:
                u.Corpse = keyVal[1].replace('\n', '')
            elif 'UnitNumber' in keyVal[0]:
                u.UnitNumber = keyVal[1].replace('\n', '')
            elif 'firestandorders' in keyVal[0]:
                u.firestandorders = keyVal[1].replace('\n', '')
            elif 'StandingFireOrder' in keyVal[0]:
                u.StandingFireOrder = keyVal[1].replace('\n', '')
            elif 'mobilestandorders' in keyVal[0]:
                u.mobilestandorders = keyVal[1].replace('\n', '')
            elif 'StandingMoveOrder' in keyVal[0]:
                u.StandingMoveOrder = keyVal[1].replace('\n', '')
            elif 'canmove' in keyVal[0]:
                u.canmove = keyVal[1].replace('\n', '')
            elif 'canpatrol' in keyVal[0]:
                u.canpatrol = keyVal[1].replace('\n', '')
            elif 'canstop' in keyVal[0]:
                u.canstop = keyVal[1].replace('\n', '')
            elif 'canguard' in keyVal[0]:
                u.canguard = keyVal[1].replace('\n', '')
            elif 'MaxVelocity' in keyVal[0]:
                u.MaxVelocity = keyVal[1].replace('\n', '')
            elif 'BrakeRate' in keyVal[0]:
                u.BrakeRate = keyVal[1].replace('\n', '')
            elif 'Acceleration' in keyVal[0]:
                u.Acceleration = keyVal[1].replace('\n', '')
            elif 'TurnRate' in keyVal[0]:
                u.TurnRate = keyVal[1].replace('\n', '')
            elif 'SteeringMode' in keyVal[0]:
                u.SteeringMode = keyVal[1].replace('\n', '')
            elif 'ShootMe' in keyVal[0]:
                u.ShootMe = keyVal[1].replace('\n', '')
            elif 'EnergyMake' in keyVal[0]:
                u.EnergyMake = keyVal[1].replace('\n', '')
            elif 'DefaultMissionType' in keyVal[0]:
                u.DefaultMissionType = keyVal[1].replace('\n', '')
            elif 'maneuverleashlength' in keyVal[0]:
                u.maneuverleashlength = keyVal[1].replace('\n', '')
            elif 'MovementClass' in keyVal[0]:
                u.MovementClass = keyVal[1].replace('\n', '')
            elif 'Upright' in keyVal[0]:
                u.Upright = keyVal[1].replace('\n', '')
            elif 'Weapon1' in keyVal[0]:
                u.Weapon1 = keyVal[1].replace('\n', '')
            elif 'Weapon2' in keyVal[0]:
                u.Weapon2 = keyVal[1].replace('\n', '')
            elif 'Weapon3' in keyVal[0]:
                u.Weapon3 = keyVal[1].replace('\n', '')
            elif 'wpri_badTargetCategory' in keyVal[0]:
                u.wpri_badTargetCategory = keyVal[1].replace('\n', '')
            elif 'BadTargetCategory' in keyVal[0]:
                u.BadTargetCategory = keyVal[1].replace('\n', '')
            elif 'canattack' in keyVal[0]:
                u.canattack = keyVal[1].replace('\n', '')
            elif 'NoChaseCategory' in keyVal[0]:
                u.NoChaseCategory = keyVal[1].replace('\n', '')
        i -= 1
    return allUnitInstances





class listWorkingDirectory(APIView):
    def get(self, request, format=None):
        
        file_list = []
        dir_list = []
        user_gui_data = [] 
        strResponse = ''
        #path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = '/usr/src/app/static/' + str(request.GET['path'])
        # context = {"files":file_list, "directories":dir_list}
        print(path)
        for (dirpath, dirnames, filenames) in walk(path):
            print(dirpath)
            print(dirnames)
            print(filenames)
            for file in filenames:
                if any(file in s for s in file_list):
                    print('nah...')
                else:
                    user_gui_data.append({
                        "target_path":(path + '/' + file),
                        "file_name":file,
                        "api_uri_unit":(path + '/' + file).replace('/usr/src/app/static/',''),
                        "thumbnail":('http://52.27.28.55/static/' + path + '/' + file).replace('/usr/src/app/static/','').replace('.FBI','.png').replace('.fbi','.fbi').replace('units','unitpics'),
                        "nothing":"123123",
                        "nothing2":"123123"})
                    dir_list.append(path + '/' + file)
                    file_list.append(file)
            if len(dirnames) > 0:
                for file in file_list: 
                    file_list.append(file)
                dir_list.append(dirnames)
                strResponse += str(dirnames)
                #print(bcolors.pink + ' ' + '☭ ☭ ☭ directories: ' + bcolors.ENDC + bcolors.lightgreen + str(dirnames) + bcolors.ENDC + bcolors.purple + ' ✪ ' + '\n' + bcolors.ENDC)
                #print(bcolors.lightcyan + ' ' + '☭ ☭ ☭ filenames: ' + bcolors.ENDC + bcolors.lightgreen + str(filenames) + bcolors.ENDC + bcolors.purple + ' ✪ ' + '\n' + bcolors.ENDC)
        #context = {"files":file_list, "directories":dir_list}
        
        context = {"data": strResponse, "dirlist":dir_list, "files":file_list, "gui_data":user_gui_data}
        return Response(context)


class index(APIView):
    def get(self, request, format=None):
        if platform.system() == "Darwin":
            context = {
                "free": 298400,
                "available": 770988,
                "total": 2614172}
            return Response(context)

        def removeWhiteSpace(str):
            return str.replace(" ", "")

        def removeKB(str):
            return str.replace(" kB", "")

        def cleanFirstElement(str):
            return str.replace("b'", "")

        def main_first(str):
            return removeWhiteSpace(removeKB(cleanFirstElement(str))).replace("MemTotal:", "")

        def all_others(str):
            return removeWhiteSpace(removeKB(str))

        print(request)
        print(request.GET.__str__())

        p = Popen(['cat', '/proc/meminfo'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        final = str(output).split("\\n")

        memTotal = main_first(final[0])
        memFree = main_first(final[1]).replace("MemFree:", "")
        memAvailable = main_first(final[2]).replace("MemAvailable:", "")
        allUnitInstances = get_unit_instances(request.GET['path'])
        listOfShit = []
        for item in allUnitInstances:
            listOfShit.append({"data":str(item), "MaxDamage":item.MaxDamage})
        context = {"total": 0, "free": 0, "available": 0, "request": listOfShit, "request.GET __str__": str(request.GET['path'])}
        context['total'] = int(memTotal)
        context['free'] = int(memFree)
        context['available'] = int(memAvailable)

        return Response(context)



class convertPcxToPng(APIView):
    def get(self, request, format=None):
        path = '/usr/src/app/static/' + str(request.GET['path'])
        unitListPrettyJSON = LazarusListUnits(path)
        unitListPrettyJSON.printContents()

        print('')
        print(json.dumps(unitListPrettyJSON.jsonResponse))
        print(unitListPrettyJSON.outputConsole)
        print(unitListPrettyJSON.outputConsole_unit)
        print(unitListPrettyJSON.outputConsole_errors)

        v1 = str(json.dumps(unitListPrettyJSON.jsonResponse))
        v2 = str(unitListPrettyJSON.outputConsole)
        v3 = str(unitListPrettyJSON.outputConsole_unit)
        v4 = str(unitListPrettyJSON.outputConsole_errors)
        context = {"v1": v1, "v2": v2, "v3": v3, "v4":v4}
        return Response(context)



class getRam(APIView):
    def get(self, request, format=None):
        if platform.system() == "Darwin":
            context = {
                "free": 298400,
                "available": 770988,
                "total": 2614172}
            return Response(context)

        def removeWhiteSpace(str):
            return str.replace(" ", "")

        def removeKB(str):
            return str.replace(" kB", "")

        def cleanFirstElement(str):
            return str.replace("b'", "")

        def main_first(str):
            return removeWhiteSpace(removeKB(cleanFirstElement(str))).replace("MemTotal:", "")

        def all_others(str):
            return removeWhiteSpace(removeKB(str))

        p = Popen(['cat', '/proc/meminfo'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        final = str(output).split("\\n")

        memTotal = main_first(final[0])
        memFree = main_first(final[1]).replace("MemFree:", "")
        memAvailable = main_first(final[2]).replace("MemAvailable:", "")

        context = {"total": 0, "free": 0, "available": 0}
        context['total'] = int(memTotal)
        context['free'] = int(memFree)
        context['available'] = int(memAvailable)

        return Response(context)


class getStorage(APIView):  # cat swaps
    def get(self, request, format=None):

        if platform.system() == "Darwin":
            context = [
                {
                    "size": "2689020",
                    "name": "/dev/sda5",
                    "used": "1196720"}]
            return Response(context)

        p = Popen(['cat', '/proc/swaps'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        context = {"size": "", "used": "", "name": ""}
        final = str(output).split("\\n")
        returnArray = []

        skippedFirst = False
        for item in final:
            strArray = item.replace('\\t', '  ').split(' ')
            i = 0
            size = ""
            used = ""
            name = ""
            for str1 in strArray:
                goodStr = str1.replace(' ', '')
                if goodStr != '' and skippedFirst == True:
                    if i == 2:
                        size = goodStr
                    elif i == 3:
                        used = goodStr
                    elif i == 0:
                        name = goodStr
                    i += 1
            skippedFirst = True
            if size != '':
                context = {"size": size, "used": used, "name": name}
                returnArray.append(context)

        return Response(returnArray)


class getCPUInfo(APIView):  # cat cpuinfo
    def get(self, request, format=None):

        if platform.system() == "Darwin":
            context = {
                "cache_size": "8192 KB",
                "cores": "3",
                "speed_MHz": "2711.893",
                "model_name": "Intel(R) Core(TM) i7-6820HQ CPU @ 2.70GHz"
            }
            return Response(context)

        p = Popen(['cat', '/proc/cpuinfo'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        final = str(output).split("\\n")

        cache_size = ''
        model_name = ''
        processor_id = ''
        speed_MHz = ''
        total_cpus = ''

        for item in final:
            line = item.replace("\\t", "")

            key = ''
            value = ''

            try:
                value = line.split(":")[1]
                key = line.split(":")[0]
            except:
                key = line.split(":")[0]
                value = 'n/a'

            if key == 'cache size':
                cache_size = value
            elif key == 'model name':
                model_name = value
            elif key == 'processor id':
                processor_id = value
            elif key == 'cpu MHz':
                speed_MHz = value
            elif key == 'cpu cores':
                total_cpus = value

        context = {"cache_size": cache_size.strip(),
                   "model_name": model_name.strip(),
                   "speed_MHz": speed_MHz.strip(),
                   "cores": total_cpus.strip()}

        return Response(context)


class getUpTime(APIView):  # cat uptime
    def get(self, request, format=None):
        if platform.system() == "Darwin":
            context = {
                "ticks": "2491.52",
                "secs": "864.89"
            }
            return Response(context)

        p = Popen(['cat', '/proc/uptime'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        final = str(output).split(" ")

        context = {"secs": final[0].replace('\n', '').replace("b'", ""),
                   "ticks": final[1].replace('\\n', '').replace("'", "")}

        return Response(context)


class getProcesses(APIView):  # ps aux

    def get(self, request, format=None):

        finalWrapper = {
            "CPU_Usage": float(0),
            "RAM_Usage": float(0),
            "Processes": []}

        sumOfCPU = 0.0
        sumOfRAM = 0.0

        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        def getColName(i):
            if i == 1:
                return 'USER'
            elif i == 2:
                return 'PID'
            elif i == 3:
                return 'CPU'
            elif i == 4:
                return 'MEM'
            elif i == 5:
                return 'VSZ'
            elif i == 6:
                return 'RSS'
            elif i == 7:
                return 'TTY'
            elif i == 8:
                return 'STAT'
            elif i == 9:
                return 'START'
            elif i == 10:
                return 'TIME'
            else:
                return '||'

        p = Popen(['ps', 'aux'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        final = str(output).split("\\n")

        for item in final:
            process_name = item[66:]
            row = item.split(" ")
            i = 1
            context = {"COMMAND": process_name,
                       "PID": "",
                       "CPU": "",
                       "MEM": "",
                       "VSZ": "",
                       "RSS": "",
                       "TTY": "",
                       "STAT": "",
                       "START": "",
                       "TIME": "", }
            for col in row:
                if col != '':
                    if i < 11:
                        context[getColName(i)] = col
                        if i == 3 and is_number(col) == True:
                            sumOfCPU += float(col.strip())
                        elif i == 4 and is_number(col) == True:
                            sumOfRAM += float(col.strip())
                        i += 1
            i = 1
            finalWrapper['Processes'].append(context)
            finalWrapper['CPU_Usage'] = sumOfCPU
            finalWrapper['RAM_Usage'] = sumOfRAM
        return Response(finalWrapper)
        # print(item)



class getProcessesDummy(APIView):  # ps aux

    def get(self, request, format=None):
        finalWrapper = {
            "CPU_Usage": float(0),
            "RAM_Usage": float(0),
            "Processes": []}

        sumOfCPU = 0.0
        sumOfRAM = 0.0

        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        def getColName(i):
            if i == 1:
                return 'USER'
            elif i == 2:
                return 'PID'
            elif i == 3:
                return 'CPU'
            elif i == 4:
                return 'MEM'
            elif i == 5:
                return 'VSZ'
            elif i == 6:
                return 'RSS'
            elif i == 7:
                return 'TTY'
            elif i == 8:
                return 'STAT'
            elif i == 9:
                return 'START'
            elif i == 10:
                return 'TIME'
            else:
                return '||'

        p = Popen(['ps', 'aux'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(b"input data that is passed to subprocess' stdin")
        rc = p.returncode

        final = str(output).split("\\n")

        skippedFirst = False
        for item in final:
            process_name = item[66:]
            row = item.split(" ")
            i = 1
            context = {"COMMAND": process_name,
                       "PID": "",
                       "CPU": "",
                       "MEM": "",
                       "VSZ": "",
                       "RSS": "",
                       "TTY": "",
                       "STAT": "",
                       "START": "",
                       "TIME": "", }

            rowUser = {"value": "cinicraft", "classes": "text-bold"}
            rowCommand = {"value": process_name[:50], "classes": "text-boxed m-0 grey-400-bg white-fg"}
            rowAvgIO = {"value": 0, "classes": "purple-700-fg"}
            rowAvgCPU = {"value": 0, "classes": "green-fg"}
            rowAvgMem = {"value": 2, "classes": "blue-700-fg"}

            for col in row:
                if col != '':
                    if i < 11:

                        colName = getColName(i)
                        context[getColName(i)] = col

                        if colName == "COMMAND":
                            rowCommand['value'] = col
                        elif colName == "USER":
                            rowUser['value'] = col
                        elif colName == "CPU":
                            rowAvgCPU['value'] = col
                        elif colName == "MEM":
                            rowAvgMem['value'] = col
                        elif colName == "RSS":
                            rowAvgIO['value'] = col

                        if i == 3 and is_number(col) == True:
                            sumOfCPU += float(col.strip())
                        elif i == 4 and is_number(col) == True:
                            sumOfRAM += float(col.strip())
                        i += 1

            if rowUser['value'] == '':
                rowUser['classes'] = 'text-boxed m-0 red-400-bg white-fg'
            rows = [rowUser, rowCommand, rowAvgIO, rowAvgCPU, rowAvgMem]
            if skippedFirst == True and rowUser['value'] != "'":
                finalWrapper['Processes'].append(rows)
            skippedFirst = True
            i = 1
        finalWrapper['CPU_Usage'] = sumOfCPU
        finalWrapper['RAM_Usage'] = sumOfRAM
        return Response(finalWrapper)



class getProcessesDummyScaffold(APIView):  # ps aux

    def get(self, request, format=None):

        col1 = {"title": "NAME"}
        col2 = {"title": "USER"}
        col3 = {"title": "Avg. IO"}
        col4 = {"title": "Avg. CPU"}
        col5 = {"title": "Avg. Mem"}
        columns = [col1,col2,col3,col4,col5]

        rowName = {"value": "cinicraft", "classes": "text-bold"}
        rowUser = {"value": "dovecot", "classes": "text-boxed m-0 grey-400-bg white-fg"}
        rowAvgIO = {"value": 0, "classes": "amber-700-fg"}
        rowAvgCPU = {"value": 0, "classes": "red-fg"}
        rowAvgMem = {"value": 2, "classes": "amber-700-fg"}
        rows = [rowName, rowUser, rowAvgIO, rowAvgCPU, rowAvgMem]

        table = {"columns": columns, "rows": [rows]}

        finalWrapper = {"title": "Process Explorer",
                        "table": table}

        return Response(finalWrapper)





class getProcessesNew(APIView):  # ps aux

    def get(self, request, format=None):

        col1 = {"title": "Name"}
        col2 = {"title": "User"}
        col3 = {"title": "Avg. IO"}
        col4 = {"title": "Avg. CPU"}
        col5 = {"title": "Avg. Mem"}
        columns = [col1,col2,col3,col4,col5]

        rowName = {"value": "", "classes": ""}
        rowUser = {"value": "", "classes": ""}
        rowAvgIO = {"value": "", "classes": ""}
        rowAvgCPU = {"value": "", "classes": ""}
        rowAvgMem = {"value": "", "classes": ""}
        rows = [rowName, rowUser, rowAvgIO, rowAvgCPU, rowAvgMem]

        finalWrapper = {"title": "Process Explorer",
                        "table": columns,
                        "rows": rows}

        return Response(finalWrapper)
