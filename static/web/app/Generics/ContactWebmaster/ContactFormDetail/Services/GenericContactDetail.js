(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        var service = {
            getById: getById,
            deleteById: deleteById
        };

        function getById(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/generic/contact/detail/'+id+'/'
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }
        
        
        function deleteById(id) {
            var deferred = $q.defer();
            $http({
                method: 'DELETE',
                url: '/generic/contact/detail/'+id+'/'
            }).then(function successCallback(response) {
                /// Success
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