/* 

save changes to filesystem using URL:


 [ GET ]

 /krogoth_gantry/SaveSQLToFileSystem/

...
*/


(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu, AKClassEditorComponentClone01,
        $q, UltraEditorDefaultsClone01, $mdDialog, SaveToSQLClone01, $mdSidenav, $timeout) {
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


        vm.getKrogothCorePartsSet1 = getKrogothCorePartsSet1;
        vm.getKrogothCorePartsSet2 = getKrogothCorePartsSet2;


        vm.goBackToExplorerHome = goBackToExplorerHome;


        vm.muted = false;


        /// I.
        function onInit() {
            $log.log("\n 🔵 onInit() \n");
            vm.selectedMaster = $state.params.masterId;
            vm.createFirstTreeNodes();
            vm.playSFX("startup");
            ///vm.buildBreadCrumbs();
        }

        function createFirstTreeNodes() {

            $log.log("\n 🔵 createFirstTreeNodes() \n");
            UltraEditorDefaultsClone01.populateBoilerplate(vm.selectedMaster).then(function(treeData) {
                vm.treeData = treeData;
                vm.getKrogothCorePartsSet1();
            });

        }

        function getKrogothCorePartsSet1() {
            $log.log("\n 🔵 getKrogothCorePartsSet1() \n");
            AKClassEditorComponentClone01.loadKrogothCoreList()
                .then(function(nodesForTree) {

                
                    vm.treeData[0].nodes = nodesForTree.js_nodes;
                    vm.treeData[1].nodes = AKClassEditorComponentClone01.html_nodes;
                	vm.treeData[2].nodes = nodesForTree.js_directive_nodes;

                    AKClassEditorComponentClone01.loadHTMLCoreList()
                        .then(function(htmlNodes) {

                            vm.loadOSXDoc(function() {
                                var audio = new Audio("/static/audio/kg_startup.wav");
                                audio.load();
                                audio.oncanplay = function() {
                                    audio.play();
                                    $log.log("\n AUDIO CAN PLAY \n");
                                };
                                audio.onended = function() {
                                    $log.log("\n AUDIO ENDED \n");
                                };
                            });



                        });


                    //vm.treeData[1].nodes = nodesForTree_set2;



                });
        }

        function getKrogothCorePartsSet2() {

            $log.log("\n 🔵 getKrogothCorePartsSet2() \n");
            AKClassEditorComponentClone01.loadKrogothCoreList()
                .then(function(nodesForTree) {

                    vm.treeData[0].nodes = nodesForTree;
                    //vm.treeData[1].nodes = nodesForTree_set2;

                    vm.loadOSXDoc(function() {


                    });

                });

        }

        vm.cleanedOnce = false;

        function loadFileIntoEditor(parentIndex, index, scope) {
            vm.cleanedOnce = false;
            $log.log("\n 🔵 loadFileIntoEditor( \n");
            $log.info("EDITOR IS CLEAN: " + vm.editorModel.doc.isClean());

            $log.info("vm.srcHolder: ");
            $log.log(vm.srcHolder);

            vm.unsavedChangesExist = -1;
            vm.loadedIndex = index;
            vm.loadedParentIndex = parentIndex;

            //if (vm.editorLoadedFirstDoc === true) {
            //    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].sourceCode = vm.editorModel.doc.getValue();
            //}
            vm.editorLoadedFirstDoc = true;

            const srcCodeKey = parentIndex.toString() + "-" + index.toString();
            const srcTitle = "_" + scope.title;
            const key = srcCodeKey + srcTitle;
            $log.log("making query...");
            $log.info(key);
            const src = vm.srcHolder[parseInt(vm.srcMap[key])];
            vm.activeEditorKey = parseInt(vm.srcMap[key]);

            vm.editorModel.doc.setValue(src);

            vm.unsavedChangesExist = -1;
            const syntax = vm.treeData[parentIndex].nodes[index].syntax;
            const _class = vm.treeData[parentIndex].nodes[index].class;
            vm.editorModel.setOption("mode", syntax);

            if (vm.customThemeMode === false) {
                vm.setThemeBasedOnClass(_class);
            }
            vm.editorModel.doc.markClean();
            vm.markAllAsUnloaded();
            vm.playSFX("beep_new_line_data");
            vm.treeData[parentIndex].nodes[index].isLoaded = true;
        }

        vm.markAllAsUnloaded = markAllAsUnloaded;

        function markAllAsUnloaded() {
            $log.info("NOW MARKING ALL AS UNLOADED!!!");
            angular.forEach(vm.treeData, function(parentNode) {
                $log.info("vm.treeData");
                angular.forEach(parentNode.nodes, function(node) {
                    $log.info("UNLOADING...");
                    node.isLoaded = false;
                });
            });
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

            $log.debug("parentIndex: " + parentIndex);
            $log.debug("index: " + index);
            $log.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FULL NODE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
            $log.debug(node);
            $log.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");



            const srcCodeKey = parentIndex.toString() + "-" + index.toString();
            const srcTitle = "_" + node.title;
            const key = srcCodeKey + srcTitle;

            if (parentIndex === 1) {
                ///saveHtmlCore	
                SaveToSQLClone01.saveHtmlCore(node, vm.srcHolder[parseInt(vm.srcMap[key])])
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
                        vm.playSFX("info_alert");
                        $mdToast.show(
                            $mdToast.simple()
                            .textContent('Document Saved.')
                            .position('top right')
                            .hideDelay(3000)
                        );
                    });
            } else {
                SaveToSQLClone01.saveDocument(node, vm.srcHolder[parseInt(vm.srcMap[key])])
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
                        vm.playSFX("info_alert");
                        $mdToast.show(
                            $mdToast.simple()
                            .textContent('Document Saved.')
                            .position('top right')
                            .hideDelay(3000)
                        );
                    });
            }


        }





        /// <PROCESS RESPONSE INTO RAM III. > 💚

        vm.unsavedChangesExist = -1;

        function editorContentWillChange() {
            $log.log("\n 🔵 editorContentWillChange( \n");
            $log.info("EDITOR IS CLEAN: " + vm.editorModel.doc.isClean());
            $log.info('unsavedChangesExist ' + vm.unsavedChangesExist);
        }

        function editorContentDidChange() {
            if (vm.cleanedOnce === false) {
                vm.cleanedOnce = true;
                vm.editorModel.doc.markClean();
            }
            $log.log("\n 🔵 editorContentDidChange( \n");
            $log.info("EDITOR IS CLEAN: " + vm.editorModel.doc.isClean());
            if (vm.loadedParentIndex !== -1 && vm.loadedIndex !== -1)
                if (vm.editorModel.doc.isClean() === false) {
                    vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].hasUnsavedChanges = true;

                    vm.setBrowserTabEditMode(true);
                }
            vm.srcHolder[vm.activeEditorKey] = vm.editorModel.doc.getValue();
            ///vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].sourceCode = vm.editorModel.doc.getValue();
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


        /* - - -< SRC CODE MAPPER >- - - */
        vm.activeEditorKey = "";
        vm.testGetMap = testGetMap;
        vm.srcMap = {};
        vm.srcHolder = [];
        vm.queryiedSrc = '';
        vm.consoleMode = true;
        vm.consoleOpen = false;
        vm.loadedOnce = false;

        function loadOSXDoc(callback) {
            $log.log("\n 🔵 loadOSXDoc( \n");
            if (!vm.loadedOnce) {
                if (null == vm.treeData || "object" != typeof vm.treeData) {} else {
                    /*
                    var copy = vm.treeData.constructor();
                    for (var attr in vm.treeData) {
                    	if (vm.treeData.hasOwnProperty(attr)) {
                    		copy[attr] = vm.treeData[attr];
                    	}
                    }
                    */
                    ///vm.treeModalIsVisible = !vm.treeModalIsVisible;
                    //vm.treeData = copy;
                    for (var i = 0; i < vm.treeData.length; i++) {
                        const nodeInRoot = vm.treeData[i];
                        $log.debug(nodeInRoot);

                        for (var j = 0; j < nodeInRoot.nodes.length; j++) {
                            const srdId = i.toString() + "-" + j.toString(); ///vm.simplifiedTreeData[i].nodes[j].id.toString();
                            const srcTitle = "_" + vm.treeData[i].nodes[j].title;
                            const key = srdId + srcTitle;
                            vm.srcMap[key] = vm.srcHolder.length.toString();
                            const code = vm.treeData[i].nodes[j].sourceCode;
                            vm.srcHolder.push(code);
                            vm.treeData[i].nodes[j].sourceCode = "NAN";
                        }
                    }
                    vm.loadedOnce = true;
                    callback();
                }
            }
        }

        /// ----- < GUI SFX > -----
        vm.playSFX = playSFX;

        function playSFX(wav) {
            /// click_select_units
            if (!vm.muted) {
                switch (wav) {
                    case "error":
                        var audio = new Audio("/static/audio/kg_" + wav + ".wav");
                        audio.play();
                        break;
                    case "info_alert":
                        var audio = new Audio("/static/audio/kg_" + wav + ".mp3");

                        audio.play();
                        break;
                    case "ping":

                        var audio = new Audio("/static/audio/kg_" + wav + ".wav");
                        audio.play();
                        break;
                    case "startup":
                        var audio = new Audio("/static/audio/kg_" + wav + ".wav");
                        audio.onplay = function() {
                            audio.play();
                        };
                        break;
                    default:
                        var audio = new Audio("/static/audio/" + wav + ".wav");
                        audio.play();
                        break;
                        $log.log("...");
                }
            }
        }
        ///----- </GUI SFX > -----

        function testGetMap() {
            $log.info(vm.srcMapInput);
            vm.queryiedSrc = vm.srcHolder[parseInt(vm.srcMap[vm.srcMapInput])];
        }
        /* - - -</ SRC CODE MAPPER >- - - */


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