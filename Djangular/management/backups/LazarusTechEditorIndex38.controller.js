(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, $timeout) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        /// 
        vm.totalUnits = 0;
        vm.modName = 'X';
        $http({
            method: 'GET',
            url: '/LazarusDatabase/UnitFBIFromSQLView/'
        }).then(function successCallback(response) {
            vm.totalUnits = response.data['list_response'].length;
            vm.modName = response.data['mod'];
        }, function errorCallback(response) {

        });
        /// 




        /// [1] - LOAD THE MOD
        ///
        vm.userMods = [];
        vm.reloadMods = reloadMods;
        vm.currentlyLoadedMod = {};

        function reloadMods() {
            $http({
                method: 'GET',
                url: '/LazarusDatabase/SelectedModProject/'
            }).then(function successCallback(response) {
                vm.userMods = response.data['results'];
                for (var i = 0; i < vm.userMods.length; i++) {
                    if (vm.userMods[i]['is_selected'] === true) {
                        vm.currentlyLoadedMod = vm.userMods[i];
                        vm.loadAssets(vm.currentlyLoadedMod['id']);
                    }
                }
            }, function errorCallback(response) {

            });
        }
        vm.reloadMods();


        /// [2] - LOAD THE ASSETS
        ///
        vm.modAssets = [];
        vm.loadAssets = loadAssets;

        function loadAssets(withModId) {
            $http({
                method: 'GET',
                url: '/LazarusDatabase/TotalAnnihilation/LazarusModAsset/?project_id=' + withModId
            }).then(function successCallback(response) {
                vm.modAssets = response.data['results'];
                for (var i = 0; i < vm.modAssets.length; i++) {
                    vm.loadDependencies(vm.modAssets[i]['id']);
                }

            }, function errorCallback(response) {

            });
        }




        /// [3] - LOAD THE DEPENDENCIES
        ///
        vm.modDependencies = [];
        vm.loadDependencies = loadDependencies;
        vm.dependenciesDidLoad = false;

        vm.groupedAssetsWithDependencies = {};
        vm.totalAssetSets = 0;
        vm.workersWithBuildSchematic = {};

        function loadDependencies(withAssetId) {
            $http({
                method: 'GET',
                url: '/LazarusDatabase/TotalAnnihilation/LazarusModDependency/?asset_id=' + withAssetId
            }).then(function successCallback(response) {
                /// vm.modDependencies = response.data['results'];
                for (var i = 0; i < response.data['results'].length; i++) {
                    var dependencyItem = response.data['results'][i];
                    if (dependencyItem.model_schema === 'DownloadTDF') {
                        dependencyItem.bgClass = 'md-warn-bg';
                    } else if (dependencyItem.model_schema === 'FeatureTDF') {
                        dependencyItem.bgClass = 'md-accent-bg';
                    } else {
                        dependencyItem.bgClass = 'md-primary-bg md-hue-3';
                    }
                    /// i.e. 'HoveraTAck'
                    var localPath = dependencyItem.system_path.replace('/usr/src/persistent/media/ta_data/', '');
                    var index_end = localPath.indexOf("/");
                    var origNameHPI = localPath.substring(0, index_end);
                    /// i.e. 'speeder'
                    var index_end_2 = dependencyItem.name.indexOf("_");
                    var unitName = dependencyItem.name.substring(0, index_end_2);
                    var picName = unitName.toLowerCase() + '.png';
                    var previewPicUrl = '/media/ta_data/' + origNameHPI + '/unitpics/' + picName;

                    dependencyItem.pngImg = previewPicUrl;
                    if (dependencyItem.type === 'unitpic') {
                        for (var j = 0; j < 9; j++) {
                            vm.modDependencies.push({
                                heightRowSpan: 1,
                                widthColSpan: 1,
                                bgClass: 'hideThis'
                            });
                        }
                    }
                    vm.modDependencies.push(dependencyItem);

                    if (dependencyItem.model_schema === 'DownloadTDF') {
                        /// BUILDER -> [possible units BUILDER can produce]
                        dependencyItem.built_by = dependencyItem.type.split(' -> ')[0];
                        dependencyItem.snowflake = dependencyItem.type.split(' -> ')[1];
                        if (vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()]) {
                            if (vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()].includes(dependencyItem) === false)
                                vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()].push(dependencyItem);
                        } else {
                            vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()] = [];
                            vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()].push(dependencyItem);
                        }

                        /// Unit/Structure Product -> [all workers who can build this product]
                        if (vm.groupedAssetsWithDependencies[dependencyItem.asset_id + '|' + dependencyItem.snowflake]) {
                            vm.groupedAssetsWithDependencies[dependencyItem.asset_id + '|' + dependencyItem.snowflake].push(dependencyItem);
                        } else {
                            vm.groupedAssetsWithDependencies[dependencyItem.asset_id + '|' + dependencyItem.snowflake] = [];
                            vm.groupedAssetsWithDependencies[dependencyItem.asset_id + '|' + dependencyItem.snowflake].push(dependencyItem);
                            vm.totalAssetSets += 1;
                        }
                    }

                    vm.groupedAssetsWithDependencies.totalAssetSets = vm.totalAssetSets;
                }
                //timer callback
                var loadGui = function() {
                    vm.dependenciesDidLoad = true;
                }
                //run!!
                $timeout(loadGui, 1000);

            }, function errorCallback(response) {

            });
        }


        vm.vanillaArmConstructorDict = {
            ARMAAP: "/static/vanillaTAUnitPics/ARMAAP.PNG",
            ARMACA: "/static/vanillaTAUnitPics/ARMACA.PNG",
            ARMACK: "/static/vanillaTAUnitPics/ARMACK.PNG",
            ARMACV: "/static/vanillaTAUnitPics/ARMACV.PNG",
            ARMALAB: "/static/vanillaTAUnitPics/ARMALAB.PNG",
            ARMAP: "/static/vanillaTAUnitPics/ARMAP.PNG",
            ARMASY: "/static/vanillaTAUnitPics/ARMASY.PNG",
            ARMAVP: "/static/vanillaTAUnitPics/ARMAVP.PNG",
            ARMCA: "/static/vanillaTAUnitPics/ARMCA.PNG",
            ARMCK: "/static/vanillaTAUnitPics/ARMCK.PNG",
            ARMCOM: "/static/vanillaTAUnitPics/ARMCOM.PNG",
            ARMCS: "/static/vanillaTAUnitPics/ARMCS.PNG",
            ARMCV: "/static/vanillaTAUnitPics/ARMCV.PNG",
            ARMLAB: "/static/vanillaTAUnitPics/ARMLAB.PNG",
            ARMVP: "/static/vanillaTAUnitPics/ARMVP.PNG",
            CORAAP: "/static/vanillaTAUnitPics/CORAAP.PNG",
            CORACA: "/static/vanillaTAUnitPics/CORACA.PNG",
            CORACK: "/static/vanillaTAUnitPics/CORACK.PNG",
            CORACV: "/static/vanillaTAUnitPics/CORALAB.PNG",
            CORALAB: "/static/vanillaTAUnitPics/CORALAB.PNG",
            CORAP: "/static/vanillaTAUnitPics/CORAP.PNG",
            CORASY: "/static/vanillaTAUnitPics/CORASY.PNG",
            CORAVP: "/static/vanillaTAUnitPics/CORAVP.PNG",
            CORCA: "/static/vanillaTAUnitPics/CORCA.PNG",
            CORCK: "/static/vanillaTAUnitPics/CORCK.PNG",
            CORCOM: "/static/vanillaTAUnitPics/CORCOM.PNG",
            CORCS: "/static/vanillaTAUnitPics/CORCS.PNG",
            CORCV: "/static/vanillaTAUnitPics/CORCV.PNG",

            ARMACSUB: "/static/TACC_unitdata/ARMACSUB.PNG",
            ARMCH: "/static/TACC_unitdata/ARMCH.PNG",
            ARMCSA: "/static/TACC_unitdata/ARMCSA.PNG",
            ARMHP: "/static/TACC_unitdata/ARMHP.PNG",
            ARMPLAT: "/static/TACC_unitdata/ARMPLAT.PNG",

            CORACSUB: "/static/TACC_unitdata/CORACSUB.PNG",
            CORCH: "/static/TACC_unitdata/CORCH.PNG",
            CCORCSA: "/static/TACC_unitdata/CCORCSA.PNG",
            CORGANT: "/static/TACC_unitdata/.PNG",
            CORHP: "/static/TACC_unitdata/CORGANT.PNG",
            CORPLAT: "/static/TACC_unitdata/CORPLAT.PNG",
        };


        /// Third Party Factories Have (TEDClass: "PLANT")
        /// Third Party Workers Have (TEDClass: "CNSTR" or "VTOL")
        // "VTOL" - worker tech lvl 1
        // "CNSTR" - worker tech lvl 2
        /// - - - - - - - - - - - - - - - - - - - - - - - - - - - -


        vm.vanillaArmConstructorPics = [{
            "snowflake": "ARMAAP",
            "img": "/static/vanillaTAUnitPics/ARMAAP.PNG"
        }, {
            "snowflake": "ARMACA",
            "img": "/static/vanillaTAUnitPics/ARMACA.PNG"
        }, {
            "snowflake": "ARMACK",
            "img": "/static/vanillaTAUnitPics/ARMACK.PNG"
        }, {
            "snowflake": "ARMACV",
            "img": "/static/vanillaTAUnitPics/ARMACV.PNG"
        }, {
            "snowflake": "ARMALAB",
            "img": "/static/vanillaTAUnitPics/ARMALAB.PNG"
        }, {
            "snowflake": "ARMAP",
            "img": "/static/vanillaTAUnitPics/ARMAP.PNG"
        }, {
            "snowflake": "ARMASY",
            "img": "/static/vanillaTAUnitPics/ARMASY.PNG"
        }, {
            "snowflake": "ARMAVP",
            "img": "/static/vanillaTAUnitPics/ARMAVP.PNG"
        }, {
            "snowflake": "ARMCA",
            "img": "/static/vanillaTAUnitPics/ARMCA.PNG"
        }, {
            "snowflake": "ARMCK",
            "img": "/static/vanillaTAUnitPics/ARMCK.PNG"
        }, {
            "snowflake": "ARMCOM",
            "img": "/static/vanillaTAUnitPics/ARMCOM.PNG"
        }, {
            "snowflake": "ARMCS",
            "img": "/static/vanillaTAUnitPics/ARMCS.PNG"
        }, {
            "snowflake": "ARMCV",
            "img": "/static/vanillaTAUnitPics/ARMCV.PNG"
        }, {
            "snowflake": "ARMLAB",
            "img": "/static/vanillaTAUnitPics/ARMLAB.PNG"
        }];









    }
})();