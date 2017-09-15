(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, LazarusRESTfulCRUD, $mdMenu, $mdToast) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        ///$log.log('💜💙💚💛❤️  ✅⚠️❌');
        $log.log('⚠️ initializing FUSE_APP_NAME');

        vm.requestAllUnitFbiDataRESTful = requestAllUnitFbiDataRESTful;
        vm.requestSelectedModProjectRESTful = requestSelectedModProjectRESTful;
        vm.requestModAssetsRESTful = requestModAssetsRESTful;
        vm.didClickRequestUnitFbiRESTful = didClickRequestUnitFbiRESTful;
        vm.didClickRequestWeaponTdfRESTful = didClickRequestWeaponTdfRESTful;
        vm.didClickRequestAssetDependencies = didClickRequestAssetDependencies;
        vm.didClickPatchWeaponRequest = didClickPatchWeaponRequest;

        vm.weaponTdfPatchForm = {};

        vm.openMenu = openMenu;
        /// 
        vm.totalUnits = 0;
        vm.modName = '';
        vm.fbiData = [];
        vm.selectedModProject = {};

        vm.allModAssets = [];
        vm.selectedAssetDependencies = [];
        ///

        vm.selectedWeaponTdfDetail = {};
        vm.selectedUnitFbiDetail = {};

        vm.requestAllUnitFbiDataRESTful();

        $log.log('💜 ✴️ initializing FUSE_APP_NAME');

        function requestAllUnitFbiDataRESTful() {
            $log.log('💜 ⚠️ requestAllUnitFbiDataRESTful');
            LazarusRESTfulCRUD.getAllUnitFBIsFromSQL().then(function(data) {
                $log.log('💙 ✅ requestAllUnitFbiDataRESTful');
                vm.fbiData = data.list_response;
                vm.modName = data.mod;
                vm.requestSelectedModProjectRESTful();
            });
        }

        function requestSelectedModProjectRESTful() {
            $log.log('💙 ⚠️ requestSelectedModProjectRESTful');
            LazarusRESTfulCRUD.getSelectedModProject().then(function(data) {
                $log.log('💚 ✅ requestAllUnitFbiDataRESTful');
                vm.selectedModProject = data.results;
                vm.requestModAssetsRESTful();
            });
        }

        function requestModAssetsRESTful() {
            $log.log('💚 ⚠️ requestAllUnitFbiDataRESTful');
            LazarusRESTfulCRUD.getModAssets(vm.selectedModProject[0].id, true).then(function(data) {
                $log.log(data);
                $log.log('💛 ❌ requestAllUnitFbiDataRESTful');
                vm.allModAssets = data.results;
            }, function(fail) {
                $log.info(fail);
            });
        }

        function didClickRequestAssetDependencies(id) {
            $log.log('💛 ⚠️ didClickRequestAssetDependencies ' + id);
            LazarusRESTfulCRUD.getAssetDependencies(id).then(function(data) {
                $log.log('❤️ ❌ didClickRequestAssetDependencies');
                $log.debug(data);
                vm.selectedAssetDependencies = data.results;
            });
        }

        function didClickRequestUnitFbiRESTful(id) {
            $log.log("☢ ☢ ☢");
            $log.info("Did Click Request Unit FBI RESTful: " + id);
            LazarusRESTfulCRUD.getUnitFbiDetail(id).then(function(data) {
                $log.log(' Server Returned: ');
                vm.selectedUnitFbiDetail = data;
            });
        }

        function didClickRequestWeaponTdfRESTful(id) {
            $log.log('   Requesting Weapon TDF from REST: ' + id);
            $log.info('- - - - - -');
            LazarusRESTfulCRUD.getWeaponTdfDetail(id).then(function(data) {
                $log.log('');
                $log.debug(data);
                vm.selectedWeaponTdfDetail = data;
            });
        }

        function didClickPatchWeaponRequest() {
            var testString = 'property: ' + vm.weaponTdfPatchForm.property +
                ' value: ' + vm.weaponTdfPatchForm.value + ' key: ' + vm.selectedWeaponTdfDetail.id;
            $mdToast.show($mdToast.simple()
                .textContent(testString));
            /// patchWeaponTdf(id, key, value)
        }

        function openMenu($mdMenu, ev) {
            $mdMenu.open(ev);
        }



    }
})();