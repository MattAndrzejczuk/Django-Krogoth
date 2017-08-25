/**
 * Created by mattmbp on 8/2/17.
 */
(function() {
    'use strict';
    angular.module('fuse').config(routeConfig);

    function routeConfig($stateProvider, $urlRouterProvider, $locationProvider) {
        $locationProvider.hashPrefix('!');
        $urlRouterProvider.otherwise('/home');
        var $cookies;
        angular.injector(['ngCookies']).invoke(['$cookies', function(_$cookies) {
            $cookies = _$cookies;
        }]);
        var layoutStyle = $cookies.get('layoutStyle') || 'LAYOUT_STYLE';
        ' + '
        var layouts = {
            LAYOUT_STYLE: {
                main: '/dynamic_lazarus_page/NgIncludedHtml/?name=htmlMainLayout',
                toolbar: '/dynamic_lazarus_page/NgIncludedHtml/?name=htmlToolbarLayout',
                navigation: '/dynamic_lazarus_page/NgIncludedHtml/?name=htmlNavLayout'
            },
            contentOnly: {
                main: '/static/app/core/layouts/content-only.html',
                toolbar: '',
                navigation: ''
            },
            contentWithToolbar: {
                main: '/static/app/core/layouts/content-with-toolbar.html',
                toolbar: '/static/app/toolbar/layouts/content-with-toolbar/toolbar.html',
                navigation: ''
            }
        };
        $stateProvider.state('app', {
            abstract: true,
            views: {
                'main@': {
                    templateUrl: layouts[layoutStyle].main,
                    controller: 'MainController as vm'
                },
                'toolbar@app': {
                    templateUrl: layouts[layoutStyle].toolbar,
                    controller: 'ToolbarController as vm'
                },
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
    }
})();