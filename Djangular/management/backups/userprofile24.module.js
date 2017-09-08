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
                },
                resolve: {
                    Timeline: function(msApi) {
                        return msApi.resolve('profile.timeline@get');
                    },
                    About: function(msApi) {
                        return msApi.resolve('profile.about@get');
                    },
                    PhotosVideos: function(msApi) {
                        return msApi.resolve('profile.photosVideos@get');
                    }
                },
                bodyClass: 'profile'
            })
        _DJANGULAR_SLAVE_VC_INJECTION_POINT_; /* Djangular Slave VCs automatically injected here. */
        msApiProvider.register('profile.timeline', ['/static/app/data/profile/timeline.json']);
        msApiProvider.register('profile.about', ['/static/app/data/profile/about.json']);
        msApiProvider.register('profile.photosVideos', ['/static/app/data/profile/photos-videos.json']);
        _DJANGULAR_SLAVE_MSAPI_INJECTION_POINT_
        //        msNavigationServiceProvider.saveItem('NAV_HEADER.FUSE_APP_NAME', {
        //            title: 'FUSE_APP_TITLE',
        //            icon: 'FUSE_APP_ICON',
        //            state: 'app.FUSE_APP_NAME',
        //            weight: 3
        //        });
        _DJANGULAR_SLAVE_NAV_SERVICE_INJECTIONS_
    }
})();