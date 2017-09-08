(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log) {
        $log.debug('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        // Save data to sessionStorage
        sessionStorage.setItem('_DJANGULAR_SERVICE_NAME_Example', 'It works!!!');
        $log.debug('_DJANGULAR_SERVICE_NAME_Example Item added to session storage!!');
        // Get saved data from sessionStorage
        var data = sessionStorage.getItem('_DJANGULAR_SERVICE_NAME_Example');
        $log.debug('_DJANGULAR_SERVICE_NAME_ retrieved the value: ' + data);
        // Remove saved data from sessionStorage
        sessionStorage.removeItem('_DJANGULAR_SERVICE_NAME_Example');
        $log.debug('_DJANGULAR_SERVICE_NAME_ DELETED the value: ' + data);
        // Remove all saved data from sessionStorage
        sessionStorage.clear();
        $log.warn('_DJANGULAR_SERVICE_NAME_ HAS WIPED ALL SESSION STORAGE');

        var service = {
            testThisService: testThisService
        };

        function testThisService() {
            $log.log('_DJANGULAR_SERVICE_NAME_ is working properly.');
        }
        return service;
    }
})();