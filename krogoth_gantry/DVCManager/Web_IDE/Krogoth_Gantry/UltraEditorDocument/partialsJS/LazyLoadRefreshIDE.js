vm.lazyToken = "seed_" + (Math.floor(Math.random() * 99) + 1).toString();
vm.initAndGo = initAndGo;
vm.redirectAfterLoading = redirectAfterLoading;
vm.unloadedMasterName = "UltraEditorDocument";
vm.moduleTokenPrefix = "app." + vm.unloadedMasterName;

vm.stateParameters = {};

function initAndGo() {
	$ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=' + vm.unloadedMasterName + '&lazy=' + vm.lazyToken + '&ov=file.js');
}
$scope.$on('ocLazyLoad.moduleLoaded', function(e, module) {
	const validAutoRedirect = vm.moduleTokenPrefix + vm.lazyToken;
	vm.redirectAfterLoading(validAutoRedirect);
});
function redirectAfterLoading(validAutoRedirect) {
	$state.go(validAutoRedirect, vm.stateParameters);
}


vm.startStateTransition = startStateTransition;

function startStateTransition() {

	var frags = $location.path().split("/"); //["", "UltraEditorDocument", "13", "15", "15"]

	vm.stateParameters = {
		'categoryId': frags[2],
		'subCategoryId': frags[3],
		'masterId': frags[4]
	};

	$log.info("-=-=-=- Changing State  🌀    -=-=-=-");
	$log.debug(vm.stateParameters);
	$log.info("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-\n $location.path(): ");
	$log.log($location.path());
	const destination = "app.UltraEditorDocument";
	vm.initAndGo();
	///$state.go(destination, stateParameters);
}