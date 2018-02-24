(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            populateBoilerplate: populateBoilerplate,
            breadCategory : "",
            breadSubCategory : "",
            breadEnd : "",
            makeBread : makeBread
        };

        function populateBoilerplate() {
            var deferred = $q.defer();
            try {
                deferred.resolve(returnData);
            } catch (ex) {
                deferred.reject(returnData);
            }
            return deferred.promise;
        }


        function makeBread() {
            var deferred = $q.defer();
            try {
                deferred.resolve(returnData);
            } catch (ex) {
                deferred.reject(returnData);
            }
            return deferred.promise;
        }



        return service;
    }
})();