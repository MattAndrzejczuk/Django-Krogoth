/* 

save changes to filesystem using URL:


 [ GET ]

 /krogoth_admin/SaveSQLToFileSystem/

...
*/


(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu,
        TemplateCRUDClone01, DirectiveCRUDClone01, syntaxAnalyzePropertiesVMClone01,
        $q, AKClassEditorComponentClone01, UltraEditorDefaultsClone01, GatherURIsAsyncClone01, fileNameChangerClone01, $mdDialog,
        BatchRequestsAsyncClone01, SaveToSQLClone01, $mdSidenav, BreadCrumbsIDEClone01, $timeout, codeHighlightIDEClone01) {
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
        vm.createFirstTreeNodes = createFirstTreeNodes;
        vm.getKrogothCoreParts = getKrogothCoreParts;
        vm.loadFileIntoEditor = loadFileIntoEditor;
        vm.editorContentWillChange = editorContentWillChange;
        vm.editorContentDidChange = editorContentDidChange;
        vm.customThemeMode = false;
        vm.setThemeBasedOnClass = setThemeBasedOnClass;
        vm.saveEditorWorkToServer = saveEditorWorkToServer;
        vm.setBrowserTabEditMode = setBrowserTabEditMode;
        vm.toggleSidenav = toggleSidenav;
        vm.sideNavLocked = true;
        vm.beautifyCode = beautifyCode;
        vm.loadOSXDoc = loadOSXDoc;
        vm.treeModalIsVisible = false;
        vm.simplifiedTreeData = [];
        vm.toggleFolder = toggleFolder;

        /*

        vm.selectListItem = selectListItem;
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
        vm.loadedParentIndex = 7;

        vm.editorLoadedFirstDoc = false;
        vm.reloadData = reloadData;

        vm.createNewComponentClick = createNewComponentClick;
        vm.addNewComponentToMaster = addNewComponentToMaster;


        vm.getTemplatesHTML = getTemplatesHTML;

        vm.goBackToCategory = goBackToCategory;

        ///vm.buildBreadCrumbs = buildBreadCrumbs;
*/
        vm.goBackToExplorerHome = goBackToExplorerHome


        /// I.
        function onInit() {
            $log.log("\n 🔵 onInit() \n");
            vm.selectedMaster = $state.params.masterId;
            vm.createFirstTreeNodes();
            ///vm.buildBreadCrumbs();
        }

        function createFirstTreeNodes() {
            $log.log("\n 🔵 createFirstTreeNodes() \n");
            UltraEditorDefaultsClone01.populateBoilerplate(vm.selectedMaster).then(function(treeData) {
                vm.treeData = treeData;
                vm.getKrogothCoreParts();
            });
        }

        function getKrogothCoreParts() {
            $log.log("\n 🔵 getKrogothCoreParts() \n");
            AKClassEditorComponentClone01.loadKrogothCoreList()
                .then(function(nodesForTree) {
                    vm.treeData[7].nodes = nodesForTree;
                });
        }

        function loadFileIntoEditor(parentIndex, index, scope) {
            $log.log("\n 🔵 loadFileIntoEditor( \n");
            vm.unsavedChangesExist = -1;
            vm.loadedIndex = index;
            vm.loadedParentIndex = parentIndex;

            if (vm.editorLoadedFirstDoc === true) {
                vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].sourceCode = vm.editorModel.doc.getValue();
            }
            vm.editorLoadedFirstDoc = true;
            vm.editorModel.doc.setValue(vm.treeData[parentIndex].nodes[index].sourceCode);
            vm.unsavedChangesExist = -1;


            const syntax = vm.treeData[parentIndex].nodes[index].syntax;
            const _class = vm.treeData[parentIndex].nodes[index].class;
            vm.editorModel.setOption("mode", syntax);

            if (vm.customThemeMode === false) {
                vm.setThemeBasedOnClass(_class);
            }
        }

        function setThemeBasedOnClass(_class) {
            $log.log("\n 🔵 setThemeBasedOnClass( \n");
            if (_class === "ViewHTML") {
                vm.editorModel.setOption("theme", "ambiance");
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


        function saveEditorWorkToServer(parentIndex, index, node) {
            $log.log("\n 🔵 saveEditorWorkToServer( \n");
            SaveToSQLClone01.saveDocument(node, vm.treeData[parentIndex].nodes[index].sourceCode)
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
            $log.log("\n 🔵 editorContentWillChange( \n");
            $log.info('unsavedChangesExist ' + vm.unsavedChangesExist);
        }

        function editorContentDidChange() {
            $log.log("\n 🔵 editorContentDidChange( \n");
            if (vm.loadedParentIndex !== -1 && vm.loadedIndex !== -1)
                if (vm.unsavedChangesExist === 0) {
                    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].hasUnsavedChanges = true;
                    vm.setBrowserTabEditMode(true);
                }
            vm.unsavedChangesExist += 1;
        }


        function setBrowserTabEditMode(isActive) {
            $log.log("\n 🔵 setBrowserTabEditMode( \n");
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
            $log.log("\n 🔵 toggleSidenav( \n");
            $mdSidenav(sidenavId).toggle();
        }

        vm.editorOptions = {
            lineWrapping: true,
            lineNumbers: true,
            mode: "javascript",
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };



        function codemirrorLoaded(_editor) {

            $log.log("\n 🔵 codemirrorLoaded( \n");
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



        function loadOSXDoc() {
            $log.log("\n 🔵 loadOSXDoc( \n");

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



        function toggleFolder(scope) {
            $log.log("\n 🔵 toggleFolder( \n");
            scope.toggle();
        }

        function beautifyCode() {
            $log.log("\n 🔵 beautifyCode( \n");
            vm.editorModel.execCommand("indentAuto");
        }

        function goBackToExplorerHome() {
            $log.log("\n 🔵 goBackToExplorerHome( \n");
            $state.go('app.UltraEditorBrowse');
        }

    }
})();