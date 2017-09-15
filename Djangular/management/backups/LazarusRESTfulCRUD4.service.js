(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            getSelectedModProject: getSelectedModProject,
            getModAssets: getModAssets,
            getAssetDependencies: getAssetDependencies,
            getAllUnitFBIsFromSQL: getAllUnitFBIsFromSQL,
            getWeaponTdfDetail: getWeaponTdfDetail,
            getUnitFbiDetail: getUnitFbiDetail
        };

        function getSelectedModProject() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/LazarusDatabase/SelectedModProject/'
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getModAssets(id, verbose) {
            var deferred = $q.defer();
            if (verbose)
                $log.info('/LazarusDatabase/TotalAnnihilation/LazarusModAsset/?project_id=' + id);
            $http({
                method: 'GET',
                url: '/LazarusDatabase/TotalAnnihilation/LazarusModAsset/?project_id=' + id
            }).then(function successCallback(response) {
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getAssetDependencies(id) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/LazarusDatabase/TotalAnnihilation/LazarusModDependency/?asset_id=' + id
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

        function patchWeaponTdf(id, key, value) {
            var deferred = $q.defer();
            $http({
                method: 'PATCH',
                data: {
                    key: value
                },
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