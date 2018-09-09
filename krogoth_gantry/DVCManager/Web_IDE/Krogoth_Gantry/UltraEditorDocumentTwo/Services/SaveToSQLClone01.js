(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            saveDocument: saveDocument,
            getRESTfulModelName: getRESTfulModelName,
            addSiblingToMaster: addSiblingToMaster,
            createNew: createNew
        };

        function saveDocument(treeData, newCode) {
            var payload = {
                code: newCode
            };
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            $log.log("    PATCH");
            $log.log("    " + treeData.RESTfulURI);
            $log.log(payload);
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            ///payload[treeData.sourceKey] = newCode;
            var deferred = $q.defer();
            $http({
                method: 'PATCH',
                data: payload,
                url: treeData.RESTfulURI
            }).then(function successCallback(response) {
                /// Success
                $log.info(" 💾 Work has been saved 💾 ");
                $log.log(response.data);
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        function getRESTfulModelName(usingName) {
            /*
            $log.log(' ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ getRESTfulModelName');
            $log.log(usingName);

            if (usingName === "ControllerJS") {
                return "MasterViewController";
            } else if (usingName === "ModuleJS") {
                return "MasterViewController";
            } else if (usingName === "ViewHTML") {
                return "MasterViewController";
            } else if (usingName === "StyleCSS") {
                return "MasterViewController";
            } else if (usingName === "ThemeCSS") {
                return "MasterViewController";
            } else if (usingName === "Service") {
                return "Service";
            } else if (usingName === "Directive") {
                return "Directive";
            } else if (usingName === "SlaveView") {
                return "SlaveViewController";
            } else {
                return "SlaveViewController";
            }
			*/
        }

        function makeid() {
            /*
            var text = "";
            var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            for (var i = 0; i < 5; i++)
                text += possible.charAt(Math.floor(Math.random() * possible.length));
            return text;
			*/
        }

        function createNew(treeRoot, newName) {
            /*
            var payload = {};
            payload["title"] = newName + "_Untitled";
            payload["name"] = newName + "_" + makeid();
            $log.info("  🎲  RANDOM STRING GENERATED  🎲  ");
            $log.log(payload["name"]);
            const RESTfulURI = '/krogoth_gantry/viewsets/' + treeRoot.class + '/';
            var deferred = $q.defer();
            $http({
                method: 'POST',
                data: payload,
                url: RESTfulURI
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
			*/
        }

        function addSiblingToMaster(siblings, newModelJson, djangoModel, masterId) {
            /*
            $log.log(' - - - - - - - - - - - - - - - - - - ');
            $log.info('ADDING NEW COMPONENT TO MASTER: ');
            $log.debug('siblings:');
            $log.log(siblings);
            $log.debug('newModelJson:');
            $log.log(newModelJson);
            $log.debug('djangoModel:');
            $log.log(djangoModel);
            $log.debug('masterId:');
            $log.log(masterId);
            $log.log(' - - - - - - - - - - - - - - - - - - ');
            var pname = 'djangular_service';
            var payload = {};
            var siblingIds = [];
            for (var i = 0; i < siblings.length; i++) {
                siblingIds.push(siblings[i]);
            }

            if (djangoModel === "Service") {
                pname = 'djangular_service';
            } else if (djangoModel === "Directive") {
                pname = 'djangular_directive';
            } else if (djangoModel === "SlaveViewController") {
                pname = 'djangular_slave_vc';
            }
            siblingIds.push(newModelJson.id);
            payload[pname] = siblingIds;

            const RESTfulURI = '/krogoth_gantry/viewsets/MasterViewController/' + masterId + '/';

            var deferred = $q.defer();
            $http({
                method: 'PATCH',
                data: payload,
                url: RESTfulURI
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
			*/
        }

        return service;
    }
})();