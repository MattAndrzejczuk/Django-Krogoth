(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, $mdDialog, $mdToast, $timeout, $scope, $cookies) {
        var vm = this;

        /* UPLOAD MINI-CONTROLLER */
        function initUploaderTabMiniCtrl() {
            /// This controller will boot up here:
            var reload = function() {
                vm.reloadDataREST();
            }
            if (vm.uploadMiniControllerDidLoad === false) {
                vm.popToastRepository('initializing FUSE_APP_NAMEController...');
                $timeout(reload, 1000);
            }
            vm.uploadMiniControllerDidLoad = true;
        }
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
        vm.showUploadDialog = showUploadDialog;
        vm.uploadMiniControllerDidLoad = false;
        vm.newRepositoryRESTfulPOST = newRepositoryRESTfulPOST;
        vm.newRepositoryEditorMode = false;
        vm.newRepository = {};
        vm.startUpload = startUpload;



        function startUpload() {
            var fileInputField = document.getElementById('file_input');
            var file = fileInputField.files[0];
            var data = new FormData();
            data.append("upload", file);
            data.append("name", file.name);
            data.append("size", file.size);
            data.append("type", file.name.slice(-3));
            //data.append("lastModifiedDate",
            //    file.lastModifiedDate.toString().slice(-4) + '000000Z');
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
            $http({
                method: 'PATCH',
                data: patchData,
                url: '/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/' + id + '/'
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
                //vm.dtUploaderInstance.rerender();
                //vm.dtUploaderInstance.reloadData();
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

        function showUploadDialog($event) {
            $mdDialog.show({
                targetEvent: $event,
                template: '<md-dialog>' +
                    '  <md-dialog-content>Upload file to ' +
                    '{{ repositoryFromOutside }}!' +
                    '<br>' +
                    '<iframe width="600" height="500" src="/SandboxDB/UploadDataTA/"></iframe>' +
                    '</md-dialog-content>' +
                    '  <md-dialog-actions>' +
                    '    <md-button ng-click="closeDialog()" class="md-primary">' +
                    '      exit' +
                    '    </md-button>' +
                    '  </md-dialog-actions>' +
                    '</md-dialog>',
                controller: UploadController,
                onComplete: afterShowAnimation,
                locals: {
                    repositorySelectedSQL: vm.selectedRepo['name']
                }
            });

            function afterShowAnimation(scope, element, options) {
                /// Dialog finished appearing, do something here...
            }
        }

        function UploadController($scope, $mdDialog, repositorySelectedSQL) {
            $scope.repositoryFromOutside = repositorySelectedSQL;
            $scope.closeDialog = function() {
                $mdDialog.hide();
            };
        }

        /* UPLOAD CONTROLLER */


        /* DIRECTORY EXPLORER FOR HPI FILES */
        function initDirectoryExplorerTabMiniCtrl() {
            vm.loadingDirectoryExplorer = false;
            /// This controller will boot up here:
            /// $log.log('Making request to view all uploads: ');
            /// $log.log('/LazarusII/ExecuteBash_LS_AllCustomModFiles/?mod_repo=' + vm.selectedRepo['name']);

            if (vm.selectedRepo) {
                $http({
                    method: 'GET',
                    url: '/LazarusII/ExecuteBash_LS_AllCustomModFiles/?mod_repo=' + vm.selectedRepo['name']
                }).then(function successCallback(response) {
                    var autoSelectDefaultDirectory = function() {
                        vm.selectDirectory(0);
                        vm.loadingDirectoryExplorer = false;
                    };
                    vm.customMods = response.data;
                    $timeout(autoSelectDefaultDirectory, 1000);
                }, function errorCallback(response) {
                    vm.customMods = {
                        "FAIL": [],
                        "SOMETHING BROKE": []
                    };
                });
            } else {
                vm.popToastRepository('You need to select a repository first.');
            }
        }

        vm.loadingDirectoryExplorer = true;
        vm.modRepoParameterRESTful = 'MattsMod';
        vm.showAdvancedDialog = showAdvancedDialog;
        vm.checkIfModIsSelected = checkIfModIsSelected;
        vm.requestFbiFile = requestFbiFile;
        vm.requestTdfFile = requestTdfFile;
        vm.selectDirectory = selectDirectory;
        vm.showSimpleToast = showSimpleToast;
        vm.selectDtRow = selectDtRow;
        vm.showFBIToSQLDialog = showFBIToSQLDialog;
        vm.selectedFbi = {};
        vm.selectedTdf = {};
        vm.currentNavItem = 'page1';
        vm.filteredByJsonified = false;
        vm.filterSet = '';
        vm.status = '';
        vm.showSimpleToast(window.innerWidth);
        // vm.dtInstance = {};
        vm.selectedDtRow = '';
        /*
        vm.dtOptions = {
            dom: '<"top"f>rt<"bottom"<"left"<"length"l>><"right"<"info"i><"pagination"p>>>',
            pagingType: 'simple',
            autoWidth: false,
            responsive: true,
            displayLength: 20
        };
		*/
        vm.selectedDtFileName = '';
        vm.selectedDtFileType = '';
        vm.selectedDirItems = [];
        vm.customMods = {
            "": [],
            "": []
        };
        vm.selectedDirectory = 0;
        vm.initDirectoryExplorerTabMiniCtrl = initDirectoryExplorerTabMiniCtrl;


        initUploaderTabMiniCtrl();
        vm.selectedModProject = {};

        function checkIfModIsSelected() {
            $log.log('THIS HAS CHANGED ! ! !');
            var getCurrentModProjectURL = '/LazarusDatabase/SelectedModProject/';
            $http({
                method: 'GET',
                url: getCurrentModProjectURL
            }).then(function successCallback(response) {
                vm.selectedModProject = response.data['results'];
                if (vm.selectedModProject.length > 0) {
                    vm.showSimpleToast('WARNING - You must create a New Mod Project to proceed!!!');
                }
            }, function errorCallback(response) {
                vm.customMods = {
                    "FAIL": [],
                    "SOMETHING BROKE": []
                };
            });
        }


        function selectDirectory(index) {
            if (vm.customMods['mod_paths'][index]) {
                vm.selectedDirItems = vm.customMods['mod_paths'][index]['directories'];
                vm.selectedDirectory = index;
                //vm.dtInstance.rerender();
                //vm.dtInstance.reloadData();
            } else {
                //vm.dtInstance.rerender();
                //vm.dtInstance.reloadData();
            }
            /// vm.selectedDirectory = name;
        }

        function DialogController($scope, $mdDialog, $http) {
            $scope.hide = function() {
                $mdDialog.hide();
            };
            $scope.cancel = function() {
                $mdDialog.cancel();
            };
            $scope.answer = function(answer) {
                $mdDialog.hide(answer);
            };
        }

        function showAdvancedDialog(ev, title, file_type, mod_path) {
            $mdDialog.show({
                    controller: DialogController,
                    templateUrl: '/dynamic_lazarus_page/OpenTADataFile/?type=' + file_type + '&title=' + title + '&encoded_path=' + mod_path.replace('/LazarusII/UnitFBIViewset/?encoded_path=', ''),
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    fullscreen: false
                })
                .then(function(answer) {
                    vm.status = 'You said the information was "' + answer + '".';
                    vm.showSimpleToast(vm.status);
                }, function() {
                    vm.status = 'You cancelled the dialog.';
                });
        }

        /*
         function showFBIToSQLDialog($event, iframeUrlParam) {
         $mdDialog.show({
         targetEvent: $event,
         template: '<md-dialog>' +
         '  <md-dialog-content> Raw unit FBI, add it to your {{ repositoryFromOutside }} repository ' +
         'so that Arm Prime can process the unit dependencies. ' +
         '<br>' +
         '<iframe width="600" height="500" src="{{ RESTfulFBIiFrame }}"></iframe>' +
         '</md-dialog-content>' +
         '  <md-dialog-actions>' +
         '    <md-button ng-click="closeDialog()" class="md-accent">' +
         '      add to {{ repositoryFromOutside }} Repository' +
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

         function afterShowAnimation(scope, element, options) {
         vm.popToastRepository('Go to the HPI Directory Explorer to process units contained ' +
         ' within your uploads.'
         );
         }
         }
         */
        function showFBIToSQLDialog($event, iframeUrlParam) {
            $mdDialog.show({
                targetEvent: $event,
                template: '<md-dialog>' +
                    '  <md-dialog-content class="md-background-fg md-hue-3"> Raw unit FBI, add it to your {{ repositoryFromOutside }} repository ' +
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
                    '      Add To Project' +
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

            function afterShowAnimation(scope, element, options) {
                vm.popToastRepository('Go to the HPI Directory Explorer to process units contained ' +
                    ' within your uploads.'
                );
            }
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
                    $scope.status = 'SUCCESS';
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
                    url: '/LazarusIII/DependenciesForUnitFBI/?uid=' + $scope.rawResponse[0]['UnitName']
                }).then(function successCallback(response) {
                    // this callback will be called asynchronously
                    // when the response is available
                    $scope.rawResponse = {};
                    var logDiv = document.getElementById("responseLog");
                    logDiv.innerHTML = response.data;
                }, function errorCallback(response) {
                    // called asynchronously if an error occurs
                    // or server returns response with an error status.
                });
            };

            $scope.closeDialog = function() {
                $mdDialog.hide();
            };
        }

        function showSimpleToast(msg) {
            $mdToast.show(
                $mdToast.simple()
                .textContent(msg)
                .position('bottom right')
                .hideDelay(3000)
            );
        }

        function requestFbiFile(hpi_name, fbi_name) {
            $http({
                method: 'GET',
                url: '/LazarusII/OpenTotalAnnihilationFBIFileII/?mod_name=' + hpi_name + '&file_name=' + fbi_name
            }).then(function successCallback(response) {
                vm.selectedFbi = response.data;
                $log.log(response.data);
            }, function errorCallback(response) {
                $log.log(' ERROR FAIL ! ! ! ');
                $log.log(response);
            });
        }

        function requestTdfFile(hpi_name, file_name) {
            $http({
                method: 'GET',
                url: '/LazarusII/WeaponTDFViewset/?mod_name=' + hpi_name + '&file_name=' + file_name
            }).then(function successCallback(response) {
                vm.selectedTdf = response.data;
                $log.log(response.data);
            }, function errorCallback(response) {
                $log.log(' ERROR FAIL ! ! ! ');
                $log.log(response);
            });
        }

        function selectDtRow(file_name, file_type) {
            vm.selectedDtFileName = file_name;
            vm.selectedDtFileType = file_type;
            $log.debug('YOU HAVE SELECTED: ');
            $log.log(file_name + file_type);
            if (file_type === '.fbi') {
                $http({
                    method: 'GET',
                    url: '/LazarusII/UnitFBIViewset/?mod_name=' + file_name + '&file_name=' + file_name
                }).then(function successCallback(response) {
                    vm.selectedFbi = response.data;
                    $log.log(response.data);
                }, function errorCallback(response) {
                    $log.log(' ERROR FAIL ! ! ! ');
                    $log.log(response);
                });
            } else {
                $http({
                    method: 'GET',
                    url: '/LazarusII/UnitFBIViewset/?mod_name=' + file_name + '&file_name=' + file_name
                }).then(function successCallback(response) {
                    vm.selectedFbi = response.data;
                    $log.log(response.data);
                }, function errorCallback(response) {
                    $log.log(' ERROR FAIL ! ! ! ');
                    $log.log(response);
                });
            }
        }

        /* DIRECTORY EXPLORER FOR HPI FILES */
    }
})();