(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($q, $timeout) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.parallel = parallel;
        vm.series = series;

        vm.messages = [];
        vm.failLog = [];
        vm.successLog = [];

        function parallel(fail) {

            var cpuTask1 = async('1', 1500)();
            var cpuTask2 = async('2', 1000, fail)();
            var cpuTask3 = async('3', 1000, fail)();

            $q.all([cpuTask1,
                    cpuTask2,
                    cpuTask3])
                    .then(done, oops);
        }

        function series(fail) {

            var cpuTask1 = async('1', 1500)();
            var cpuTask2 = async('2', 1000, fail);
            var cpuTask3 = async('3', 500, fail);

            cpuTask1
                .then(cpuTask2)
                .then(cpuTask3)
                .then(done, oops);
        }

        var async = function (id, delay, fail) {
            return function () {
                var deferred = $q.defer();

                vm.messages.push(id + ' has started');

                $timeout(function () {
                    if (fail) {
                        vm.messages.push(id + ' has failed');
                        deferred.reject();
                    } else {
                        vm.messages.push(id + ' has completed');
                        deferred.resolve();
                    }
                }, delay);

                return deferred.promise;
            }
        };

        var done = function () {
            vm.messages.push('all done');
            vm.successLog.push(Date().toString());
        };

        var oops = function () {
            vm.messages.push('something failed');
            vm.failLog.push(Date().toString());
        };


    }
})();