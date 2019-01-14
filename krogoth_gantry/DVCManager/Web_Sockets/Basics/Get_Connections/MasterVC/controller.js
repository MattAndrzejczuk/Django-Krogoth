(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($websocket, $mdToast, $location, $timeout, $mdSidenav) {
        /* jshint validthis: true */
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.sendVanillaPushNotification = sendVanillaPushNotification;
        vm.closeWsCon = closeWsCon;
        vm.openWsCon = openWsCon;
        vm.sendMsg = sendMsg;

        vm.$onInit = onInit;
        vm.$onDestroy = onDestroy;

        vm.connectionTimeout = 1000;

        vm.messagesTracked = [];

        vm.msgs = [];

        vm.customSocketUriForm = {};
        vm.signature = "swhite";

        const wsChannel = 'Signature%7CChat%23General?subscribe-broadcast&publish-broadcast';
        const conURI = 'ws://' + $location.host() + '/ws/' + wsChannel;

        vm.ws = $websocket.$new({
            url: conURI,
            lazy: true
        });

        vm.toggleSidenav = toggleSidenav;

        function toggleSidenav(sidenavId) {
            $mdSidenav(sidenavId).toggle();
        }

        function onInit() {
            var introMsg = 'Unknown Connection Status: ';
            if (vm.ws.$status() === 3) {
                const secsFromMiliseconds = vm.connectionTimeout / 1000;
                introMsg = 'Connecting to Web Socket in ' + secsFromMiliseconds + ' seconds... ';

                $timeout(function() {
                    vm.openWsCon(); // it will open the websocket after 5 seconds
                }, vm.connectionTimeout);
            } else {
                introMsg = introMsg + ' ' + vm.ws.$status();
            }
            $mdToast.show({
                template: '<md-toast class="md-toast">' + introMsg + '</md-toast>',
                hideDelay: 4000,
                position: 'bottom right'
            });
        }

        function closeWsCon() {
            if (vm.ws.$status() === 1)
                vm.ws.$close();
            /// DETACH ALL EVENTS:
            vm.ws.$un('$message');
            vm.ws.$un('$open');
            vm.ws.$un('$close');
        }

        vm.otherChannelMembers = [];

        function openWsCon() {
            var p1 = vm.customSocketUriForm.p1 + "%7C";
            var p2 = vm.customSocketUriForm.p2 + "%23";
            var p3 = vm.customSocketUriForm.p3 + "?subscribe-broadcast&publish-broadcast";
            var chnl = p1 + p2 + p3;
            var uri = 'ws://' + $location.host() + '/ws/' + chnl;

            vm.ws = $websocket.$new({
                url: uri,
                lazy: false
            });

            vm.ws.$on('$message', function(message) { // it listents for 'incoming event'
                if (message !== '--heartbeat--') {
                    console.log('$message incoming from the server: ' + message);
                    if (message['data']) {
                        vm.messagesTracked.push(message);
                        vm.msgs.push(message['data']);
                        if (message['type'] === "chatroom_list") {
                            var audio2 = new Audio('/static/gui_sfx/beep_surrender.wav');
                            $mdToast.show(
                                $mdToast.simple()
                                .textContent('someone has disconnected.')
                                .position('bottom left')
                                .hideDelay(2000)
                            );
                            audio2.play();
                        } else {
                            $mdToast.show(
                                $mdToast.simple()
                                .textContent(message['data'])
                                .position('bottom left')
                                .hideDelay(4000)
                            );
                            var audio = new Audio('/static/gui_sfx/beep_new_line_data.wav');
                            audio.play();
                            var shouldAddNewMember = true;
                            for (var i = 0; i < vm.otherChannelMembers.length; i++) {
                                if (vm.otherChannelMembers[i].id === message["data"]["sender"]) {
                                    shouldAddNewMember = false;
                                }
                            }
                            if (shouldAddNewMember === true)
                                vm.otherChannelMembers.push(message["data"]["sender"]);
                        }
                    }
                    vm.sendVanillaPushNotification(message['data']);
                }
            });
            vm.ws.$on('$open', function() {
                console.log(vm.ws.$status()); // it prints ws.$OPEN
                $mdToast.show({
                    template: '<md-toast class="md-toast">' + vm.ws.$status() + '</md-toast>',
                    hideDelay: 4000,
                    position: 'bottom right'
                });
            });
            vm.ws.$on('$close', function() {
                console.log(vm.ws.$status()); // it prints ws.$CLOSED
                console.log('Connection closed!');

                $mdToast.show({
                    template: '<md-toast class="md-toast">' + vm.ws.$status() + '</md-toast>',
                    hideDelay: 4000,
                    position: 'bottom right'
                });
            });
        }

        function sendMsg() {
            var userFeedback = 'Failed to send message! No connection is established.';
            var msg = {
                text: vm.userInput,
                sender: vm.signature
            };
            if (vm.ws.$status() === 1) {
                userFeedback = 'Message sent!';
                vm.ws.$emit('text', msg);
                vm.messagesTracked.push({
                    data: msg
                });
                vm.userInput = "";
            }
            $mdToast.show(
                $mdToast.simple()
                .textContent(userFeedback)
                .position('bottom right')
                .hideDelay(2000)
            );
        }

        function sendVanillaPushNotification(strMsg) {
            Notification.icon = 'http://localhost/static/assets/images/logos/CORE_logo.png';
            Notification.badge = 'http://localhost/static/assets/images/logos/CORE_logo.png';
            Notification.image = 'http://localhost/static/assets/images/logos/CORE_logo.png';
            Notification.requireInteraction = true;
            if (!("Notification" in window)) {
                console.log("This browser does not support desktop notification");
            } else if (Notification.permission === "granted") {
                var notification = new Notification(strMsg);
            } else if (Notification.permission !== 'denied' || Notification.permission === "default") {
                Notification.requestPermission(function(permission) {
                    if (permission === "granted") {
                        var notification = new Notification(strMsg);
                    }
                });
            }
        }

        function onDestroy() {
            var audio = new Audio('/static/gui_sfx/click_side_arm2.wav');
            audio.play();
            vm.closeWsCon();
        }

    }
})();