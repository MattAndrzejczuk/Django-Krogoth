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
            putCatagorySlaveBrowser: putCatagorySlaveBrowser,
            getIconUsingId: getIconUsingId
        };

        function getIconUsingId(icoId) {
            /// "/krogoth_gantry/viewsets/Icon/586/"
            const uri = "/krogoth_gantry/viewsets/Icon/" + icoId + "/";
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: uri
            }).then(function successCallback(response) {

                /// Establish valid icon CSS classes				
                var isValid = false;
                const valids = ["fa ", "fas ", "far ", "fab ", "fal ", "mdi ", "entypo-"];

                /// Check if this icon is not invalid
                for (var i = 0; i < valids.length; i++) {
                    if (response.data.code.indexOf(valids[i]) >= 0) {
                        isValid = true;
                    }
                }

                /// Return a valid icon, or else try fixing it
                if (isValid === true) {
                    deferred.resolve(response.data.code);
                } else {
                    $log.error("Invalid icon code: ");
                    $log.debug(response.data);
                    deferred.resolve("mdi mdi-" + response.data.code);
                }

            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }




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