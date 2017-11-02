(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, $mdDialog, $mdToast, $timeout, $scope, $cookies) {
        var vm = this;


        vm.controllerIsReloading = false;
        vm.uploadMiniControllerDidLoad = false;
        vm.newRepositoryEditorMode = false;
        vm.loadingDirectoryExplorer = true;


        vm.selectedDirItems = [];
        vm.userRepoItems = [];
        vm.newRepository = {};
        vm.allUserRepos = {};
        vm.selectedRepo = {};
        vm.selectedDirectory = 0;


        vm.selectDirectory = selectDirectory;
        vm.showFBIToSQLDialog = showFBIToSQLDialog;
        vm.popToastRepository = popToastRepository;
        vm.selectRepository = selectRepository;


        /// RESTful Methods
        vm.startUpload = startUpload;
        vm.newRepositoryRESTfulPOST = newRepositoryRESTfulPOST;
        vm.selectDtRepositoryRow = selectDtRepositoryRow;
        vm.reloadDataREST = reloadDataREST;
        vm.initDirectoryExplorerTabMiniCtrl = initDirectoryExplorerTabMiniCtrl;



        function initUploaderTabMiniCtrl() {
            var reload = function() {
                vm.reloadDataREST();
            };
            if (vm.uploadMiniControllerDidLoad === false) {
                $timeout(reload, 1000);
            }
            vm.uploadMiniControllerDidLoad = true;
        }


        initUploaderTabMiniCtrl();


        function selectRepository(index) {
            vm.userRepoItems = vm.customMods['mod_paths'][index]['directories'];
            vm.selectedDirectory = index;
            if (name) {
                vm.selectedDirectory = name;
            }
        }

        function selectDirectory(index) {
            if (vm.allUserRepos['mod_paths'][index]) {
                vm.selectedDirItems = vm.allUserRepos['mod_paths'][index]['directories'];
                vm.selectedDirectory = index;
            }
        }

        function popToastRepository(msg) {
            $mdToast.show(
                $mdToast.simple()
                .textContent(msg)
                .position('bottom right')
                .hideDelay(3000)
            );
        }


        function showFBIToSQLDialog($event, iframeUrlParam) {
            $mdDialog.show({
                targetEvent: $event,
                template: '<md-dialog>' +
                    '  <md-dialog-content class="md-background-fg md-hue-3"> Raw unit FBI, import it to your currently ' +
                    'selected mod project by clicking "Begin Reclaimation Process". ' +
                    'so that Arm Prime can process the unit dependencies. ' +
                    '<br>' +
                    /// '<iframe width="600" height="500" src="{{ RESTfulFBIiFrame }}"></iframe>' +
                    '<p class="md-background-fg md-hue-3"><b> status: {{ status }} </b></p>' +
                    '<p class="md-background-fg md-hue-3"> {{ info }} </p>' +
                    '<br>' +
                    '<pre class="md-accent-fg md-hue-3"> {{ rawResponse | json }} </pre> <br>' +
                    '<div id="responseLog" style="background-color: black"></div> <br>' +
                    '</md-dialog-content>' +
                    '  <md-dialog-actions>' +
                    '    <div layout="row" layout-align="center center" ng-if="status === \'BOOTING\'">' +
                    '        <md-progress-circular md-mode="indeterminate"></md-progress-circular>' +
                    '    </div>' +
                    '    <md-button ng-click="addModAsset()" class="md-accent">' +
                    '      Begin Reclaimation Process' +
                    '    </md-button>' +
                    '    <md-button ng-click="closeDialog()" class="md-warn">' +
                    '      cancel' +
                    '    </md-button>' +
                    '  </md-dialog-actions>' +
                    '</md-dialog>',
                controller: ConvertFBIToSQLController,
                onComplete: afterShowAnimation,
                locals: {
                    repositorySelectedSQL: vm.selectedRepo['name'],
                    iframeUrl: iframeUrlParam + '&repo_name=' + vm.selectedRepo['name']
                }
            });

            ///iframeUrl: iframeUrlParam.replace('LazarusII/UnitFBIViewset', 'LazarusPublisherTest/PhaseOneReclaim') + '&repo_name=' + vm.selectedRepo['name']
            function afterShowAnimation(scope, element, options) {}
        }

        function ConvertFBIToSQLController($scope, $mdDialog, repositorySelectedSQL,
            iframeUrl, $http) {
            $scope.repositoryFromOutside = repositorySelectedSQL;
            $scope.RESTfulFBIiFrame = iframeUrl;
            $scope.status = 'BOOTING';
            $scope.rawResponse = {};
            $scope.info = '';
            var waitForDialogToOpen = function() {
                $http({
                    method: 'GET',
                    url: iframeUrl
                }).then(function successCallback(response) {
                    $scope.rawResponse = response.data;
                    $scope.status = 'SUCCESS: ' + iframeUrl;
                    $scope.info = "Success! this unit's FBI data has been parsed and successfully saved " +
                        "to the database. To proceed, click the 'ADD MOD ASSET' button below. This will allow " +
                        "you to use this asset in your Mod Project.";
                }, function errorCallback(response) {
                    $scope.status = 'FAIL ';
                });
            };
            $timeout(waitForDialogToOpen, 1000);
            $scope.addModAsset = function() {
                $http({
                    method: 'GET',
                    url: '/LazarusIII/DependenciesForUnitFBI/?uid=' + $scope.rawResponse[0]['_SNOWFLAKE']
                }).then(function successCallback(response) {
                    $scope.rawResponse = {};
                    var logDiv = document.getElementById("responseLog");
                    logDiv.innerHTML = response.data;
                }, function errorCallback(response) {});
            };
            $scope.closeDialog = function() {
                $mdDialog.hide();
            };
        }


        function startUpload() {
            var fileInputField = document.getElementById('file_input');
            var file = fileInputField.files[0];
            var data = new FormData();
            data.append("upload", file);
            data.append("name", file.name);
            data.append("size", file.size);
            data.append("type", file.name.slice(-3));
            $log.debug('STARTING UPLOAD...');
            var xhr = new XMLHttpRequest();
            xhr.withCredentials = true;
            xhr.addEventListener("readystatechange", function() {
                if (this.readyState === 4) {
                    console.log(this.responseText);
                    vm.popToastRepository(this.responseText);
                }
            });
            xhr.open("POST", "/LazarusDatabase/TotalAnnihilation/Upload/");
            xhr.setRequestHeader("authorization", "Token " + $cookies.get('token'));
            xhr.send(data);
        }

        function newRepositoryRESTfulPOST() {
            vm.userRepoItems = [];
            vm.controllerIsReloading = true;
            var postData = {
                "is_selected": false,
                "name": vm.newRepository.name,
                "description": vm.newRepository.description
            };
            $log.log('/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/');
            $http({
                method: 'POST',
                data: postData,
                url: '/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/'
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
            $log.log('/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/');
            $http({
                method: 'PATCH',
                data: patchData,
                url: '/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/' + id + '/'
            }).then(function successCallback(response) {
                vm.reloadDataREST();
                vm.controllerIsReloading = false;
                $timeout(vm.initDirectoryExplorerTabMiniCtrl, 2000);
            }, function errorCallback(response) {
                var msg = 'Failed to update repository.';
                vm.popToastRepository(msg);
            });
        }

        function reloadDataREST() {
            $log.log('/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/');
            $http({
                method: 'GET',
                url: '/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/'
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
            }, function errorCallback(response) {
                vm.popToastRepository('Failed to load selected upload repositories.');
            });
        }


        function initDirectoryExplorerTabMiniCtrl() {
            $log.log('/LazarusII/ExecuteBash_LS_AllCustomModFiles/?mod_repo=' + vm.selectedRepo['name']);
            vm.loadingDirectoryExplorer = false;
            if (vm.selectedRepo) {
                $http({
                    method: 'GET',
                    url: '/LazarusII/ExecuteBash_LS_AllCustomModFiles/?mod_repo=' + vm.selectedRepo['name']
                }).then(function successCallback(response) {
                    var autoSelectDefaultDirectory = function() {
                        vm.selectDirectory(0);
                        vm.loadingDirectoryExplorer = false;
                    };
                    vm.allUserRepos = response.data;
                    $timeout(autoSelectDefaultDirectory, 1000);
                }, function errorCallback(response) {
                    vm.allUserRepos = {
                        "FAIL": [],
                        "SOMETHING BROKE": []
                    };
                });
            } else {
                vm.popToastRepository('You need to select a repository first.');
            }
        }


        /* DIRECTORY EXPLORER FOR HPI FILES */
    }
})();