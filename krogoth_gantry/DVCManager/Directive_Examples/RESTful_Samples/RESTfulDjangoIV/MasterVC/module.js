(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider,  msApiProvider, msNavigationServiceProvider) {
        $stateProvider
            .state('app.FUSE_APP_NAME', {
                url: '/FUSE_APP_NAME',
                views: {
                    'content@app': {
                        templateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }
                }
            });

        /* krogoth_gantry Slave VCs automatically injected here. */
        _DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_ /*OverrideNavStart*/
        msNavigationServiceProvider.saveItem('AK_NAVCAT_KROGOTH.AK_SUBCATAGORY_KROGOTH.FUSE_APP_NAME', {
            title: 'FUSE_APP_TITLE',
            icon: 'FUSE_APP_ICON',
            state: 'app.FUSE_APP_NAME',
            weight: 4
        }); /*OverrideNavEnd*/
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
    }
})();