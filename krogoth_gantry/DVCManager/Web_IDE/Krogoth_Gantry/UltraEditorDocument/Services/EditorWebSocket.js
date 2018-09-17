/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q, $location, $timeout, $mdToast, $websocket) {

        const wsChannel = 'FUSE_APP_NAME%7CFUSE_APP_NAME%23FUSE_APP_NAME?subscribe-broadcast&publish-broadcast';
        const conURI = 'ws://' + $location.host() + '/ws/' + wsChannel;

        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        var service = {
            initializeWebSocket: initializeWebSocket,
            onDestroy: onDestroy,

            closeWsCon: closeWsCon,
            openWsCon: openWsCon,
            sendMsg: sendMsg,
            sendVanillaPushNotification: sendVanillaPushNotification,
            keyboardSfxMuted: false,

            /// - - - - - - <   DELEGATE BACK TO CONTROLLER   > - - - - - - - - - -
            observerCallbacks: [],
            registerObserverCallback: registerObserverCallback,
            notifyObservers: notifyObservers,
            /// - - - - - - < / DELEGATE BACK TO CONTROLLER / > - - - - - - - - - -
            patchIncomingMsgThrough: patchIncomingMsgThrough,
            observerCallbacks_Save: [],
            registerObserver_Save_Callback: registerObserver_Save_Callback,
            notifyObservers_Save: notifyObservers_Save,

            connectionTimeout: 2000,
            msgs: [],

            ws: $websocket.$new({
                url: conURI,
                lazy: true
            }),

            messagesTracked: []

        };


        /// - - - - - - <   DELEGATE BACK TO CONTROLLER   > - - - - - - - - - -
        function registerObserverCallback(callback) {
            service.observerCallbacks.push(callback);
        }

        function notifyObservers(parentIndex, nodeIndex) {
            angular.forEach(service.observerCallbacks, function(callback) {
                callback(parentIndex, nodeIndex);
            });
        }
        /// - - - - - - < / DELEGATE BACK TO CONTROLLER / > - - - - - - - - - -
        function registerObserver_Save_Callback(callback) {
            service.observerCallbacks_Save.push(callback);
        }

        function notifyObservers_Save(parentIndex, nodeIndex) {
            angular.forEach(service.observerCallbacks_Save, function(callback) {
                callback(parentIndex, nodeIndex);
            });
        }



        function initializeWebSocket(chnl) {
            const wschannel = chnl + '%7C' + chnl + '%23' + chnl + '?subscribe-broadcast&publish-broadcast';
            const wsuri = 'ws://' + $location.host() + '/ws/' + wschannel;
            service.ws = $websocket.$new({
                url: wsuri,
                reconnect: true,
                reconnectInterval: 2000,
                enqueue: true,
                lazy: true
            });
            var introMsg = 'Unknown Connection Status: ';
            if (service.ws.$status() === 3) {
                const secsFromMiliseconds = service.connectionTimeout / 1000;
                introMsg = 'Connecting to ' + wschannel + ' in ' + secsFromMiliseconds + ' seconds... ';

                $timeout(function() {
                    service.openWsCon(); // it will open the websocket after 5 seconds
                }, service.connectionTimeout);
            } else {
                introMsg = introMsg + ' ' + service.ws.$status();
            }
            $mdToast.show({
                template: '<md-toast class="md-toast">' + introMsg + '</md-toast>',
                hideDelay: 4000,
                position: 'bottom right'
            });
        }



        function closeWsCon() {
            if (service.ws.$status() === 1)
                service.ws.$close();
            /// DETACH ALL EVENTS:
            service.ws.$un('$message');
            service.ws.$un('$open');
            service.ws.$un('$close');
        }

        function patchIncomingMsgThrough(message) {
            $log.log(message);
            if (message.data.action === "edit") {
                service.notifyObservers(message.data.info.parentIndex,
                    message.data.info.nodeIndex,
                    message.data.sentByWebBrowser);
            } else if (message.data.action === "save") {
                service.notifyObservers_Save(message.data.info.parentIndex,
                    message.data.info.nodeIndex,
                    message.data.sentByWebBrowser);
            }
        }

        function openWsCon() {
            if (service.ws.$status() !== 1)
                service.ws.$open();
            service.ws.$on('$message', function(message) { // it listents for 'incoming event'
                if (message !== '--heartbeat--') {
                    console.log('$message incoming from the server: ' + message);
                    $log.debug(message.data.info);
                    if (message['data']) {
                        service.messagesTracked.push(message);
                        service.msgs.push(message['data']);
                        if (message['data'] === []) {
                            var audio2 = new Audio('/static/gui_sfx/beep_surrender.wav');

                            $mdToast.show(
                                $mdToast.simple()
                                .textContent('someone has disconnected.')
                                .position('bottom left')
                                .hideDelay(2000)
                            );

                            audio2.play();
                        } else {
                            /*
                            $mdToast.show(
                                $mdToast.simple()
                                .textContent(message['data'])
                                .position('bottom left')
                                .hideDelay(4000)
                            );*/

                            service.patchIncomingMsgThrough(message);

                            if (service.keyboardSfxMuted === false) {
                                service.keyboardSfxMuted = true;
                            }

                            //audio.onended = function() {
                            //    service.keyboardSfxMuted = false;
                            //    $log.log("\n AUDIO ENDED \n");
                            //};
                        }
                    }
                    service.sendVanillaPushNotification(message['data']);
                }
            });

            service.ws.$on('$open', function() {
                console.log(service.ws.$status()); // it prints ws.$OPEN
                $mdToast.show({
                    template: '<md-toast class="md-toast">' + service.ws.$status() + '</md-toast>',
                    hideDelay: 4000,
                    position: 'bottom right'
                });
            });
            service.ws.$on('$close', function() {
                console.log(service.ws.$status()); // it prints ws.$CLOSED
                console.log('Connection closed!');

                $mdToast.show({
                    template: '<md-toast class="md-toast">' + service.ws.$status() + '</md-toast>',
                    hideDelay: 4000,
                    position: 'bottom right'
                });
            });
        }

        function sendMsg(msg) {
            var userFeedback = 'Failed to send message! No connection is established.';
            if (service.ws.$status() === 1) {
                userFeedback = 'Message sent!';
                service.ws.$emit('messageType', msg);
                service.messagesTracked.push({
                    msg
                });
                /// service.userInput = "";
            }
            /*
            $mdToast.show(
                $mdToast.simple()
                .textContent(userFeedback)
                .position('bottom right')
                .hideDelay(2000)
            );
			*/
        }

        function sendVanillaPushNotification(strMsg) {
            /*
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
			*/
        }



        function onDestroy() {
            var audio = new Audio('/static/gui_sfx/click_side_arm2.wav');
            audio.play();
            service.closeWsCon();
        }



        return service;
    }
})();