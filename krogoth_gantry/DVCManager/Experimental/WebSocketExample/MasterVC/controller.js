(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($websocket, $mdToast) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.sendMsg = sendMsg;
        vm.msgs = [];

        var str = 'Public%7CChat%23General?subscribe-broadcast&publish-broadcast';
        var ws = $websocket.$new('ws://localhost/ws/' + str);
        ws.$on('$message', function (message) { // it listents for 'incoming event'
            if (message !== '--heartbeat--') {
                console.log('$message incoming from the server: ' + message);
                vm.msgs.push(message);
                $mdToast.show(
                    $mdToast.simple()
                        .textContent(message.data)
                        .position('bottom left')
                        .hideDelay(2000)
                );
            }
        });


        function sendMsg() {
            console.log('sending a message... ');
            ws.$emit('messageType', vm.userInput);
                            $mdToast.show(
                    $mdToast.simple()
                        .textContent('Message Sent!')
                        .position('bottom right')
                        .hideDelay(2000)
                );
        }


    }
})();