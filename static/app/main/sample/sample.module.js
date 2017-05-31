(function ()
{
    'use strict';

    angular
        .module('app.sample', [])
        .config(config);

    /** @ngInject */
    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider)
    {
        // State
        $stateProvider
            .state('app.sample', {
                url    : '/sample',
                views  : {
                    'content@app': {
                        templateUrl: '/static/app/main/sample/sample.html',
                        controller : 'SampleController as vm'
                    }
                }
            });

        // Translation
        $translatePartialLoaderProvider.addPart('/static/app/main/sample');

        // Api
        msApiProvider.register('sample', ['/static/app/data/sample/sample.json']);


        // Navigation
        // msNavigationServiceProvider.saveItem('fuse', {
        //     title : 'SAMPLE',
        //     group : true,
        //     weight: 1
        // });

        msNavigationServiceProvider.saveItem('apps.file-manager', {
            title    : 'Sample',
            icon     : 'icon-tile-four',
            state    : 'app.sample',
            //stateParams: {
            //    'param1': 'page'
            // },
            translate: 'SAMPLE.SAMPLE_NAV',
            weight   : 1
        });
        /*
        */
    }
})();