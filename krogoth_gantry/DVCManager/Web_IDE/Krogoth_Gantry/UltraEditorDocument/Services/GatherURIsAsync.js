/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        var service = {
            async: async,
            list: []
        };

        function async (array, className) {
            return function() {
                var deferred = $q.defer();
                var pendingRESTfulRequests = [];
                try {
                    for (var i = 0; i < array.length; i++) {
                        var id_in = array[i];
                        if (className === 'SlaveViewController') {
                            pendingRESTfulRequests.push({
                                'class': 'SlaveViewController',
                                'id': id_in
                            });
                        } else if (className === 'Directive') {
                            pendingRESTfulRequests.push({
                                'class': 'Directive',
                                'id': id_in
                            });
                        } else {
                            pendingRESTfulRequests.push({
                                'class': 'Service',
                                'id': id_in
                            });
                        }
                    }
                    service.list = pendingRESTfulRequests;
                    deferred.resolve(pendingRESTfulRequests);
                } catch (ex) {
                    deferred.reject(pendingRESTfulRequests);
                }
                return deferred.promise;
            };
        }





        return service;
    }
})();