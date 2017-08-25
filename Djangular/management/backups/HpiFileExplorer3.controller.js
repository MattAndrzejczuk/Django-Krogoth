(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, $mdDialog, $mdToast) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        vm.showAdvancedDialog = showAdvancedDialog;
        vm.toggleJsonifiedFilter = toggleJsonifiedFilter;
        vm.requestFbiFile = requestFbiFile;
        vm.requestTdfFile = requestTdfFile;
        vm.selectDirectory = selectDirectory;
        vm.showSimpleToast = showSimpleToast;
        vm.selectDtRow = selectDtRow;


        vm.selectedFbi = {};
        vm.selectedTdf = {};
        vm.currentNavItem = 'page1';

        vm.filteredByJsonified = false;
        vm.filterSet = '';
        vm.status = '';

        vm.showSimpleToast(window.innerWidth);

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
                "mod_path": "media/ta_data/dictator/anims",
                "dir_type": "anims",
                "raw_data_tdf": "dictator_gadget.gaf",
                "file_name": "dictator_gadget",
                "file_type": ".gaf"
            }];
        vm.customMods = {
            "": [],
            "": []
        };
        vm.selectedDirectory = 0;


        function toggleJsonifiedFilter() {
            $log.log('THIS HAS CHANGED ! ! !');
            if (vm.filteredByJsonified) {
                vm.filterSet = 'Viewset/?encoded_path=';
            } else {
                vm.filterSet = '';
            }
        }

        function selectDirectory(index) {
            $log.debug('name');
            $log.log(name);
            $log.debug('vm.selectedDirItems');
            $log.log(vm.selectedDirItems);
            vm.selectedDirItems = vm.customMods['mod_paths'][index]['directories'];
            $log.debug('vm.customMods');
            $log.log(vm.customMods);
            $log.debug('vm.customMods[name]');
            $log.log(vm.customMods[name]);
            vm.selectedDirectory = index;
            vm.selectedDirectory = name;

            vm.dtInstance.rerender();
            vm.dtInstance.reloadData();
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

            $log.log('/dynamic_lazarus_page/OpenTADataFile/?type=' + file_type + '&title=' + title + '&encoded_path=' + mod_path.replace('/LazarusII/UnitFBIViewset/?encoded_path=', ''));
            $log.log(mod_path);
            $log.log(mod_path);
            $log.log(mod_path.replace('/LazarusII/UnitFBIViewset/?encoded_path=', ''));
            $log.log(mod_path.replace('/LazarusII/UnitFBIViewset/?encoded_path=', ''));


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
        };



        function showSimpleToast(msg) {
            $mdToast.show(
                $mdToast.simple()
                .textContent(msg)
                .position('bottom right')
                .hideDelay(3000)
            );
        };


        $http({
            method: 'GET',
            url: '/LazarusII/ExecuteBash_LS_AllCustomModFiles/'
        }).then(function successCallback(response) {
            vm.customMods = response.data;
            $log.log(response.data);
        }, function errorCallback(response) {
            vm.customMods = {
                "FAIL": [],
                "SOMETHING BROKE": []
            };
        });




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




    }
})();