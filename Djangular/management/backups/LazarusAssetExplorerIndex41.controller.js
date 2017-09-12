(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, $timeout) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.showFirstJsonRow = false;
        vm.showSecondJsonRow = false;

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

                    if (vm.groupedAssetsWithDependencies[dependencyItem.asset_id]) {
                        vm.groupedAssetsWithDependencies[dependencyItem.asset_id].push(dependencyItem);
                    } else {
                        vm.groupedAssetsWithDependencies[dependencyItem.asset_id] = [];
                        vm.groupedAssetsWithDependencies[dependencyItem.asset_id].push(dependencyItem);
                        vm.totalAssetSets += 1;
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




        /*
                vm.getRectXY = getRectXY;

                function getRectXY(id) {
                    var rec = document.getElementById(id).getBoundingClientRect();
                    var xy = {
                        x: rec.left + window.scrollX,
                        y: rec.top + window.scrollY - 64
                    };
                    $log.log('GETTING RECT DIMENSIONS: ');
                    $log.info(xy);
                    return rec.left + window.scrollX;
                }

                function findLeft(element) { /// DETECT DIV X,Y COORDINATES
                    var rec = document.getElementById(element).getBoundingClientRect();
                    return rec.left + window.scrollX;
                }

                function findTop(element) { /// DETECT DIV X,Y COORDINATES
                    var rec = document.getElementById(element).getBoundingClientRect();
                    return rec.top + window.scrollY;
                } //call it like findTop('#header');
                function findTopLeft(element) {
                    var rec = document.getElementById(element).getBoundingClientRect();
                    return {
                        top: rec.top + window.scrollY,
                        left: rec.left + window.scrollX
                    };
                } //call it like findTopLeft('#header');



                var formatHtml = function() {
                    for (var i = 0; i < vm.listData.posts.length; i++) {
                        vm.formatThreadBody(vm.listData.posts[i]['body'], vm.listData.posts[i]['id']);
                    }
                }
                $timeout(formatHtml, 500);

                function formatThreadBody(text, threadId) {
                    $log.info('Will now format the thread: ');
                    $log.debug("threadBody" + threadId);
                    document.getElementById("threadBody" + threadId).innerHTML = text;
                }

                vm.getRectXY('div2');
        */








    }
})();