from django.conf.urls import url, include
from LazarusIII import views



urlpatterns = [

    url(r'^sample', views.sample.as_view()),
    url(r'^proccessWholeHPIToSQL', views.proccessWholeHPIToSQL.as_view()),

    url(r'^DependenciesForUnitFBI', views.DependenciesForUnitFBI.as_view(), name='NEW Dependencies For Unit FBI'),

]


class bcolors():
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

    def printpathwithfile(path, filename):
        print(bcolors.orange + path + bcolors.ENDC + bcolors.green + filename + bcolors.ENDC)

    def printpathwithweapon(path, filename):
        print(bcolors.TEAL + path + bcolors.ENDC + bcolors.purple + filename + bcolors.ENDC)

    def printkeywithvalue(key, value):
        definer = bcolors.TEAL + \
                  key + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '  ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.lightred + \
                  value + \
                  bcolors.ENDC
        print(definer + midchar + end_val)

    def printweaponkeywithvalue(weapon, value):
        definer = bcolors.red + \
                  weapon + \
                  bcolors.ENDC
        midchar = bcolors.lightgreen + \
                  '  ->  ' + \
                  bcolors.ENDC
        end_val = bcolors.purple + \
                  value + \
                  bcolors.ENDC
        print(definer + midchar + end_val)

    def printpurple(str):
        print(bcolors.purple + str + bcolors.ENDC)

    def printcyan(str):
        print(bcolors.cyan + str + bcolors.ENDC)

    def printgray(str):
        print(bcolors.darkgrey + str + bcolors.ENDC)

