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
from dynamic_lazarus_page.models import AngularFuseApplication, NgIncludedHtml, NgIncludedJs

from DatabaseSandbox.models import VisitorLogSB, LazarusCommanderAccountSB, \
    LazarusModProjectSB, BasicUploadTrackerSB

from .app_settings import (
    TokenSerializer, UserDetailsSerializer, LoginSerializer,
    PasswordResetSerializer, PasswordResetConfirmSerializer,
    PasswordChangeSerializer
)

from GeneralWebsiteInfo.models import BootScreenLoader
from rest_framework.permissions import IsAuthenticated, AllowAny

from Djangular.models import DjangularService, DjangularDirective, DjangularSlaveViewController, \
    DjangularIcon, DjangularCategory, DjangularMasterViewController, SampleModelOne


import subprocess

redis_connection_pool = ConnectionPool(**redis_settings.WS4REDIS_CONNECTION)



# def index(request):
#     permission_classes = (AllowAny,)
#     template = loader.get_template('index.html')
#
#     splash_html = '<ms-splash-screen id="splash-screen"> <div class="center"> <div class="logo" style="width:250px; font-size: 36px; background-color: darkorange;"> <span>Lazarus</span> </div> <!-- Material Design Spinner --> <div class="spinner-wrapper"> <div class="spinner"> <div class="inner"> <div class="gap"></div> <div class="left"> <div class="half-circle"></div> </div> <div class="right"> <div class="half-circle"></div> </div> </div> </div> </div> <!-- / Material Design Spinner --> </div></ms-splash-screen>'
#
#     splash_title = 'Lazarus'
#     font_size = 36
#     splash_logo_bg_color = 'antiquewhite'
#     width = 250
#     main_bg_color = 'darkolive'
#     font_color = 'black'
#
#     try:
#         splash = BootScreenLoader.objects.filter(enabled=True)
#         splash_html = splash[0].html_code
#         splash_title = splash[0].title
#         font_size = splash[0].font_size
#         splash_logo_bg_color = splash[0].logo_background_color
#         width = splash[0].width
#         main_bg_color = splash[0].main_background_color
#         font_color = splash[0].font_color
#     except:
#         print('There is no splash screen in the Database!')
#
#
#     AngularFuseApplications = []
#     all_applications = AngularFuseApplication.objects.all()
#     for application in all_applications:
#         AngularFuseApplications.append(application.name)
#
#     _1 = str(request.META['REMOTE_ADDR'])
#     _2 = str(request.META['HTTP_USER_AGENT'])
#     _3 = str(request.META['HTTP_ACCEPT_LANGUAGE'])
#     newRecord = VisitorLogSB(remote_addr=_1, http_usr=_2, http_accept=_3, other_misc_notes='index.html requested.')
#     newRecord.save()
#
#     # GET LAZARUS BUILD VERSION:
#     bash_cmd = ['git', 'rev-list', '--count', 'master']
#     get_build_cmd = str(subprocess.check_output(bash_cmd))
#     current_build_1 = ''
#     current_build_2 = ''
#     try:
#         current_build_1 = ('0.' + str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", "")) + '.'
#         current_build_2 = (str(get_build_cmd).replace("b'", "").replace("\\n", "").replace("'", ""))[1:]
#     except:
#         print('failed to check version!!!')
#
#     context = {
#         "message": "TA Lazarus " + current_build_1[:3] + "." + current_build_2,
#         "AngularFuseApplications": AngularFuseApplications,
#         "splash_title": splash_title,
#         "font_size": font_size,
#         "splash_logo_bg_color": splash_logo_bg_color,
#         "width": width,
#         "main_bg_color": main_bg_color,
#         "font_color": font_color,
#     }
#     return HttpResponse(template.render(context, request))

import jsbeautifier

