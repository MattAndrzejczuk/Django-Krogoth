(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
        $stateProvider
            .state('app.FUSE_APP_NAME', {
                url: '/FUSE_APP_NAME',
                views: {
                    'main@': {
                        templateUrl: '/static/app/core/layouts/content-only.html',
                        controller: 'MainController as vm'
                    },
                    'content@app.FUSE_APP_NAME': {
                        templateUrl: '/Djangular/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }

                }
            })
        _DJANGULAR_SLAVE_VC_INJECTION_POINT_; /* Djangular Slave VCs automatically injected here. */
        _DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_
        /*
        msNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', { 
        	title: 'FUSE_APP_TITLE', 
        	icon: 'FUSE_APP_ICON', 
        	state: 'app.FUSE_APP_NAME', 
        	weight: 3 
        }); 
        */
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
    }
})();