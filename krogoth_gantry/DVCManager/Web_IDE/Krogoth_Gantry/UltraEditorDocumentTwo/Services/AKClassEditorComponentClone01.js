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
            loadKrogothCoreList: loadKrogothCoreList,

            addNodeToEditor: addNodeToEditor,
            addNodeToEditorSet2: addNodeToEditorSet2,
            needMore: false,
            nextPage: "",
            js_nodes: [],
            js_nodes_2: []
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



        function addNodeToEditorSet2(uri) {
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            $log.log("    GET");
            $log.log("    " + uri);
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: uri
            }).then(function successCallback(response) {
                var cores = response.data.results;
                ///var returnNods = [];

                service.needMore = false;

                if (response.data.next) {
                    service.needMore = true;
                    service.nextPage = response.data.next;
                }

                $(cores).each(function(i, item_in) {
                    var item_in = cores[i];
                    var newNode = {
                        id: item_in.id,
                        parentIndex: 1,
                        index: service.js_nodes.length,
                        title: item_in.unique_name,
                        name: item_in.uniquename,
                        class: item_in.last_name,
                        canRemove: false,
                        canEdit: true,
                        isMaster: false,
                        sourceCode: item_in.code,
                        sourceKey: 'code',
                        RESTfulId: item_in.id,
                        RESTfulURI: "/krogoth_gantry/viewsets/AKFoundation/" + item_in.id + "/",
                        syntax: 'javascript',
                        icon: 'nodejs'
                    };
                    service.addNodeToEditorSet2(newNode);
                    //$log.info("ADDING NODE " + i + ": " + item_in.first_name + item_in.last_name);
                });

                deferred.resolve(service.js_nodes);
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
            var URL = '/krogoth_gantry/viewsets/AKFoundation/';
            if (service.nextPage)
                URL = service.nextPage;
            $http({
                method: 'GET',
                url: URL
            }).then(function successCallback(response) {
                var cores = response.data.results;
                ///var returnNods = [];
                service.needMore = false;

                if (response.data.next) {
                    service.needMore = true;
                    service.nextPage = response.data.next;
                }

                $(cores).each(function(i, item_in) {
                    var item_in = cores[i];

                    var newNode = {
                        id: item_in.id,
                        parentIndex: 0,
                        index: service.js_nodes.length,
                        title: item_in.first_name,
                        name: item_in.uniquename,
                        class: item_in.last_name,
                        canRemove: false,
                        canEdit: true,
                        isMaster: false,
                        sourceCode: item_in.code,
                        sourceKey: 'code',
                        RESTfulId: item_in.id,
                        RESTfulURI: "/krogoth_gantry/viewsets/AKFoundation/" + item_in.id + "/",
                        syntax: 'javascript',
                        icon: 'nodejs'
                    };
                    service.addNodeToEditor(newNode);
                    ///$log.info("ADDING NODE " + i + ": " + item_in.first_name + item_in.last_name);
                });
                deferred.resolve(service.js_nodes);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function addNodeToEditor(newNode) {
            $log.info("[1]: " + newNode.class);
            if (newNode.class === "controller")
                newNode.icon = "pillar";
            if (newNode.class === "constant")
                newNode.icon = "react";
            if (newNode.class === "filter")
                newNode.icon = "layers-outline";
            service.js_nodes.push(newNode);
        }

        function addNodeToEditorSet2(newNode) {
            $log.info("[2]: " + newNode.class);
            if (newNode.class === "controller")
                newNode.icon = "pillar";
            if (newNode.class === "constant")
                newNode.icon = "react";
            if (newNode.class === "filter")
                newNode.icon = "layers-outline";
            service.js_nodes_2.push(newNode);
        }

        return service;
    }
})();