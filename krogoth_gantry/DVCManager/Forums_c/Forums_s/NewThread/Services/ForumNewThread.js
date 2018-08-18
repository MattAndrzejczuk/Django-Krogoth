(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q, $cookies) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        var service = {
            submitNewThread: submitNewThread
        };

        function submitNewThread(category, title, text) {

            /*
            {
            	"title": "",
            	"parent": null,
            	"author": null,
            	"category": null,
            	"date_modified": null,
            	"content": ""
            }
            */

            if (title !== "REPLY") {
                const payload = {
                    "category": category,
                    "title": title,
                    "content": text,
                    "author": $cookies.get("user_id")
                };

                var deferred = $q.defer();
                $http({
                    method: 'POST',
                    data: payload,
                    url: '/krogoth_social/api/AKThreadSocialMedia/'
                }).then(function successCallback(response) {
                    /// Success
                    deferred.resolve(response.data);
                }, function errorCallback(response) {
                    /// Fail
                    deferred.reject(response);
                });
            }

            return deferred.promise;
        }

        return service;
    }
})();