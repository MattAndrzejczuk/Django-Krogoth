(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu, RESTfulUltraBrowser, $q) {
        var vm = this;


        /// Show These Documents With Unique Color:
        vm.primaryDocs = ['FBITest', 'LazarusMainMenu', 'uploadRepository', 'home'];

        // Master View Controller Setup
        vm.codemirrorLoaded = codemirrorLoaded;
        vm.editorModel = {};
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


        function onInit() {
            vm.getCategories();
            vm.getUncommitedSQL();
        }


        function updateName(tile) {
            vm.putCatagory(tile);
        }

        function updateTitle(tile) {
            vm.putCatagory(tile);
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
                        if (allCategories[i].name !== "DVCManager")
                            vm.objectList.push(allCategories[i]);
                    }
                }
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