(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            loadMasterInitializer: loadMasterInitializer
        };

        function loadMasterInitializer(selectedMasterId) {
            var deferred = $q.defer();
            var servicesPendingRequest = [];
            var directivesPendingRequest = [];
            var slavesPendingRequest = [];
            var returnedJsonFull = {};
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/MasterViewController/' + selectedMasterId + '/'
            }).then(function successCallback(response) {
                returnedJsonFull = response.data;
                for (var i = 0; i < response.data.djangular_service.length; i++) {
                    var item_in = response.data.djangular_service[i];
                    servicesPendingRequest.push(item_in);
                }
                for (var i = 0; i < response.data.djangular_directive.length; i++) {
                    var item_in = response.data.djangular_directive[i];
                    directivesPendingRequest.push(item_in);
                }
                for (var i = 0; i < response.data.djangular_slave_vc.length; i++) {
                    var item_in = response.data.djangular_slave_vc[i];
                    slavesPendingRequest.push(item_in);
                }
                var firstCompletedAPICall = {
                    services: servicesPendingRequest,
                    directives: directivesPendingRequest,
                    slaves: slavesPendingRequest,
                    objectList: returnedJsonFull
                };
                deferred.resolve(firstCompletedAPICall);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }
        return service;
    }
})();