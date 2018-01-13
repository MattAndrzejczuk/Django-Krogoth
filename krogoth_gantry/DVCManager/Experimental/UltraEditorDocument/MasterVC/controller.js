(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu, DjangularEditorRESTfulII, $q) {
        var vm = this;


        // Master View Controller Setup
        vm.codemirrorLoaded = codemirrorLoaded;
        vm.editorModel = {};
        vm.objectList = {};
        vm.messages = [];


        vm.$onInit = onInit;
        vm.getListView = getListView;
        vm.putObject = putObject;


        vm.editable = 'hello, click this';
        vm.updateName = updateName;
        vm.updateTitle = updateTitle;
        vm.selectListItem = selectListItem;

        vm.selectedMaster = 0;


        function onInit() {
            vm.selectedMaster = $state.params.masterId;
            vm.getListView();
        }


        function updateName(tile) {
            vm.putCatagory(tile);
        }

        function updateTitle(tile) {
            vm.putCatagory(tile);
        }

        vm.servicesPendingRequest = [];
        vm.directivesPendingRequest = [];
        vm.slavesPendingRequest = [];

        function getListView() {
            //var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/MasterViewController/' + vm.selectedMaster + '/'
            }).then(function successCallback(response) {
                /// Success
                //deferred.resolve(response.data);
                vm.objectList = response.data;
                vm.editorModel.doc.setValue(response.data.controller_js);

                /// for service in services_array
                for (var i = 0; i < response.data.djangular_service.length; i++) {
                    var item_in = response.data.djangular_service[i];
                    vm.servicesPendingRequest.push(item_in);
                }

                /// for service in services_array
                for (var i = 0; i < response.data.djangular_directive.length; i++) {
                    var item_in = response.data.djangular_directive[i];
                    vm.directivesPendingRequest.push(item_in);
                }

                /// for service in services_array
                for (var i = 0; i < response.data.djangular_slave_vc.length; i++) {
                    var item_in = response.data.djangular_slave_vc[i];
                    vm.slavesPendingRequest.push(item_in);
                }

            }, function errorCallback(response) {
                /// Fail
                //deferred.reject(response);
            });
            //return deferred.promise;
        }


        vm.parallelRESTfulStart = parallelRESTfulStart;

        function parallelRESTfulStart() {

            var cpuTask1 = async(vm.servicesPendingRequest, 'Service')();
            var cpuTask2 = async(vm.directivesPendingRequest, 'Directive')();
            var cpuTask3 = async(vm.slavesPendingRequest, 'SlaveViewController')();

            $q.all([cpuTask1,
                cpuTask2,
                cpuTask3])
                .then(vm.parallelRESTfulReady, vm.parallelRESTfulAbort);
        }

        vm.parallelRESTfulReady = parallelRESTfulReady;
        vm.parallelRESTfulAbort = parallelRESTfulAbort;

        vm.parallelRESTfulCompleted = parallelRESTfulCompleted;
        vm.parallelRESTfulServerError = parallelRESTfulServerError;

        function parallelRESTfulReady() {
            var threads = [];
            vm.messages.push('all done: parallelRESTfulReady');
            for (var i = 0; i < vm.pendingRESTfulRequests.length; i++) {
                var request_in = vm.pendingRESTfulRequests[i];
                var cpuTaskX;
                cpuTaskX = asyncREST(request_in.id, request_in.class)();
                threads.push(cpuTaskX);
            }
            $q.all(threads)
                .then(vm.parallelRESTfulCompleted, vm.parallelRESTfulServerError);
        }

        function parallelRESTfulAbort() {
            vm.messages.push('something failed: parallelRESTfulAbort');
        }

        vm.pendingRESTfulRequests = [];
        vm.finishedRESTfulResponses = [];

        var async = function (array, className) {
            return function () {
                var deferred = $q.defer();
                $log.log('loop did start...');
                try {
                    /// for service in services_array
                    for (var i = 0; i < array.length; i++) {
                        var id_in = array[i];
                        $log.log('for service in services_array ' + i + ' ' + array[i]);
                        if (className === 'SlaveViewController')
                            vm.pendingRESTfulRequests.push({'class': 'SlaveViewController', 'id': id_in});
                        else if (className === 'Directive')
                            vm.pendingRESTfulRequests.push({'class': 'Directive', 'id': id_in});
                        else
                            vm.pendingRESTfulRequests.push({'class': 'Service', 'id': id_in});
                    }
                    deferred.resolve();
                }
                catch (ex) {
                    vm.messages.push(ex);
                    deferred.reject();
                }

                return deferred.promise;
            }
        };


        var asyncREST = function (id, className) {
            return function () {
                var deferred = $q.defer();

                $http({
                    method: 'GET',
                    url: '/krogoth_gantry/viewsets/' + className + '/' + id + '/'
                }).then(function successCallback(response) {
                    deferred.resolve();
                    vm.finishedRESTfulResponses.push(response.data);
                }, function errorCallback(response) {
                    deferred.reject(response);
                });

                return deferred.promise;
            }
        };

        function parallelRESTfulCompleted() {
            vm.messages.push('all done: parallelRESTfulCompleted');
        }

        function parallelRESTfulServerError() {
            vm.messages.push('something failed: parallelRESTfulServerError');
        }


        function putObject(instance) {
            //var deferred = $q.defer();
            $http({
                method: 'PUT',
                data: instance,
                url: '/krogoth_gantry/viewsets/MasterViewController/' + instance.id + '/'
            }).then(function successCallback(response) {
                //deferred.resolve(response.data);
                vm.masters = response.data;
            }, function errorCallback(response) {
                //deferred.reject(response);
            });
            //return deferred.promise;
        }


        function selectListItem(id) {
            $state.go('app.FUSE_APP_NAME.slave', {'categoryId': id});

        }


        function codemirrorLoaded(_editor) {
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function () {
                $log.log('beforeChange');
            });
            _editor.on("change", function () {
                $log.log('change');
            });
            vm.editorModel = _editor;
        }


        vm.editorOptions = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'javascript',
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };
        ////// -----------


        vm.remove = remove;
        vm.toggle = toggle;
        vm.moveLastToTheBeginning = moveLastToTheBeginning;
        vm.newSubItem = newSubItem;


        function remove(scope) {
            scope.remove();
        }

        function toggle(scope) {
            scope.toggle();
        }

        function moveLastToTheBeginning() {
            var a = vm.data.pop();
            vm.data.splice(0, 0, a);
        }

        function newSubItem(scope) {
            var nodeData = scope.$modelValue;
            nodeData.nodes.push({
                id: nodeData.id * 10 + nodeData.nodes.length,
                title: nodeData.title + '.' + (nodeData.nodes.length + 1),
                nodes: []
            });
        }


        vm.data = [{
            'id': 1,
            'title': 'node1',
            'nodes': [{
                'id': 11,
                'title': 'node1.1',
                'nodes': [{
                    'id': 111,
                    'title': 'node1.1.1',
                    'nodes': []
                }]
            }, {
                'id': 12,
                'title': 'node1.2',
                'nodes': []
            }]
        }, {
            'id': 2,
            'title': 'node2',
            'nodrop': true, // An arbitrary property to check in custom template for nodrop-enabled
            'nodes': [{
                'id': 21,
                'title': 'node2.1',
                'nodes': []
            }, {
                'id': 22,
                'title': 'node2.2',
                'nodes': []
            }]
        }, {
            'id': 3,
            'title': 'node3',
            'nodes': [{
                'id': 31,
                'title': 'node3.1',
                'nodes': []
            }]
        }];

    }
})();