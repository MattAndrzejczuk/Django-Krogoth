vm.getMasterViewCtrlDetail = getMasterViewCtrlDetail;
vm.createFirstTreeNodes = createFirstTreeNodes;
vm.reloadData = reloadData;
vm.parallelRESTfulStart = parallelRESTfulStart;
vm.parallelRESTfulReady = parallelRESTfulReady;
vm.parallelRESTfulAbort = parallelRESTfulAbort;
vm.parallelRESTfulCompleted = parallelRESTfulCompleted;
vm.cleanUpRAM = cleanUpRAM;





vm.refreshLoadedFile = refreshLoadedFile;
function refreshLoadedFile() {
	
}

function reloadData() {
	vm.treeData = [];
	vm.editorModel = {};
	vm.objectList = {};
	vm.finishedRESTfulResponses = [];
	vm.newComponentForm = {};
	vm.servicesPendingRequest = [];
	vm.directivesPendingRequest = [];
	vm.slavesPendingRequest = [];
	vm.pendingRESTfulRequests = [];
	vm.createFirstTreeNodes();
}

function createFirstTreeNodes() {
	UltraEditorDefaults.populateBoilerplate(vm.selectedMaster).then(function(treeData) {
		vm.treeData = treeData;
		vm.getMasterViewCtrlDetail();
	});
}


function getMasterViewCtrlDetail() {
	AKClassEditorComponent.loadMasterInitializer(vm.selectedMaster)
		.then(function(finishedProcess) {
		vm.servicesPendingRequest = finishedProcess.services;
		vm.directivesPendingRequest = finishedProcess.directives;
		vm.slavesPendingRequest = finishedProcess.slaves;
		vm.objectList = finishedProcess.objectList;

		vm.getTemplatesHTML();
		vm.getTemplatesJS();

		vm.parallelRESTfulStart();
	});
}


/*   ⚡️   */
function parallelRESTfulStart() {
	var cpuTask1 = GatherURIsAsync.async(vm.servicesPendingRequest, "Service")()
	.then(function(list) {
		Array.prototype.push.apply(vm.pendingRESTfulRequests, list);
	});
	var cpuTask2 = GatherURIsAsync.async(vm.directivesPendingRequest, "Directive")()
	.then(function(list) {
		Array.prototype.push.apply(vm.pendingRESTfulRequests, list);
	});
	var cpuTask3 = GatherURIsAsync.async(vm.slavesPendingRequest, "SlaveViewController")()
	.then(function(list) {
		Array.prototype.push.apply(vm.pendingRESTfulRequests, list);
	});
	$q.all([cpuTask1,
			cpuTask2,
			cpuTask3
		   ])
		.then(vm.parallelRESTfulReady, vm.parallelRESTfulAbort);
}

function parallelRESTfulAbort() {
	///vm.messages.push("something failed: parallelRESTfulAbort");
}

function parallelRESTfulReady() {
	var threads = [];
	for (var i = 0; i < vm.pendingRESTfulRequests.length; i++) {
		var request_in = vm.pendingRESTfulRequests[i];
		var cpuTaskX;
		cpuTaskX = Dependency.async(request_in.id, request_in.class, vm.treeData)()
			.then(function(list) {
			vm.treeData = list[0];
			vm.finishedRESTfulResponses = list[1];
			vm.forwardThisCode(list[2].parentIndex,
							   list[2].index,
							   list[2].srcCode,
							   list[2].title);
		});
		threads.push(cpuTaskX);
	}
	$q.all(threads)
		.then(vm.parallelRESTfulCompleted, vm.parallelRESTfulServerError);
}

function parallelRESTfulCompleted() {
	const moduleJS = new AKEditorComponentMaster(
		"ViewHTML", /* _class */
		vm.treeData[tMaste].nodes.length, /* index */
		0, /* parentIndex */
		vm.objectList.view_html, /* sourceCode */
		'view_html', /* sourceKey */
		vm.treeData[tMaste].id, /* restId */
		'htmlmixed', /* syntax */
		'language-html5' /* icon */
	);
	vm.treeData[tMaste].nodes.push(moduleJS);
	const ctrlJS = new AKEditorComponentMaster(
		"ModuleJS",
		vm.treeData[tMaste].nodes.length,
		0,
		vm.objectList.module_js,
		'module_js',
		vm.treeData[tMaste].id,
		'javascript',
		'angular'
	);
	vm.treeData[tMaste].nodes.push(ctrlJS);
	const viewHTML = new AKEditorComponentMaster(
		"ControllerJS",
		vm.treeData[tMaste].nodes.length,
		0,
		vm.objectList.controller_js,
		'controller_js',
		vm.treeData[tMaste].id,
		'javascript',
		'angularjs'
	);
	vm.treeData[tMaste].nodes.push(viewHTML);
	const styleCSS = new AKEditorComponentMaster(
		"StyleCSS",
		vm.treeData[tStyle].nodes.length,
		1,
		vm.objectList.style_css,
		'style_css',
		vm.treeData[tStyle].id,
		'css',
		'language-css3'
	);
	vm.treeData[tStyle].nodes.push(styleCSS);
	const themestyleCSS = new AKEditorComponentMaster(
		"ThemeCSS",
		vm.treeData[tStyle].nodes.length,
		1,
		vm.objectList.themestyle,
		'themestyle',
		vm.treeData[tStyle].id,
		'css',
		'language-css3'
	);
	vm.masterName = vm.objectList.name;
	vm.browserTabText = vm.masterName;
	vm.treeData[tStyle].nodes.push(themestyleCSS);
	EditorWebSocket.initializeWebSocket(vm.masterName);
	vm.loadingIDE = false;
	vm.cleanUpRAM();
	vm.loadFontSettingsCookies();
}



function cleanUpRAM() {
	vm.objectList = [];
	vm.finishedRESTfulResponses = [];
	vm.newComponentForm = {};
	vm.servicesPendingRequest = [];
	vm.directivesPendingRequest = [];
	vm.slavesPendingRequest = [];
	vm.pendingRESTfulRequests = [];
}