(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            breadCategory: {},
            breadSubCategory: {},
            breadEnd: {},
            cookBread: cookBread,
            makeBread: makeBread
        };


        function cookBread(catId, subId, docId) {
            var deferred = $q.defer();
            $log.info("[   ]:   0%");
            service.makeBread(catId)
                .then(function(firstSlice) {
                    $log.info("[   ]:  25%");
                    service.breadCategory = firstSlice;
                    service.makeBread(subId)
                        .then(function(secondSlice) {
                            $log.info("[   ]:  50%");
                            service.breadSubCategory = secondSlice;
                            service.breadEnd = {
                                "MasterVCId": docId
                            };
                            $log.info("[   ]:  75%");
                            var finishedBread = [];
                            finishedBread.push(service.breadCategory);
                            finishedBread.push(service.breadSubCategory);
                            finishedBread.push(service.breadEnd);
                            $log.info("[   ]: 100%");
                            $log.debug(" Bread has finished cooking, Mmm... ");
                            $log.log(finishedBread);
                            deferred.resolve(finishedBread);
                        });
                });
            return deferred.promise;
        }


        function makeBread(catId) {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: "/krogoth_gantry/viewsets/Category/" + catId + "/"
            }).then(function successCallback(response) {
                /// Success               
                $log.info(" - - - - - - - - - - - - - makeBread ! ! ! ! ! ");
                $log.log("/krogoth_gantry/viewsets/Category/" + catId + "/");
                //service.breadSubCategory = response.data.parent;
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }



        return service;
    }
})();