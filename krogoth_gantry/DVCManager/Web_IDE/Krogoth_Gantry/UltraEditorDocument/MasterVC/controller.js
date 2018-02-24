(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu,
        $q, AKClassEditorComponent, UltraEditorDefaults, GatherURIsAsync,
        BatchRequestsAsync, SaveToSQL, $mdSidenav, untitledServiceIDE01, BreadCrumbsIDE) {
        var vm = this;

        vm.codemirrorLoaded = codemirrorLoaded;

        const tMaste = 0;
        const tStyle = 1;
        const tSlave = 2;
        const tDirec = 3;
        const tServi = 4;
        const tXHTML = 5;
        const tXtrJS = 6;

        vm.$onInit = onInit;
        vm.getMasterViewCtrlDetail = getMasterViewCtrlDetail;

        vm.editorContentWillChange = editorContentWillChange;
        vm.editorContentDidChange = editorContentDidChange;

        vm.selectListItem = selectListItem;
        vm.loadFileIntoEditor = loadFileIntoEditor;
        vm.parallelRESTfulStart = parallelRESTfulStart;


        /// REQUEST ALL DATA II.  💛
        vm.finishedRESTfulResponses = [];
        vm.parallelRESTfulReady = parallelRESTfulReady;
        vm.parallelRESTfulAbort = parallelRESTfulAbort;
        vm.parallelRESTfulCompleted = parallelRESTfulCompleted;
        vm.parallelRESTfulServerError = parallelRESTfulServerError;

        // Master View Controller Setup
        vm.selectedMaster = 0;
        vm.treeData = [];
        vm.editorModel = {};
        vm.objectList = {};
        vm.messages = [];
        vm.finishedRESTfulResponses = [];
        vm.newComponentForm = {};
        vm.dumpNode = {};
        vm.servicesPendingRequest = [];
        vm.directivesPendingRequest = [];
        vm.slavesPendingRequest = [];
        vm.pendingRESTfulRequests = [];
        vm.loadedIndex = -1;
        vm.loadedParentIndex = -1;

        vm.editorLoadedFirstDoc = false;
        vm.reloadData = reloadData;
        vm.saveEditorWorkToServer = saveEditorWorkToServer;
        vm.createNewComponentClick = createNewComponentClick;
        vm.addNewComponentToMaster = addNewComponentToMaster;

        vm.createFirstTreeNodes = createFirstTreeNodes;
        vm.getKrogothCoreParts = getKrogothCoreParts;
        vm.getTemplatesHTML = getTemplatesHTML;

        vm.goBackToCategory = goBackToCategory;
        vm.toggleSidenav = toggleSidenav;
        vm.buildBreadCrumbs = buildBreadCrumbs;
        vm.sideNavLocked = true;

        vm.editorOptions = {
            lineWrapping: true,
            lineNumbers: true,
            mode: "javascript",
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };

        /// I.
        function onInit() {
            vm.selectedMaster = $state.params.masterId;
            $log.debug('MASTER ID:');
            $log.debug('MASTER ID:');
            $log.debug('MASTER ID:');
            $log.debug('MASTER ID:');
            $log.log('|' + vm.selectedMaster + '|');
            vm.createFirstTreeNodes();
            vm.buildBreadCrumbs();
        }

        function reloadData() {
            vm.treeData = [];
            vm.editorModel = {};
            vm.objectList = {};
            vm.messages = [];
            vm.finishedRESTfulResponses = [];
            vm.newComponentForm = {};
            vm.dumpNode = {};
            vm.servicesPendingRequest = [];
            vm.directivesPendingRequest = [];
            vm.slavesPendingRequest = [];
            vm.pendingRESTfulRequests = [];
            vm.createFirstTreeNodes();
        }

        function createFirstTreeNodes() {
            UltraEditorDefaults.populateBoilerplate(vm.selectedMaster).then(function(treeData) {
                vm.treeData = treeData;
                vm.getMasterViewCtrlDetail();

            });
        }

        /// II.
        function getMasterViewCtrlDetail() {
            AKClassEditorComponent.loadMasterInitializer(vm.selectedMaster)
                .then(function(finishedProcess) {
                    vm.servicesPendingRequest = finishedProcess.services;
                    vm.directivesPendingRequest = finishedProcess.directives;
                    vm.slavesPendingRequest = finishedProcess.slaves;
                    vm.objectList = finishedProcess.objectList;
                    vm.getTemplatesHTML();
                    vm.getKrogothCoreParts();

                    /// III.
                    vm.parallelRESTfulStart();
                });
        }

        function getKrogothCoreParts() {
            AKClassEditorComponent.loadKrogothCoreList()
                .then(function(nodesForTree) {
                    vm.treeData[7].nodes = nodesForTree;
                });
        }

        function getTemplatesHTML() {
            AKClassEditorComponent.loadHTMLIncludeList(vm.objectList.name)
                .then(function(htmlTemps) {
                    $log.log("GOT THE NEW NG INCLUDE HTML TEMPLATES: ");
                    $log.info(htmlTemps);
                    vm.treeData[5].nodes = htmlTemps;
                });
        }

        /*   ⚡️   */
        function parallelRESTfulStart() {
            var cpuTask1 = GatherURIsAsync.async(vm.servicesPendingRequest, "Service")()
                .then(function(list) {
                    Array.prototype.push.apply(vm.pendingRESTfulRequests, list);
                });
            var cpuTask2 = GatherURIsAsync.async(vm.directivesPendingRequest, "Directive")()
                .then(function(list) {
                    Array.prototype.push.apply(vm.pendingRESTfulRequests, list);
                });
            var cpuTask3 = GatherURIsAsync.async(vm.slavesPendingRequest, "SlaveViewController")()
                .then(function(list) {
                    Array.prototype.push.apply(vm.pendingRESTfulRequests, list);
                });
            $q.all([cpuTask1,
                    cpuTask2,
                    cpuTask3
                ])
                .then(vm.parallelRESTfulReady, vm.parallelRESTfulAbort);
        }

        function parallelRESTfulAbort() {
            vm.messages.push("something failed: parallelRESTfulAbort");
        }

        /// 🧡 </INITIALIZATION I. >


        /// <REQUEST ALL DATA II. > 💛



        function parallelRESTfulReady() {
            var threads = [];
            vm.messages.push("all done: parallelRESTfulReady");
            for (var i = 0; i < vm.pendingRESTfulRequests.length; i++) {
                var request_in = vm.pendingRESTfulRequests[i];
                var cpuTaskX;
                cpuTaskX = BatchRequestsAsync.async(request_in.id, request_in.class, vm.treeData)()
                    .then(function(list) {
                        vm.treeData = list[0];
                        vm.finishedRESTfulResponses = list[1];
                    });
                threads.push(cpuTaskX);
            }
            $q.all(threads)
                .then(vm.parallelRESTfulCompleted, vm.parallelRESTfulServerError);
        }
        /// 💛 </REQUEST ALL DATA II. >


        /// <PROCESS RESPONSE INTO RAM III. > 💚
        function parallelRESTfulCompleted() {
            $log.log('vm.finishedRESTfulResponses ~ ~ ~ ~ ~ ~ ~  ~~  ~~ ~~ ');
            $log.log(vm.finishedRESTfulResponses);
            const moduleJS = new AKEditorComponentMaster(
                "ViewHTML",
                vm.treeData[tMaste].nodes.length,
                0,
                vm.objectList.view_html,
                'view_html',
                vm.treeData[tMaste].id,
                'htmlmixed',
                'language-html5'
            );
            vm.treeData[tMaste].nodes.push(moduleJS);
            const ctrlJS = new AKEditorComponentMaster(
                "ModuleJS",
                vm.treeData[tMaste].nodes.length,
                0,
                vm.objectList.module_js,
                'module_js',
                vm.treeData[tMaste].id,
                'javascript',
                'angular'
            );
            vm.treeData[tMaste].nodes.push(ctrlJS);
            const viewHTML = new AKEditorComponentMaster(
                "ControllerJS",
                vm.treeData[tMaste].nodes.length,
                0,
                vm.objectList.controller_js,
                'controller_js',
                vm.treeData[tMaste].id,
                'javascript',
                'angularjs'
            );
            vm.treeData[tMaste].nodes.push(viewHTML);
            const styleCSS = new AKEditorComponentMaster(
                "StyleCSS",
                vm.treeData[tStyle].nodes.length,
                1,
                vm.objectList.style_css,
                'style_css',
                vm.treeData[tStyle].id,
                'css',
                'language-css3'
            );
            vm.treeData[tStyle].nodes.push(styleCSS);
            const themestyleCSS = new AKEditorComponentMaster(
                "ThemeCSS",
                vm.treeData[tStyle].nodes.length,
                1,
                vm.objectList.themestyle,
                'themestyle',
                vm.treeData[tStyle].id,
                'css',
                'language-css3'
            );
            vm.treeData[tStyle].nodes.push(themestyleCSS);
        }


        // vvv REMOVE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        function AKEditorComponentMaster(_class, index, parentIndex, sourceCode, sourceKey, restId, syntax, icon) {
            this.id = -1;
            this.parentIndex = parentIndex;
            this.index = index;
            this.name = -1;
            this.title = _class;
            this.class = _class;
            this.sourceCode = sourceCode;
            this.sourceKey = sourceKey;
            this.nodes = [];
            this.canRemove = false;
            this.canEdit = true;
            this.isMaster = true;
            this.RESTfulId = restId;
            this.RESTfulURI = '/krogoth_gantry/viewsets/MasterViewController/' + restId + '/';
            this.hasUnsavedChanges = false;
            this.syntax = syntax;
            this.icon = icon;
        }
        // ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



        /*  ⚡️  */
        function loadFileIntoEditor(parentIndex, index, scope) {
            /*
            $log.info("PARENT INDEX: " + parentIndex);
            $log.info("INDEX: " + index);
            $log.info("SCOPE: ");
            $log.debug(scope);
            $log.info("TREE DATA: ");
            $log.debug(vm.treeData);
			*/
            vm.unsavedChangesExist = -1;
            if (vm.editorLoadedFirstDoc === true) {
                vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].sourceCode = vm.editorModel.doc.getValue();
            }
            vm.editorLoadedFirstDoc = true;
            vm.editorModel.doc.setValue(vm.treeData[parentIndex].nodes[index].sourceCode);
            vm.unsavedChangesExist = -1;
            vm.loadedIndex = index;
            vm.loadedParentIndex = parentIndex;
            vm.editorModel.setOption("mode", vm.treeData[parentIndex].nodes[index].syntax);

        }



        function saveEditorWorkToServer(node) {
            SaveToSQL.saveDocument(node, vm.editorModel.doc.getValue())
                .then(function(savedWork) {

                    var pi = node.parentIndex;
                    var ni = node.index;


                    vm.loadedParentIndex = pi;
                    vm.loadedIndex = ni;
                    var key = vm.treeData[pi].nodes[ni].sourceKey;
                    $log.info(key);
                    $log.info("HERE's OUR SAVED WORK: ");
                    $log.info(savedWork[key]);

                    if (savedWork[key]) {
                        vm.treeData[pi].nodes[ni].sourceCode = savedWork.sourceCode;
                    } else if (key === "contents") {
                        vm.treeData[pi].nodes[ni].sourceCode = savedWork;
                    } else {

                    }
                    ///vm.loadFileIntoEditor(pi, ni, node);
                    vm.treeData[pi].nodes[ni].hasUnsavedChanges = false;
                    vm.unsavedChangesExist = -1;
                    $mdToast.show(
                        $mdToast.simple()
                        .textContent('Document Saved.')
                        .position('top right')
                        .hideDelay(2000)
                    );
                });
        }


        function createNewComponentClick(treeRoot) {
            var siblings = treeRoot.nodes;
            const djangoModelName = SaveToSQL.getRESTfulModelName(treeRoot.class);
            SaveToSQL.createNew(treeRoot, 'testCreation')
                .then(function(newNode) {
                    vm.addNewComponentToMaster(siblings, newNode, djangoModelName, treeRoot.id);
                });
        }


        function addNewComponentToMaster(siblings, newNode, djangoModelName, masterId) {
            SaveToSQL.addSiblingToMaster(siblings, newNode, djangoModelName, masterId)
                .then(function(newNodeForTree) {
                    $log.debug('newNodeForTree:');
                    $log.log(newNodeForTree);
                    $log.debug('TODO FINISH THIS PART ! ! !');
                });
        }


        /// <PROCESS RESPONSE INTO RAM III. > 💚

        vm.unsavedChangesExist = -1;

        function editorContentWillChange() {
            $log.info('unsavedChangesExist ' + vm.unsavedChangesExist);
        }

        function editorContentDidChange() {
            if (vm.loadedParentIndex !== -1 && vm.loadedIndex !== -1)
                if (vm.unsavedChangesExist >= 0) {
                    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].hasUnsavedChanges = true;
                }
            vm.unsavedChangesExist += 1;
        }

        function parallelRESTfulServerError() {
            vm.messages.push("something failed: parallelRESTfulServerError");
        }


        function selectListItem(id) {
            $state.go("app.FUSE_APP_NAME.slave", {
                "categoryId": id
            });
        }

        function codemirrorLoaded(_editor) {
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption("firstLineNumber", 0);
            _editor.on("beforeChange", function() {
                vm.editorContentWillChange();
            });
            _editor.on("change", function() {
                vm.editorContentDidChange();
            });
            vm.editorModel = _editor;
        }

        function goBackToCategory() {
            $state.go('app.UltraEditorBrowse.slave', {
                'categoryId': vm.finishedBreadCrumbsJson._1st.id,
                'childId': vm.finishedBreadCrumbsJson._2nd.id
            });
        }

        ////// -----------

        vm.remove = remove;
        vm.toggleFolder = toggleFolder;
        vm.newSubItem = newSubItem;


        /*  ⚡️  */
        function remove(scope) {
            scope.remove();
        }

        /*  ⚡️  */
        function toggleFolder(scope) {
            scope.toggle();
        }


        /*  ⚡️  */
        function newSubItem(scope) {
            var nodeData = scope.$modelValue;
            nodeData.nodes.push({
                id: nodeData.id * 10 + nodeData.nodes.length,
                title: nodeData.title + '.' + (nodeData.nodes.length + 1),
                nodes: []
            });
        }

        vm.finishedBreadCrumbsJson = {};

        function buildBreadCrumbs() {
            BreadCrumbsIDE.cookBread($state.params.categoryId, $state.params.subCategoryId, $state.params.masterId)
                .then(function(finishedBread) {
                    vm.finishedBreadCrumbsJson._1st = finishedBread[0];
                    vm.finishedBreadCrumbsJson._2nd = finishedBread[1];
                    vm.finishedBreadCrumbsJson._3rd = finishedBread[2];
                })
        }

        function toggleSidenav(sidenavId) {
            $mdSidenav(sidenavId).toggle();
        }

    }
})();