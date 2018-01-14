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

        const tMaste = 0;
        const tStyle = 1;
        const tSlave = 2;
        const tDirec = 3;
        const tServi = 4;
        const tXHTML = 5;
        const tXtrJS = 6;

        vm.$onInit = onInit;
        vm.getListView = getListView;
        vm.putObject = putObject;


        vm.editable = 'hello, click this';
        vm.updateName = updateName;
        vm.updateTitle = updateTitle;
        vm.selectListItem = selectListItem;

        vm.selectedMaster = 0;

        vm.treeData = [];

        function onInit() {
            vm.selectedMaster = $state.params.masterId;
            vm.getListView();
            vm.populateTreeRoots();
        }

        vm.populateTreeRoots = populateTreeRoots;

        function populateTreeRoots() {
            var master = {id: tMaste, title: ' Master Views', nodes: [], canRemove: false, canEdit: false};
            var styles = {id: tStyle, title: ' CSS', nodes: [], canRemove: false, canEdit: false};
            var slaves = {id: tSlave, title: ' Slave Views', nodes: [], canRemove: false, canEdit: false};
            var direct = {id: tDirec, title: ' Directives', nodes: [], canRemove: false, canEdit: false};
            var servic = {id: tServi, title: ' Services', nodes: [], canRemove: false, canEdit: false};
            var xtHTML = {id: tXHTML, title: ' HTML Templates', nodes: [], canRemove: false, canEdit: false};
            var xtraJS = {id: tXtrJS, title: ' JavaScript Templates', nodes: [], canRemove: false, canEdit: false};
            vm.treeData.push(master);
            vm.treeData.push(styles);
            vm.treeData.push(slaves);
            vm.treeData.push(direct);
            vm.treeData.push(servic);
            vm.treeData.push(xtHTML);
            vm.treeData.push(xtraJS);
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
        vm.loadFileIntoEditor = loadFileIntoEditor;

        vm.mostRecentRESTfulCall = '';

        function getListView() {
            //var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/MasterViewController/' + vm.selectedMaster + '/'
            }).then(function successCallback(response) {
                /// Success
                //deferred.resolve(response.data);
                vm.mostRecentRESTfulCall = '/krogoth_gantry/viewsets/MasterViewController/' + vm.selectedMaster + '/';
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
                    /// add all directives, services and slaves into RAM:
                    for (var i = 0; i < array.length; i++) {
                        var id_in = array[i];
                        $log.log('for service in services_array ' + i + ' ' + array[i]);
                        if (className === 'SlaveViewController') {
                            vm.pendingRESTfulRequests.push({'class': 'SlaveViewController', 'id': id_in});
                        }

                        else if (className === 'Directive') {
                            vm.pendingRESTfulRequests.push({'class': 'Directive', 'id': id_in});
                        }

                        else {
                            vm.pendingRESTfulRequests.push({'class': 'Service', 'id': id_in});
                        }
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

        vm.appendKrogothComponent = appendKrogothComponent;

        /// Load components into RAM I:
        function appendKrogothComponent(name_str, id_int, data_json) {
            vm.finishedRESTfulResponses.push(data_json);
            if (name_str === 'Service')
                vm.treeData[tServi].nodes.push(
                    {
                        id: id_int,
                        name: data_json.name,
                        title: data_json.title,
                        class: name_str,
                        nodes: [],
                        canRemove: true,
                        canEdit: true
                    }
                );
            else if (name_str === 'Directive')
                vm.treeData[tDirec].nodes.push(
                    {
                        id: id_int,
                        name: data_json.name,
                        title: data_json.title,
                        class: name_str,
                        nodes: [],
                        canRemove: true,
                        canEdit: true
                    }
                );
            else if (name_str === 'SlaveViewController')
                vm.treeData[tSlave].nodes.push(
                    {
                        id: id_int,
                        name: data_json.name,
                        title: data_json.title,
                        class: name_str,
                        nodes: [],
                        canRemove: true,
                        canEdit: true
                    }
                );
        }

        var asyncREST = function (id, className) {
            return function () {
                var deferred = $q.defer();

                $http({
                    method: 'GET',
                    url: '/krogoth_gantry/viewsets/' + className + '/' + id + '/'
                }).then(function successCallback(response) {
                    vm.appendKrogothComponent(className, id, response.data);
                    $log.info('- - -');
                    $log.log(response.data);
                    vm.mostRecentRESTfulCall = '/krogoth_gantry/viewsets/' + className + '/' + id + '/';
                    deferred.resolve();
                }, function errorCallback(response) {
                    deferred.reject(response);
                });

                return deferred.promise;
            }
        };

        function AKEditorComponentMaster(_class) {
            this.id = vm.objectList.id;
            this.name = vm.objectList.name;
            this.title = _class;
            this.class = _class;
            this.nodes = [];
            this.canRemove = false;
            this.canEdit = true;
            this.isMaster = true;
        }

        AKEditorComponentMaster.prototype.sourceCode = function (cls) {
            if (cls === 'ViewHTML') return vm.objectList.view_html;
            else if (cls === 'ModuleJS') return vm.objectList.module_js;
            else if (cls === 'ControllerJS') return vm.objectList.controller_js;
            else if (cls === 'StyleCSS') return vm.objectList.style_css;
            else if (cls === 'ThemeCSS') return vm.objectList.themestyle;
            else return 'ERROR';
        };

        AKEditorComponentMaster.prototype.propertyName = function (cls) {
            if (cls === 'ViewHTML') return vm.objectList.view_html;
            else if (cls === 'ModuleJS') return vm.objectList.module_js;
            else if (cls === 'ControllerJS') return vm.objectList.controller_js;
            else if (cls === 'StyleCSS') return vm.objectList.style_css;
            else if (cls === 'ThemeCSS') return vm.objectList.themestyle;
            else if (cls === 'Service') return vm.objectList.service_js;
            else if (cls === 'Directive') return vm.objectList.directive_js;
            else if (cls === 'SlaveView') return vm.objectList.view_html;
            else if (cls === 'SlaveCtrl') return vm.objectList.controller_js;
            else return 'ERROR';
        };

        /// Load components into RAM II:
        function parallelRESTfulCompleted() {
            const moduleJS = new AKEditorComponentMaster('ViewHTML');
            const ctrlJS = new AKEditorComponentMaster('ModuleJS');
            const viewHTML = new AKEditorComponentMaster('ControllerJS');
            const styleCSS = new AKEditorComponentMaster('StyleCSS');
            const themestyleCSS = new AKEditorComponentMaster('ThemeCSS');
            vm.treeData[tMaste].nodes.push(moduleJS);
            vm.treeData[tMaste].nodes.push(ctrlJS);
            vm.treeData[tMaste].nodes.push(viewHTML);
            vm.treeData[tStyle].nodes.push(styleCSS);
            vm.treeData[tStyle].nodes.push(themestyleCSS);
            vm.messages.push('all done: parallelRESTfulCompleted');
        }

        vm.RESTfulUpdateEndpoint = {};
        function loadFileIntoEditor(id_int, type_str) {
            // var doc;
            $log.info('Loading File Into Editor: ');
            $log.log('type_str: ' + type_str);
            $log.log('id_int: ' + id_int);

            if (type_str === 'ViewHTML' || type_str === 'ModuleJS' || type_str === 'ControllerJS' ||
                type_str === 'StyleCSS' || type_str === 'ThemeCSS')
            {
                var code = new AKEditorComponentMaster(type_str);
                vm.editorModel.doc.setValue(code.sourceCode(type_str));
                vm.RESTfulUpdateEndpoint.uri = '/krogoth_gantry/viewsets/MasterViewController/' + id_int + '/';
            }

            for (var i = 0; i < vm.finishedRESTfulResponses.length; i++) {
                const itemIn = vm.finishedRESTfulResponses[i];
                $log.log('itemIn: ');
                $log.debug(itemIn);
                if (itemIn.id === id_int) {
                    if (type_str === 'Service') {
                        vm.editorModel.doc.setValue(itemIn.service_js);
                        vm.RESTfulUpdateEndpoint.uri = '/krogoth_gantry/viewsets/' + type_str + '/' + id_int + '/';
                        break;
                    }
                    else if (type_str === 'Directive') {
                        vm.editorModel.doc.setValue(itemIn.directive_js);
                        vm.RESTfulUpdateEndpoint.uri = '/krogoth_gantry/viewsets/' + type_str + '/' + id_int + '/';
                        break;
                    }
                    else if (type_str === 'SlaveCtrl') {
                        vm.editorModel.doc.setValue(itemIn.controller_js);
                        vm.RESTfulUpdateEndpoint.uri = '/krogoth_gantry/viewsets/' + type_str + '/' + id_int + '/';
                        break;
                    }
                    else if (type_str === 'SlaveView') {
                        vm.editorModel.doc.setValue(itemIn.view_html);
                        vm.RESTfulUpdateEndpoint.uri = '/krogoth_gantry/viewsets/' + type_str + '/' + id_int + '/';
                        break;
                    }
                }
            }
            // vm.editorModel.doc.setValue(doc);
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


    }
})();