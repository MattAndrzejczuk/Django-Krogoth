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








def index(request):
    template = loader.get_template('index.html')
    context = {
        "message": "Welcome to CiniCrafts official website!",
    }
    return HttpResponse(template.render(context, request))

def list_ta_units(request):
    unitListPrettyJSON = LazarusListUnits()
    unitListPrettyJSON.printContents()
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
        self.f = []
        self.d = []
        self.output_final = open('workfile', 'w')
        self.jsonResponse = []
        self.root = os.path.join(BASE_DIR, 'static') + '/'



    def printSubContents(self, pathName):
        jsonResponse = []

        for (dirpath, dirnames, filenames) in walk(self.root + pathName):
            print('PATHNAME')

            if pathName == 'unitpics':
                for file in filenames:
                    filename, file_extension = os.path.splitext(file)
            # print(file_extension + "     :     " + filename)
                    print(self.root + pathName + '/' + file)
                    print( file_extension.lower())
                    pathToFile = self.root + pathName + '/' + file
                #if file_extension.lower() == '.pcx':
                    try:
                        img = Image.open(pathToFile)
                        imgSaveTo = self.root + pathName + '/' + filename + '.png'
                        img.save(imgSaveTo, format='png')
                        jsonResponse.append({'thumbnail': imgSaveTo, 'object_name':filename})
                    except:
                        print('OHHHH SHIT!!!')
                break
        return jsonResponse

    def printContents(self):
        jsonFinal = []
        for (dirpath, dirnames, filenames) in walk(self.root):
            self.f.extend(filenames)
            self.d.extend(dirnames)
            for path in dirnames:
                self.printSubContents(path)
            break

    def printUnitFBI(self):
        return
    # data = open('HPI/' + pathName + '/' + file, 'r')
    # try:
    #     output_final.write(data.read())
    # except:
    #     print('FAIL')
    # print(file_extension)


    def getUnitInfo(self, unitId):
        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


    def get(self, request, format=None):
        unitListPrettyJSON = LazarusListUnits()
        unitListPrettyJSON.printContents()
        return Response(unitListPrettyJSON.jsonResponse)


class LoginView(GenericAPIView):

    """
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
