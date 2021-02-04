/*
GET   http://localhost:8000/global_static_text/load_static_text_readonly/core.module.es6
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