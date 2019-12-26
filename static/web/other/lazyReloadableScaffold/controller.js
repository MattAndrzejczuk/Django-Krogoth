(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($scope, $state, $ocLazyLoad) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.lazarusVersion = document.getElementById("krogoth_gantryVersion").innerHTML.replace('krogoth_gantry ', '');



        vm.lazyToken = "_SPLIT_seed_" + (Math.floor(Math.random() * 99) + 1).toString();
		vm.stateParameters = {};

        vm.lazyReloadThisCtrl = lazyReloadThisCtrl;
        vm.redirectAfterLoading = redirectAfterLoading;






        $scope.$on('ocLazyLoad.moduleLoaded', function (e, module) {
        	console.log("e: ");
        	console.log(e);
        	console.log("module: ");
        	console.log(module);
        	let nameWithoutToken = "app.FUSE_APP_NAME".split("_SPLIT_")[0];
            const validAutoRedirect = nameWithoutToken + vm.lazyToken;
            vm.redirectAfterLoading(validAutoRedirect);
        });

        function redirectAfterLoading(validAutoRedirect) {
            $state.go(validAutoRedirect, vm.stateParameters);
        }

        function lazyReloadThisCtrl() {
			let nameWithoutToken = "FUSE_APP_NAME".split("_SPLIT_")[0];
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + nameWithoutToken + '&lazy=' +
				vm.lazyToken + '&ov=file.js');
        }

    }
})();