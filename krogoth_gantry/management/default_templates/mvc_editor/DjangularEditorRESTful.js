(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            getkrogoth_gantryMasterViewControllers: getkrogoth_gantryMasterViewControllers,
            getkrogoth_gantryMasterViewControllerDetail: getkrogoth_gantryMasterViewControllerDetail,
            putkrogoth_gantryMasterViewController: putkrogoth_gantryMasterViewController,

            getkrogoth_gantrySlaveViewControllers: getkrogoth_gantrySlaveViewControllers,
            getkrogoth_gantrySlaveViewControllerDetail: getkrogoth_gantrySlaveViewControllerDetail,
            putkrogoth_gantrySlaveViewController: putkrogoth_gantrySlaveViewController,

            djangoManagePyCollectStatic: djangoManagePyCollectStatic
        };

        function getkrogoth_gantryMasterViewControllers() {
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

        function getkrogoth_gantryMasterViewControllerDetail(id) {
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

        function putkrogoth_gantryMasterViewController(id, content) {
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

        function getkrogoth_gantrySlaveViewControllers(id) {
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

        function getkrogoth_gantrySlaveViewControllerDetail(id) {
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

        function putkrogoth_gantrySlaveViewController(id, content) {
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
        /*
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
        */
        return service;
    }
})();