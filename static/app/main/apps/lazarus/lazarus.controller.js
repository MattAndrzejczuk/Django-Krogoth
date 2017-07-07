(function () {
    'use strict';

    angular
        .module('app.lazarus')
        .controller('LazarusController', LazarusController);

    /** @ngInject */
    function LazarusController($mdSidenav, $log, $http, $mdToast, $mdDialog, $scope, $mdMenu) {
        var vm = this;


        // Data
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
        $log.log('LazarusController');
        // $log.log(Documents);
        vm.path = 'just a sample path'; //Documents['arm_data'];
        vm.folders = []; // Documents.data['thumbnail'];
        vm.files = [
            {
                "MetalStorage": "0",
                "Acceleration": "0.086",
                "Weapon3": "CORMECH_ROCKET",
                "firestandorders": "1",
                "BadTargetCategory": "",
                "Builder": 0,
                "SightDistance": "425",
                "BMcode": "1",
                "SteeringMode": "2",
                "SelfDestructAs": "NUCLEAR_MISSILE",
                "Side": "ARM",
                "GermanDescription": "",
                "Corpse": "armbanth_dead",
                "BuildCostMetal": "18854",
                "canattack": "1",
                "NoChaseCategory": "",
                "MaxWaterDepth": "12",
                "FootprintX": "3",
                "MaxVelocity": "0.957",
                "ShootMe": "1",
                "DefaultMissionType": "Standby",
                "WorkerTime": "0",
                "MaxSlope": "17",
                "RadarDistance": "0",
                "wpri_badTargetCategory": "",
                "NoAutoFire": "0",
                "Category": "NOTAIR",
                "Objectname": "ARMBANTH",
                "canpatrol": "1",
                "Name": "Bantha",
                "ThreeD": "1",
                "EnergyStorage": "0",
                "StandingFireOrder": "2",
                "Designation": "ARM-KK",
                "Copyright": "Copyright 1997 Humongous Entertainment. All rights reserved.",
                "StandingMoveOrder": "1",
                "FrenchDescription": "",
                "MovementClass": "TANKDH3",
                "BuildTime": "262743",
                "ZBuffer": "1",
                "MaxDamage": "18918",
                "canmove": "1",
                "FootprintZ": "3",
                "UnitName": "ARMBANTH",
                "EnergyUse": "1.1",
                "SoundCategory": "KROGOTH",
                "TurnRate": "960",
                "Version": "1.2",
                "Weapon2": "ARMSEAP_WEAPON1",
                "canstop": "1",
                "canguard": "1",
                "UnitNumber": "10107",
                "Upright": "1",
                "maneuverleashlength": "640",
                "Weapon1": "CORATL_TORPEDO",
                "mobilestandorders": "1",
                "ExplodeAs": "MINE_HEAVY",
                "BrakeRate": "0.174",
                "Description": "experimenteller Sturm-Kbot",
                "BuildCostEnergy": "106567",
                "TEDClass": "KBOT",
                "EnergyMake": "1.1"
            }];
        vm.selected = vm.files[0];


        // Fuse Methods
        vm.fileAdded = fileAdded;
        vm.select = select;
        vm.toggleDetails = toggleDetails;
        vm.toggleSidenav = toggleSidenav;
        vm.toggleView = toggleView;

        // Open Unit FBI Data in Dialog
        vm.dialogShowRawFbi = dialogShowRawFbi;

        // ArmPrime Variables - Toast
        vm.isDlgOpen = false;

        // ArmPrime Methods - Toast
        vm.closeToast = closeToast;
        vm.openMoreInfo = openMoreInfo;
        vm.showCustomToast = showCustomToast;


        // ArmPrime Sound Effects
        vm.playSoundError = playSoundError;
        vm.playSoundClickUnit = playSoundClickUnit;
        vm.playSoundClickSkirmish = playSoundClickSkirmish;
        vm.playSoundModFinishedLoading = playSoundModFinishedLoading;


        vm.openMenuDropDown = openMenuDropDown;
        function openMenuDropDown($mdMenu, ev) {
            var audio = new Audio("/static/gui_sfx/click_unit_order.wav");
            audio.addEventListener('ended', function () {
            }, false);
            audio.addEventListener('canplaythrough', function () {
                audio.play();
            }, false);
            $mdMenu.open(ev);
        }

        

        function dialogShowRawFbi(ev) {
            // alert(vm.selected['JsonDump']['UnitName']);
            $mdDialog.show({
                controller: DialogController,
                templateUrl: 'http://52.27.28.55/LazarusII/UnitFbiData/?mod_name=totala_files2&will_show_raw_fbi=pretty&unit_id=' + vm.selected['UnitName'],
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose: true,
                fullscreen: $scope.customFullscreen // Only for -xs, -sm breakpoints.
            })
                .then(function (answer) {
                    $scope.status = 'You said the information was "' + answer + '".';
                }, function () {
                    $scope.status = 'You cancelled the dialog.';
                });
        };

        //
        function playSoundError() {
            var audio = new Audio("/static/gui_sfx/alert_warn1.wav");
            audio.addEventListener('canplaythrough', function () {
                audio.play();
            }, false);
        }

        function playSoundClickUnit() {
            var audio = new Audio("/static/gui_sfx/click_select_units.wav");
            audio.addEventListener('canplaythrough', function () {
                audio.play();
            }, false);
        }

        function playSoundClickSkirmish() {
            var audio = new Audio("/static/gui_sfx/click_select_skirmish.wav");
            audio.addEventListener('canplaythrough', function () {
                audio.play();
            }, false);
        }

        function playSoundModFinishedLoading() {
            var audio = new Audio("/static/gui_sfx/click_side_arm.wav");
            audio.addEventListener('canplaythrough', function () {
                audio.play();
            }, false);
        }


        function showCustomToast() {
            var msg = document.getElementById('search_params').value;
            $log.log(msg);
            vm.searchTextCustom = msg;
            // if (msg) {
            //     var final_msg = msg.replace(" ", "%20");
            //     $mdToast.show({
            //         hideDelay: 4000,
            //         position: 'bottom left',
            //         controller: 'ToastCtrl',
            //         templateUrl: '/LazarusII/CustomToast/?msg=' + final_msg
            //     });
            // }
        }


        function closeToast() {
            if (vm.isDlgOpen) return;

            $mdToast
                .hide()
                .then(function () {
                    vm.isDlgOpen = false;
                    $log.info('TODO: add close sound effect here.');
                });
        }


        function openMoreInfo(e) {
            // if (vm.isDlgOpen) return;

            vm.isDlgOpen = true;
            $mdDialog
                .show($mdDialog
                    .alert()
                    .title('More info goes here.')
                    .textContent('Something witty.')
                    .ariaLabel('More info')
                    .ok('Got it')
                    .targetEvent(e)
                )
                .then(function () {
                    vm.isDlgOpen = false;
                })
        }


        /**
         * File added callback
         * Triggers when files added to the uploader
         *
         * @param file
         */
        function fileAdded(file) {
            // Prepare the temp file data for file list
            // var uploadingFile = {
            //     id: file.uniqueIdentifier,
            //     file: file,
            //     type: '',
            //     owner: 'Emily Bennett',
            //     size: '',
            //     modified: moment().format('MMMM D, YYYY'),
            //     opened: '',
            //     created: moment().format('MMMM D, YYYY'),
            //     extention: '',
            //     location: 'My Files > Documents',
            //     offline: false,
            //     preview: '/static/assets/images/etc/sample-file-preview.jpg'
            // };

            var data = new FormData();
            data.append("file", file);

            var xhr = new XMLHttpRequest();
            xhr.withCredentials = true;

            xhr.addEventListener("readystatechange", function () {
                if (this.readyState === 4) {
                    console.log(this.responseText);
                }
            });

            xhr.open("POST", "/SandboxDB/UploadDataTA/");
            xhr.setRequestHeader("cache-control", "no-cache");
            xhr.setRequestHeader("postman-token", "51b775d3-214e-83a0-2e18-35a46f3cfeb4");
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

            xhr.send(data);

            // $http({
            //     method: 'POST',
            //     url: '/SandboxDB/UploadDataTA/',
            //     headers: {
            //         'Content-Type': undefined,
            //         'cache-control': 'no-cache'
            //     },
            //     data: {
            //         file: file
            //     },
            //     transformRequest: function (data, headersGetter) {
            //         var formData = new FormData();
            //         angular.forEach(data, function (value, key) {
            //             formData.append(key, value);
            //         });
            //         return formData;
            //     }
            // })
            //     .success(function () {
            //         showCustomToast('Upload Complete !');
            //     })
            //     .error(function () {
            //         showCustomToast('Failed to upload unit, we will resolve this issue soon!');
            //         vm.playSoundError();
            //     });

            // Append it to the file list
            // vm.files.push(uploadingFile);
        }


        /**
         * Select an item
         *
         * @param item
         */
        function select(item) {
            console.log(item);
            // Simple GET request example:

            $http({
                method: 'GET',
                url: '/LazarusII/UnitFbiData/?mod_name=' + vm.selectedMod + '&unit_id=' + item["UnitName"].toLowerCase()
            }).then(function successCallback(response) {
                vm.playSoundClickUnit();
                vm.selected = response.data[0];
                console.log(response.data[0]);
                // this callback will be called asynchronously
                // when the response is available
            }, function errorCallback(response) {
                console.log(response.data);
                showCustomToast('Failed to load unit, we will resolve this issue soon!');
                vm.playSoundError();
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        }

        vm.selectModNamed = selectModNamed;
        function selectModNamed(mod_name) {
            vm.playSoundClickSkirmish();
            vm.selectedMod = mod_name;
            vm.isLoadingMod = true;
            $http({
                method: 'GET',
                url: '/LazarusII/LazarusListUnits/?mod_name=' + vm.selectedMod
            }).then(function successCallback(response) {

                vm.files = response.data;
                vm.isLoadingMod = false;

                vm.playSoundModFinishedLoading();
                // this callback will be called asynchronously
                // when the response is available
            }, function errorCallback(response) {
                console.log(response.data);
                showCustomToast('Failed to load mod, we will resolve this issue soon!');
                vm.playSoundError();
                vm.isLoadingMod = false;
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        }


        /// /LazarusII/LazarusListUnits/?should_get_user_content=true&mod_name=
        vm.selectUploadedModNamed = selectUploadedModNamed;
        function selectUploadedModNamed(mod_name) {
            vm.playSoundClickSkirmish();
            vm.selectedMod = mod_name;
            vm.isLoadingMod = true;
            $http({
                method: 'GET',
                url: '/LazarusII/LazarusListUnits/?should_get_user_content=true&mod_name=' + vm.selectedMod
            }).then(function successCallback(response) {

                vm.files = response.data;
                vm.isLoadingMod = false;

                vm.playSoundModFinishedLoading();
                // this callback will be called asynchronously
                // when the response is available
            }, function errorCallback(response) {
                console.log(response.data);
                showCustomToast('Failed to load mod, we will resolve this issue soon!');
                vm.playSoundError();
                vm.isLoadingMod = false;
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        }

        vm.customMods = [];

        $http({
            method: 'GET',
            url: '/SandboxDB/UploadDataTA/'
        }).then(function successCallback(response) {
            $log.log(response.data);
            vm.customMods = response.data;
        }, function errorCallback(response) {
            // failed to load custom mods
            $log.log('FAIL ! ! !');
            $log.log(response.data);
        });

        /**
         * Toggle details
         *
         * @param item
         */
        function toggleDetails(item) {
            vm.selected = item;
            toggleSidenav('details-sidenav');
        }

        /**
         * Toggle sidenav
         *
         * @param sidenavId
         */
        function toggleSidenav(sidenavId) {
            $mdSidenav(sidenavId).toggle();
        }

        /**
         * Toggle view
         */
        function toggleView() {
            vm.currentView = vm.currentView === 'list' ? 'grid' : 'list';
        }

        function DialogController($scope, $mdDialog) {
            $scope.hide = function () {
                $mdDialog.hide();
            };

            $scope.cancel = function () {
                $mdDialog.cancel();
            };

            $scope.answer = function (answer) {
                $mdDialog.hide(answer);
            };
        }
    }
})();


(function () {
    'use strict';
    angular
        .module('app.toastCtrl',
            [
                // 3rd Party Dependencies
                'flow'
            ]
        );

})();

(function () {
    'use strict';
    angular
        .module('app.toastCtrl')
        .controller('ToastCtrl', ToastCtrl);
    /** @ngInject */
    function ToastCtrl($scope, $mdToast) {
        var vm = this;

        $scope.closeToast = function () {
            $mdToast.hide();
        };
    }
})();


/*

 THIS WILL NOW BE AUTOMAGICALLY GENERATED BY DJANGO

 (function () {
 'use strict';

 angular
 .module('app.lazarus',
 [
 // 3rd Party Dependencies
 'flow'
 ]
 )
 .config(config);

 /*
 function config($stateProvider, $translatePartialLoaderProvider, msApiProvider, msNavigationServiceProvider) {
 // State
 $stateProvider.state('app.dynamic_sample1', {
 url: '/dynamic_sample1',
 views: {
 'content@app': {
 templateUrl: '/static/app/main/apps/lazarus/lazarus.html',
 controller: 'LazarusController as vm'
 }
 },
 bodyClass: 'file-manager'
 });

 // Navigation
 msNavigationServiceProvider.saveItem('apps.dynamic_sample1', {
 title: 'Dynamic Sample 1',
 icon: 'icon-star',
 state: 'app.dynamic_sample1',
 weight: 5
 });
 }
 })();

 (function () {
 'use strict';
 angular
 .module('app.dynamic_sample1')
 .controller('DynamicSample1Ctrl', ToastCtrl);
 function DynamicSample1Ctrl($log) {
 var vm = this;
 $log.info('DynamicSample1Ctrl is online ! ! ! ');
 }
 })();
 */












