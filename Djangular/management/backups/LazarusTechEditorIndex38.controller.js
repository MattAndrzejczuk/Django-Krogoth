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
            $log.log('[GET]');
            $log.info('/LazarusDatabase/UnitFBIFromSQLView/');
            $log.debug(response.data['list_response']);
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
                $log.log('[GET]');
                $log.info('/LazarusDatabase/SelectedModProject/');
                $log.debug(response.data['results']);
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
                $log.log('- - - - - - - - - - - - - - - -');
                $log.log('-ASSETS ARE LOCKED AND LOADED -');
                $log.log('- - - - - - - - - - - - - - - -');
                $log.log('[GET]');
                $log.info('/LazarusDatabase/TotalAnnihilation/LazarusModAsset/?project_id=' + withModId);
                $log.debug(response.data['results']);
                vm.modAssets = response.data['results'];
                $log.debug('Okay, the asset needs to fucking loop through some shit.');
                for (var i = 0; i < vm.modAssets.length; i++) {
                    $log.log('looping... ' + i);
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
        vm.globalUnitPngDictionary = {};

        function loadDependencies(withAssetId) {
            $http({
                method: 'GET',
                url: '/LazarusDatabase/TotalAnnihilation/LazarusModDependency/?asset_id=' + withAssetId
            }).then(function successCallback(response) {
                /// vm.modDependencies = response.data['results'];
                $log.log('[GET]');
                $log.info('/LazarusDatabase/TotalAnnihilation/LazarusModDependency/?asset_id=' + withAssetId);
                $log.debug(response.data['results']);
                for (var i = 0; i < response.data['results'].length; i++) {
                    var dependencyItem = response.data['results'][i];
                    if (dependencyItem.model_schema === 'DownloadTDF') {
                        dependencyItem.bgClass = 'md-warn-bg';
                    } else if (dependencyItem.model_schema === 'FeatureTDF') {
                        dependencyItem.bgClass = 'md-accent-bg';
                    } else {
                        dependencyItem.bgClass = 'md-primary-bg md-hue-3';
                    }

                    if (dependencyItem.model_schema === 'file.pcx') {

                    }

                    if (dependencyItem.model_schema === 'DownloadTDF') {
                        /// i.e. 'HoveraTAck'
                        var localPath = dependencyItem.system_path.replace('/usr/src/persistent/media/ta_data/', '');
                        var index_end = localPath.indexOf("/");
                        var origNameHPI = localPath.substring(0, index_end);
                        /// i.e. 'speeder'
                        var index_end_2 = dependencyItem.name.indexOf("_");
                        var unitName = dependencyItem.name.substring(0, index_end_2);
                        var picName = unitName.toLowerCase() + '.png';

                        // grab the unit's UnitName
                        var builderToProduct = dependencyItem.type; // ARMASY -> ANAbel
                        var unitNameNew = builderToProduct.split(' -> ')[1].toLowerCase();
                        var previewPicUrl = '/media/ta_data/' + origNameHPI + '/unitpics/' + unitNameNew + '.png';

                        if (vm.globalUnitPngDictionary[unitName.toUpperCase()]) {

                        } else {
                            vm.globalUnitPngDictionary[unitName.toUpperCase()] = previewPicUrl;
                        }
                    }

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

                        var rawMetaData = dependencyItem.meta_data; /// "entry=MENUENTRY1|menu=4|button=4"
                        var parse1 = rawMetaData.replace('entry=', '');
                        var entriesSplit = parse1.split('|');
                        var button_num = entriesSplit[2].replace('button=', '');
                        var entry_num = entriesSplit[0];
                        var menu_num = entriesSplit[1].replace('menu=', '');
                        dependencyItem.button_png = '/static/editorTiles/MENUENTRY/DLTDF_' + button_num + '.png';
                        dependencyItem.entry_id = entry_num;
                        dependencyItem.menu_num = menu_num;

                        if (vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()]) {
                            //if (vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()][dependencyItem].includes(dependencyItem) === false)
                            vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()][dependencyItem.type] = (dependencyItem);
                        } else {
                            vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()] = {};
                            vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()][dependencyItem.type] = (dependencyItem);
                        }
                        // the if block below results in duplicates:
                        /*
                        if (vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()]) {
                            if (vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()].includes(dependencyItem) === false)
                                vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()].push(dependencyItem);
                        } else {
                            vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()] = [];
                            vm.workersWithBuildSchematic[dependencyItem.built_by.toUpperCase()].push(dependencyItem);
                        }
						*/

                        /// Unit/Structure Product -> [all workers who can build this product]
                        if (vm.groupedAssetsWithDependencies[dependencyItem.snowflake]) {
                            vm.groupedAssetsWithDependencies[dependencyItem.snowflake].push(dependencyItem);
                        } else {
                            vm.groupedAssetsWithDependencies[dependencyItem.snowflake] = [];
                            vm.groupedAssetsWithDependencies[dependencyItem.snowflake].push(dependencyItem);
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

        // vm.vanillaArmConstructorDict.hasOwnProperty('ARMCOMARMCOM')  =  true
        // vm.vanillaArmConstructorDict.hasOwnProperty('RABLEAFGLLTT')  =  false
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

            ARMACSUB: "/static/CCTAUnitPics/ARMACSUB.PNG",
            ARMCH: "/static/CCTAUnitPics/ARMCH.PNG",
            ARMCSA: "/static/CCTAUnitPics/ARMCSA.PNG",
            ARMHP: "/static/CCTAUnitPics/ARMHP.PNG",
            ARMPLAT: "/static/CCTAUnitPics/ARMPLAT.PNG",

            CORACSUB: "/static/CCTAUnitPics/CORACSUB.PNG",
            CORCH: "/static/CCTAUnitPics/CORCH.PNG",
            CCORCSA: "/static/CCTAUnitPics/CCORCSA.PNG",
            CORGANT: "/static/CCTAUnitPics/CORGANT.PNG",
            CORHP: "/static/CCTAUnitPics/CORHP.PNG",
            CORPLAT: "/static/CCTAUnitPics/CORPLAT.PNG",
        };


        /// Third Party Factories Have (TEDClass: "PLANT")
        /// Third Party Workers Have (TEDClass: "CNSTR" or "VTOL")
        // "VTOL" - worker tech lvl 1
        // "CNSTR" - worker tech lvl 2
        /// - - - - - - - - - - - - - - - - - - - - - - - - - - - -









    }
})();