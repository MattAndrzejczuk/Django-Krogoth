(function ()
{
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
        $stateProvider.state('app.FUSE_APP_NAME', {
            url: '/FUSE_APP_NAME',
            views: {
                'content@app': {
                    templateUrl: '/dynamic_lazarus_page/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                    controller: 'FUSE_APP_NAMEController as vm'
                }
            },
            bodyClass: 'file-manager'
        });
        msNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', {
            title: 'FUSE_APP_TITLE',
            icon: 'icon-newspaper',
            state: 'app.FUSE_APP_NAME',
            weight: 3
        });
    }
})();
