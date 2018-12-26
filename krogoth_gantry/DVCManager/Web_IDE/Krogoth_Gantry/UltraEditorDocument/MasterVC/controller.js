/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu,
        TemplateCRUD, DirectiveCRUD, CustomKeyValuesEditor, EditorWebSocket, $ocLazyLoad, $location,
        $q, AKClassEditorComponent, UltraEditorDefaults, GatherURIsAsync, fileNameChanger, $mdDialog,
        Dependency, SaveToSQL, $mdSidenav, BreadCrumbsIDE, $timeout, codeHighlightIDE) {
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
        ///renameObjectClick
        vm.$onInit = onInit;


        vm.editorContentWillChange = editorContentWillChange;
        vm.editorContentDidChange = editorContentDidChange;

        vm.selectListItem = selectListItem;
        vm.loadFileIntoEditor = loadFileIntoEditor;


        /// REQUEST ALL DATA II.  💛
        vm.finishedRESTfulResponses = [];
        vm.parallelRESTfulServerError = parallelRESTfulServerError;

        // Master View Controller Setup
        vm.selectedMaster = 0;
        vm.treeData = [];
        vm.editorModel = {};
        vm.objectList = {};
        ///vm.messages = [];
        vm.finishedRESTfulResponses = [];
        vm.newComponentForm = {};
        vm.finishedBreadCrumbsJson = {};
        vm.servicesPendingRequest = [];
        vm.directivesPendingRequest = [];
        vm.scannedVMs = [];
        vm.slavesPendingRequest = [];
        vm.pendingRESTfulRequests = [];
        vm.masterName = ". . .";
        vm.scrollTopsSaved = {};
        vm.loadedIndex = -1;
        vm.loadedParentIndex = -1;

        vm.editorLoadedFirstDoc = false;

        vm.saveEditorWorkToServer = saveEditorWorkToServer;




        vm.getTemplatesHTML = getTemplatesHTML;

        vm.goBackToCategory = goBackToCategory;
        vm.toggleSidenav = toggleSidenav;
        vm.buildBreadCrumbs = buildBreadCrumbs;
        vm.sideNavLocked = true;

        vm.beautifyCode = beautifyCode;
        vm.goBackToExplorerHome = goBackToExplorerHome

        vm.cursorActivity = cursorActivity;
        vm.unsavedChangesExist = -1;
        vm.customThemeMode = false;
        vm.setThemeBasedOnClass = setThemeBasedOnClass;
        vm.remove = remove;
        vm.toggleFolder = toggleFolder;
        vm.newSubItem = newSubItem;

        vm.browserTabEmoji = " 🔨 ";
        vm.browserTabText = "Krogoth Editor";
        vm.setBrowserTabText = setBrowserTabText;
        vm.setBrowserTabEditMode = setBrowserTabEditMode;
        vm.isDisplayingPropModal = false;


        vm.loadOSXDoc = loadOSXDoc;

        vm.openedDocTitle = "";
        vm.highlightInputCustom = highlightInputCustom;
        vm.removeHighlights = removeHighlights;

        vm.changeBgWallpaper = changeBgWallpaper;
        vm.bg_image = Math.floor(Math.random() * 9) + 1;

        vm.welcomeSFX = new Audio("/static/gui_sfx/kg_startup.wav");
        vm.welcomeSFX.load();


        vm.scrollToY = scrollToY;
        vm.saveScrollY = saveScrollY;

        vm.loadingIDE = true;
        vm.aeroMode = true;

        vm.buttonCoolingDownWallpaper = false;
        vm.startCoolDownWallpaper = startCoolDownWallpaper;







        # codeSyntaxSelect

        # EditorStartupSequences

        # extraCodeMirrorIDECtrls

        # WebSocketMethods


        function startCoolDownWallpaper() {
            vm.buttonCoolingDownWallpaper = true;
            $timeout(function() {
                vm.buttonCoolingDownWallpaper = false;
            }, 900);
        }

        function changeBgWallpaper() {
            if (vm.buttonCoolingDownWallpaper === false) {
                vm.startCoolDownWallpaper();
                if (vm.bg_image === 9) {
                    vm.bg_image = 1;
                } else {
                    ++vm.bg_image;
                }
            }
        }

        /// I.
        function onInit() {
            vm.selectedMaster = $state.params.masterId;


            vm.stateParameters = {
                'categoryId': $state.params.selectedCategory,
                'subCategoryId': $state.params.selectedSubCategory,
                'masterId': $state.params.masterId
            };

            //vm.welcomeSFX.oncanplay = function() {
            vm.welcomeSFX.play();
            vm.buildBreadCrumbs();
            vm.createFirstTreeNodes();
            //};

            //vm.welcomeSFX.onended = function() {

            //};
        }

        /// < ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ DONT PUT SOURCE INTO UI TREE ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ >
        vm.forwardThisCode = forwardThisCode;

        function forwardThisCode(parentIndex, index, srcCode, title) {
            const srdId = parentIndex.toString() + "-" + index.toString();
            const srcTitle = "_" + title;
            const key = srdId + srcTitle;
            vm.srcMap[key] = vm.srcHolder.length.toString();
            vm.srcHolder.push(srcCode);
        }
        /// < ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ / DONT PUT SOURCE INTO UI TREE / ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ >


        // vvv REMOVE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        function AKEditorComponentMaster(_class, index, parentIndex, srcCode, sourceKey, restId, syntax, icon) {
            vm.forwardThisCode(parentIndex, index, srcCode, _class);
            this.id = -1;
            this.parentIndex = parentIndex;
            this.index = index;
            this.name = _class;
            this.title = _class;
            this.class = _class;
            this.sourceCode = "MOVED"; //srcCode;
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
            this.wasSavedInOtherBrowser = false;
            this.openInOtherBrowser = false;
        }
        // ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


        vm.cleanedOnce = false;
        /*  ⚡️  */
        function loadFileIntoEditor(parentIndex, index, scope) {
            vm.cleanedOnce = false;
            $log.log("\n 🔵 loadFileIntoEditor( \n");
            $log.info("EDITOR IS CLEAN: " + vm.editorModel.doc.isClean());
            vm.unsavedChangesExist = -1;


            vm.loadedIndex = scope.index;
            vm.loadedParentIndex = scope.parentIndex;
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
            $log.log("vm.treeData[parentIndex].nodes[index]: ");
            $log.info(vm.treeData[parentIndex].nodes[index]);
            $log.log("parentIndex: " + parentIndex);
            $log.log("index: " + index);
            $log.log(scope);
            const syntax = scope.syntax;
            const _class = scope.class;
            vm.editorModel.setOption("mode", syntax);
            if (vm.customThemeMode === false) {
                vm.setThemeBasedOnClass(_class);
            }
            vm.editorModel.doc.markClean();
            vm.playSFX("kg_gui-08");
            vm.markAllAsUnloaded();
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

        vm.editorOptions = {
            lineWrapping: false,
            lineNumbers: true,
            mode: "javascript",
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: false
        };

        function setThemeBasedOnClass(_class) {
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
            _editor.on("cursorActivity", function() {
                vm.cursorActivity();
            });
            vm.editorModel = _editor;
        }


        ///----- < CURSOR CLICK > -----
        function cursorActivity() {
            /*
            console.log(" . . . . . . . . . getScrollInfo");
            $log.info(vm.editorModel.getScrollInfo());
            console.log(" . . . . . . . . . cursorCoords");
            $log.info(vm.editorModel.cursorCoords());
            console.log(" . . . . . . . . . getViewport");
            $log.info(vm.editorModel.getViewport());
            console.log(" . . . . . . . . . scrollTop");
            $log.info(document.getElementById("positionTracker").scrollTop);
			*/
        }
        ///----- </CURSOR CLICK > -----



        function scrollToY() {
            var pi = vm.loadedParentIndex;
            var ni = vm.loadedIndex;
            var topY = vm.scrollTopsSaved[vm.treeData[pi].nodes[ni].title];
            document.getElementById("positionTracker").scrollTo(0, topY);
        }


        function saveScrollY() {
            var pi = vm.loadedParentIndex;
            var ni = vm.loadedIndex;
            var topY = document.getElementById("positionTracker").scrollTop;
            vm.scrollTopsSaved[vm.treeData[pi].nodes[ni].title] = topY;
        }


        function saveEditorWorkToServer(parentIndex, index, node) {
            const srcCodeKey = parentIndex.toString() + "-" + index.toString();
            const srcTitle = "_" + node.title;
            const key = srcCodeKey + srcTitle;
            SaveToSQL.saveDocument(node, vm.srcHolder[parseInt(vm.srcMap[key])])
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
                    vm.treeData[pi].nodes[ni].hasUnsavedChanges = false;
                    vm.unsavedChangesExist = -1;
                    vm.setBrowserTabEditMode(false);
                    vm.playSFX("kg_gui-06");
                    $mdToast.show(
                        $mdToast.simple()
                        .textContent('Document Saved.')
                        .position('top right')
                        .hideDelay(3000)
                    );
                    vm.sendWSMessageWithAction("save");
                });
        }





        /// <PROCESS RESPONSE INTO RAM III. > 💚

        function editorContentWillChange() {
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
                    vm.sendWSMessageWithAction("edit");
                    vm.setBrowserTabEditMode(true);
                }
            vm.srcHolder[vm.activeEditorKey] = vm.editorModel.doc.getValue();
            vm.unsavedChangesExist += 1;
        }


        function parallelRESTfulServerError() {
            ///vm.messages.push("something failed: parallelRESTfulServerError");
        }

        vm.startStateTransition = startStateTransition;

        function startStateTransition(stateName, cargo) {
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



        /*  ⚡️  */
        function remove(scope) {
            scope.remove();
        }

        /*  ⚡️  */
        function toggleFolder(scope, pi) {
            $log.log("TOGGLE FOLDER: ");
            $log.log(pi);
            vm.treeData[pi].expanded = !vm.treeData[pi].expanded;
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



        function buildBreadCrumbs() {
            BreadCrumbsIDE.cookBread($state.params.categoryId, $state.params.subCategoryId, $state.params.masterId)
                .then(function(finishedBread) {
                    vm.finishedBreadCrumbsJson._1st = finishedBread[0];
                    vm.finishedBreadCrumbsJson._2nd = finishedBread[1];
                    vm.finishedBreadCrumbsJson._3rd = finishedBread[2];
                    var changeTabTitle = document.getElementById("browser_tab_text");
                    changeTabTitle.innerHTML = " 🔨 " + vm.masterName;
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

        function getTemplatesHTML() {
            Dependency.loadTmplIncludeList(vm.objectList.name, "Html")
                .then(function(htmlTemps) {
                    $(htmlTemps.srcTMPLs).each(function(i, src) {
                        vm.forwardThisCode(src.parentIndex, src.index, src.srcCode, src.title);
                    });
                    vm.treeData[5].nodes = htmlTemps.returnNodes;
                });
        }

        vm.getTemplatesJS = getTemplatesJS;

        function getTemplatesJS() {
            Dependency.loadTmplIncludeList(vm.objectList.name, "Js")
                .then(function(jsTemps) {
                    $(jsTemps.srcTMPLs).each(function(i, src) {
                        vm.forwardThisCode(src.parentIndex, src.index, src.srcCode, src.title);
                    });
                    vm.treeData[6].nodes = jsTemps.returnNodes;
                });
        }






        function beautifyCode() {
            vm.editorModel.execCommand("indentAuto");
        }

        function goBackToExplorerHome() {
            $state.go('app.UltraEditorBrowse');
        }


        vm.highlightedPositions = [];

        function highlightInputCustom() {
            codeHighlightIDE.highlightCustom(vm.editorModel, vm.findStringForm)
                .then(function(completion) {
                    vm.editorModel = completion.editorModel;
                    vm.highlightedPositions = completion.positionOfHighlighted;
                });
        }

        function removeHighlights() {
            codeHighlightIDE.clearHighlights(vm.editorModel)
                .then(function(completion) {
                    vm.editorModel = completion.editorModel;
                    vm.highlightedPositions = [];
                });
            ///vm.editorModel.doc.setValue(vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex].sourceCode);
        }







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
                    for (var i = 0; i < vm.treeData.length; i++) {
                        const nodeInRoot = vm.treeData[i];
                        $log.debug(nodeInRoot);
                        $log.debug(callback);
                        for (var j = 0; j < nodeInRoot.nodes.length; j++) {
                            const srdId = i.toString() + "-" + j.toString();
                            const srcTitle = "_" + vm.treeData[i].nodes[j].title;
                            const key = srdId + srcTitle;
                            vm.srcMap[key] = vm.srcHolder.length.toString();
                            const code = vm.treeData[i].nodes[j].sourceCode;
                            vm.srcHolder.push(code);
                            vm.treeData[i].nodes[j].sourceCode = "NAN";
                        }
                    }
                    vm.loadedOnce = true;
                    if (callback) callback();
                }
            }
        }

        /// ----- < GUI SFX > -----
        vm.playSFX = playSFX;

        function playSFX(wav) {
            /// click_select_units
            $log.log("/static/gui_sfx/" + wav + ".wav");
            if (!vm.muted) {
                switch (wav) {
                    case "error":
                        var audio = new Audio("/static/gui_sfx/kg_" + wav + ".wav");
                        audio.play();
                        break;
                    case "info_alert":
                        var audio = new Audio("/static/gui_sfx/kg_" + wav + ".mp3");
                        audio.play();
                        break;
                    case "ping":
                        var audio = new Audio("/static/gui_sfx/kg_" + wav + ".wav");
                        audio.play();
                        break;
                    case "startup":
                        var audio = new Audio("/static/gui_sfx/kg_" + wav + ".wav");
                        audio.onplay = function() {
                            audio.play();
                        };
                        break;
                    default:
                        var audio = new Audio("/static/gui_sfx/" + wav + ".wav");
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




        vm.dumpJsonTreeData = dumpJsonTreeData;

        /* - - - - - */


        function dumpJsonTreeData() {
            $log.log(" 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 TREE DATA OBJECT: ");
            $log.info(vm.treeData);
            $log.log(" 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 🍊 ");

            $log.log(" 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 TREE DATA JSON STRING: ");
            $log.info(JSON.stringify(vm.treeData));
            $log.log(" 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 🍇 ");

            $log.log(" 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 SRC MAP: ");
            $log.info(JSON.stringify(vm.srcMap));
            $log.log(" 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 🍋 ");

            $log.log(" 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 SRC HOLDER: ");
            $log.info((vm.srcHolder));
            $log.log(" 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 🍒 ");
        }



        #CreateRenameDependencies

        #LazyLoadRefreshIDE


    }
})();