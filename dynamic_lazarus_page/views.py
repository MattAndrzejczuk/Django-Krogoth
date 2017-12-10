from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView

from dynamic_lazarus_page.models import FuseAppComponent, AngularFuseApplication, NgIncludedHtml, NgIncludedJs
from Djangular.models import DjangularMasterViewController

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from django.conf import settings

from GeneralWebsiteInfo.models import WebsiteColorTheme, WebsiteLayout, NavigationBar, BootScreenLoader


CCD = {
    0: '\033[0m',  # end

    200: '\033[3m',  # italic
    201: '\033[4m',  # underline
    202: '\033[1m',  # bold
    203: '\033[2m',  # darkish

    108: '\033[7m',  # highlight
    107: '\033[107m',  # oj highlight
    106: '\033[106m',  # cyan highlight
    105: '\033[105m',  # magenta highlight
    104: '\033[104m',  # blue highlight
    103: '\033[103m',  # yellow highlight
    102: '\033[102m',  # green highlight
    101: '\033[101m',  # red highlight
    100: '\033[100m',  # purple highlight

    1: '\033[31m',  # dark red
    2: '\033[32m',  # dark green
    3: '\033[33m',  # dark yellow
    4: '\033[34m',  # dark blue
    5: '\033[35m',  # dark magenta
    6: '\033[36m',  # dark cyan
    7: '\033[37m',  # dark yellow

    10: '\033[90m',  # bright purple
    11: '\033[30m',  # purple
    12: '\033[97m',  # oj
    13: '\033[96m',  # cyan
    14: '\033[95m',  # magenta
    15: '\033[94m',  # blue
    16: '\033[93m',  # yellow
    17: '\033[92m',  # green neon
    18: '\033[91m',  # red
}



class NgIncludedJsView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])
        try:
            try:
                data = str(request.GET['data'])
                js_view = NgIncludedJs.objects.get(name=name)
                final_html = js_view.contents.replace('INJECTED_DATA', data)
                return HttpResponse(final_html)
            except:
                js_view = NgIncludedJs.objects.get(name=name)
                return HttpResponse(js_view.contents)
        except:
            html = 'alert("fatal Djangular error, unable to load HTML view: ' + name + \
                    ' try executing: python3 manage.py make_default_layout");'
            return HttpResponse(html)


class NgIncludedHtmlView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = str(request.GET['name'])
        try:
            try:
                data = str(request.GET['data'])
                html_view = NgIncludedHtml.objects.get(name=name)
                final_html = html_view.contents.replace('INJECTED_DATA', data)
                return HttpResponse(final_html)
            except:
                html_view = NgIncludedHtml.objects.get(name=name)
                return HttpResponse(html_view.contents)
        except:
            html = '<div> <h1>Fatal Error</h1> <p>Unable to load HTML: <b>' + name + '</b> </p> </div>'
            html += '<script>alert("fatal Djangular error, unable to load HTML view: ' + name + \
                    ' try executing: python3 manage.py make_default_layout");</script>'
            return HttpResponse(html)



