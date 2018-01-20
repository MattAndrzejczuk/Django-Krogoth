(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            getMastersSlaveBrowser: getMastersSlaveBrowser,
            getCategoriesSlaveBrowser: getCategoriesSlaveBrowser,
            putCatagorySlaveBrowser: putCatagorySlaveBrowser
        };

        function getMastersSlaveBrowser(catId) {
            const uri = "/krogoth_gantry/viewsets/MasterViewController/?category=" + catId;
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: uri
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data.results);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getCategoriesSlaveBrowser() {
            const uri = '/krogoth_gantry/viewsets/Category/';
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: uri
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data.results);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function putCatagorySlaveBrowser(instance) {
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                data: instance,
                url: '/krogoth_gantry/viewsets/Category/' + instance.id + '/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data.results);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        return service;
    }
})();