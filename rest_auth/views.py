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


from django.contrib.auth.models import User
from dynamic_lazarus_page.models import AngularFuseApplication

from DatabaseSandbox.models import VisitorLogSB, LazarusCommanderAccountSB, \
    LazarusModProjectSB, BasicUploadTrackerSB

from .app_settings import (
    TokenSerializer, UserDetailsSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer
)

from GeneralWebsiteInfo.models import BootScreenLoader


import subprocess

redis_connection_pool = ConnectionPool(**redis_settings.WS4REDIS_CONNECTION)



def index(request):
    template = loader.get_template('index.html')

    Djangular = []

    all_applications = AngularFuseApplication.objects.all()
    for application in all_applications:
        Djangular.append(application.name)

    _1 = str(request.META['REMOTE_ADDR'])
    _2 = str(request.META['HTTP_USER_AGENT'])
    _3 = str(request.META['HTTP_ACCEPT_LANGUAGE'])
    newRecord = VisitorLogSB(remote_addr=_1, http_usr=_2, http_accept=_3, other_misc_notes='index.html requested.')
    newRecord.save()

    # GET LAZARUS BUILD VERSION:
    bash_cmd = ['git', 'rev-list', '--count', 'master']
    get_build_cmd = str(subprocess.check_output(bash_cmd))
    current_build_1 = ''
    current_build_2 = ''
    try:
        current_build_1 = ('0.' + str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", "")) + '.'
        current_build_2 = (str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", ""))[1:]
    except:
        print('failed to check version!!!')

    context = {
        "message": "TA Lazarus " + current_build_1[:3] + "." + current_build_2,
        "Djangular": Djangular
    }
    return HttpResponse(template.render(context, request))



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


class RegisterUserBasic(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print('PRINTING POST REQUEST: ')
        print(request.POST)
        try:
            #user = User.objects.create_user('foo', password='bar')
            #user.is_superuser = True
            #user.is_staff = True
            #user.save()
            return Response({"result": "Successfully registered."},
                            status=status.HTTP_201_CREATED)
        except:
            return Response({"result": "Registration failed."},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
