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
            },
            // Error
            function (response) {
                console.error(response);
            }
        );


        function sendMsg() {
            console.log('sending a message... ');
            ws.$emit(vm.userInput);

            api.blog.list.get({},
                // Success
                function (response) {
                    console.log(response);
                },
                // Error
                function (response) {
                    console.error(response);
                }
            );
        }


    }
})();