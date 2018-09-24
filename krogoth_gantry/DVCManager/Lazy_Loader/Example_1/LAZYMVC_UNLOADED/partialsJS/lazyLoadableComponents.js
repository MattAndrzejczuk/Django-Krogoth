vm.viewDidLoad = viewDidLoad;

        vm.initLazyModule = initLazyModule;
        vm.stateGoToLazy = stateGoToLazy;


        vm.initTokenizedLazyModule = initTokenizedLazyModule;
        vm.initAndGo = initAndGo;
        vm.redirectAfterLoading = redirectAfterLoading;

        vm.unloadedMasterName = "LAZYMVC_UNLOADED";
        vm.moduleTokenPrefix = "app." + vm.unloadedMasterName;

        vm.redirectEnabled = false;
        vm.log = log;

		vm.randomReloadSeed = "V" + (Math.floor(Math.random() * 999999) + 1).toString() + "M";



		function onInit() {
            console.log('FUSE_APP_NAME did finish loading');
            vm.viewDidLoad();
			
			$timeout(function(){
				vm.lazyToken = vm.randomReloadSeed;
			}, 1000);
        }

        function viewDidLoad() {
            $('<p>Newly Loaded Dynamic Master View Controllers Will Appear Below.</p><br>').appendTo('ak-main');
        }

        function initLazyModule() {
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' +
                vm.unloadedMasterName + '&ov=file.js');
            vm.log(vm.unloadedMasterName);
        }

        function initTokenizedLazyModule() {
            vm.redirectEnabled = false;
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' +
                vm.unloadedMasterName + '&lazy=' + vm.lazyToken + '&ov=file.js');
            vm.log(vm.lazyToken);
        }

        function initAndGo() {
            vm.redirectEnabled = true;
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' +
                vm.unloadedMasterName + '&lazy=' + vm.lazyToken + '&ov=file.js');
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