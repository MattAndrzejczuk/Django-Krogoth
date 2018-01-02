(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController(api) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        vm.sendMsg = sendMsg;
        vm.data = {};


        api.example.list.get({},
            // Success
            function (response) {
                console.log(response);
                vm.data = response;
            },
            // Error
            function (response) {
                console.error(response);
                vm.data = response;
            }
        );


        function sendMsg() {
            console.log('sending a message... ');

            api.example.list.get({},
                // Success
                function (response) {
                    console.log(response);
                    vm.data = response;
                },
                // Error
                function (response) {
                    console.error(response);
                    vm.data = response;
                }
            );
        }


    }
})();