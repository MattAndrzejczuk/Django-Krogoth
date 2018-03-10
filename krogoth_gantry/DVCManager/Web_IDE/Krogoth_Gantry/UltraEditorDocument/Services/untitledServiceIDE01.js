(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {

        var service = {
            renameService: renameService
        };

        function renameService(newName, uri) {
            var payload = {};
            payload.name = newName;
            var deferred = $q.defer();
            $http({
                method: 'PATCH',
                data: payload,
                url: uri
            }).then(function successCallback(response) {
                /// Success
                $log.info(" 💾 Service name has been changed 💾 ");
                $log.log(response.data);
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        return service;
    }
})();