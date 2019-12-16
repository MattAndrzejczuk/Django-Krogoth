vm.launchXtraCodeMirror = launchXtraCodeMirror;
vm.loadCodeIntoXtraEditor = loadCodeIntoXtraEditor;



vm.xtraCodeMirrorEditorOptions = {
    lineWrapping: false,
    lineNumbers: true,
    mode: "javascript",
    theme: "colorforth",
    indentUnit: 4,
    indentWithTabs: false
};



function launchXtraCodeMirror(_editor) {
    var _doc = _editor.getDoc();
    _editor.focus();
    _doc.markClean();
    _editor.setOption("firstLineNumber", 1);
    _editor.on("beforeChange", function() {
        vm.editorContentWillChange();
    });
    _editor.on("change", function() {
        vm.editorContentDidChange();
    });
    _editor.on("cursorActivity", function() {
        vm.cursorActivity();
    });
    vm.xtraEditorModel = _editor;
}


function loadCodeIntoXtraEditor() {
    let code = vm.treeData[vm.loadedParentIndex].nodes[vm.loadedIndex];
	vm.xtraEditorModel.doc.setValue(code);
}


vm.socketMsgs = [];


function logSocketMessage(msg) {
	vm.socketMsgs.push(msg);
}


/*
.setSelection(anchor: {line, ch}, ?head: {line, ch}, ?options: object)
*/