(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, $mdToast, $timeout, $scope, $mdDialog) {
        var vm = this;

        /* UPLOAD MINI-CONTROLLER */
        function initUploaderTabMiniCtrl() {
            /// This controller will boot up here:
            var reload = function() {
                vm.reloadDataREST();
            }
            if (vm.uploadMiniControllerDidLoad === false) {
                vm.popToastRepository('initializing FUSE_APP_NAMEController...');
                $timeout(reload, 2000);
            }
            vm.uploadMiniControllerDidLoad = true;
        }

        var defaultTabName = document.getElementById("DjangularMetaText_01").innerHTML;
        document.getElementById("DjangularMetaText_01").innerHTML = 'ArmPrime Mods';

        /*
                vm.dtUploaderInstance = {};
                vm.dtUploaderOptions = {
                    dom: '<"top"f>rt<"bottom"<"left"<"length"l>><"right"<"info"i><"pagination"p>>>',
                    pagingType: 'simple',
                    autoWidth: false,
                    responsive: true,
                    order: [1, 'desc']
                };
        */
        vm.userRepoItems = [];
        vm.thisControllerDidFullyLoad = false;
        vm.controllerIsReloading = false;
        vm.selectedRepo = {};

        vm.reloadDataREST = reloadDataREST;
        vm.popToastRepository = popToastRepository;
        vm.selectDtRepositoryRow = selectDtRepositoryRow;
        vm.selectRepository = selectRepository;
        vm.uploadMiniControllerDidLoad = false;
        vm.newRepositoryRESTfulPOST = newRepositoryRESTfulPOST;
        vm.newRepositoryEditorMode = false;
        vm.newRepository = {};
        /// vm.initUploaderTabMiniCtrl = initUploaderTabMiniCtrl;
        function selectRepository(index) {
            vm.userRepoItems = vm.customMods['mod_paths'][index]['directories'];
            vm.selectedDirectory = index;
            //vm.dtUploaderInstance.rerender();
            //vm.dtUploaderInstance.reloadData();
            if (name) {
                vm.selectedDirectory = name;
            }
        }

        function newRepositoryRESTfulPOST() {
            vm.userRepoItems = [];
            vm.controllerIsReloading = true;
            var postData = {
                "is_selected": false,
                "name": vm.newRepository.name,
                "description": vm.newRepository.description
            };
            $http({
                method: 'POST',
                data: postData,
                url: '/LazarusDatabase/TotalAnnihilation/LazarusModProject/'
            }).then(function successCallback(response) {
                vm.reloadDataREST();
                vm.controllerIsReloading = false;
                vm.newRepository = {};
            }, function errorCallback(response) {
                var msg = 'Server has failed to create a new repository, make sure the name you\'ve selected is unique.';
                vm.popToastRepository(msg);
                vm.newRepository = {};
            });
        }

        function selectDtRepositoryRow(id) {
            vm.userRepoItems = [];
            vm.controllerIsReloading = true;
            var patchData = {
                "is_selected": true
            };
            $http({
                method: 'PATCH',
                data: patchData,
                url: '/LazarusDatabase/TotalAnnihilation/LazarusModProject/' + id + '/'
            }).then(function successCallback(response) {
                vm.reloadDataREST();
                vm.controllerIsReloading = false;
            }, function errorCallback(response) {
                var msg = 'Failed to update repository.';
                vm.popToastRepository(msg);
            });
        }

        function reloadDataREST() {
            $http({
                method: 'GET',
                url: '/LazarusDatabase/SelectedModProjectsList/'
            }).then(function successCallback(response) {
                vm.userRepoItems = response.data['results'];
                for (var i = 0; i < vm.userRepoItems.length; i++) {
                    if (vm.userRepoItems[i]['is_selected'] === true) {
                        vm.selectedRepo = vm.userRepoItems[i];
                    } else {
                        $log.info('userRepoItems[' + i + ']');
                        $log.info(vm.userRepoItems[i]);
                    }
                }
                // vm.dtUploaderInstance.rerender();
                // vm.dtUploaderInstance.reloadData();
                vm.thisControllerDidFullyLoad = true;
            }, function errorCallback(response) {
                vm.popToastRepository('Failed to load selected upload repositories.');
            });
        }

        function popToastRepository(msg) {
            $mdToast.show(
                $mdToast.simple()
                .textContent(msg)
                .position('bottom right')
                .hideDelay(3000)
            );
        }

        vm.reloadMods = reloadMods;

        function reloadMods() {
            $http({
                method: 'GET',
                url: '/LazarusDatabase/SelectedModProject/'
            }).then(function successCallback(response) {
                vm.userRepoItems = response.data['results'];
                vm.popToastRepository('Mods have been reloaded!');
                for (var i = 0; i < vm.userRepoItems.length; i++) {
                    if (vm.userRepoItems[i]['is_selected'] === true) {
                        vm.selectedRepo = vm.userRepoItems[i];
                    } else {
                        $log.info('userRepoItems[' + i + ']');
                        $log.info(vm.userRepoItems[i]);
                    }
                }
                // vm.dtUploaderInstance.rerender();
                // vm.dtUploaderInstance.reloadData();
                vm.thisControllerDidFullyLoad = true;
            }, function errorCallback(response) {
                vm.popToastRepository('Failed to load selected upload repositories.');
            });
        }

        initUploaderTabMiniCtrl();







        vm.initGridModel = initGridModel;

        function initGridModel() {
            vm.publishedMods = [{
                info: "Alpha",
                build: '0.1',
                compatibility: 'v3.1'
            }, {
                info: "Alpha",
                build: '0.2',
                compatibility: 'v3.1'
            }, {
                info: "Alpha",
                build: '0.3',
                compatibility: 'v3.1'
            }, {
                info: "Public Beta",
                build: '0.4',
                compatibility: 'v3.9.02'
            }, {
                info: "Release Candidate",
                build: '1.0',
                compatibility: 'v3.9.02'
            }];
            vm.panel_ModEditorList = buildGridModel_ModEditorList({
                icon: "avatar:svg-",
                title: "Svg-",
                background: "md-amber-bg"
            }, vm.userRepoItems.length);
        }

        function buildGridModel_ModEditorList(tileTmpl, totalTiles) {
            var it = [];
            var results = [];
            for (var j = 0; j < totalTiles; j++) {
                it = angular.extend({}, tileTmpl);
                it.icon = 'icon-cloud-download' ///it.icon + (j + 1);
                it.title = vm.publishedMods[j].build + ' ' + vm.publishedMods[j].info;
                it.universalCompatibility = (vm.publishedMods[j].compatibility === 'v3.9.02');
                it.background = "md-background-bg md-hue-3";
                it.span = {
                    row: 1,
                    col: 1
                };
                /*
                switch (j + 1) {
                    case 1:
                        it.background = "md-accent-bg md-hue-1";
                        it.title = 'Initial Build';
                        break; 
                    case 2:
                        it.background = "md-accent-bg md-hue-1";
                        it.title = 'WEAPON EDITOR';
                        break;
                    case 3:
                        it.background = "md-accent-bg md-hue-1";
                        it.title = 'TECH TREE EDITOR';
                        break;
                }
				*/
                results.push(it);
            }
            return results;
        }







    }
})();