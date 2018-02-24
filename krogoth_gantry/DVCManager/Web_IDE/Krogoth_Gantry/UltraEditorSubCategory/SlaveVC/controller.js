(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_SLAVE_NAMEController', FUSE_APP_SLAVE_NAMEController);

    function FUSE_APP_SLAVE_NAMEController($log, $http, $state, RESTfulUltraBrowser, RESTfulUltraSubCat) {
        var vm = this;

        // Master View Controller Setup
        vm.$onInit = onInit;
        vm.getCategories = getCategories;
        vm.putCatagory = putCatagory;
        vm.updateName = updateName;
        vm.updateTitle = updateTitle;
        vm.goToParentCategory = goToParentCategory;
        vm.selectMaster = selectMaster;
        vm.processCategoryResults = processCategoryResults;
        vm.getMasters = getMasters;

        vm.objectList = [];
        vm.selectedCategory = -1;
        vm.selectedMaster = -1;

        function onInit() {
            vm.selectedCategory = $state.params.categoryId;
            if ($state.params.childId) {
                vm.selectedMaster = $state.params.childId;
                vm.getMasters($state.params.childId);
            } else {
                vm.getCategories();
            }
        }


        function updateName(tile) {
            vm.putCatagory(tile);
        }

        function updateTitle(tile) {
            vm.putCatagory(tile);
        }


        function getMasters(catId) {
            RESTfulUltraSubCat.getMastersSlaveBrowser(catId)
                .then(function(results) {
                    vm.objectList = results;
                });
        }


        function getCategories() {
            RESTfulUltraSubCat.getCategoriesSlaveBrowser()
                .then(function(results) {
                    vm.processCategoryResults(results);
                });
        }

        function processCategoryResults(resultsArray) {
            for (var i = 0; i < resultsArray.length; i++) {
                if (resultsArray[i].parent !== null) {
                    if (vm.selectedCategory.toString() === resultsArray[i].parent.toString()) {
                        vm.objectList.push(resultsArray[i]);
                    }
                }
            }
        }

        function putCatagory(instance) {
            RESTfulUltraSubCat.putCatagorySlaveBrowser(instance)
                .then(function(results) {
                    vm.objectList = results;
                });
        }


        //function selectListItem(id) {
        //    $state.go('app.FUSE_APP_NAME.slave', {
        //        'categoryId': id
        //    });
        //}

        function selectMaster(id) {
            $state.go('app.UltraEditorDocument', {
                'categoryId': vm.selectedCategory,
                'subCategoryId': $state.params.childId,
                'masterId': id
            });
        }

        function goToParentCategory() {
            $state.go('app.FUSE_APP_NAME', {
                'categoryId': vm.selectedCategory
            });
        }


        ////// -----------
    }
})();