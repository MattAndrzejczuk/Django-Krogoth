(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, $log, LazarusRESTfulCRUD) {
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
            LazarusRESTfulCRUD.getUnitFbiDetail(id).then(function(data) {
                vm.selectedUnitFbiDetail = data.results;
            });
        }

        function didClickRequestWeaponTdfRESTful(id) {
            LazarusRESTfulCRUD.selectedWeaponTdfDetail(id).then(function(data) {
                vm.selectedWeaponTdfDetail = data.results;
            });
        }

    }
})();