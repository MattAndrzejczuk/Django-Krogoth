(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            getAllUnits: getAllUnits
        };

        function getAllUnits() {
            var deferred = $q.defer();
            $log.log('getAllUnits() called ! ! ! !');
            $http({
                method: 'GET',
                url: '/LazarusDatabase/UnitFBIFromSQLView/'
            }).then(function successCallback(response) {
                $log.log('RESTful GET Unit FBIs ');
                $log.log(response.data);
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        return service;
    }
})();