def index(request):
    permission_classes = (AllowAny,)
    template = loader.get_template('index.html')

    splash_html = '<ms-splash-screen id="splash-screen"> <div class="center"> <div class="logo" style="width:250px; font-size: 36px; background-color: darkorange;"> <span>Lazarus</span> </div> <!-- Material Design Spinner --> <div class="spinner-wrapper"> <div class="spinner"> <div class="inner"> <div class="gap"></div> <div class="left"> <div class="half-circle"></div> </div> <div class="right"> <div class="half-circle"></div> </div> </div> </div> </div> <!-- / Material Design Spinner --> </div></ms-splash-screen>'

    splash_title = 'Lazarus'
    font_size = 36
    splash_logo_bg_color = 'antiquewhite'
    width = 250
    main_bg_color = 'darkolive'
    font_color = 'black'

    try:
        splash = BootScreenLoader.objects.filter(enabled=True)
        splash_html = splash[0].html_code
        splash_title = splash[0].title
        font_size = splash[0].font_size
        splash_logo_bg_color = splash[0].logo_background_color
        width = splash[0].width
        main_bg_color = splash[0].main_background_color
        font_color = splash[0].font_color
    except:
        print('There is no splash screen in the Database!')



    print('SOMEONE IS REQUESTING THE INDEX HTML PAGE ! ! !')
    check_if_default_vc_exists = DjangularMasterViewController.objects.all()
    print(len(check_if_default_vc_exists))
    if len(check_if_default_vc_exists) == 0:

        defaultIcon = DjangularIcon(name='home, house', code='icon-home')
        defaultIcon.save()

        print('NO DEFAULT APP DETECTED!')
        print('creating a default Djangular application...')
        defaultCategory = DjangularCategory(name='Djangular', code='hello!!')
        defaultCategory.save()

        default_html_header = '<h1>It works!</h1>'
        default_html_body = "<h4>Congratulations, you've successfully installed a new Djangular Application.</h4>"
        default_html_pt1 = '<div flex="20"></div><div flex="60" layout="column">'
        default_html_pt2 = '</div><div flex="20"></div>'

        default = DjangularMasterViewController(name='home',
                                                title='It Works',
                                                icon=defaultIcon,
                                                category=defaultCategory,
                                                view_html=default_html_pt1 + default_html_header + default_html_body + default_html_pt2)
        default.save()




    DjangularMasterViewControllers = []
    all_applications = DjangularMasterViewController.objects.all()
    for application in all_applications:
        DjangularMasterViewControllers.append(application.name)

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

    index_route_js = '/static/app/index.route.js'
    try:
        mainHtmlLayout = NgIncludedJs.objects.get(name='mainHtmlLayout')
        index_route_js = mainHtmlLayout.url_helper
        print('_ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ _')
        print(index_route_js)
        print('_ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ _')
    except:
        _main_ = " '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar-2.html' "
        _toolbar_ = " '/static/app/toolbar/layouts/vertical-navigation-fullwidth-toolbar-2/toolbar.html' "
        _navigation_ = " '/static/app/navigation/layouts/vertical-navigation-fullwidth-toolbar-2/navigation.html' "
        js_raw = "(function () {'use strict';angular.module('fuse').config(routeConfig); function routeConfig($stateProvider, $urlRouterProvider, $locationProvider) {$locationProvider.hashPrefix('!');$urlRouterProvider.otherwise('/home');var $cookies;angular.injector(['ngCookies']).invoke(['$cookies', function (_$cookies) {$cookies = _$cookies;}]);var layoutStyle = $cookies.get('layoutStyle') || 'LAYOUT_STYLE';' + " \
                 "'var layouts = {LAYOUT_STYLE: {main: " + \
                 _main_ + \
                 ",toolbar: " + \
                 _toolbar_ + \
                 ",navigation: " + \
                 _navigation_ + \
                 "}, " + \
                 "contentOnly: {main: '/static/app/core/layouts/content-only.html', toolbar: '', navigation: ''},contentWithToolbar: {main: '/static/app/core/layouts/content-with-toolbar.html',toolbar: '/static/app/toolbar/layouts/content-with-toolbar/toolbar.html',navigation: ''}};$stateProvider.state('app', {abstract: true,views: {'main@': {templateUrl: layouts[layoutStyle].main, controller: 'MainController as vm'},'toolbar@app': {templateUrl: layouts[layoutStyle].toolbar, controller: 'ToolbarController as vm'},'navigation@app': {templateUrl: layouts[layoutStyle].navigation,controller: 'NavigationController as vm'},'quickPanel@app': {templateUrl: '/static/app/quick-panel/quick-panel.html',controller: 'QuickPanelController as vm'}}});}})();"
        newLayout = NgIncludedJs(name='mainHtmlLayout', contents=jsbeautifier.beautify(js_raw))
        newLayout.save()
        index_route_js = newLayout.url_helper
        print(' ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')
        print(index_route_js)
        print(' ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ☭ ')

    if current_build_2 == '00':
        current_build_2 = '0'
    else:
        current_build_2 = current_build_2.replace('0', '')

    context = {
        "message": "Djangular " + current_build_1[:3] + "." + current_build_2,
        "DjangularMasterViewControllers": DjangularMasterViewControllers,
        "splash_title": splash_title,
        "font_size": font_size,
        "splash_logo_bg_color": splash_logo_bg_color,
        "width": width,
        "main_bg_color": main_bg_color,
        "font_color": font_color,
        "index_route_js": index_route_js
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
