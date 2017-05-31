(function ()
{
    'use strict';

    angular
        .module('app.lazarus',
            [
                // 3rd Party Dependencies
                'flow'
            ]
        )
        .config(config);

    /** @ngInject */
    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider)
    {
        // State
        $stateProvider.state('app.lazarus', {
            url      : '/lazarus',
            views    : {
                'content@app': {
                    templateUrl: '/static/app/main/apps/lazarus/lazarus.html',
                    controller : 'FileManagerController as vm'
                }
            },
            resolve  : {
                Documents: function (msApi)
                {
                    return msApi.resolve('fileManager.documents@get');
                }
            },
            bodyClass: 'file-manager'
        });

        // Translation
        $translatePartialLoaderProvider.addPart('/static/app/main/apps/lazarus');

        // Api
        msApiProvider.register('fileManager.documents', ['/static/app/data/lazarus/documents.json']);

        // Navigation
        msNavigationServiceProvider.saveItem('apps.lazarus', {
            title : 'Lazarus',
            icon  : 'icon-folder',
            state : 'app.lazarus',
            weight: 5
        });
    }

})();