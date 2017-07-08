from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView

from dynamic_lazarus_page.models import SuperBasicModel, Car, FuseAppComponent, AngularFuseApplication
from dynamic_lazarus_page.serializers import SuperBasicModelSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from django.conf import settings

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



class CustomHtmlGenerator(APIView):
    def get(self, request, format=None):
        # msg = str(request.GET['msg'])
        html = '<div> <h1>Some Basic HTML</h1> <p>This is everything.</p> </div>'
        return HttpResponse(html)


class DynamicIndexModule(APIView):
    def get(self, request, format=None):
        index_module_pt1 = "(function (){'use strict';angular.module('fuse', ['uiGmapgoogle-maps','textAngular'," + \
                           "'xeditable','app.core','app.sample','app.navigation','app.toolbar','app.quick-panel',"
        index_module_pt2 = "'app.dashboards','app.calendar','app.e-commerce','app.mail','app.chat','app.file-manager'," + \
                           "'app.gantt-chart','app.scrumboard','app.todo','app.contacts','app.notes','app.toastCtrl',"
        my_apps = "'app.lazarus','app.sample',"

        # inject dynamic apps
        all_applications = AngularFuseApplication.objects.all()
        for application in all_applications:
            my_apps += ("'app." + application.name + "',")

        my_apps += "'ui.tree',"

        index_module_pt3 = "'app.pages','app.ui','app.components']);})();"
        indexModuleJs = index_module_pt1 + index_module_pt2 + my_apps + index_module_pt3
        return HttpResponse(indexModuleJs)



class DynamicIndexRoute(APIView):
    def get(self, request, format=None):
        full_js = "(function (){    'use strict';    angular        .module('fuse')        .config(routeConfig);    /** @ngInject */    function routeConfig($stateProvider, $urlRouterProvider, $locationProvider)    {        $locationProvider.hashPrefix('!');        $urlRouterProvider.otherwise('/FUSE_DEFAULT_APP');        var $cookies;        angular.injector(['ngCookies']).invoke([            '$cookies', function (_$cookies)            {                $cookies = _$cookies;            }        ]);        var layoutStyle = $cookies.get('layoutStyle') || 'verticalNavigation';        var layouts = {            verticalNavigation  : {                main      : '/static/app/core/layouts/vertical-navigation.html',                toolbar   : 'FUSE_TOOLBAR_HTML',                navigation: '/static/app/navigation/layouts/vertical-navigation/navigation.html'            },            verticalNavigationFullwidthToolbar  : {                main      : '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar.html',                toolbar   : '/static/app/toolbar/layouts/vertical-navigation-fullwidth-toolbar/toolbar.html',                navigation: '/static/app/navigation/layouts/vertical-navigation/navigation.html'            },            verticalNavigationFullwidthToolbar2  : {                main      : '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar-2.html',                toolbar   : '/static/app/toolbar/layouts/vertical-navigation-fullwidth-toolbar-2/toolbar.html',                navigation: '/static/app/navigation/layouts/vertical-navigation-fullwidth-toolbar-2/navigation.html'            },            horizontalNavigation: {                main      : '/static/app/core/layouts/horizontal-navigation.html',                toolbar   : '/static/app/toolbar/layouts/horizontal-navigation/toolbar.html',                navigation: '/static/app/navigation/layouts/horizontal-navigation/navigation.html'            },            contentOnly         : {                main      : '/static/app/core/layouts/content-only.html',                toolbar   : '',                navigation: ''            },            contentWithToolbar  : {                main      : '/static/app/core/layouts/content-with-toolbar.html',                toolbar   : '/static/app/toolbar/layouts/content-with-toolbar/toolbar.html',                navigation: ''            }        };        $stateProvider            .state('app', {                abstract: true,                views   : {                    'main@'         : {                        templateUrl: layouts[layoutStyle].main,                        controller : 'MainController as vm'                    },                    'toolbar@app'   : {                        templateUrl: layouts[layoutStyle].toolbar,                        controller : 'ToolbarController as vm'                    },                    'navigation@app': {                        templateUrl: layouts[layoutStyle].navigation,                        controller : 'NavigationController as vm'                    },                    'quickPanel@app': {                        templateUrl: '/static/app/quick-panel/quick-panel.html',                        controller : 'QuickPanelController as vm'                    }                }            });    }})();"

        default_url = 'News' # FUSE_DEFAULT_APP
        toolbar_html = '/dynamic_lazarus_page/DynamicHTMLToolbar/' # FUSE_TOOLBAR_HTML

        parsed_js_1 = full_js.replace('FUSE_DEFAULT_APP', default_url)
        parsed_js_2 = parsed_js_1.replace('FUSE_TOOLBAR_HTML', toolbar_html)
        return HttpResponse(parsed_js_2)


