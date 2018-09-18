(function () {
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
            })
        _DJANGULAR_SLAVE_VC_INJECTION_POINT_;
        /* krogoth_gantry Slave VCs automatically injected here. */
        _DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_
        msNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', {
            title: 'FUSE_APP_TITLE',
            icon: 'FUSE_APP_ICON',
            state: 'app.FUSE_APP_NAME',
            weight: 4
        });
        /* _DJANGULAR_ SLAVE_NAV_ SERVICE_INJECTIONS_ */
    }
})();




/*


 *
 *   COMPILED MODULE
 *


(function () {
    'use strict';
    angular.module('app.General', ['flow']).config(config);

    function config($stateProvider,  msApiProvider, msNavigationServiceProvider) {
        $stateProvider.state('app.General', {
            url: '/General',
            views: {
                'content@app': {
                    templateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=General',
                    controller: 'GeneralController as vm'
                }
            }
        }).state('app.General.Thread', {
            url: '/Thread/:id',
            views: {
                'content@app': {
                    templateUrl: '/krogoth_gantry/DynamicHTMLSlaveInjector/1/',
                    controller: 'ThreadController as vm'
                }
            },
            resolve: {
                ModelThread: function (msApi) {
                    return msApi.resolve('app.General.GeneralREST@get');
                }
            }
        });
        msApiProvider.register('app.General.GeneralREST', ['/krogoth_gantry/CRUD/SampleModelOneView/:id']);
        msNavigationServiceProvider.saveItem('Administration.General', {
            title: 'Forums',
            icon: '',
            state: 'app.General',
            weight: 4
        });
    }
})();
*/
