from django.contrib.auth import login, logout
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from chat.models import JawnUser
from chat.serializers import JawnUserSerializer
from rest_framework.renderers import JSONRenderer
from redis import ConnectionPool, StrictRedis
from jawn import settings as redis_settings
from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.models import User
from moho_extractor.models import NgIncludedJs

from .app_settings import (
    TokenSerializer, UserDetailsSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer
)

from rest_framework.permissions import IsAuthenticated, AllowAny
from krogoth_gantry.models import KrogothGantryIcon, KrogothGantryCategory, KrogothGantryMasterViewController
from krogoth_core.models import AKFoundationAbstract

import jsbeautifier

import subprocess

redis_connection_pool = ConnectionPool(**redis_settings.WS4REDIS_CONNECTION)





def index(request):
    permission_classes = (AllowAny,)
    template = loader.get_template('index.html')

    splash_html = '<ms-splash-screen id="splash-screen"> <div class="center"> <div class="logo" style="width:250px; font-size: 36px; background-color: darkorange;"> <span>Lazarus</span> </div> <!-- Material Design Spinner --> <div class="spinner-wrapper"> <div class="spinner"> <div class="inner"> <div class="gap"></div> <div class="left"> <div class="half-circle"></div> </div> <div class="right"> <div class="half-circle"></div> </div> </div> </div> </div> <!-- / Material Design Spinner --> </div></ms-splash-screen>'

    splash_title = 'Krogoth'
    font_size = 36
    splash_logo_bg_color = 'antiquewhite'
    width = 250
    main_bg_color = 'darkolive'
    font_color = 'black'



    print('SOMEONE IS REQUESTING THE INDEX HTML PAGE ! ! !')



    KrogothGantryMasterViewControllers = []
    all_applications = KrogothGantryMasterViewController.objects.filter(is_enabled=True)
    for application in all_applications:
        KrogothGantryMasterViewControllers.append(application.name)


    # if current_build_2 == '00':
    #     current_build_2 = '0'
    # else:
    #     rm_0s = current_build_2.replace('01', '1').replace('02', '2').replace('03', '3').replace('04', '4')
    #     current_build_2 = rm_0s.replace('05', '5').replace('06', '6').replace('07', '7').replace('08', '8').replace('09', '9')
    version_build = 'Krogoth ' + settings.APP_VERSION
    seo_title = "Krogoth "
    seo_description = 'description'
    seo_description += ', description - 2'
    try:
        if request.META['PATH_INFO'] == '/features/':
            seo_title = 'ArmPrime - Upcoming features for TA mod development'
            seo_description = 'Features and web based tools ArmPrime will have in the future for Total Annihilation.'
            seo_description += ' Random Map Generator, Enhanced Skirmish Mode, and more Lazarus updates'
    except:
        pass

    try:
        if request.META['PATH_INFO'] == '/news/':
            seo_title = 'ArmPrime - Latest News and Updates'
            seo_description = 'Lazarus is almost ready for building and playing Total Annihilation mods.'
            seo_description += ' - Posted by Matt on September 14, 2017'
    except:
        pass

    try:
        if request.META['PATH_INFO'] == '/whatIsLazarus/':
            seo_title = 'ArmPrime - What is Total Annihilation: Lazarus?'
            seo_description = 'Total Annihilation Lazarus is a new web based mod builder and conflict crusher '
            seo_description += 'for the 1997 classic Total Annihilation released by Cavedog entertainment.'
    except:
        pass

    try:
        if request.META['PATH_INFO'] == '/status/':
            seo_title = 'ArmPrime Lazarus - Current Project Status'
            seo_description = 'There are currently 3 major components of Lazarus that will need to be completed before the public beta test.'
            seo_description += ' Mod Nanolather, Download TDF Editor, and Weapon TDF Editor'
    except:
        pass

    try:
        if request.META['PATH_INFO'] == '/forums/':
            seo_title = 'ArmPrime - Community Forums'
            seo_description = 'Discuss anything related to Cavedog\'s 1997 Real Time Strategy game Total Annihilation.'
    except:
        pass


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

    context = {
        "version_build": version_build,
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



class GooglePlusOAuthCallbackView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        msg = "There's nothing here yet..."
        return Response(
            msg,
            status=200
        )



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
        jawn_user = JawnUser.get_or_create_jawn_user(username=self.user.username) #JawnUser.objects.get(base_user=self.user)
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
