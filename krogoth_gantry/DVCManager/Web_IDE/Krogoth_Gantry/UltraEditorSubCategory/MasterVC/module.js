(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider,  msApiProvider, msNavigationServiceProvider) {
        $stateProvider
            .state('app.FUSE_APP_NAME', {
                url: '/FUSE_APP_NAME/:categoryId',
                views: {
                    'main@': {
                        templateUrl: '/moho_extractor/NgIncludedHtml/?name=content-only.html',
                        controller: 'MainController as vm'
                    },
                    'content@app.FUSE_APP_NAME': {
                        templateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }

                }
            })
            .state('app.FUSE_APP_NAME.slave', {
                url: '/slave/:categoryId/:childId',
                views: {
                    'main@': {
                        templateUrl: '/moho_extractor/NgIncludedHtml/?name=content-only.html',
                        controller: 'MainController as vm'
                    },
                    'content@app.FUSE_APP_NAME.slave': {
                        templateUrl: '/krogoth_gantry/DynamicHTMLSlaveInjector/?name=FUSE_APP_SLAVE_NAME',
                        controller: 'FUSE_APP_SLAVE_NAMEController as vm'
                    }

                }
            });

        /*
                msNavigationServiceProvider.saveItem('AK_NAVCAT_KROGOTH.AK_SUBCATAGORY_KROGOTH.FUSE_APP_NAME', {
                    title: 'FUSE_APP_TITLE',
                    icon: 'FUSE_APP_ICON',
                    state: 'app.FUSE_APP_NAME',
                    weight: 10
                });
        */
    }
})();