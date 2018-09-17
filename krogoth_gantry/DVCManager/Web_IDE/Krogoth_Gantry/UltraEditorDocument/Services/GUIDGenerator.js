/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        var service = {
            makeGUID: makeGUID
        };

        function makeGUID() {
            var deferred = $q.defer();

            function s4() {
                return Math.floor((1 + Math.random()) * 0x10000)
                    .toString(16).toUpperCase()
                    .substring(1);
            }
            deferred.resolve(s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4());
            return deferred.promise;
        }
        return service;
    }
})();