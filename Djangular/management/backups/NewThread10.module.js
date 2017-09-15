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

        /// Does Djangular work??

        msNavigationServiceProvider.saveItem('Forums', {
            title: 'Forums',
            icon: 'icon-bulletin-board',
            weight: 5
        });

        msNavigationServiceProvider.saveItem('Forums.FUSE_APP_NAME', {
            title: 'General Discussion',
            icon: 'icon-numeric-1-box-outline',
            state: 'app.FUSE_APP_NAME',
            weight: 1
        });
        /*
                _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
        */
    }
})();