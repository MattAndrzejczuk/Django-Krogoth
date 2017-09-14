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



        msNavigationServiceProvider.saveItem('Home', {
            title: 'Home',
            icon: 'mdi mdi-bell',
            weight: 1
        });
        msNavigationServiceProvider.saveItem('Home.FUSE_APP_NAME', {
            title: 'FUSE_APP_TITLE',
            icon: 'icon-newspaper',
            state: 'app.FUSE_APP_NAME',
            weight: 1
        });
        msNavigationServiceProvider.saveItem('Home.upcomingFeats', {
            title: 'Upcoming Features',
            icon: 'mdi mdi-star-circle',
            weight: 2
        });
        msNavigationServiceProvider.saveItem('Home.whatIsLazarus', {
            title: 'What Is Lazarus',
            icon: 'mdi mdi-information-variant',
            weight: 3
        });
        /*
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
		*/
    }
})();