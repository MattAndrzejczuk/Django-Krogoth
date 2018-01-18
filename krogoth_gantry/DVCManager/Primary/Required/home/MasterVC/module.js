(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
        $stateProvider
            .state('app.FUSE_APP_NAME', {
                url: '/FUSE_APP_NAME',
                views: {
                    'content@app': {
                        templateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }
                }
            })
        _DJANGULAR_SLAVE_VC_INJECTION_POINT_; /* krogoth_gantry Slave VCs automatically injected here. */
        _DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_


        _KROGOTH_CATEGORIES_

        msNavigationServiceProvider.saveItem('Lazarus', {
            title: 'Lazarus',
            icon: 'mdi mdi-react',
            /*state: 'app.FUSE_APP_NAME',*/
            weight: 3
        });
        msNavigationServiceProvider.saveItem('AK_NAVCAT_KROGOTH.AK_SUBCATAGORY_KROGOTH.FUSE_APP_NAME', {
            title: 'Mod Editor',
            icon: 'mdi mdi-dna',
            state: 'app.FUSE_APP_NAME',
            weight: 2
        });
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
    }
})();