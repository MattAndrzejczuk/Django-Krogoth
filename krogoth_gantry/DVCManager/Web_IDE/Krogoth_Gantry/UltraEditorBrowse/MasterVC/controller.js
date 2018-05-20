(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu, constAddNewMVCTile,
        RESTfulUltraBrowser, $q, $mdBottomSheet) {
        var vm = this;


        /// Show These Documents With Unique Color:
        vm.primaryDocs = ['FBITest', 'LazarusMainMenu', 'uploadRepository', 'home'];

        // Master View Controller Setup
        //vm.codemirrorLoaded = codemirrorLoaded;
        //vm.editorModel = {};
        vm.getMasterViewControllerDetail = getMasterViewControllerDetail;
        vm.didClickInit = didClickInit;

        vm.objectList = [];


        vm.serverSideChanges = [];
        vm.getUncommitedSQL = getUncommitedSQL;


        vm.$onInit = onInit;
        vm.getCategories = getCategories;
        vm.putCatagory = putCatagory;


        vm.editable = 'hello, click this';
        vm.updateName = updateName;
        vm.updateTitle = updateTitle;
        vm.selectListItem = selectListItem;

        vm.selectedCategory = $state.params.categoryId;


        vm.openBottomSheet = openBottomSheet;

        vm.querySubCatsWithParent = querySubCatsWithParent;
        vm.openUltraEditorDocumentTwo = openUltraEditorDocumentTwo;


        function onInit() {
            vm.getCategories();
            vm.getUncommitedSQL();
        }

        vm.addCatMenuIsOpen = false;
        vm.mvcFormName = "";
        vm.mvcCatName = "";
        vm.mvcSubCatName = "";
        vm.mvcSubCatOptions = [];
        vm.mvcCatOptions = [];

        vm.selectedCategoryWizardName = "";
        vm.categoryWizardSelected = "EXISTING";
        vm.subCategoryWizardSelected = "NEW";

        vm.submitCreateNewMVC = submitCreateNewMVC;
        vm.saveUncommitedSQLToFilesystem = saveUncommitedSQLToFilesystem;

        function openBottomSheet() {
            vm.addCatMenuIsOpen = !vm.addCatMenuIsOpen;
        }

        function submitCreateNewMVC() {
            const restPayloadNewMVC = {
                "name": vm.mvcFormName,
                "cat": vm.selectedCategoryWizardName,
                "subcat": vm.mvcSubCatName,
                "weight": 5,
                "is_lazy": 0,
                "app_icon": "tdtdtd",
                "app_icon_prefix": "tdtdtd",
                "cat_icon": "tdtdtd",
                "cat_icon_prefix": "tdtdtd",
                "subcat_icon": "tdtdtd",
                "subcat_icon_prefix": "tdtdtd"
            };
            $http({
                method: 'POST',
                data: restPayloadNewMVC,
                url: "/krogoth_admin/createNewMasterViewController/"
            }).then(function successCallback(response) {
                //deferred.resolve(response.data);
                vm.masters = response.data;
            }, function errorCallback(response) {
                //deferred.reject(response);
            });
        }

        function updateName(tile) {
            vm.putCatagory(tile);
        }

        function updateTitle(tile) {
            vm.putCatagory(tile);
        }


        function querySubCatsWithParent() {

            $log.info("GETTING PARENTS...");
            $log.log(JSON.parse(vm.mvcCat));
            $log.info("/krogoth_gantry/viewsets/Category/?id=&name=&parent__id=" + JSON.parse(vm.mvcCat)['id']);
            vm.mvcSubCatOptions = [];

            vm.selectedCategoryWizardName = JSON.parse(vm.mvcCat)['name'];

            $http({
                method: 'GET',
                url: "/krogoth_gantry/viewsets/Category/?id=&name=&parent__id=" + JSON.parse(vm.mvcCat)['id']
            }).then(function successCallback(response) {
                //deferred.resolve(response.data);
                const results = response.data.results;
                vm.masters = response.data;


                for (var i = 0; i < results.length; i++) {
                    const parentId = results[i].parent;
                    $log.log("HERE's THE PARENT: " + parentId);
                    $log.log(results[i]);
                    $log.log(results[i].name);
                    vm.mvcSubCatOptions.push(results[i]);
                }

            }, function errorCallback(response) {
                //deferred.reject(response);
            });
        }


        function getUncommitedSQL() {
            //var deferred = $q.defer();
            $http({
                method: 'GET',
                url: "/krogoth_admin/KrogothAdministration/UncommitedSQL/"
            }).then(function successCallback(response) {
                /// Success
                //deferred.resolve(response.data);
                $log.log("response.data");
                $log.debug(response.data);
                if (response.data.results) {
                    var rawResponse = response.data.results;
                    for (var i = 0; i < rawResponse.length; i++) {
                        vm.serverSideChanges.push(rawResponse[i]);
                        $log.info(i);
                    }
                } else {
                    $log.log("Failed to get UncommitedSQL, admin access required.");
                }

            }, function errorCallback(response) {
                /// Fail
                //deferred.reject(response);
            });
            //return deferred.promise;
        }


        function saveUncommitedSQLToFilesystem() {
            //var deferred = $q.defer();
            $http({
                method: 'GET',
                url: "/krogoth_admin/SaveSQLToFileSystem/"
            }).then(function successCallback(response) {
                /// Success
                //deferred.resolve(response.data);
                vm.serverSideChanges = [];
                vm.getUncommitedSQL();
            }, function errorCallback(response) {
                /// Fail
                //deferred.reject(response);
            });
            //return deferred.promise;
        }


        function getCategories() {
            //var deferred = $q.defer();
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/Category/'
            }).then(function successCallback(response) {
                /// Success
                //deferred.resolve(response.data);

                var allCategories = response.data.results;
                for (var i = 0; i < allCategories.length; i++) {
                    if (allCategories[i].parent === null) {
                        if (allCategories[i].name !== "DVCManager") {
                            vm.objectList.push(allCategories[i]);
                            vm.mvcCatOptions.push(allCategories[i]);
                        }
                    } else {
                        ///vm.mvcSubCatOptions.push(allCategories[i]);
                    }
                }

                constAddNewMVCTile.makeTileJson()
                    .then(function(t) {
                        vm.objectList.push(t);
                    });

            }, function errorCallback(response) {
                /// Fail
                //deferred.reject(response);
            });
            //return deferred.promise;
        }

        function putCatagory(instance) {
            //var deferred = $q.defer();
            $http({
                method: 'PUT',
                data: instance,
                url: '/krogoth_gantry/viewsets/Category/' + instance.id + '/'
            }).then(function successCallback(response) {
                //deferred.resolve(response.data);
                vm.masters = response.data;
            }, function errorCallback(response) {
                //deferred.reject(response);
            });
            //return deferred.promise;
        }


        function selectListItem(id) {
            $state.go('app.UltraEditorSubCategory', {
                'categoryId': id
            });

        }


        /*
        function codemirrorLoaded(_editor) {
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.editorModel = _editor;
        }
		*/

        function didClickInit() {
            vm.getMasterViewControllerDetail(1);
        }


        function getMasterViewControllerDetail(id) {
            RESTfulUltraBrowser.getDjangularMasterViewControllerDetail(id).then(function(data) {
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

        function openUltraEditorDocumentTwo() {
            $state.go("app.UltraEditorDocumentTwo");
        }

        /*
        vm.editorOptions = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'javascript',
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };
		*/
        ////// -----------
    }
})();