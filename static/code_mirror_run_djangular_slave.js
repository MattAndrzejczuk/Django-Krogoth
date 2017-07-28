window.onload = function () {

    console.log('CODEMIRROR INITIALIZING... ');

    var txt_js_controller = document.getElementById('id_controller_js');
    var txt_html_main = document.getElementById('id_view_html');


    var editor2 = CodeMirror.fromTextArea(txt_js_controller, {
        lineNumbers: true,
        mode: "javascript",
        theme: "colorforth",
        indentUnit: 4,
        indentWithTabs: true
    });


    var editor3 = CodeMirror.fromTextArea(txt_html_main, {
        lineNumbers: true,
        mode: "htmlmixed",
        theme: "dracula",
        indentUnit: 4,
        indentWithTabs: true
    });


    // iPad
    if (window.innerWidth <= 1124) {
        editor2.setSize('640px', '480px');
        editor3.setSize('640px', '480px');
    } else {
        editor2.setSize('1000px', '1400px');
        editor3.setSize('1000px', '1400px');
    }

};


(function () {
    'use strict';
    angular.module('fuse').config(routeConfig);
    function routeConfig($stateProvider, $urlRouterProvider, $locationProvider) {
        $locationProvider.hashPrefix('!');
        $urlRouterProvider.otherwise('/home');
        var $cookies;
        angular.injector(['ngCookies']).invoke(['$cookies', function (_$cookies) {
            $cookies = _$cookies;
        }]);
        var layoutStyle = $cookies.get('layoutStyle') || 'LAYOUT_STYLE';
        ' + '
        var layouts = {
                LAYOUT_STYLE: {
                    main: /static/
                    app / core / layouts / vertical - navigation - fullwidth - toolbar - 2.
                html,
                toolbar: /static/
                app / toolbar / layouts / vertical - navigation - fullwidth - toolbar - 2 / toolbar.html, navigation
    :
        /static/
        app / navigation / layouts / vertical - navigation - fullwidth - toolbar - 2 / navigation.html
    },
        contentOnly: {
            main: '/static/app/core/layouts/content-only.html', toolbar
        :
            '', navigation
        :
            ''
        }
    ,
        contentWithToolbar: {
            main: '/static/app/core/layouts/content-with-toolbar.html', toolbar
        :
            '/static/app/toolbar/layouts/content-with-toolbar/toolbar.html', navigation
        :
            ''
        }
    }
        ;
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
    }
})();