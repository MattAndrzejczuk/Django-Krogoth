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



        msNavigationServiceProvider.saveItem('Home', {
            title: 'Home',
            icon: 'mdi mdi-home',
            weight: 1
        });
        msNavigationServiceProvider.saveItem('Home.FUSE_APP_NAME', {
            title: 'FUSE_APP_TITLE',
            icon: 'icon-newspaper',
            state: 'app.FUSE_APP_NAME',
            weight: 1
        });
        msNavigationServiceProvider.saveItem('Home.upcomingFeats', {
            title: 'Future Plans',
            icon: 'mdi mdi-star-circle',
            state: 'app.upcomingFeatures',
            weight: 6
        });
        msNavigationServiceProvider.saveItem('Home.whatIsLazarus', {
            title: 'What Is Lazarus',
            icon: 'mdi mdi-information-variant',
            state: 'app.whatIsLaz',
            weight: 3
        });
        /*
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
		*/
    }
})();