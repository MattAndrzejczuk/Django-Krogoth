(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_SLAVE_NAMEController', FUSE_APP_SLAVE_NAMEController);

    function FUSE_APP_SLAVE_NAMEController($stateParams, $http, $log) {
        var vm = this;
        vm.viewName = '_SLAVE_NAME_' + $stateParams.categoryId;

        vm.$onInit = onInit;
        vm.loadMasters = loadMasters;

        $log.log('IS THE FUCKING CONTROLLER LOADED?');

        vm.objectList = {};


        function onInit() {
            vm.loadMasters();
        }


        function loadMasters() {
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/MasterViewController/?category=' + $stateParams.categoryId
            }).then(function successCallback(response) {
                vm.objectList = response.data;
                //deferred.resolve(response.data);
            }, function errorCallback(response) {
                //deferred.reject(response);
            });
        }




    }
})();