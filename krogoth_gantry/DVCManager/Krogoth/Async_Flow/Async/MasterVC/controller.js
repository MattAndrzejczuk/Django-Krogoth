(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($scope, $q, $timeout) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        $scope.messages = [];
        $scope.failLog = [];
        $scope.successLog = [];

        $scope.parallel = function(fail) {
            $q.all([async ('1', 1500)(),
                    async ('2', 1000, fail)(),
                    async ('3', 500)()
                ])
                .then(done, oops);
        };

        $scope.series = function(fail) {
            async ('1', 1500)()
            .then(async ('2', 1000, fail))
                .then(async ('3', 500))
                .then(done, oops);
        };

        var async = function(id, delay, fail) {
            return function() {
                var deferred = $q.defer();

                $scope.messages.push(id + ' has started');

                $timeout(function() {
                    if (fail) {
                        $scope.messages.push(id + ' has failed');
                        deferred.reject();
                    } else {
                        $scope.messages.push(id + ' has completed');
                        deferred.resolve();
                    }
                }, delay);

                return deferred.promise;
            }
        };

        var done = function() {
            $scope.messages.push('all done');
            $scope.successLog.push(Date().toString());
        };

        var oops = function() {
            $scope.messages.push('something failed');
            $scope.failLog.push(Date().toString());
        };


    }
})();