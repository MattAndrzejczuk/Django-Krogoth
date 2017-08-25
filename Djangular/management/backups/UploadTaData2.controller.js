(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, $mdDialog, $mdToast, $timeout, $scope) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        vm.selectedFbi = {};
        vm.selectedTdf = {};
        vm.currentNavItem = 'page1';
        vm.filteredByJsonified = false;
        vm.filterSet = '';
        vm.status = '';

        vm.dtInstance = {};
        vm.selectedDtRow = '';
        vm.dtOptions = {
            dom: '<"top"f>rt<"bottom"<"left"<"length"l>><"right"<"info"i><"pagination"p>>>',
            pagingType: 'simple',
            autoWidth: false,
            responsive: true
        };
        vm.selectedDtFileName = '';
        vm.selectedDtFileType = '';
        vm.selectedDirItems =
            [{
                "id": 1,
                "is_selected": false,
                "name": "MattsMod",
                "description": "A bunch of ArmPrime assets.",
                "created": "2017-08-11T13:01:11.575804Z",
                "author": 5
            }];

        vm.reloadDataREST = reloadDataREST;
        vm.popToast = popToast;
        vm.selectDtRow = selectDtRow;
        vm.selectDirectory = selectDirectory;
        vm.showDialog = showDialog;
        vm.thisControllerDidFullyLoad = false;
        vm.controllerIsReloading = false;
        vm.selected = {};

        function init() {
            vm.popToast('initializing FUSE_APP_NAMEController...');
            var reload = function() {
                vm.reloadDataREST();
            }
            $timeout(reload, 2000);
        }

        function selectDirectory(index) {
            vm.selectedDirItems = vm.customMods['mod_paths'][index]['directories'];
            vm.selectedDirectory = index;
            vm.dtInstance.rerender();
            vm.dtInstance.reloadData();
            if (name) {
                vm.selectedDirectory = name;
            }
        }

        function selectDtRow(id) {
            vm.controllerIsReloading = true;
            var patchData = {
                "is_selected": true
            }
            $http({
                method: 'PATCH',
                data: patchData,
                url: '/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/' + id + '/'
            }).then(function successCallback(response) {
                vm.reloadDataREST();
                vm.controllerIsReloading = false;
            }, function errorCallback(response) {
                $log.log(' ERROR FAIL ! ! ! ');
                $log.log(response);
            });
        }


        function reloadDataREST() {
            $http({
                method: 'GET',
                url: '/LazarusDatabase/TotalAnnihilation/SelectedAssetUploadRepository/'
            }).then(function successCallback(response) {
                vm.selectedDirItems = response.data['results'];
                $log.log('selectedDirItems: len ' + vm.selectedDirItems.length);
                $log.log(vm.selectedDirItems);
                for (var i = 0; i < vm.selectedDirItems.length; i++) {
                    if (vm.selectedDirItems[i]['is_selected'] === true) {
                        $log.debug('selectedDirItems[' + i + ']');
                        $log.debug(vm.selectedDirItems[i]);
                        vm.selected = vm.selectedDirItems[i];
                    } else {
                        $log.info('selectedDirItems[' + i + ']');
                        $log.info(vm.selectedDirItems[i]);
                    }
                }

                vm.popToast('reloading data...');
                vm.dtInstance.rerender();
                vm.dtInstance.reloadData();
                vm.thisControllerDidFullyLoad = true;
            }, function errorCallback(response) {
                vm.popToast('Failed to load selected upload repositories.');
            });
        }

        function popToast(msg) {
            $mdToast.show(
                $mdToast.simple()
                .textContent(msg)
                .position('bottom right')
                .hideDelay(3000)
            );
        }

        /*
                function showDialog($event) {
                    var parentEl = angular.element(document.body);
                    $mdDialog.show({
                        parent: parentEl,
                        targetEvent: $event,
                        template: '<md-dialog aria-label="List dialog">' +
                            '  <md-dialog-content>' +
                            '	<iframe width="600" height="500" src="/SandboxDB/UploadDataTA/"></iframe>'
                        '    <md-list>' +
                        '      <md-list-item ng-repeat="item in items">' +
                        '       <p>Number {{item}}</p>' +
                        '      ' +
                        '    </md-list-item></md-list>' +
                        '  </md-dialog-content>' +
                        '  <md-dialog-actions>' +
                        '    <md-button ng-click="closeDialog()" class="md-primary">' +
                        '      Close Dialog' +
                        '    </md-button>' +
                        '  </md-dialog-actions>' +
                        '</md-dialog>',
                        locals: {
                            items: $scope.items
                        },
                        controller: DialogController
                    });
                }
        */

        function showDialog($event) {
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
                controller: GreetingController,
                onComplete: afterShowAnimation,
                locals: {
                    repositorySelectedSQL: vm.selected['name']
                }
            });
            // When the 'enter' animation finishes...
            function afterShowAnimation(scope, element, options) {
                // post-show code here: DOM element focus, etc.
                vm.popToast('Go to the HPI Directory Explorer to process units contained ' +
                    ' within your uploads.'
                );
            }
        }

        function GreetingController($scope, $mdDialog, repositorySelectedSQL) {
            // Assigned from construction <code>locals</code> options...
            $scope.repositoryFromOutside = repositorySelectedSQL;
            $scope.closeDialog = function() {
                // Easily hides most recent dialog shown...
                // no specific instance reference is needed.
                $mdDialog.hide();
            };
        }



        init();

    }


})();