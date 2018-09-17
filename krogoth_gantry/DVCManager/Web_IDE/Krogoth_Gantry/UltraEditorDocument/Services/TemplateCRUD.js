/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            renameTemplate: renameTemplate,
            createTemplate: createTemplate
        };

        function renameTemplate(path_0, path_1, path_2, old, new_) {
            var payload = {};
            payload.path_0 = path_0;
            payload.path_1 = path_1;
            payload.path_2 = path_2;
            payload.old_name = old;
            payload.new_name = new_;

            const uri = "/krogoth_admin/renameAngularJSTemplate/";
            $log.info(uri);
            $log.info(payload);
            var deferred = $q.defer();
            $http({
                method: 'POST',
                data: payload,
                url: uri
            }).then(function successCallback(response) {
                /// Success
                $log.info(" 💾 Template name has been changed 💾 ");
                $log.log(response.data);
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function createTemplate(payload) {
            var deferred = $q.defer();
            const uri = "/krogoth_admin/createAngularJSTemplate/";
            $log.log("POST --> [" + uri + "]");
            $http({
                method: 'POST',
                data: payload,
                url: uri
            }).then(function successCallback(response) {
                /// Success
                $log.info(" 💾 Template has been created 💾 ");
                $log.log(response.data);
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                $log.log(response);
                deferred.reject(response);
            });
            return deferred.promise;
        }
        return service;
    }
})();