#### 07/12/2017
class OpenTADataFile(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        # msg = str(request.GET['msg'])
        parse_path1 = str(request.GET['encoded_path']).replace('_SLSH_', '/')
        file_type = str(request.GET['type'])
        title = str(request.GET['title'])
        file_path = '/usr/src/persistent/' + parse_path1 + file_type

        try:
            try:
                print('opening file...')
                print(file_path)
                fbi_file = open(file_path, 'r', errors='replace')

                print('file was opened successfully.')

                html1 = '<md-dialog><form ng-cloak>'
                html2_start = '<md-toolbar><div class="md-toolbar-tools"><h2>TITLE_DIALOG_HEADER</h2><span flex></span>'
                html3 = '<md-button class="md-icon-button" ng-click="cancel()">' + \
                        '<md-icon md-svg-src="icon-hexagon" aria-label="Close dialog"></md-icon></md-button>'
                print('1...')
                html4_end = '</div></md-toolbar><md-dialog-content><div class="md-dialog-content">'
                html5 = '</div></md-dialog-content>'
                dialog_actions = '<md-dialog-actions layout="row"><span flex></span>' + \
                                 '<md-button ng-click="answer(\'not useful\')">Cancel</md-button>' + \
                                 '<md-button ng-click="answer(\'useful\')">Add To Current Mod</md-button>' + \
                                 '</md-dialog-actions></form></md-dialog>'
                print('2...')
                content_head = html1 + html2_start + html3 + html4_end
                content_foot = html5 + dialog_actions

                read_file_str = content_head.replace('TITLE_DIALOG_HEADER', title) + remove_comments(fbi_file.read())
                print('3...')
                # read_file_str = read_file_str.replace(';', '; <br>&emsp;')
                # read_file_str = read_file_str.replace('{', '{<br>&emsp;')
                read_file_str += content_foot
                return HttpResponse(read_file_str)
                # json_response = {'raw_data': fbi_file.read()}

            except:
                unitsArray = readFile(unit_path)
                return Response(unitsArray)

        except:
            return Response('oh shit')


class CustomHtmlGenerator(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        # msg = str(request.GET['msg'])
        html = '<div> <h1>Some Basic HTML</h1> <p>This is everything.</p> </div>'
        return HttpResponse(html)


class DynamicIndexModule(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        index_module_pt1 = "(function (){'use strict';angular.module('fuse', ['uiGmapgoogle-maps','textAngular', " + \
                           "'jkAngularCarousel','xeditable','ui.codemirror','app.core','app.sample','app.navigation','app.toolbar','app.quick-panel',"

        index_module_pt2 = ''

        # index_module_pt2 = "'app.dashboards','app.calendar','app.e-commerce','app.mail','app.chat','app.file-manager'," + \
        #                   "'app.gantt-chart','app.scrumboard','app.todo','app.contacts','app.notes','app.toastCtrl','app.lazarus',"

        my_apps = "'app.sample',"

        # inject dynamic apps
        # all_applications = AngularFuseApplication.objects.all()
        # for application in all_applications:
        #     my_apps += ("'app." + application.name + "',")


        all_djangular = DjangularMasterViewController.objects.filter(is_enabled=True)
        for application in all_djangular:
            my_apps += ("'app." + application.name + "',")

        my_apps += "'ui.tree', "

        # my_apps += "'app.pages','app.ui','app.components', "
        my_apps += "'app.sample'"

        index_module_pt3 = "" + \
                           "]);})();"
        indexModuleJs = index_module_pt1 + index_module_pt2 + my_apps + index_module_pt3
        return HttpResponse(indexModuleJs)



class DynamicIndexRoute(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        full_js = "(function (){    'use strict';    angular        .module('fuse')        .config(routeConfig);    /** @ngInject */    function routeConfig($stateProvider, $urlRouterProvider, $locationProvider)    {        $locationProvider.hashPrefix('!');        $urlRouterProvider.otherwise('/Home');        var $cookies;        angular.injector(['ngCookies']).invoke([            '$cookies', function (_$cookies)            {                $cookies = _$cookies;            }        ]);        var layoutStyle = $cookies.get('layoutStyle') || 'verticalNavigation';        var layouts = {            verticalNavigation  : {                main      : '/static/app/core/layouts/vertical-navigation.html',                toolbar   : '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar.html',                navigation: '/static/app/navigation/layouts/vertical-navigation/navigation.html'            },            verticalNavigationFullwidthToolbar  : {                main      : '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar.html',                toolbar   : '/static/app/toolbar/layouts/vertical-navigation-fullwidth-toolbar/toolbar.html',                navigation: '/static/app/navigation/layouts/vertical-navigation/navigation.html'            },            verticalNavigationFullwidthToolbar2  : {                main      : '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar-2.html',                toolbar   : '/static/app/toolbar/layouts/vertical-navigation-fullwidth-toolbar-2/toolbar.html',                navigation: '/static/app/navigation/layouts/vertical-navigation-fullwidth-toolbar-2/navigation.html'            },            horizontalNavigation: {                main      : '/static/app/core/layouts/horizontal-navigation.html',                toolbar   : '/static/app/toolbar/layouts/horizontal-navigation/toolbar.html',                navigation: '/static/app/navigation/layouts/horizontal-navigation/navigation.html'            },            contentOnly         : {                main      : '/static/app/core/layouts/content-only.html',                toolbar   : '',                navigation: ''            },            contentWithToolbar  : {                main      : '/static/app/core/layouts/content-with-toolbar.html',                toolbar   : '/static/app/toolbar/layouts/content-with-toolbar/toolbar.html',                navigation: ''            }        };        $stateProvider            .state('app', {                abstract: true,                views   : {                    'main@'         : {                        templateUrl: layouts[layoutStyle].main,                        controller : 'MainController as vm'                    },                    'toolbar@app'   : {                        templateUrl: layouts[layoutStyle].toolbar,                        controller : 'ToolbarController as vm'                    },                    'navigation@app': {                        templateUrl: layouts[layoutStyle].navigation,                        controller : 'NavigationController as vm'                    },                    'quickPanel@app': {                        templateUrl: '/static/app/quick-panel/quick-panel.html',                        controller : 'QuickPanelController as vm'                    }                }            });    }})();"
        default_url = 'Home'
        try:
            print('Getting Djangular app with id: 1')
            application = DjangularMasterViewController.objects.get(id=1)
            print(application.title)
            default_url = application.name.replace(' ', '_')
            print(application.name)
        except:
            print('Something fucked up, reverting to Home')
            default_url = 'Home'
        toolbar_html =  '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar.html' ## '/dynamic_lazarus_page/DynamicHTMLToolbar/'
        parsed_js_1 = full_js.replace('FUSE_DEFAULT_APP', default_url)
        parsed_js_2 = parsed_js_1.replace('FUSE_TOOLBAR_HTML', toolbar_html)
        return HttpResponse(parsed_js_2)






class DynamicSplashScreenView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        splash = BootScreenLoader.objects.filter(enabled=True)
        final_html = splash[0]
        return HttpResponse(final_html)




class DynamicJavaScriptInjector(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = request.GET['name']
        application = AngularFuseApplication.objects.get(name=name)
        components = FuseAppComponent.objects.filter(parent_app=application)

        clean_js_slate = application.js_module + ' ' + application.js_controller

        parsed1 = clean_js_slate.replace('FUSE_APP_NAME', application.name)
        parsed2 = parsed1.replace('FUSE_APP_TITLE', application.name.replace('_', ' '))
        parsed3 = parsed2.replace('FUSE_APP_ICON', application.icon)
        parsed4 = parsed3.replace('NAV_HEADER', application.category)
        raw_js_response = parsed4

        for comp in components:
            if comp.type == 'js':
                parsed1 = comp.contents.replace('FUSE_APP_NAME', application.name)
                parsed2 = parsed1.replace('FUSE_APP_TITLE', application.name.replace('_', ' '))
                parsed3 = parsed2.replace('FUSE_APP_ICON', application.icon)
                raw_js_response += parsed3
        return HttpResponse(raw_js_response)


class DynamicHTMLInjector(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        name = request.GET['name']
        application = AngularFuseApplication.objects.get(name=name)
        components = FuseAppComponent.objects.filter(parent_app=application)
        raw_html_response = application.html_main
        for comp in components:
            if comp.type == 'html':
                parsed1 = comp.contents.replace('FUSE_APP_NAME', application.name)
                parsed2 = parsed1.replace('FUSE_APP_TITLE', application.name.replace('_', ' '))
                raw_html_response += parsed2
        if raw_html_response == '':
            raw_html_response += '<div layout="column" layout-padding layout-margin>'
            raw_html_response += '<h1>' + application.name.replace('_', ' ') + '</h1>'
            raw_html_response += '<h3>No Fuse App HTML Component</h3>'
            info = "You're seeing this message because no Fuse App HTML component with the type: HTML has not been " + \
                   "added to this Angular Fuse Application named " + application.name
            raw_html_response += "<p>" + info + "</p>"
            raw_html_response += '</div>'
        return HttpResponse(raw_html_response)



class AngularFuseApplicationView(APIView):
    # serializer_class = SuperBasicModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)  

    def get(self, request, format=None):
        try:
            name = request.GET['name']
            print('got the name')
            application = AngularFuseApplication.objects.get(name=name)
            print('got the application')
            json_response = {'id': application.id, 'name': application.name, 'components': []}
            print('made the json_response')
            components = FuseAppComponent.objects.filter(parent_app=application)
            print('queried the components')
            for comp in components:
                json_response['components'].append({'name': comp.name,
                                                    'id': comp.id,
                                                    'type': comp.type,
                                                    'contents': comp.contents.replace('FUSE_APP_NAME',
                                                                                      application.name)})
            return Response(json_response)
        except:
            allmodels = AngularFuseApplication.objects.all()
            final_json = {}
            all_ = []
            for item in allmodels:
                all_.append({'name': item.name,
                             'id': item.id})
            final_json['AngularFuseApplication_list'] = all_
            return Response(final_json)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        new_app = AngularFuseApplication(name=name)
        new_app.save()
        response = {'result': 'If you are reading this, that means it worked!!! ',
                    'new_app': str(new_app)}
        return Response(response)


class FuseAppComponentView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)  # IsAuthenticated

    def get(self, request, format=None):
        try:
            print('trying to grab GET shit...')
            component_id = request.GET['component_id']
            print('try will fail here.... so moving on.')
            component = FuseAppComponent.objects.get(name=component_id)
            return HttpResponse(component.contents.replace('FUSE_APP_NAME', name))
        except:
            print('DOING EXCEPTION SHIT NOW...')
            allmodels = FuseAppComponent.objects.all()
            final_json = {}
            all_ = []
            for item in allmodels:
                all_.append({'name': item.name,
                             'id': item.id,
                             'contents': item.contents.replace('FUSE_APP_NAME', item.parent_app.name),
                             'application_name': item.parent_app.name})
            final_json['AngularFuseApplication_list'] = all_
            return Response(final_json)

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        type = request.POST['type']
        parent_app = request.POST['parent_app']
        contents = request.POST['contents']

        print(CCD[1] + ' name ' + CCD[0] + CCD[12] + name + CCD[0])
        print(CCD[2] + ' type ' + CCD[0] + CCD[13] + type + CCD[0])
        print(CCD[3] + ' parent_app ' + CCD[0] + CCD[14] + parent_app + CCD[0])
        print(CCD[4] + ' contents ' + CCD[0] + CCD[15] + contents + CCD[0])

        obj_parent_app = AngularFuseApplication.objects.get(name=parent_app)
        new_app = FuseAppComponent(name=name, type=type, contents=contents, parent_app=obj_parent_app)
        new_app.save()
        response = {'result': 'If you are reading this, that means it worked!!! ', 'new_app': str(new_app)}
        return Response(response)

    def put(self, request, *args, **kwargs):
        name = request.POST['name']
        type = request.POST['type']
        parent_app = request.POST['parent_app']
        contents = request.POST['contents']

        obj_parent_app = AngularFuseApplication.objects.get(name=parent_app)

        modified_component = AngularFuseApplication.objects.get(name=name)
        modified_component.name = name
        modified_component.type = type
        modified_component.contents = contents
        modified_component.parent_app = obj_parent_app

        modified_component.save()
        return Response({'result_PUT': 'If you are reading this, that means it worked!!! '})























class SuperBasicModelView(APIView):
    # serializer_class = SuperBasicModelSerializer
    permission_classes = (AllowAny,)  # IsAuthenticated

    def get(self, request, format=None):
        allmodels = Car.objects.all()
        print(allmodels)
        return Response(allmodels)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        f = open('/usr/src/app/static/uploaded_file', 'w')
        print('preparing to write file to /usr/src/app/static/uploaded_file')
        myfile = File(f)
        # myfile.write(ContentFile(file_obj.read()))
        path = default_storage.save('tmp/THE_FILE', ContentFile(file_obj.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        print('writing completed ! ! !')
        myfile.close()
        print('closing files')
        f.close()
        print('PROCESS COMPLETED!!!')
        response = {'result': 'everything is finished ! ! ! ' + str(tmp_file)}
        return Response(response)


class SampleAPI(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        sample_response = {'data': 'hello world'}
        return Response(sample_response)
