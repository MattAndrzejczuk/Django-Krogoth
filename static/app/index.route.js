(function () {
    'use strict';
    angular.module('fuse').config(routeConfig);
    /** @ngInject */ function routeConfig($stateProvider, $urlRouterProvider, $locationProvider, $httpProvider) {

        $locationProvider.hashPrefix('!');
        $urlRouterProvider.otherwise('/home');

        var $cookies;

        angular.injector(['ngCookies']).invoke(['$cookies', function (_$cookies) {
            $cookies = _$cookies;
        }]);

        var layoutStyle = $cookies.get('layoutStyle') || 'verticalNavigation';
        var layouts = {
            verticalNavigation: {
                main: '/static/app/core/layouts/vertical-navigation.html',
                toolbar: '/dynamic_lazarus_page/DynamicHTMLToolbar/',
                navigation: '/static/app/navigation/layouts/vertical-navigation/navigation.html'
            },
            verticalNavigationFullwidthToolbar: {
                main: '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar.html',
                toolbar: '/static/app/toolbar/layouts/vertical-navigation-fullwidth-toolbar/toolbar.html',
                navigation: '/static/app/navigation/layouts/vertical-navigation/navigation.html'
            },
            verticalNavigationFullwidthToolbar2: {
                main: '/static/app/core/layouts/vertical-navigation-fullwidth-toolbar-2.html',
                toolbar: '/static/app/toolbar/layouts/vertical-navigation-fullwidth-toolbar-2/toolbar.html',
                navigation: '/static/app/navigation/layouts/vertical-navigation-fullwidth-toolbar-2/navigation.html'
            },
            horizontalNavigation: {
                main: '/static/app/core/layouts/horizontal-navigation.html',
                toolbar: '/static/app/toolbar/layouts/horizontal-navigation/toolbar.html',
                navigation: '/static/app/navigation/layouts/horizontal-navigation/navigation.html'
            },
            contentOnly: {main: '/static/app/core/layouts/content-only.html', toolbar: '', navigation: ''},
            contentWithToolbar: {
                main: '/static/app/core/layouts/content-with-toolbar.html',
                toolbar: '/static/app/toolbar/layouts/content-with-toolbar/toolbar.html',
                navigation: ''
            }
        };

        $stateProvider.state('app', {
            abstract: true,
            views: {
                'main@': {templateUrl: layouts[layoutStyle].main, controller: 'MainController as vm'},
                'toolbar@app': {templateUrl: layouts[layoutStyle].toolbar, controller: 'ToolbarController as vm'},
                'navigation@app': {
                    templateUrl: layouts[layoutStyle].navigation,
                    controller: 'NavigationController as vm'
                },
                'quickPanel@app': {
                    templateUrl: '/static/app/quick-panel/quick-panel.html',
                    controller: 'QuickPanelController as vm'
                }
            }
        });

        $httpProvider.interceptors.push(function (userService) {
            return {
                request: function (req) {
                    // Set the `Authorization` header for every outgoing HTTP request
                    req.headers.Authorization = 'Token 72f4186c78ac72fb4d6fe803946d8753b8872715';
                    return req;
                }
            };
        }




        ///*  - - - - - - - - - - - - - - - - - - - - - - - -  *///
    }
})();


