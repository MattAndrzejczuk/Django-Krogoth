(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {

        var service = {
            getList: getList,
            postNewObject: postNewObject,
            deleteObject: deleteObject,
            getForeignKeys: getForeignKeys
        };


        function getForeignKeys() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/api/__ExamplesManufacturer/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getList() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/api/__ExamplesCar/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function postNewObject(objectJson) {
            var deferred = $q.defer();
            $http({
                method: 'POST',
                data: objectJson,
                url: '/api/__ExamplesCar/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function deleteObject(objectId) {
            var deferred = $q.defer();
            $http({
                method: 'DELETE',
                url: '/api/__ExamplesCar/' + objectId + ''
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }



        return service;
    }
})();