(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            populateBoilerplate: populateBoilerplate
        };

        function populateBoilerplate(_masterVCID) {
            var deferred = $q.defer();
            var returnData = [];
            try {

                
                
                var core = {
                    id: _masterVCID,
                    index: returnData.length,
                    title: 'Krogoth Core',
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: false
                };
                returnData.push(core);

                
                
                var xtraJS = {
                    id: _masterVCID,
                    index: returnData.length,
                    title: 'HTML Templates',
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: false
                };
                returnData.push(xtraJS);

                
                
                var directives = {
                    id: _masterVCID,
                    index: returnData.length,
                    title: 'Directives',
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: false
                };
                returnData.push(directives);
                
                
                
                
                

                deferred.resolve(returnData);
            } catch (ex) {
                deferred.reject(returnData);
            }
            return deferred.promise;
        }
        return service;
    }
})();