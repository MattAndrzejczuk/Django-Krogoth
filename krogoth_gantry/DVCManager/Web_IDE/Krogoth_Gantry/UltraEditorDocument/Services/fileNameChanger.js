/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {

        var service = {
            renameService: renameService,
            createService: createService
        };

        function renameService(path_0, path_1, path_2, old, new_) {
            var payload = {};
            payload.path_0 = path_0;
            payload.path_1 = path_1;
            payload.path_2 = path_2;
            payload.old_name = old;
            payload.new_name = new_;
            const uri = "/krogoth_admin/renameAngularJSService/";
            $log.info(uri);
            var deferred = $q.defer();
            $http({
                method: 'POST',
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




        function createService(payload) {

            var deferred = $q.defer();
            const uri = "/krogoth_admin/createAngularJSService/";

            $http({
                method: 'POST',
                data: payload,
                url: uri
            }).then(function successCallback(response) {
                /// Success
                $log.info(" 💾 Service has been created 💾 ");
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