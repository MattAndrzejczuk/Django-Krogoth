(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        /// 
        vm.totalUnits = 0;
        vm.modName = 'X';
        $http({
            method: 'GET',
            url: '/LazarusDatabase/UnitFBIFromSQLView/'
        }).then(function successCallback(response) {
            vm.totalUnits = response.data['list_response'].length;
            vm.modName = response.data['mod'];
        }, function errorCallback(response) {

        });
        /// 

    }
})();