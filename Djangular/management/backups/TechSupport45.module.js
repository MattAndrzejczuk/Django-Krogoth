(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
        $stateProvider
            .state('app.FUSE_APP_NAME', {
                url: '/FUSE_APP_NAME',
                views: {
                    'content@app': {
                        templateUrl: '/Djangular/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }
                }
            })
        _DJANGULAR_SLAVE_VC_INJECTION_POINT_; /* Djangular Slave VCs automatically injected here. */
        _DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_
        msNavigationServiceProvider.saveItem('TechSupport', {
            title: 'Support',
            icon: 'mdi mdi-medical-bag',
            weight: 9
        });
        msNavigationServiceProvider.saveItem('TechSupport.FUSE_APP_NAME', {
            title: 'Total Annihilation',
            icon: 'icon-ta-core',
            state: 'app.FUSE_APP_NAME',
            weight: 9
        });
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
    }
})();