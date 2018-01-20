(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_SLAVE_NAMEController', FUSE_APP_SLAVE_NAMEController);

    function FUSE_APP_SLAVE_NAMEController($log, $http, $state, RESTfulUltraBrowser, RESTfulUltraSubCat) {
        var vm = this;

        // Master View Controller Setup
        vm.codemirrorLoaded = codemirrorLoaded;
        vm.getMasterViewControllerDetail = getMasterViewControllerDetail;
        vm.didClickInit = didClickInit;
        vm.$onInit = onInit;
        vm.getCategories = getCategories;
        vm.putCatagory = putCatagory;
        vm.updateName = updateName;
        vm.updateTitle = updateTitle;
        vm.selectListItem = selectListItem;
        vm.objectList = [];
        vm.selectedCategory = -1;
        vm.processCategoryResults = processCategoryResults;

        function onInit() {
            vm.selectedCategory = $state.params.categoryId;
            if ($state.params.childId) {
                $log.info(" vm.getCategories () ");
                vm.getMasters($state.params.childId);
            } else {
                $log.info(" vm.getMasters () ");
                vm.getCategories();
            }
        }


        function updateName(tile) {
            vm.putCatagory(tile);
        }

        function updateTitle(tile) {
            vm.putCatagory(tile);
        }

        vm.getMasters = getMasters;

        function getMasters(catId) {
            RESTfulUltraSubCat.getMastersSlaveBrowser(catId)
                .then(function (results) {
                    vm.objectList = results;
                });
        }


        function getCategories() {
            RESTfulUltraSubCat.getCategoriesSlaveBrowser()
                .then(function (results) {
                    vm.processCategoryResults(results);
                });
        }

        function processCategoryResults(resultsArray) {
            $log.info("resultsArray: ");
            $log.info(resultsArray);
            for (var i = 0; i < resultsArray.length; i++) {
                if (resultsArray[i].parent !== null) {
                    $log.info("resultsArray[i]: ");
                    $log.info(resultsArray[i]);
                    if (vm.selectedCategory.toString() === resultsArray[i].parent.toString()) {
                        vm.objectList.push(resultsArray[i]);
                    }
                }
            }
        }

        function putCatagory(instance) {
            RESTfulUltraSubCat.putCatagorySlaveBrowser(instance)
                .then(function (results) {
                    vm.objectList = results;
                });
        }

        vm.selectMaster = selectMaster;

        function selectListItem(id) {
            $log.info("SELECTED CATEGORY ID: " + id);
            $state.go('app.FUSE_APP_NAME.slave', {
                'categoryId': id
            });
        }

        function selectMaster(id) {
            $log.info("SELECTED MASTER ID: " + id);
            $state.go('app.FUSE_APP_NAME.slave', {
                'categoryId': vm.selectedCategory, 'childId': id
            });
        }

        function codemirrorLoaded(_editor) {
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function () {
                vm.codeWillChange();
            });
            _editor.on("change", function () {
                vm.codeChanged();
            });
            vm.editorModel = _editor;
        }


        function didClickInit() {
            vm.getMasterViewControllerDetail(1);
        }


        function getMasterViewControllerDetail(id) {
            RESTfulUltraBrowser.getDjangularMasterViewControllerDetail(id).then(function (data) {
                vm.editorContentMaster = data;
                vm.editorModel.doc.setValue(data.controller_js);
                vm.input.mvcId = data.id;
                vm.slaves = [];
                vm.docWasModified = false;
                vm.getSlaveViewControllers(data.id);
                vm.toolbarInfo.id = data.id;
                vm.toolbarInfo.name = data.name;
                vm.toolbarInfo.title = data.title;
            });
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
    }
})();