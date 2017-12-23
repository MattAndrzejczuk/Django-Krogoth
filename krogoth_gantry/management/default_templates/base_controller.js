(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($websocket) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        var ws = $websocket.$new('ws://localhost/ws/Test%7CThis%7CSocket%23Socket?subscribe-broadcast&publish-broadcast&echo&subscribe-typing');
        ws.$emit('hello', 'world');
        ws.$on('$open', function () {
            ws.$emit('hello', 'world'); // it sends the event 'hello' with data 'world'
        })
            .$on('incoming event', function (message) { // it listents for 'incoming event'
                console.log('something incoming from the server: ' + message);
            });


        /* - - - - - */
    }
})();