(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $state, $ocLazyLoad, $scope) {
        var vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';
        vm.viewDidLoad = viewDidLoad;

        vm.initLazyModule = initLazyModule;
        vm.initLazyCanvasDemoModule = initLazyCanvasDemoModule;

        vm.initTokenizedLazyModule = initTokenizedLazyModule;
        vm.stateGoToLazy = stateGoToLazy;
        vm.initAndGo = initAndGo;
        vm.redirectAfterLoading = redirectAfterLoading;

        vm.unloadedMasterName = "LAZYMVC_UNLOADED";
        vm.moduleTokenPrefix = "app." + vm.unloadedMasterName;

        vm.redirectEnabled = false;
        vm.log = log;

        function onInit() {
            console.log('FUSE_APP_NAME did finish loading');
            vm.viewDidLoad();
        }

        function viewDidLoad() {
            $('<p>Welcome.</p><br>').appendTo('ak-main');
        }

        function initLazyModule() {
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + vm.unloadedMasterName + '&ov=file.js');
            vm.log(vm.unloadedMasterName);
        }

        function initLazyCanvasDemoModule() {
            const dvc_name = "HTML_To_Canvas";
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + dvc_name + '&ov=file.js');
        }

        function initTokenizedLazyModule() {
            vm.redirectEnabled = false;
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + vm.unloadedMasterName + '&lazy=' + vm.lazyToken + '&ov=file.js');
            vm.log(vm.lazyToken);
        }

        function initAndGo() {
            vm.redirectEnabled = true;
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + vm.unloadedMasterName + '&lazy=' + vm.lazyToken + '&ov=file.js');
            $state.go('app.' + vm.unloadedMasterName + vm.lazyToken);
        }

        $scope.$on('ocLazyLoad.moduleLoaded', function(e, module) {
            const validAutoRedirect = vm.moduleTokenPrefix + vm.lazyToken;
            if (validAutoRedirect === module.toString()) {
                vm.redirectAfterLoading(validAutoRedirect);
            }
        });

        function redirectAfterLoading(validAutoRedirect) {
            if (vm.redirectEnabled)
                $state.go(validAutoRedirect);
        }

        function stateGoToLazy() {
            $state.go('app.' + vm.unloadedMasterName);
        }



        function log(info) {
            $('<p>Loaded: ' + info + '.</p><br>').appendTo('ak-main');
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