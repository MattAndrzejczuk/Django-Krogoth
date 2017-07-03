(function () {
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
    function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
        // State
        $stateProvider.state('app.lazarus', {
            url: '/lazarus',
            views: {
                'content@app': {
                    templateUrl: '/static/app/main/apps/lazarus/lazarus.html',
                    controller: 'LazarusController as vm'
                }
            },
            resolve: {
                Documents: function (msApi) {
                    return msApi.resolve('lazarus.units@get');
                }
            },
            bodyClass: 'file-manager'
        });

        // Translation
        $translatePartialLoaderProvider.addPart('/static/app/main/apps/lazarus');

        var full_url = window.location.href;
        var url_arrayed_single = full_url.split("=");

        
        // Api
        if (url_arrayed_single[1]) {
            msApiProvider.register('lazarus.units', ['/LazarusII/LazarusListUnits/', {mod_name: url_arrayed_single[1]}, 'get', true]);
        } else {
            msApiProvider.register('lazarus.units', ['/LazarusII/LazarusListUnits/', {mod_name: 'totala_files2'}, 'get', true]);
        }


        // Navigation
        msNavigationServiceProvider.saveItem('apps.lazarus', {
            title: 'Lazarus',
            icon: 'icon-folder',
            state: 'app.lazarus',
            weight: 5
        });

    }

})();