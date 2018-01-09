(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider, $ocLazyLoadProvider) {



        //Config For ocLazyLoading
        $ocLazyLoadProvider.config({
            'debug': true, // For debugging 'true/false'
            'events': true, // For Event 'true/false'
            'modules': [{ // Set modules initially
                name: 'lazyMVC', // State1 module
                files: ['/krogoth_gantry/DynamicJavaScriptInjector/?name=FUSE_APP_NAME&ov=file.js']
            },
                {
                    name: 'test', // State1 module
                    files: ['/krogoth_gantry/DynamicJavaScriptInjector/?name=lazyMVC&ov=file.js']
                }]
        });


        $stateProvider
            .state('app.FUSE_APP_NAME', {
                url: '/FUSE_APP_NAME/',
                views: {
                    'content@app': {
                        templateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }
                },
                resolve: { // Any property in resolve should return a promise and is executed before the view is loaded
                    loadMyCtrl: ['$ocLazyLoad', function ($ocLazyLoad) {
                        // you can lazy load files for an existing module
                        return $ocLazyLoad.load('lazyMVC');
                    }]
                }
            })
            .state('app.FUSE_APP_NAME.slave', {
                url: '/FUSE_APP_NAME/:sampleObject',
                views: {
                    'content@app': {
                        templateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }
                },
                resolve: { // Any property in resolve should return a promise and is executed before the view is loaded
                    loadMyCtrl: ['$ocLazyLoad', function ($ocLazyLoad) {
                        // you can lazy load files for an existing module
                        return $ocLazyLoad.load('lazyMVC');
                    }]
                }
            })
        _DJANGULAR_SLAVE_VC_INJECTION_POINT_;
        /* krogoth_gantry Slave VCs automatically injected here. */
        _DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_
        msNavigationServiceProvider.saveItem('AK_NAVCAT_KROGOTH.Pages.FUSE_APP_NAME', {
            title: 'FUSE_APP_TITLE',
            icon: 'FUSE_APP_ICON',
            state: 'app.FUSE_APP_NAME',
            weight: 3
        });
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
    }
})();