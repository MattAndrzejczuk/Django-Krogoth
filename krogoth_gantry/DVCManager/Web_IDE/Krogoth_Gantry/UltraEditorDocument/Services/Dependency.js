/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            async: async,
            loadHTMLIncludeList: loadHTMLIncludeList,
            ClassIsolatedSource: ClassIsolatedSource
        };

        function async (id_int, name_str, treeDataOld) {
            return function() {
                var deferred = $q.defer();

                $http({
                    method: "GET",
                    url: "/krogoth_gantry/viewsets/" + name_str + "/" + id_int + "/"
                }).then(function successCallback(response) {
                    var data_json = response.data;
                    var finishedRESTfulResponses = [];
                    var isolatedSrc;

                    finishedRESTfulResponses.push(data_json);
                    if (name_str === "Service") {

                        /// <   Service   >
                        var pi = 4;
                        var i = treeDataOld[4].nodes.length;
                        var src = data_json.service_js;
                        var title = data_json.title;
                        treeDataOld[4].nodes.push({
                            id: id_int,
                            parentIndex: pi,
                            index: i,
                            name: data_json.name,
                            title: title,
                            class: name_str,
                            sourceCode: "MOVED",
                            sourceKey: "service_js",
                            nodes: [],
                            canRemove: true,
                            canAdd: false,
                            canEdit: true,
                            isMaster: false,
                            RESTfulId: id_int,
                            RESTfulURI: '/krogoth_gantry/viewsets/Service/' + id_int + '/',
                            hasUnsavedChanges: false,
                            syntax: 'javascript',
                            isLoaded: false,
                            wasSavedInOtherBrowser: false,
                            openInOtherBrowser: false,
                            icon: 'language-javascript'
                        });
                        var service = new ClassIsolatedSource(pi, i, src, title);
                        isolatedSrc = (service);
                        $log.log("ClassIsolatedSource - service");
                        $log.log(service);
                        /// <   Service   >

                    } else if (name_str === "Directive") {

                        /// <   Directive   >
                        var pi = 3;
                        var i = treeDataOld[3].nodes.length;
                        var src = data_json.directive_js;
                        var title = data_json.title;
                        treeDataOld[3].nodes.push({
                            id: id_int,
                            parentIndex: pi,
                            index: i,
                            name: data_json.name,
                            title: title,
                            class: name_str,
                            sourceCode: "MOVED",
                            sourceKey: "directive_js",
                            nodes: [],
                            canRemove: true,
                            canAdd: false,
                            canEdit: true,
                            isMaster: false,
                            RESTfulId: id_int,
                            RESTfulURI: '/krogoth_gantry/viewsets/Directive/' + id_int + '/',
                            hasUnsavedChanges: false,
                            syntax: 'javascript',
                            isLoaded: false,
                            wasSavedInOtherBrowser: false,
                            openInOtherBrowser: false,
                            icon: 'language-javascript'
                        });
                        var directive = new ClassIsolatedSource(pi, i, src, title);
                        isolatedSrc = (directive);
                        $log.log("ClassIsolatedSource - directive");
                        $log.log(directive);
                        /// < / Directive / >

                    } else if (name_str === "SlaveViewController") {

                        /// <   Slave Ctrl   >
                        var piC = 2;
                        var iC = treeDataOld[2].nodes.length;
                        var srcC = data_json.controller_js;
                        var titleC = data_json.title + '|controller_js';
                        treeDataOld[2].nodes.push({
                            id: id_int,
                            parentIndex: 2,
                            index: treeDataOld[2].nodes.length,
                            name: data_json.name + '|controller_js',
                            title: data_json.title + '|controller_js',
                            class: name_str,
                            sourceCode: "MOVED",
                            sourceKey: "controller_js",
                            nodes: [],
                            canRemove: true,
                            canAdd: false,
                            canEdit: true,
                            isMaster: false,
                            RESTfulId: id_int,
                            RESTfulURI: '/krogoth_gantry/viewsets/SlaveViewController/' + id_int + '/',
                            hasUnsavedChanges: false,
                            syntax: 'javascript',
                            isLoaded: false,
                            wasSavedInOtherBrowser: false,
                            openInOtherBrowser: false,
                            icon: 'angularjs'
                        });
                        var slaveCtrl = new ClassIsolatedSource(piC, iC, srcC, titleC);
                        isolatedSrc = (slaveCtrl);
                        $log.log("ClassIsolatedSource - slaveCtrl");
                        $log.log(slaveCtrl);
                        /// < / Slave Ctrl / >

                        /// <   Slave View   >
                        var piV = 2;
                        var iV = treeDataOld[2].nodes.length;
                        var srcV = data_json.view_html;
                        var titleV = data_json.title + '|view_html';
                        treeDataOld[2].nodes.push({
                            id: id_int,
                            parentIndex: piV,
                            index: iV,
                            name: data_json.name + '|view_html',
                            title: titleV,
                            class: name_str,
                            sourceCode: "MOVED",
                            sourceKey: "view_html",
                            nodes: [],
                            canRemove: true,
                            canAdd: false,
                            canEdit: true,
                            isMaster: false,
                            RESTfulId: id_int,
                            RESTfulURI: '/krogoth_gantry/viewsets/SlaveViewController/' + id_int + '/',
                            hasUnsavedChanges: false,
                            syntax: 'htmlmixed',
                            isLoaded: false,
                            wasSavedInOtherBrowser: false,
                            openInOtherBrowser: false,
                            icon: 'language-javascript'
                        });
                        var slaveView = new ClassIsolatedSource(piV, iV, srcV, titleV);
                        isolatedSrc = (slaveView);
                        $log.log("ClassIsolatedSource - slaveView");
                        $log.log(slaveView);
                        /// < / Slave View / >
                    }


                    $log.info("asyncREST - " + "/krogoth_gantry/viewsets/" + name_str + "/" + id_int + "/");
                    var r = [treeDataOld, finishedRESTfulResponses, isolatedSrc];
                    deferred.resolve(r);
                }, function errorCallback(response) {
                    deferred.reject(response);
                });
                return deferred.promise;
            };
        }



        function loadHTMLIncludeList(masterName, tmplName) {
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");
            $log.log("    GET");
            $log.log("    /krogoth_gantry/viewsets/Included" + tmplName + "Master/?master_vc__name=" + masterName);
            $log.log("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~");

            var _syntax;
            if (tmplName === "Html") {
                _syntax = "htmlmixed";
            } else {
                _syntax = "javascript";
            }

            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: "/krogoth_gantry/viewsets/" + tmplName + "/?master_vc__name=" + masterName
            }).then(function successCallback(response) {
                var htmls = response.data.results;
                var r_ = {
                    returnNodes: [],
                    srcHTMLs: []
                };
                //var srcToPass = [];
                //var returnNodes = [];
                for (var i = 0; i < htmls.length; i++) {
                    var item_in = htmls[i];

                    var pi = 6;
                    var i = r_.returnNodes.length;
                    var src = item_in.contents;
                    var title = item_in.name;

                    var newNode = {
                        id: item_in.id,
                        parentIndex: pi,
                        index: i,
                        title: title,
                        name: item_in.url_helper,
                        class: "NgIncluded" + tmplName,
                        canRemove: true,
                        canEdit: true,
                        isMaster: false,
                        isLoaded: false,
                        wasSavedInOtherBrowser: false,
                        openInOtherBrowser: false,
                        sourceCode: src,
                        sourceKey: 'contents',
                        RESTfulId: item_in.id,
                        RESTfulURI: "/krogoth_gantry/viewsets/Included" + tmplName + "Master/" + item_in.id + "/",
                        syntax: _syntax,
                        icon: 'link-variant'
                    };

                    var TMPL = new ClassIsolatedSource(pi, i, src, title);

                    r_.srcTMPLs.push(TMPL);
                    r_.returnNodes.push(newNode);
                }
                deferred.resolve(r_);
            }, function errorCallback(response) {
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function ClassIsolatedSource(pi, i, src, t) {
            this.parentIndex = pi;
            this.index = i;
            this.srcCode = src;
            this.title = t;
        }


        return service;
    }
})();