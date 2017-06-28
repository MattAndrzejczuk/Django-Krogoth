from django.contrib.auth import login, logout
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from chat.models import JawnUser
from chat.serializers import JawnUserSerializer
from rest_framework.renderers import JSONRenderer
from redis import ConnectionPool, StrictRedis
from jawn import settings as redis_settings
from django.template import loader
from django.http import HttpResponse
import json
import os
from os import walk
from PIL import Image


from .app_settings import (
    TokenSerializer, UserDetailsSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer
)

redis_connection_pool = ConnectionPool(**redis_settings.WS4REDIS_CONNECTION)



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




def index(request):
    template = loader.get_template('index.html')
    context = {
        "message": "Welcome to CiniCrafts official website!",
    }
    return HttpResponse(template.render(context, request))


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

def list_ta_units_advanced(request):
    allUnitInstances = []
    file_object = open('test', 'r')

def list_ta_units(request):
    unitListPrettyJSON = LazarusListUnits()
    unitListPrettyJSON.printContents()
    print(bcolors.cyan + request.GET.__str__() + bcolors.ENDC)
    return Response(json.dumps(unitListPrettyJSON.jsonResponse))
    # return HttpResponse(
    #     unitListPrettyJSON.jsonResponse, status=status.HTTP_200_OK
    # )

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

        for (dirpath, dirnames, filenames) in walk(self.root + pathName):
            #print('PATHNAME')

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
                                'RESTful_unit_data': '/static/' + mod_name + '/units/' + filename + '.fbi'
                            }
                        )
                    except:
                        print('[CRITICAL ERROR]: failed to open ' + str(filename) + ' [' + str(file_extension) + ']')


        print(bcolors.purple + 'Path: ' + bcolors.ENDC + bcolors.FAIL + dirpath + bcolors.ENDC)
        #print(self.jsonResponse)
        return self.jsonResponse

    def printContents(self, mod_name):
        jsonFinal = []
        for (dirpath, dirnames, filenames) in walk(mod_name):
            self.f.extend(filenames)
            self.d.extend(dirnames)
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
            print(bcolors.blue + 'Mod Name: ' + bcolors.ENDC + bcolors.lightgreen + str(request.GET['mod_name']) + bcolors.ENDC)
            unitListPrettyJSON = LazarusListUnits()
            unitListPrettyJSON.printContents('/usr/src/app/static/' + str(request.GET['mod_name']) + '/')
            final_response = {'arm_data': unitListPrettyJSON.jsonResponse}
            return Response(final_response)
        except:
            print(bcolors.FAIL + 'Mod Name Doesnt Exist, Opening: ' + bcolors.ENDC + bcolors.blue + 'totala_files2' + bcolors.ENDC)
            unitListPrettyJSON = LazarusListUnits()
            unitListPrettyJSON.printContents('/usr/src/app/static/totala_files2/')
            final_response = {'arm_data': unitListPrettyJSON.jsonResponse}
            return Response(final_response)


def getUnitFbiUsingId(request):
    mod_name = str(request.GET['mod_name'])
    unit_id = str(request.GET['unit_id'])
    unit_path = '/usr/src/app/static/' + mod_name + '/units/' + unit_id + '.fbi'
    print('unit path: ')
    print(unit_path)
    data = open(unit_path, 'r')
    json_response = {
        "raw_fbi_file": data.read()
    }
    # try:
    #     output_final.write(data.read())
    # except:
    #     print('FAIL')
    return Response(json.dumps(json_response))


class LoginView(GenericAPIView):
    """
    Windows Server 2016 (English DVD)
    Product Key: 2KNJJ-33Y9H-2GXGX-KMQWH-G6H67

    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework

    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = Token
    response_serializer = TokenSerializer



    def login(self):
        # ACTIVATE REDIS CONNECITON
        c = StrictRedis(connection_pool=redis_connection_pool)



        self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(
            user=self.user)

        # SERIALIZE JAWN USER FOR WRITING TO REDIS
        jawn_user = JawnUser.objects.get(base_user=self.user)
        j = JawnUserSerializer(jawn_user, context=self.get_serializer_context())
        json = JSONRenderer().render(j.data)

        # This is where we write to the Redis Store
        c.set('tokens:' + self.token.key, json.decode("utf-8"))


        if getattr(settings, 'REST_SESSION_LOGIN', True):
            login(self.request, self.user)

    def get_response(self):
        return Response(
            self.response_serializer(self.token).data, status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)
        self.login()
        return self.get_response()


class LogoutView(APIView):

    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.

    Accepts/Returns nothing.
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class UserDetailsView(RetrieveUpdateAPIView):

    """
    Returns User's details in JSON format.

    Accepts the following GET parameters: token
    Accepts the following POST parameters:
        Required: token
        Optional: email, first_name, last_name and UserProfile fields
    Returns the updated UserProfile and/or User object.
    """
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class PasswordResetView(GenericAPIView):

    """
    Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.
    """

    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return Response(
            {"success": "Password reset e-mail has been sent."},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmView(GenericAPIView):

    """
    Password reset e-mail link is confirmed, therefore this resets the user's password.

    Accepts the following POST parameters: new_password1, new_password2
    Accepts the following Django URL arguments: token, uid
    Returns the success/fail message.
    """

    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "Password has been reset with the new password."})


class PasswordChangeView(GenericAPIView):

    """
    Calls Django Auth SetPasswordForm save method.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """

    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": "New password has been saved."})
