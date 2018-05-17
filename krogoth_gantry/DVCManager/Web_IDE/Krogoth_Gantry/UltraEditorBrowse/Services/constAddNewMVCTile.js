(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        var service = {
            makeTileJson: makeTileJson
        };

        function makeTileJson() {
            var deferred = $q.defer();

            const tile = {
                "id": 1,
                "name": "AddMVC",
                "title": "",
                "weight": 3,
                "icon": null,
                "parent": null
            }

            deferred.resolve(tile);
            return deferred.promise;
        }

        return service;
    }
})();