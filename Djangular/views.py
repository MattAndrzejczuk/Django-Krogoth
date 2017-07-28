from django.contrib.auth import login, logout
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.renderers import JSONRenderer

from django.template import loader
from django.http import HttpResponse
import json
import os
from os import walk
from PIL import Image

from django.contrib.auth.models import User
from Djangular.models import DjangularMasterViewController


from GeneralWebsiteInfo.models import BootScreenLoader
from rest_framework.permissions import IsAuthenticated, AllowAny


from DatabaseSandbox.models import VisitorLogSB

from Djangular.models import DjangularService, DjangularDirective, DjangularSlaveViewController, \
    DjangularIcon, DjangularCategory, DjangularMasterViewController, SampleModelOne

from rest_framework import status
from rest_framework import viewsets

from Djangular.serializers import SampleModelOneSerializer

import subprocess





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
                                                icon='icon-home',
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

    context = {
        "message": "TA Lazarus " + current_build_1[:3] + "." + current_build_2,
        "DjangularMasterViewControllers": DjangularMasterViewControllers,
        "splash_title": splash_title,
        "font_size": font_size,
        "splash_logo_bg_color": splash_logo_bg_color,
        "width": width,
        "main_bg_color": main_bg_color,
        "font_color": font_color,
    }
    return HttpResponse(template.render(context, request))



class DynamicJavaScriptInjector(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = request.GET['name']

        application = DjangularMasterViewController.objects.get(name=name)

        raw_js_services_and_directives = ''
        djangular_services = application.djangular_service.all()
        print('SHITTING...')
        # raw_js_services_and_directives += '\n\n'
        djangular_directives = application.djangular_directive.all()

        #     raw_js_services_and_directives = raw_js_services_and_directives.replace('_DJANGULAR_DIRECTIVE_TITLE_', directive.title)
        # raw_js_services_and_directives += '\n\n'

        djangular_slaves = application.djangular_slave_vc.all()
        slave_controllers_js = ''
        slave__states = []
        msApiProviders = []
        for slave in djangular_slaves:
            CRUD_MODEL = 'SampleModelOneView'
            slave.name = application.name
            STATE_IDENTIFIER = 'FUSE_APP_NAME.' + slave.name
            STATE_URI = slave.title
            print('dude... wtf...')
            slave_identifier = slave.name + '.' + slave.title # FUSE_APP_NAME._SLAVE_NAME_
            state_pt_1 = ".state('app."+slave_identifier+"', {url: '/" + STATE_URI + "/:id', views: { "
            state_pt_2 = "'content@app': { templateUrl: '/Djangular/DynamicHTMLSlaveInjector/" + str(slave.id) + "/', "
            state_pt_3 = " controller: '"+slave.title+"Controller as vm' } "
            state_pt_4 = "  }, resolve: { Model"+slave.title+": function (msApi) { "
            state_pt_5 = " return msApi.resolve('app."+STATE_IDENTIFIER+"REST@get' "
            state_pt_6 = " ); } } })  "
            msApiStateItem = state_pt_1 + state_pt_2 + state_pt_3 + state_pt_4 + state_pt_5 + state_pt_6
            msApiProvider = "msApiProvider.register('app."+STATE_IDENTIFIER+"REST', ['"
            msApiProvider += "/Djangular/CRUD/" + CRUD_MODEL + "/:id']);"
            slave__states.append(msApiStateItem)
            msApiProviders.append(msApiProvider)
            slave_controllers_js += slave.controller_js.replace('_SLAVE_NAME_', slave.title).replace('FUSE_APP_NAME', application.name)

        statesAsString = ''
        providersAsString = ''
        for state in slave__states:
            statesAsString += state

        for provider in msApiProviders:
            providersAsString += provider

        module_with_injected_msApi = application.module_js.replace('_DJANGULAR_SLAVE_VC_INJECTION_POINT_', statesAsString)
        module_with_injected_msApi_2 = module_with_injected_msApi.replace('_DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_', providersAsString)

        newMsNavSrv = ''
        for slave in djangular_slaves:
            parse_1 = "msNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME"+slave.title+"', { "
            parse_2 = "	title: 'FUSE_APP_TITLE"+slave.title+"', "
            parse_3 = " icon: 'FUSE_APP_ICON', "
            parse_4 = " state: 'app.FUSE_APP_NAME."+slave.title+"', "
            parse_5 = " weight: 3 }); "
            newMsNavSrv += parse_1 + parse_2 + parse_3 + parse_4 + parse_5
            print(newMsNavSrv)

        module_with_injected_navigation = module_with_injected_msApi_2.replace('_DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_', newMsNavSrv)
        print('WHAT')
        clean_js_slate = ''

        clean_js_slate += module_with_injected_navigation + \
                          ' ' + application.controller_js
        clean_js_slate += slave_controllers_js


        # clean_js_slate += application.controller_js.replace('_DJANGULAR_SLAVE_VC_INJECTION_POINT_', '') + \
        #                  ' ' + application.controller_js

        for service in djangular_services:
            raw_js_services_and_directives += service.service_js.replace('_DJANGULAR_SERVICE_NAME_', service.name).replace('_DJANGULAR_SERVICE_TITLE_', service.title)
            # raw_js_services_and_directives = raw_js_services_and_directives.replace('_DJANGULAR_SERVICE_TITLE_', service.title)

        print('THE')
        for directive in djangular_directives:
            raw_js_services_and_directives += directive.directive_js.replace('_DJANGULAR_DIRECTIVE_NAME_', directive.name).replace("_DJANGULAR_DIRECTIVE_TITLE_", directive.title)
            # raw_js_services_and_directives = raw_js_services_and_directives


        clean_js_slate += raw_js_services_and_directives
        print('FUCK')
        parsed1 = clean_js_slate.replace('FUSE_APP_NAME', application.name.replace(' ','_'))
        parsed2 = parsed1.replace('FUSE_APP_TITLE', application.title)
        parsed3 = parsed2.replace('FUSE_APP_ICON', application.icon.code)
        parsed4 = parsed3.replace('NAV_HEADER', application.category.name.replace(' ','_'))
        raw_js_response = parsed4

        return HttpResponse(raw_js_response)


class DynamicHTMLInjector(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = request.GET['name']
        application = DjangularMasterViewController.objects.get(name=name)
        raw_html_response = application.view_html


        if raw_html_response == '':
            raw_html_response += '<div layout="column" layout-padding layout-margin>'
            raw_html_response += '<h1>' + application.name.replace('_', ' ') + '</h1>'
            raw_html_response += '<h3>No Fuse App HTML Component</h3>'
            info = "You're seeing this message because no Fuse App HTML component with the type: HTML has not been " + \
                   "added to this Angular Fuse Application named " + application.name
            raw_html_response += "<p>" + info + "</p>"
            raw_html_response += '</div>'
        return HttpResponse(raw_html_response)


class DynamicHTMLSlaveInjector(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, id, format=None):
        slave_application = DjangularSlaveViewController.objects.get(id=id)
        return HttpResponse(slave_application.view_html.replace('FUSE_APP_NAME', slave_application.name).replace('_SLAVE_NAME_', slave_application.title))


class DynamicJavaScriptSlaveInjector(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, id, format=None):
        slave_application = DjangularSlaveViewController.objects.get(id=id)
        return HttpResponse(slave_application.controller_js.replace('FUSE_APP_NAME', slave_application.name).replace('_SLAVE_NAME_', slave_application.title))


class SampleModelOneView(viewsets.ModelViewSet):
    serializer_class = SampleModelOneSerializer
    queryset = SampleModelOne.objects.all()