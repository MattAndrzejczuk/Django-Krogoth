(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            getDjangularMasterViewControllers: getDjangularMasterViewControllers,
            getDjangularMasterViewControllerDetail: getDjangularMasterViewControllerDetail,
            putDjangularMasterViewController: putDjangularMasterViewController,

            getDjangularSlaveViewControllers: getDjangularSlaveViewControllers,
            getDjangularSlaveViewControllerDetail: getDjangularSlaveViewControllerDetail,
            putDjangularSlaveViewController: putDjangularSlaveViewController,

            djangoManagePyCollectStatic: djangoManagePyCollectStatic
        };

        function getDjangularMasterViewControllers() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/MasterViewControllerEditorList/'
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getDjangularMasterViewControllerDetail(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/MasterViewControllerEditorDetail/?id=' + id
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function putDjangularMasterViewController(id, content) {
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                data: content,
                url: '/krogoth_gantry/MasterViewControllerEditorDetail/?id=' + id
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getDjangularSlaveViewControllers(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/SlaveViewControllerEditorList/?master_id=' + id
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getDjangularSlaveViewControllerDetail(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/SlaveViewControllerEditorDetail/?id=' + id
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function putDjangularSlaveViewController(id, content) {
            var deferred = $q.defer();
            $http({
                method: 'PUT',
                data: content,
                url: '/krogoth_gantry/SlaveViewControllerEditorDetail/?id=' + id
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function djangoManagePyCollectStatic() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/LazarusII/AutoCollectStatic/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getUnitFbiDetail(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/LazarusII/serialized/FBISerialized/' + id + '/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getWeaponTdfDetail(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/LazarusII/serialized/WeaponTDF/' + id + '/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getAllUnitFBIsFromSQL() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/LazarusDatabase/UnitFBIFromSQLView/'
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