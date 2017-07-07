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


def printKeyValuePair(key, value):
    return
    try:
        print(bcolors.lightcyan + str(key) + bcolors.ENDC + bcolors.orange + ' : ' + bcolors.ENDC + bcolors.lightblue + str(value) + bcolors.ENDC)
    except:
        print('FAIL! printKeyValuePair')

def printKeyValuePair1(key, value):
    return
    try:
        print(bcolors.purple + str(key) + bcolors.ENDC + bcolors.pink + ' : ' + bcolors.ENDC + bcolor + str(value) + bcolors.ENDC)
    except:
        print('FAIL! printKeyValuePair')

def printKeyValuePair2(key, value):
    return
    try:
        print(bcolors.OKBLUE + str(key) + bcolors.ENDC + bcolors.TEAL + ' : ' + bcolors.ENDC + bcolors.OKBLUE + str(value) + bcolors.ENDC)
    except:
        print('FAIL! printKeyValuePair')

def printKeyValuePair3(key, value):
    return
    try:
        print(bcolors.blue + str(key) + bcolors.ENDC + bcolors.orange + ' : ' + bcolors.ENDC + bcolors.cyan + str(value) + bcolors.ENDC)
    except:
        print('FAIL! printKeyValuePair')

def printError(msg):
    return
    try:
       print('\033[96m[' + '\033[31mError\033[0m' + '\033[96m]\033[0m: \033[31m' + str(msg) + '\033[0m')
    except:
        print('FAIL! printError')

def printWarning(msg):
    return
    try:
        print('\033[96m[' + '\033[91mWarning\033[0m' + '\033[96m]\033[0m: \033[33m' + str(msg) + '\033[0m')
    except:
        print('FAIL! printWarning')


def printInfo(msg):
    return
    try:
        print('\033[96m[' + '\033[94mInfo\033[0m' + '\033[96m]\033[0m: ' + str(msg) + '\033[0m')
    except:
        print('FAIL! printInfo')

def printLog(msg):
    return
    try:
        print('\033[96m[' + '\033[33mLog\033[0m' + '\033[96m]\033[0m: \033[92m' + str(msg) + '\033[0m')
    except:
        print('FAIL! printLog')

def printDebug(msg, origin):
    return
    try:
        print('\033[96m[\033[36m' + origin + '\033[0m\033[96m]\033[0m: \033[34m' + str(msg) + '\033[0m')
    except:
        print('FAIL! printDebug')

