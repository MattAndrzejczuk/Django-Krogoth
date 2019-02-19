(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast, $timeout, $log, RESTfulModelVII) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.toastMsg = '';


        vm.$onInit = onInit;
        vm.$onDestroy = onDestroy;


        function onInit() {

        }

        function onDestroy() {

        }
        
        
    }
})();