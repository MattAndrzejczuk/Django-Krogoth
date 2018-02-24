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
        vm.startStateTransition = startStateTransition;

        vm.objectList = [];
        vm.selectedCategory = -1;
        vm.selectedSubCategory = -1;

        function onInit() {
            vm.selectedCategory = $state.params.categoryId;
            vm.selectedSubCategory = $state.params.childId;
            vm.getMasters(vm.selectedSubCategory);
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


        function startStateTransition(stateName, cargo) {
            $log.info("-=-=-=- Changing State  🌀    -=-=-=-");
            $log.info("-=-       " + stateName);
            $log.debug(cargo);
            $log.info("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-");
            $state.go(stateName, cargo);
        }

        function selectMaster(id) {
            const destination = "app.UltraEditorDocument";
            const cargo = {
                'categoryId': vm.selectedCategory,
                'subCategoryId': vm.selectedSubCategory,
                'masterId': id
            };
            vm.startStateTransition(destination, cargo);
        }

        function goToParentCategory() {
            const destination = "app.FUSE_APP_NAME";
            const cargo = {
                'categoryId': vm.selectedCategory
            };
            vm.startStateTransition(destination, cargo);
        }


        ////// -----------
    }
})();