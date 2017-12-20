(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');
        //var ws = new WebSocket("ws://armprime.co/ws/GenericConnection%23General?subscribe-broadcast&publish-broadcast&echo&subscribe-typing");
        var service = {
            /*
            didConnect: didConnect,
            didDisconnect: didDisconnect,
			*/
            didReceiveMessage: didReceiveMessage
        };


        function didReceiveMessage() {
            /*
            var deferred = $q.defer();
            ws.onmessage = function(evt) {
                var received_msg = evt.data;
                if (evt.data) {
                    if (evt.data !== '--heartbeat--') {
                        $log.info('WebSocket Message Received:');
                        $log.debug(evt.data);
                        deferred.resolve(evt.data);
                    } else {
                        $log.debug(evt.data);
                    }
                } else {
                    deferred.reject(evt);
                }
            };
            return deferred.promise;
			*/
        }

        /*
                function didConnect() {
                    var deferred = $q.defer();
                    ws.onopen = function() {
                        // Web Socket is connected, send data using send()
                        if (response.data) {
                            deferred.resolve(response.data);
                        } else {
                            deferred.reject(response);
                        }
                    };
                    return deferred.promise;
                }


                function didDisconnect() {
                    var deferred = $q.defer();
                    ws.onclose = function() {
                        // Web Socket is connected, send data using send()
                        if (response.data) {
                            deferred.resolve(response.data);
                        } else {
                            deferred.reject(response);
                        }
                    };
                    return deferred.promise;
                }

        */

        return service;
    }
})();