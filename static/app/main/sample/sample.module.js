(function () {
    'use strict';

    angular
        .module('app.sample',
            [
                // 3rd Party Dependencies
                'flow'
            ]
        )
        .config(config);

    /** @ngInject */
    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
        // State
        $stateProvider.state('app.sample', {
            url: '/sample',
            views: {
                'content@app': {
                    templateUrl: '/static/app/main/sample/sample.html',
                    controller: 'SampleController as vm'
                }
            },
            resolve: {
                Documents: function (msApi) {
                    return msApi.resolve('sample.data@get');
                }
            },
            bodyClass: 'file-manager'
        });

        // Translation
        // $translatePartialLoaderProvider.addPart('/static/app/main/apps/lazarus');


        // Api
        msApiProvider.register('sample.data', ['/static/app/main/sample/sample_data.json', {param1: 'sample'}, 'get', true]);


        // Navigation
        // msNavigationServiceProvider.saveItem('apps.sample', {
        //     title: 'Sample',
        //     icon: 'icon-star',
        //     state: 'app.sample',
        //     weight: 5
        // });
    }
})();