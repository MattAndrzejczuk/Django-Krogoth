(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast, $timeout, $log, RESTfulModelVII) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.toastMsg = '';

        vm.RESTfulJSONPayload = {};


        vm.$onInit = onInit;
        vm.$onDestroy = onDestroy;


        vm.postNewObject = postNewObject;


        function onInit() {

        }

        function onDestroy() {

        }

        function postNewObject() {
            RESTfulModelVII.postNewObject(vm.RESTfulJSONPayload.image)
                .then(function(response){
                $mdToast.show({
                    template: '<md-toast>image was uploaded.</md-toast>',
                    hideDelay: 2000,
                    position: 'bottom right'
                });
                vm.RESTfulJSONPayload = {};
            });
        }

    }
})();