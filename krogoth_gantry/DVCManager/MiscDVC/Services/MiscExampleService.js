(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        // $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        // var service = {
        //     testThisService: testThisService
        // };
        // function testThisService() {
        //     $log.log('_DJANGULAR_SERVICE_NAME_ is working properly.');
        // }
        // return service;

        var service = {
            postNewReply: postNewReply,
            postNewThread: postNewThread,
            getDetailThread: getDetailThread,
            getDetailCategory: getDetailCategory,
            getListCategories: getListCategories
        };


        const requestURI = '/api/__ExamplesFruit/';

        function getList() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: requestURI
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getDetail(objectId) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: requestURI + id + '/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function post(objectJson) {
            $log.log('creating new thread...');
            $log.log(thread);
            var deferred = $q.defer();
            $http({
                method: 'POST',
                data: thread,
                url: requestURI
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function put(objectJson) {
            $log.log('creating new reply...');
            $log.log(reply);
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                data: reply,
                url: requestURI,
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function patch(objectJson) {
            $log.log('creating new reply...');
            $log.log(reply);
            var deferred = $q.defer();
            $http({
                method: 'PATCH',
                data: reply,
                url: requestURI,
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function deleteObject(objectJson) {
            $log.log('creating new reply...');
            $log.log(reply);
            var deferred = $q.defer();
            $http({
                method: 'DELETE',
                data: reply,
                url: requestURI,
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function options() {
            var deferred = $q.defer();
            $http({
                method: 'OPTIONS',
                url: requestURI
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        return service;
        /////
    }
})();