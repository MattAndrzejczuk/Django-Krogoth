(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($websocket) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.userInput = '';

        vm.sendMsg = sendMsg;
        vm.msgs = [];
        /// "Test%7CThis%7CSocket%23Socket"
        /// &publish-broadcast
        /// &echo
        var str = 'Public%7CChat%23General?subscribe-broadcast&publish-broadcast';
        var ws = $websocket.$new('ws://localhost/ws/' + str);
        ws.$on('event', function(message) {
            //ws.$emit('hello', 'world'); // it sends the event 'hello' with data 'world'
            console.log('got some kind of event' + message);
        }).$on('$message', function(message) { // it listents for 'incoming event'
            if (message !== '--heartbeat--') {
                console.log('$message incoming from the server: ' + message);
                var oldArray = vm.msgs;
                oldArray.push(message);
                vm.msgs = oldArray;
            }
        });


        function sendMsg() {
            console.log('sending a message... ');
            ws.$emit(vm.userInput);
        }
    }
})();