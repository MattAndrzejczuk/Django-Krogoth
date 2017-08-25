(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            postNewReply: postNewReply,
            postNewThread: postNewThread,
            getDetailThread: getDetailThread,
            getDetailCategory: getDetailCategory,
            getListCategories: getListCategories
        };

        function getListCategories() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/Forum/ForumCategoryListView/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getDetailCategory(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/Forum/ForumCategoryDetailView/?cat_id=' + id
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getDetailThread(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/Forum/ForumPostDetailView/?post_id=' + id
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function postNewThread(thread) {
            $log.log('creating new thread...');
            $log.log(thread);
            var deferred = $q.defer();
            $http({
                method: 'POST',
                data: thread,
                url: '/Forum/ForumPostDetailView/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function postNewReply(reply) {
            $log.log('creating new reply...');
            $log.log(reply);
            var deferred = $q.defer();
            $http({
                method: 'POST',
                data: reply,
                url: '/Forum/ForumReplySubmitView/',
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

        return service;
    }
})();


//  API Endpoints:
///     /Forum/ForumCategoryListView [GET]
///     /Forum/ForumCategoryDetailView [GET]
///     /Forum/ForumPostDetailView [GET, POST] 
///     /Forum/ForumReplySubmitView [POST]