(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdSidenav, $log, $http, $mdToast, $mdDialog, $scope, $mdMenu) {
        var vm = this;


        vm.viewName = 'FUSE_APP_NAME';

        document.getElementById("DjangularMetaText_01").innerHTML = 'Lazarus Unit Editor';

        vm.accounts = {
            'creapond': 'johndoe@creapond.com',
            'withinpixels': 'johndoe@withinpixels.com'
        };

        vm.selectedAccount = 'creapond';
        vm.currentView = 'list';
        vm.showDetails = true;

        vm.selectedMod = 'totala_files2';
        vm.isLoadingMod = false;

        vm.searchTextCustom = '';
        $scope.searchText = 'a';
        $log.log('FUSE_APP_NAMEController');

        vm.path = 'just a sample path';
        vm.folders = [];
        vm.files = [];


        vm.selected = vm.files[0];

        //vm.fileAdded = fileAdded;
        vm.select = select;
        vm.toggleDetails = toggleDetails;
        vm.toggleSidenav = toggleSidenav;
        vm.toggleView = toggleView;

        vm.dialogShowRawFbi = dialogShowRawFbi;

        vm.isDlgOpen = false;
        vm.closeToast = closeToast;
        vm.showCustomToast = showCustomToast;

        vm.selectedMod = '';


        vm.showFbiEditForm = showFbiEditForm;

        function showFbiEditForm($event, fbiId) {
            $http({
                method: 'GET',
                url: '/Djangular/DjangularModelForm/?model_name=UnitFbiData&model_id=' + fbiId
            }).then(function successCallback(response) {
                vm.playSoundClickSkirmish();
                var dialogHtmlBody = response.data;
                $mdDialog.show({
                    targetEvent: $event,
                    template: '<md-dialog>' +
                        '<md-toolbar>' +
                        '<div class="md-toolbar-tools">' +

                        '<span flex="10"></span>' +
                        '<md-checkbox ng-model="filter.cbCombat" aria-label="Combat">' +
                        '<span class="md-background-fg md-hue-3">Combat</span>' +
                        '</md-checkbox>' +

                        '<md-checkbox ng-model="filter.cbOther" aria-label="Misc">' +
                        '<span class="md-background-fg md-hue-3">Misc</span>' +
                        '</md-checkbox>' +

                        '<md-checkbox ng-model="filter.cbResources" aria-label="Misc">' +
                        '<span class="md-background-fg md-hue-3">Resources</span>' +
                        '</md-checkbox>' +

                        '<md-checkbox ng-model="filter.cbPathfinder" aria-label="Misc">' +
                        '<span class="md-background-fg md-hue-3">Pathfinder</span>' +
                        '</md-checkbox>' +

                        '<md-checkbox ng-model="filter.cbNameInfo" aria-label="Misc">' +
                        '<span class="md-background-fg md-hue-3">NameInfo</span>' +
                        '</md-checkbox>' +

                        '<span flex></span>' +
                        '<md-button class="md-icon-button" ng-click="closeDialog()">' +
                        '<md-icon class="icon-window-close" aria-label="Close dialog"></md-icon>' +
                        '</md-button>' +
                        '</div>' +
                        '</md-toolbar>' +
                        '<md-dialog-content class="md-dialog-content" layout="column" style="width:1200px">' +
                        '<h5>{{titleFromOutside}}</h5>' +
                        '<br>' +
                        /// '<div class="md-dialog-content" layout="column" style="width:700px">' +
                        dialogHtmlBody +
                        /// '</div>' +
                        '</md-dialog-content>' +
                        '  <md-dialog-actions>' +
                        '    <md-button ng-click="saveChanges()" class="md-hover-button-blue-dialog">' +
                        '      save changes' +
                        '    </md-button>' +
                        '    <md-button ng-click="closeDialog()" class="md-hover-button-blue-dialog">' +
                        '      cancel' +
                        '    </md-button>' +
                        '  </md-dialog-actions>' +
                        '</md-dialog>',
                    controller: FBIEditorController,
                    onComplete: afterShowAnimation,
                    locals: {
                        editorTitle: 'Edit Unit Data ' + fbiId,
                        unitId: fbiId
                    }
                });
            }, function errorCallback(response) {
                console.log(response.data);
                vm.showCustomToast('Failed to load FBI data.');
                vm.playSoundError();
            });

            function afterShowAnimation(scope, element, options) {
                /// Dialog finished appearing, do something here...
            }
        }

        function FBIEditorController($scope, $mdDialog, editorTitle, unitId) {
            $scope.filter = {};
            $scope.filter.cbCombat = true;
            $scope.filter.cbResources = false;
            $scope.filter.cbPathfinder = false;
            $scope.filter.cbConstruction = false;
            $scope.filter.cbNameInfo = false;
            $scope.filter.cbOther = false;

            $scope.unitId = unitId;
            $scope.titleFromOutside = editorTitle;
            $scope.djangularForm = {};
            $http({
                method: 'GET',
                url: '/LazarusII/serialized/FBISerialized/' + unitId + '/'
            }).then(function successCallback(response) {
                $scope.djangularForm = response.data;
            }, function errorCallback(response) {
                console.log(response.data);
            });
            $scope.closeDialog = function() {
                $mdDialog.hide();
            };
            $scope.saveChanges = function() {
                $http({
                    method: 'PUT',
                    data: $scope.djangularForm,
                    url: '/LazarusII/serialized/FBISerialized/' + $scope.unitId + '/'
                }).then(function successCallback(response) {
                    $mdDialog.hide();
                }, function errorCallback(response) {
                    console.log(response.data);
                });

            };
        }
        // vm.openMenuDropDown = openMenuDropDown;
        /**
         * Select an item
         *
         * @param item
         */
        function select(item) {
            console.log("YOU SELECTED A UNIT SON! ! !");
            console.log(item);
            var txtMsg = item["_DEV_root_data_path"];
            txtMsg = txtMsg.replace('/usr/src/persistent/', '');
            var path_raw_root = txtMsg.replace('/', '_SLSH_').replace('/', '_SLSH_').replace('/', '_SLSH_').replace('/', '_SLSH_').replace('.fbi', '');
            $mdToast.show($mdToast.simple().textContent(path_raw_root));
            var fbiViewSetEndpoint = '/LazarusII/UnitFBIViewset/?encoded_path=';
            $http({
                method: 'GET',
                url: fbiViewSetEndpoint + path_raw_root
            }).then(function successCallback(response) {
                vm.playSoundClickUnit();
                vm.selected = response.data[0];
                console.log(response.data[0]);
            }, function errorCallback(response) {
                console.log(response.data);
                showCustomToast('Failed to load unit, we will resolve this issue soon!');
                vm.playSoundError();
            });
        }


        vm.isLoadingMod = true;

        $http({
            method: 'GET',
            url: '/LazarusDatabase/UnitFBIFromSQLView/'
        }).then(function successCallback(response) {
            $log.log('vm.selectModNamed has been called ! ! !');
            $log.log(response.data);
            vm.files = response.data['list_response'];
            vm.selectedMod = response.data['mod'];
            vm.isLoadingMod = false;
            vm.playSoundModFinishedLoading();
        }, function errorCallback(response) {
            console.log(response.data);
            showCustomToast('Failed to load mod, we will resolve this issue soon!');
            vm.playSoundError();
            vm.isLoadingMod = false;
        });

        vm.customMods = {
            "": [],
            "": []
        };





        vm.playSoundError = playSoundError;
        vm.playSoundClickUnit = playSoundClickUnit;
        vm.playSoundClickSkirmish = playSoundClickSkirmish;
        vm.playSoundModFinishedLoading = playSoundModFinishedLoading;
        vm.playSoundClickUnitOrder = playSoundClickUnitOrder;

        vm.playSoundClickSkirmish();

        /// PLAY SOUND FX
        function playSoundError() {
            var audio = new Audio("/static/gui_sfx/alert_warn1.wav");
            audio.addEventListener('canplaythrough', function() {
                audio.play();
            }, false);
        }

        function playSoundClickUnit() {
            var audio = new Audio("/static/gui_sfx/click_select_units.wav");
            audio.addEventListener('canplaythrough', function() {
                audio.play();
            }, false);
        }

        function playSoundClickSkirmish() {
            var audio = new Audio("/static/gui_sfx/click_select_skirmish.wav");
            audio.addEventListener('canplaythrough', function() {
                audio.play();
            }, false);
        }

        function playSoundModFinishedLoading() {
            var audio = new Audio("/static/gui_sfx/click_side_arm.wav");
            audio.addEventListener('canplaythrough', function() {
                audio.play();
            }, false);
        }

        function playSoundClickUnitOrder($mdMenu, ev) {
            var audio = new Audio("/static/gui_sfx/click_unit_order.wav");
            audio.addEventListener('ended', function() {}, false);
            audio.addEventListener('canplaythrough', function() {
                audio.play();
            }, false);
            $mdMenu.open(ev);
        }
        /// PLAY SOUND FX
        function toggleDetails(item) {
            vm.selected = item;
            toggleSidenav('details-sidenav');
        }

        function toggleSidenav(sidenavId) {
            $mdSidenav(sidenavId).toggle();
        }

        function toggleView() {
            vm.currentView = vm.currentView === 'list' ? 'grid' : 'list';
        }

        function DialogController($scope, $mdDialog) {
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

        function dialogShowRawFbi(ev) {
            $mdDialog.show({
                    controller: DialogController,
                    templateUrl: 'http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=totala_files2&will_show_raw_fbi=pretty&unit_id=' + vm.selected['UnitName'],
                    parent: angular.element(document.body),
                    targetEvent: ev,
                    clickOutsideToClose: true,
                    fullscreen: $scope.customFullscreen
                })
                .then(function(answer) {
                    $scope.status = 'You said the information was "' + answer + '".';
                }, function() {
                    $scope.status = 'You cancelled the dialog.';
                });
        };

        function showCustomToast() {
            var msg = document.getElementById('search_params').value;
            $log.log(msg);
            vm.searchTextCustom = msg;
        }

        function closeToast() {
            if (vm.isDlgOpen) return;
            $mdToast
                .hide()
                .then(function() {
                    vm.isDlgOpen = false;
                    $log.info('TODO: add close sound effect here.');
                });
        }






    }
})();