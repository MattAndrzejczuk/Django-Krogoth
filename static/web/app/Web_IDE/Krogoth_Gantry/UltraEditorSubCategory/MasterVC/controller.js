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



        vm.$onInit = onInit;
        vm.getCategories = getCategories;
        vm.putCatagory = putCatagory;


        vm.editable = 'hello, click this';
        vm.updateName = updateName;
        vm.updateTitle = updateTitle;
        vm.selectListItem = selectListItem;
        vm.goToParentCategory = goToParentCategory;
        vm.selectedCategory = -1;


        function onInit() {
            vm.selectedCategory = $state.params.categoryId;
            vm.getCategories();
        }


        function updateName(tile) {
            vm.putCatagory(tile);
        }

        function updateTitle(tile) {
            vm.putCatagory(tile);
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
                    if (allCategories[i].parent !== null) {
                        if (vm.selectedCategory.toString() === allCategories[i].parent.toString())
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



        vm.startStateTransition = startStateTransition;

        function startStateTransition(stateName, cargo) {
            $log.info("-=-=-=- Changing State  🌀    -=-=-=-");
            $log.info("-=-       " + stateName);
            $log.debug(cargo);
            $log.info("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-");
            $state.go(stateName, cargo);
        }


        function selectListItem(id, parent) {
            const destination = "app.FUSE_APP_NAME.slave";
            const cargo = {
                'categoryId': parent,
                'childId': id
            };
            vm.startStateTransition(destination, cargo);
        }


        function goToParentCategory() {
            const destination = "app.UltraEditorBrowse";
            const cargo = {};
            vm.startStateTransition(destination, cargo);
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