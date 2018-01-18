(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $state) {
        var vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';
        vm.viewDidLoad = viewDidLoad;

		vm.initLazyModule = initLazyModule;
		vm.stateGoToLazy = stateGoToLazy;

        function onInit() {
            console.log('FUSE_APP_NAME did finish loading');
            vm.viewDidLoad();
        }

        function viewDidLoad() {
			$('<p>Welcome.</p><br>').appendTo('ak-main');
        }

    }
})();

// Name:
// LAZYMVC_THING

// We will load: LAZYMVC_UNLOADED

// COMPILED HTML:
////krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME

// COMPILED JAVASCRIPT:
////krogoth_gantry/DynamicJavaScriptInjector/?name=FUSE_APP_NAME