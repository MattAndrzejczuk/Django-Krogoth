(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        $log.log('Hello. The service _DJANGULAR_SERVICE_NAME_ is online ! ! !');

        var service = {
            async: async
        };

        function async(id_int, name_str, treeDataOld) {
            return function () {
                var deferred = $q.defer();

                $http({
                    method: "GET",
                    url: "/krogoth_gantry/viewsets/" + name_str + "/" + id_int + "/"
                }).then(function successCallback(response) {
                    var data_json = response.data;
                    var finishedRESTfulResponses = [];
                    finishedRESTfulResponses.push(data_json);
                    if (name_str === "Service") {
                        treeDataOld[4].nodes.push({
                            id: id_int,
                            parentIndex: 4,
                            index: treeDataOld[4].nodes.length,
                            name: data_json.name,
                            title: data_json.title,
                            class: name_str,
                            sourceCode: data_json.service_js,
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
                            icon: 'language-javascript'
                        });
                    }
                    else if (name_str === "Directive") {
                        treeDataOld[3].nodes.push({
                            id: id_int,
                            parentIndex: 3,
                            index: treeDataOld[3].nodes.length,
                            name: data_json.name,
                            title: data_json.title,
                            class: name_str,
                            sourceCode: data_json.directive_js,
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
                            icon: 'language-javascript'
                        });
                    }
                    else if (name_str === "SlaveViewController") {
                        treeDataOld[2].nodes.push({
                            id: id_int,
                            parentIndex: 2,
                            index: treeDataOld[2].nodes.length,
                            name: data_json.name + '|controller_js',
                            title: data_json.title + '|controller_js',
                            class: name_str,
                            sourceCode: data_json.controller_js,
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
                            icon: 'angularjs'
                        });
                        treeDataOld[2].nodes.push({
                            id: id_int,
                            parentIndex: 2,
                            index: treeDataOld[2].nodes.length,
                            name: data_json.name + '|view_html',
                            title: data_json.title + '|view_html',
                            class: name_str,
                            sourceCode: data_json.view_html,
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
                            icon: 'language-javascript'
                        });
                    }


                    $log.info("asyncREST - " + "/krogoth_gantry/viewsets/" + name_str + "/" + id_int + "/");
                    var r = [treeDataOld, finishedRESTfulResponses];
                    deferred.resolve(r);
                }, function errorCallback(response) {
                    deferred.reject(response);
                });
                return deferred.promise;
            };
        }

        return service;
    }
})();