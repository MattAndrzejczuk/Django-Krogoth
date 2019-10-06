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


        msNavigationServiceProvider.saveItem('FUSE_APP_NAME', {
            title: 'Home',
            icon: 'entypo entypo-home',
            state: 'app.FUSE_APP_NAME',
            weight: 0
        });


    }
})();