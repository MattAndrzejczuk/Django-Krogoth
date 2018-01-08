/* jshint -W117, -W030 */
// factory
(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {

        /* jshint validthis: true */
        var service = {
            getList: getList,
            postNewObject: postNewObject,
            deleteObject: deleteObject,
            getManyToManyKeys: getManyToManyKeys,
            putEditedObject: putEditedObject
        };


        function getListFilteredByBreed() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/api/breeds/list',
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getListAllDogs() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/api/breeds/list/all',
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
                url: '/api/__ExamplesBasicImageUpload/',
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function putEditedObject(objectJson, objId) {
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                data: objectJson,
                url: '/api/__ExamplesBasicImageUpload/' + objId + '/',
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
                url: '/api/__ExamplesBasicImageUpload/' + objectId + '',
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