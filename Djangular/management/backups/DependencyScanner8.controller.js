(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, UnitFBIFromSQLService) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.getDepen = getDepen;
        vm.list = {};
        vm.response = '';


        var body = document.body,
            html = document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight,
            html.clientHeight, html.scrollHeight, html.offsetHeight);
        vm.heightFromButtons = height;

        UnitFBIFromSQLService.getAllUnits().then(function(data) {
            vm.list = data;
        });

        function getDepen(uid) {
            $http({
                method: 'GET',
                url: '/LazarusIII/DependenciesForUnitFBI/?uid=' + uid
            }).then(function successCallback(response) {
                // this callback will be called asynchronously
                // when the response is available
                vm.response = response.data;
                var logDiv = document.getElementById("responseLog")
                logDiv.innerHTML = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        }
    }
})();