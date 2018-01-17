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
                var master = {
                    id: _masterVCID,
                    index: 0,
                    title: 'Master Views',
                    class: "MasterViewController",
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: true
                };
                var styles = {
                    id: _masterVCID,
                    index: 1,
                    title: 'CSS',
                    class: "MasterViewController",
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: true
                };
                var slaves = {
                    id: _masterVCID,
                    index: 2,
                    title: 'Slave Views',
                    class: "SlaveViewController",
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: true
                };
                var direct = {
                    id: _masterVCID,
                    index: 3,
                    title: 'Directives',
                    class: "Directive",
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: true
                };
                var servic = {
                    id: _masterVCID,
                    index: 4,
                    title: 'Services',
                    class: "Service",
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: true
                };
                var xtHTML = {
                    id: _masterVCID,
                    index: 5,
                    title: 'HTML Templates',
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: true
                };
                var xtraJS = {
                    id: _masterVCID,
                    index: 6,
                    title: 'JavaScript Templates',
                    nodes: [],
                    canRemove: false,
                    canEdit: false,
                    canAdd: true
                };
                returnData.push(master);
                returnData.push(styles);
                returnData.push(slaves);
                returnData.push(direct);
                returnData.push(servic);
                returnData.push(xtHTML);
                returnData.push(xtraJS);
                deferred.resolve(returnData);
            } catch (ex) {
                deferred.reject(returnData);
            }
            return deferred.promise;
        }
        return service;
    }
})();