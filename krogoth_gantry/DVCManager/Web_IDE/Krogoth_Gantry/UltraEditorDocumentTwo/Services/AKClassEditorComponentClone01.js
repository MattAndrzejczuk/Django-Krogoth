(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);
    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {

            loadHTMLCoreList: loadHTMLCoreList,
            loadKrogothCoreList: loadKrogothCoreList,

            addNodeToEditor: addNodeToEditor,
            js_nodes: [],
            html_nodes: []
        };


        function loadHTMLCoreList(masterName) {
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            $log.log("    GET");
            $log.log("    /krogoth_gantry/viewsets/IncludedHtmlCore/");
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: "/krogoth_gantry/viewsets/IncludedHtmlCore/"
            }).then(function successCallback(response) {
                var htmls = response.data.results;
                var returnNodes = [];
                for (var i = 0; i < htmls.length; i++) {
                    var item_in = htmls[i];
                    var newNode = {
                        id: item_in.id,
                        parentIndex: 1,
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
                        RESTfulURI: "/krogoth_gantry/viewsets/IncludedHtmlCore/" + item_in.id + "/",
                        syntax: 'htmlmixed',
                        icon: 'link-variant'
                    };
                    service.html_nodes.push(newNode);
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
            var URL = '/krogoth_gantry/viewsets/AKFoundation/';
            $http({
                method: 'GET',
                url: URL
            }).then(function successCallback(response) {
                var cores = response.data.results;
                ///var returnNods = [];
                ///service.needMore = false;

                if (response.data.next) {
                    ///service.needMore = true;
                    ///service.nextPage = response.data.next;
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


        return service;
    }
})();