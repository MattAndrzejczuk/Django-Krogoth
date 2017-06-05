import os
from os import walk
from os import listdir
from os.path import isfile, join
from PIL import Image
import json



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
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'




print(bcolors.WARNING + "ArmPrime "  + bcolors.ENDC)
print(bcolors.OKBLUE + "Okay doge..."  + bcolors.ENDC)





class LazarusListUnits:
    f = []
    d = []
    output_final = open('workfile', 'w')
    jsonResponse = []
    root = ''

    outputConsole = ''
    outputConsole_unit = ''
    outputConsole_errors = ''

    def __init__(self):
        self.f = []
        self.d = []
        self.output_final = open('workfile', 'w')
        self.jsonResponse = []
        self.root = 'totala_files/'

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

# begin . . .


unitListPrettyJSON = LazarusListUnits()
unitListPrettyJSON.printContents()


print('')
print(json.dumps(unitListPrettyJSON.jsonResponse))

print(unitListPrettyJSON.outputConsole)
print(unitListPrettyJSON.outputConsole_unit)
print(unitListPrettyJSON.outputConsole_errors)
unitListPrettyJSON.output_final.write(unitListPrettyJSON.outputConsole_unit)

def listWorkingDirectory(path):
    print(bcolors.BOLD + '\n ' + '' + path + ' ' + ' ' + bcolors.ENDC)

    for (dirpath, dirnames, filenames) in walk(path):
        if len(dirnames) > 0:
            print(bcolors.pink + ' ' + '☭ ☭ ☭ directories: ' + bcolors.ENDC + bcolors.lightgreen + str(dirnames) + bcolors.ENDC + bcolors.purple + ' ✪ ' + '\n' + bcolors.ENDC)
            print(bcolors.lightcyan + ' ' + '☭ ☭ ☭ filenames: ' + bcolors.ENDC + bcolors.lightgreen + str(filenames) + bcolors.ENDC + bcolors.purple + ' ✪ ' + '\n' + bcolors.ENDC)



listWorkingDirectory('totala_files/')
