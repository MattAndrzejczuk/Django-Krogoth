from django.contrib.auth import login, logout
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from krogoth_chat.models import JawnUser
from krogoth_chat.serializers import JawnUserSerializer
from rest_framework.renderers import JSONRenderer
from redis import ConnectionPool, StrictRedis
from jawn import settings as redis_settings
from django.template import loader
from django.http import HttpResponse
from jawn.settings import STATIC_KROGOTH_MODE
from django.contrib.auth.models import User

from .app_settings import (
    TokenSerializer, UserDetailsSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer
)

from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_gantry.models import KrogothGantryIcon, KrogothGantryCategory, KrogothGantryMasterViewController
from krogoth_core.models import AKFoundationAbstract, AKBowerComponent
redis_connection_pool = ConnectionPool(**redis_settings.WS4REDIS_CONNECTION)

import os



def index(request):
    permission_classes = (AllowAny,)
    template = loader.get_template('index.html')
    splash_title = 'Krogoth'
    font_size = 36
    splash_logo_bg_color = 'antiquewhite'
    width = 250
    main_bg_color = 'darkolive'
    font_color = 'black'



    print('SOMEONE IS REQUESTING THE INDEX HTML PAGE ! ! !')



    KrogothGantryMasterViewControllers = []
    if STATIC_KROGOTH_MODE == False:
        all_applications = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
        for application in all_applications:
            KrogothGantryMasterViewControllers.append('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + application.name)
    else:
        all_applications = os.listdir('static/compiled')
        for application in all_applications:
            KrogothGantryMasterViewControllers.append('/static/compiled/' + application)

    version_build = 'Krogoth ' + settings.APP_VERSION
    seo_title = "Krogoth "
    seo_description = 'description'
    seo_description += ', description - 2'


    KrogothMainComponents = []
    all_parts = AKFoundationAbstract.objects.filter(is_selected_theme=True)
    for p in all_parts:
        if p.first_name == "core" or \
                p.first_name == "index" or \
                p.first_name == "main" or \
                p.first_name == "quick-panel" or \
                p.first_name == "toolbar" or \
                p.first_name == "navigation":
            pass
        else:
            KrogothMainComponents.append(p.unique_name)

    all_bowers = AKBowerComponent.objects.all()

    context = {
        "version_build": version_build,
        "all_bowers": all_bowers,
        "core":KrogothMainComponents,
        "message": seo_title,
        "description": seo_description,
        "KrogothGantryMasterViewControllers": KrogothGantryMasterViewControllers,
        "splash_title": splash_title,
        "font_size": font_size,
        "splash_logo_bg_color": splash_logo_bg_color,
        "width": width,
        "main_bg_color": main_bg_color,
        "font_color": font_color
    }
    return HttpResponse(template.render(context, request))




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
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.user.username)
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

        try:
            POST_username = request.data['username']
            POST_email = request.data['email']
            POST_password = request.data['password']
            user = User.objects.create_user(POST_username, password=POST_password)
            user.email = POST_email
            user.is_superuser = False
            user.is_staff = False
            user.save()

            jawn_user = JawnUser()
            jawn_user.base_user = user

            try:
                POST_side = request.data['faction']
                jawn_user.faction = POST_side
            except:
                pass

            jawn_user.save()

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



    # def get_object(self):
    #     return self.request.user

    def get(self, request, format=None):
        print('CURRENT USER: ')
        print('is_staff: ')
        print(request.user.is_staff)

        user = {}
        user['username'] = request.user.username
        user['id'] = request.user.id
        user['is_staff'] = request.user.is_staff

        try:
            jawn_user = JawnUser.objects.get(base_user=request.user)
            user['faction'] = jawn_user.faction
        except:
            pass

        return Response(
            user,
            status=200
        )


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
