(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu,
        TemplateCRUD, DirectiveCRUD,
        $q, AKClassEditorComponent, UltraEditorDefaults, GatherURIsAsync, fileNameChanger, $mdDialog,
        BatchRequestsAsync, SaveToSQL, $mdSidenav, BreadCrumbsIDE, $timeout, codeHighlightIDE) {
        var vm = this;

        vm.codemirrorLoaded = codemirrorLoaded;
        vm.hideTreeDataModal = true;

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



        /// I.
        function onInit() {
            vm.selectedMaster = $state.params.masterId;
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

        vm.customThemeMode = false;
        vm.setThemeBasedOnClass = setThemeBasedOnClass;

        /*  ⚡️  */
        function loadFileIntoEditor(parentIndex, index, scope) {
            vm.unsavedChangesExist = -1;
            if (vm.editorLoadedFirstDoc === true) {
                vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].sourceCode = vm.editorModel.doc.getValue();
            }
            vm.editorLoadedFirstDoc = true;
            vm.editorModel.doc.setValue(vm.treeData[parentIndex].nodes[index].sourceCode);
            vm.unsavedChangesExist = -1;
            vm.loadedIndex = index;
            vm.loadedParentIndex = parentIndex;

            const syntax = vm.treeData[parentIndex].nodes[index].syntax;
            const _class = vm.treeData[parentIndex].nodes[index].class;
            vm.editorModel.setOption("mode", syntax);

            if (vm.customThemeMode === false) {
                vm.setThemeBasedOnClass(_class);
            }
        }

        vm.editorOptions = {
            lineWrapping: true,
            lineNumbers: true,
            mode: "javascript",
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };

        function setThemeBasedOnClass(_class) {
            if (_class === "ViewHTML") {
                vm.editorModel.setOption("theme", "dracula");
            } else if (_class === "ControllerJS") {
                vm.editorModel.setOption("theme", "colorforth");
            } else if (_class === "ModuleJS") {
                vm.editorModel.setOption("theme", "night");
            } else if (_class === "StyleCSS") {
                vm.editorModel.setOption("theme", "icecoder");
            } else if (_class === "ThemeCSS") {
                vm.editorModel.setOption("theme", "vibrant-ink");
            } else if (_class === "Service") {
                vm.editorModel.setOption("theme", "3024-night");
            } else {
                vm.editorModel.setOption("theme", "isotope");
            }
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
                    vm.setBrowserTabEditMode(false);
                    $mdToast.show(
                        $mdToast.simple()
                        .textContent('Document Saved.')
                        .position('top right')
                        .hideDelay(2000)
                    );
                });
        }





        /// <PROCESS RESPONSE INTO RAM III. > 💚

        vm.unsavedChangesExist = -1;

        function editorContentWillChange() {
            $log.info('unsavedChangesExist ' + vm.unsavedChangesExist);
        }

        function editorContentDidChange() {
            if (vm.loadedParentIndex !== -1 && vm.loadedIndex !== -1)
                if (vm.unsavedChangesExist === 0) {
                    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].hasUnsavedChanges = true;
                    vm.setBrowserTabEditMode(true);
                }
            vm.unsavedChangesExist += 1;
        }

        function parallelRESTfulServerError() {
            vm.messages.push("something failed: parallelRESTfulServerError");
        }

        vm.startStateTransition = startStateTransition;

        function startStateTransition(stateName, cargo) {
            $log.info("-=-=-=- Changing State  🌀    -=-=-=-");
            $log.info("-=-       " + stateName);
            $log.debug(cargo);
            $log.info("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-");
            $state.go(stateName, cargo);
        }


        function selectListItem(id) {
            const destination = "app.FUSE_APP_NAME.slave";
            const cargo = {
                "categoryId": id
            };
            vm.startStateTransition(destination, cargo);
        }

        function goBackToCategory() {
            const destination = "app.UltraEditorSubCategory.slave";
            const cargo = {
                'categoryId': vm.finishedBreadCrumbsJson._1st.id,
                'childId': vm.finishedBreadCrumbsJson._2nd.id
            };
            vm.startStateTransition(destination, cargo);
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

        vm.browserTabEmoji = " 🔨 ";
        vm.browserTabText = "Krogoth Editor";
        vm.setBrowserTabText = setBrowserTabText;
        vm.setBrowserTabEditMode = setBrowserTabEditMode;

        function buildBreadCrumbs() {
            BreadCrumbsIDE.cookBread($state.params.categoryId, $state.params.subCategoryId, $state.params.masterId)
                .then(function(finishedBread) {
                    vm.finishedBreadCrumbsJson._1st = finishedBread[0];
                    vm.finishedBreadCrumbsJson._2nd = finishedBread[1];
                    vm.finishedBreadCrumbsJson._3rd = finishedBread[2];
                    var changeTabTitle = document.getElementById("browser_tab_text");
                    $log.log(finishedBread[2]);
                    changeTabTitle.innerHTML = " 🔨 " + vm.objectList.name;
                })
        }

        function setBrowserTabText(newText) {
            vm.browserTabText = newText;
            var changeTabTitle = document.getElementById("browser_tab_text");
            changeTabTitle.innerHTML = vm.browserTabEmoji + vm.browserTabText;
        }

        function setBrowserTabEditMode(isActive) {
            var changeTabTitle = document.getElementById("browser_tab_text");
            vm.browserTabEmoji = " 🛠 ";
            changeTabTitle.innerHTML = vm.browserTabEmoji + vm.browserTabText;

            if (isActive === true)
                $timeout(function() {
                    vm.browserTabEmoji = " 🔨 ";
                    changeTabTitle.innerHTML = vm.browserTabEmoji + vm.browserTabText;
                    $timeout(function() {
                        vm.browserTabEmoji = " 🛠 ";
                        changeTabTitle.innerHTML = vm.browserTabEmoji + vm.browserTabText;
                    }, 500);
                }, 500);

            if (isActive === false) {
                vm.browserTabEmoji = " ✅ ";
                changeTabTitle.innerHTML = vm.browserTabEmoji + vm.browserTabText;
                $timeout(function() {
                    vm.browserTabEmoji = " 🔨 ";
                    changeTabTitle.innerHTML = vm.browserTabEmoji + vm.browserTabText;
                }, 500);
            }
        }



        function toggleSidenav(sidenavId) {
            $mdSidenav(sidenavId).toggle();
        }

        vm.highlightSyntax = highlightSyntax;
        vm.highlightSyntaxGetHtmlProperties = highlightSyntaxGetHtmlProperties;


        function highlightSyntax() {
            var lineCount = vm.editorModel.getDoc().lineCount();
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/Controller/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('Controller', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 10
                    }, {
                        "css": "color : #A459FF; font-weight:bold;"
                    });
                }
            }
        }


        function highlightSyntaxGetHtmlProperties() {
            codeHighlightIDE.colorNgClick1(vm.editorModel)
                .then(function(coloredEditorModel) {
                    vm.editorModel = coloredEditorModel;
                });
        }



        vm.loadOSXDoc = loadOSXDoc;
        vm.treeModalIsVisible = false;
        vm.simplifiedTreeData = [];

        function loadOSXDoc() {
            vm.treeModalIsVisible = !vm.treeModalIsVisible;
            const backup = vm.treeData;
            vm.simplifiedTreeData = backup;
            for (var i = 0; i < vm.simplifiedTreeData.length; i++) {
                const nodeInRoot = vm.simplifiedTreeData[i];
                $log.debug(nodeInRoot);
                for (var j = 0; j < nodeInRoot.nodes.length; j++) {
                    /// const nodeInCat = nodeInRoot[j];
                    vm.simplifiedTreeData[i].nodes[j].sourceCode = "NAN";
                }
            }
        }

        vm.renameObjectForm = {};
        vm.renameObjectSubmit = renameObjectSubmit;

        function renameObjectSubmit() {
            const _0 = vm.finishedBreadCrumbsJson._1st.name;
            const _1 = vm.finishedBreadCrumbsJson._2nd.name;
            const _2 = vm.objectList.name;
            fileNameChanger.renameService(_0,
                    _1,
                    _2,
                    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name,
                    vm.renameObjectForm.new)
                .then(function(didFinish) {
                    $log.debug("The rename service operation finished on the server.");
                    $log.debug(didFinish);
                    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].name = vm.renameObjectForm.new;
                    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].title = vm.renameObjectForm.new;
                    vm.renameObjectForm.new = "";
                    /// success
                });
        }


        /* ⬇︎ ⬇︎ ⬇︎ RELOCATE ME TO A SEPARATE SERVICE ⬇︎ ⬇︎ ⬇︎ */

        function createNewComponentClick(ev, treeRoot) {
            var siblings = treeRoot.nodes;

            var djangoModelName = (treeRoot.class);
            ///var djangoModelName = SaveToSQL.getRESTfulModelName(treeRoot.class);

            $log.debug('---createNewComponentClick---');
            $log.log("treeRoot: ");
            $log.log(treeRoot);
            $log.debug('TODO FINISH THIS PART ! ! !');

            var confirm = $mdDialog.prompt()
                .title('Create new ' + djangoModelName)
                .textContent('Unique ' + djangoModelName + ' file name:')
                .placeholder(djangoModelName + '.js')
                .ariaLabel('Unique ' + djangoModelName + ' file name:')
                .initialValue('')
                .targetEvent(ev)
                .ok('Ok')
                .cancel('Cancel');
            $mdDialog.show(confirm).then(function(new_name) {

                const postPayload = {
                    "path_0": vm.finishedBreadCrumbsJson._1st.name,
                    "path_1": vm.finishedBreadCrumbsJson._2nd.name,
                    "master_name": vm.objectList.name,
                    "index": treeRoot.nodes.length,
                    "new_name": new_name
                };

                if (djangoModelName === "Directive") {
                    DirectiveCRUD.createDirective(postPayload)
                        .then(function(newTreeNode) {
                            $log.log("CREATE FINISHED");
                            $log.debug(newTreeNode);
                            const parentI = newTreeNode.parentIndex;
                            vm.treeData[parentI].nodes.push(newTreeNode);
                        });

                } else if (djangoModelName === "Service") {
                    fileNameChanger.createService(postPayload)
                        .then(function(newTreeNode) {
                            $log.log("CREATE FINISHED");
                            $log.debug(newTreeNode);
                            const parentI = newTreeNode.parentIndex;
                            vm.treeData[parentI].nodes.push(newTreeNode);
                        });

                } else if (treeRoot.title === "HTML Templates") {

                    TemplateCRUD.createTemplate(postPayload)
                        .then(function(newTreeNode) {
                            $log.log("CREATE FINISHED");
                            $log.debug(newTreeNode);
                            const parentI = newTreeNode.parentIndex;
                            vm.treeData[parentI].nodes.push(newTreeNode);
                        });
                }


            }, function() {});


        }

        function addNewComponentToMaster(siblings, newNode, djangoModelName, masterId) {
            SaveToSQL.addSiblingToMaster(siblings, newNode, djangoModelName, masterId)
                .then(function(newNodeForTree) {
                    $log.debug('newNodeForTree:');
                    $log.log(newNodeForTree);
                    $log.debug('TODO FINISH THIS PART ! ! !');
                });
        }
        /* ⬆︎ ⬆︎ ⬆︎ RELOCATE ME TO A SEPARATE SERVICE ⬆︎ ⬆︎ ⬆︎ */

    }
})();