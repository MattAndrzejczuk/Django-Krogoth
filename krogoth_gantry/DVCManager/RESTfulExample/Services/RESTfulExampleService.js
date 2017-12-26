(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            testThisService: testThisService
        };

        function testThisService() {
            $log.log('_DJANGULAR_SERVICE_NAME_ is working properly.');
        }

        return service;
    }
})();