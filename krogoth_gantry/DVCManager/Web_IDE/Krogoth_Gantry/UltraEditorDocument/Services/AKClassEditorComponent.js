(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            loadMasterInitializer: loadMasterInitializer,
            loadHTMLIncludeList: loadHTMLIncludeList,
            loadKrogothCoreList: loadKrogothCoreList
        };

        function loadMasterInitializer(selectedMasterId) {
            var deferred = $q.defer();
            var servicesPendingRequest = [];
            var directivesPendingRequest = [];
            var slavesPendingRequest = [];
            var returnedJsonFull = {};
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/MasterViewController/' + selectedMasterId + '/'
            }).then(function successCallback(response) {
                $log.log('/krogoth_gantry/viewsets/MasterViewController/' + selectedMasterId + '/');
                returnedJsonFull = response.data;
                for (var i = 0; i < response.data.djangular_service.length; i++) {
                    var item_in = response.data.djangular_service[i];
                    servicesPendingRequest.push(item_in);
                }
                for (var i = 0; i < response.data.djangular_directive.length; i++) {
                    var item_in = response.data.djangular_directive[i];
                    directivesPendingRequest.push(item_in);
                }
                for (var i = 0; i < response.data.djangular_slave_vc.length; i++) {
                    var item_in = response.data.djangular_slave_vc[i];
                    slavesPendingRequest.push(item_in);
                }
                var firstCompletedAPICall = {
                    services: servicesPendingRequest,
                    directives: directivesPendingRequest,
                    slaves: slavesPendingRequest,
                    objectList: returnedJsonFull
                };
                deferred.resolve(firstCompletedAPICall);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function loadHTMLIncludeList(masterName) {
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            $log.log("    GET");
            $log.log("    /krogoth_gantry/viewsets/IncludedHtmlMaster/?master_vc__name=" + masterName);
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: "/krogoth_gantry/viewsets/IncludedHtmlMaster/?master_vc__name=" + masterName
            }).then(function successCallback(response) {
                var htmls = response.data.results;
                var returnNodes = [];
                for (var i = 0; i < htmls.length; i++) {
                    var item_in = htmls[i];
                    var newNode = {
                        id: item_in.id,
                        parentIndex: 5,
                        index: returnNodes.length,
                        title: item_in.name,
                        name: item_in.url_helper,
                        class: "NgIncludedHtml",
                        canRemove: true,
                        canEdit: true,
                        isMaster: false,
                        isLoaded: false,
                        wasSavedInOtherBrowser: false,
                        openInOtherBrowser: false,
                        sourceCode: item_in.contents,
                        sourceKey: 'contents',
                        RESTfulId: item_in.id,
                        RESTfulURI: "/krogoth_gantry/viewsets/IncludedHtmlMaster/" + item_in.id + "/",
                        syntax: 'htmlmixed',
                        icon: 'link-variant'
                    };
                    returnNodes.push(newNode);
                }
                deferred.resolve(returnNodes);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function loadKrogothCoreList() {
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            $log.log("    GET");
            $log.log("    /krogoth_gantry/viewsets/AKFoundation/");
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/AKFoundation/'
            }).then(function successCallback(response) {
                var cores = response.data.results;
                var returnNodes = [];
                for (var i = 0; i < cores.length; i++) {
                    var item_in = cores[i];
                    var newNode = {
                        id: item_in.id,
                        parentIndex: 7,
                        index: returnNodes.length,
                        title: item_in.first_name,
                        name: item_in.uniquename,
                        class: item_in.last_name,
                        canRemove: false,
                        canEdit: true,
                        isLoaded: false,
                        wasSavedInOtherBrowser: false,
                        openInOtherBrowser: false,
                        isMaster: false,
                        sourceCode: item_in.code,
                        sourceKey: 'code',
                        RESTfulId: item_in.id,
                        RESTfulURI: "/krogoth_gantry/viewsets/AKFoundation/" + item_in.id + "/",
                        syntax: 'javascript',
                        icon: 'nodejs'
                    };
                    returnNodes.push(newNode);
                }
                deferred.resolve(returnNodes);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }

        return service;
    }
})();