class DynamicHTMLToolbar(APIView):
    def get(self, request, format=None):
        full_html = '<div layout="row" layout-align="start center">    <div layout="row" layout-align="start center" flex>        <md-button id="navigation-toggle" class="md-icon-button" ng-click="vm.toggleSidenav(\'navigation\')"                   hide-gt-sm aria-label="Toggle navigation" translate                   translate-attr-aria-label="TOOLBAR.TOGGLE_NAVIGATION">            <md-icon md-font-icon="icon-menu" class="icon"></md-icon>        </md-button>        <ms-shortcuts></ms-shortcuts>        <div class="toolbar-separator"></div>    </div>    <div layout="row" layout-align="start center">                <md-progress-circular id="toolbar-progress" ng-disabled="!$root.loadingProgress"  class="md-accent" md-diameter="32">        </md-progress-circular>                <div class="toolbar-separator"></div>        <md-menu-bar id="user-menu">            <md-menu md-position-mode="left bottom">                <md-button class="user-button" ng-click="$mdOpenMenu()"                           aria-label="User settings"                           translate translate-attr-aria-label="TOOLBAR.USER_SETTINGS">                    <div layout="row" layout-align="space-between center">                        <div class="avatar-wrapper">                            <img md-menu-align-target class="avatar" src="/static/assets/images/avatars/profile.jpg">                            <md-icon md-font-icon ng-class="vm.userStatus.icon"                                     ng-style="{\'color\': vm.userStatus.color }"                                     class="icon status s16">                            </md-icon>                        </div>                        <span class="username" hide show-gt-sm>DJANGULAR_USERNAME</span>                        <md-icon md-font-icon="icon-chevron-down"                                 class="icon s16" hide-xs></md-icon>                    </div>                </md-button>                <md-menu-content width="3">                    <md-menu-item class="md-indent" ui-sref="app.pages_profile">                        <md-icon md-font-icon="icon-account" class="icon"></md-icon>                        <md-button>My Profile</md-button>                    </md-menu-item><!--                    <md-menu-item class="md-indent" ui-sref="app.mail">                        <md-icon md-font-icon="icon-email" class="icon"></md-icon>                        <md-button>Inbox</md-button>                    </md-menu-item>                    <md-menu-item class="md-indent">                        <md-icon md-font-icon ng-class="vm.userStatus.icon"                                 ng-style="{\'color\': vm.userStatus.color }" class="icon"></md-icon>                        <md-menu id="user-status-menu">                            <md-button ng-click="$mdOpenMenu()" class="status" ng-class="vm.userStatus.class">                                {{vm.userStatus.title}}                            </md-button>                            <md-menu-content width="2">                                <md-menu-item class="status md-indent"                                              ng-class="{\'selected\': status === vm.userStatus}"                                              ng-repeat="status in vm.userStatusOptions">                                    <md-icon md-font-icon="{{status.icon}}" ng-style="{\'color\': status.color }"                                             class="icon"></md-icon>                                    <md-button ng-click="vm.setUserStatus(status)">                                        {{status.title}}                                    </md-button>                                </md-menu-item>                            </md-menu-content>                        </md-menu>                    </md-menu-item>-->                    <md-menu-divider></md-menu-divider>                    <md-menu-item class="md-indent">                        <md-icon md-font-icon="icon-logout" class="icon"></md-icon>                        <md-button ng-click="vm.logout()">Logout</md-button>                    </md-menu-item>                </md-menu-content>            </md-menu>        </md-menu-bar>                <div class="toolbar-separator"></div>        <!--        <ms-search-bar on-search="vm.search(query)" on-result-click="vm.searchResultClick(item)" debounce="300"></ms-search-bar>        <div class="toolbar-separator"></div>        <md-menu id="language-menu" md-offset="0 72" md-position-mode="target-right target">            <md-button class="language-button" ng-click="$mdOpenMenu()"                       aria-label="Language" md-menu-origin md-menu-align-target>                <div layout="row" layout-align="center center">                    <img class="flag" ng-src="/static/assets/images/flags/{{vm.selectedLanguage.flag}}.png">                    <span class="iso">{{vm.selectedLanguage.code}}</span>                </div>            </md-button>            <md-menu-content width="3" id="language-menu-content">                <md-menu-item ng-repeat="(iso, lang) in vm.languages">                    <md-button ng-click="vm.changeLanguage(lang)" aria-label="{{lang.title}}" translate                               translate-attr-aria-label="{{lang.title}}">                        <span layout="row" layout-align="start center">                            <img class="flag" ng-src="/static/assets/images/flags/{{lang.flag}}.png">                            <span translate="{{lang.translation}}">{{lang.title}}</span>                        </span>                    </md-button>                </md-menu-item>            </md-menu-content>        </md-menu>        <div class="toolbar-separator"></div>        <md-button id="quick-panel-toggle" class="md-icon-button" ng-click="vm.toggleSidenav(\'quick-panel\')"                   aria-label="Toggle quick panel" translate translate-attr-aria-label="TOOLBAR.TOGGLE_QUICK_PANEL">            <md-icon md-font-icon="icon-format-list-bulleted" class="icon"></md-icon>        </md-button>        -->    </div></div>'
        username = request.user.username # DJANGULAR_USERNAME
        final_html = full_html.replace('DJANGULAR_USERNAME', username)
        return HttpResponse(final_html)



class DynamicJavaScriptInjector(APIView):
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
    def get(self, request, format=None):
        name = request.GET['name']
        application = AngularFuseApplication.objects.get(name=name)
        components = FuseAppComponent.objects.filter(parent_app=application)
        raw_html_response = ''
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
    permission_classes = (AllowAny,)  # IsAuthenticated

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
    def get(self, request, format=None):
        sample_response = {'data': 'hello world'}
        return Response(sample_response)
