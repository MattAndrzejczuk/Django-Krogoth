/*
GET     http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/core.module.js
*/
(function () {
    'use strict';

    angular
        .module('app.core',
            [
                'ngAnimate',
                'ngAria',
                'ngWebsocket',
                'ngCookies',
                'ngMessages',
                'ngResource',
                'ngSanitize',
                'ngMaterial',
                //'pascalprecht.translate',
                'ui.router',
                //'ngFileUpload',
                'ui.codemirror',
                'oc.lazyLoad',
                'ui.tree',
                //'djangoRESTResources',
                //'formly'
            ]);
})();