(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $http, $scope, $q, $timeout) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.didClickLoadBase64 = didClickLoadBase64;
        vm.didClickSetToImage = didClickSetToImage;

        vm.base64Data = '';
        vm.base64Image = '';

        vm.imageWidth = 3840;
        vm.imageHeight = 512;

        vm.cacheImageInCookies = cacheImageInCookies;
        vm.deleteImageFromCookies = cacheImageInCookies;
        
        vm.imageName = "EpicPlanet_1.png";

        function cacheImageInCookies() {

        }

        function deleteImageFromCookies() {

        }

        function didClickLoadBase64() {
            $log.log('Did Click Load Base64');
            $http({
                method: 'GET',
                url: '/moho_extractor/LoadFileAsBase64?name=EpicPlanet_1.png'
            }).then(function successCallback(response) {
                vm.base64Data = response.data;
            }, function errorCallback(response) {
                $log.log(response);
                $log.log('FAIL...');
            });
        }

        function didClickSetToImage() {
            $log.log('Did Click Set To Image');
            vm.base64Image = 'data:image/jpg;base64,' + vm.base64Data;
        }


        vm.asyncmessages = [];
        vm.asyncfailLog = [];
        vm.asyncsuccessLog = [];

        vm.parallel = parallel;
        vm.series = series;

        function parallel() {
            $q.all([
                    async ('dispatch_task1')(),
                    async ('dispatch_task2')()
                ])
                .then(done, oops);
        };

        function series() {
            async ('dispatch_task1')()
            .then(async ('dispatch_task2'))
                .then(done, oops);
        };

        var async = function(id) {
            return function() {
                var deferred = $q.defer();
                vm.asyncmessages.push(id + ' has started');
                if (id === 'dispatch_task1') {
                    $http({
                        method: 'GET',
                        url: '/moho_extractor/LoadFileAsBase64?name=' + vm.imageName
                    }).then(function successCallback(response) {
                        vm.asyncmessages.push(id + ' has completed');
                        vm.base64Data = response.data;
                        deferred.resolve();
                    }, function errorCallback(response) {
                        vm.asyncmessages.push(id + ' has failed');
                        deferred.reject();
                    });
                } else {
                    vm.base64Image = 'data:image/jpg;base64,' + vm.base64Data;
                    deferred.resolve();
                }
                return deferred.promise;
            }
        };

        var done = function() {
            vm.asyncmessages.push('all done');
            vm.asyncsuccessLog.push(Date().toString());
        };

        var oops = function() {
            vm.asyncmessages.push('something failed');
            vm.asyncfailLog.push(Date().toString());
        };


    }
})();