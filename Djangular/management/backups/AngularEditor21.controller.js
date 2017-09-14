(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state, $mdMenu, DjangularEditorRESTful) {
        var vm = this;


        /// Show These Documents With Unique Color:
        vm.primaryDocs = ['FBITest', 'LazarusMainMenu', 'uploadRepository', 'home'];


        vm.openSlaveMenu = openSlaveMenu;
        vm.mvcSideBarOpen = true;
        vm.slaveWasOpened = false;

        vm.viewName = 'FUSE_APP_NAME';
        vm.editorOptions = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'javascript',
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };
        vm.editorOptions2 = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'htmlmixed',
            theme: "ambiance",
            indentUnit: 4,
            indentWithTabs: true
        };
        vm.editorOptions3 = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'javascript',
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };
        vm.editorOptionsSlaveCtrl = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'javascript',
            theme: "ambiance",
            indentUnit: 4,
            indentWithTabs: true
        };
        vm.editorOptionsSlaveView = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'html',
            theme: "erlang-dark",
            indentUnit: 4,
            indentWithTabs: true
        };
        var body = document.body,
            html = document.documentElement;
        var height = Math.max(body.scrollHeight, body.offsetHeight,
            html.clientHeight, html.scrollHeight, html.offsetHeight);
        vm.heightFromButtons = height;


        vm.collectStaticGET = collectStaticGET;
        vm.toolbarInfo = {};


        vm.codeChanged = codeChanged;
        vm.codeWillChange = codeWillChange;
        vm.highlightVm = highlightVm;
        vm.highlightKeyword = highlightKeyword;

        vm.editorContentMaster = {};
        vm.editorContentSlave = {};
        vm.input = {};

        vm.docWasModified = false;
        vm.markTest = markTest;
        vm.data = [];
        vm.slaves = [];
        vm.vmVarNames = [];
        vm.mvcCtrl = {};

        // Master View Controller Setup
        vm.codemirrorLoaded = codemirrorLoaded;
        vm.codemirrorLoadedModule = codemirrorLoadedModule;
        vm.codemirrorLoadedView = codemirrorLoadedView;
        vm.codemirrorLoadedSlaveController = codemirrorLoadedSlaveController;
        vm.codemirrorLoadedSlaveView = codemirrorLoadedSlaveView;
        vm.editorModel = {};
        vm.editorModuleJS = {};
        vm.editorViewHTML = {};
        vm.getMasterViewControllers = getMasterViewControllers;
        vm.getMasterViewControllerDetail = getMasterViewControllerDetail;
        vm.putMasterViewControllerDetail = putMasterViewControllerDetail;

        // Slave View Controller Setup
        vm.slaveCtrlJS = {};
        vm.slaveViewHTML = {};
        vm.getSlaveViewControllers = getSlaveViewControllers;
        vm.getSlaveViewControllerDetail = getSlaveViewControllerDetail;
        vm.putSlaveViewControllerDetail = putSlaveViewControllerDetail;

        vm.getMasterViewControllers();


        function getMasterViewControllers() {
            DjangularEditorRESTful.getDjangularMasterViewControllers().then(function(data) {
                $log.info('/Djangular/MasterViewControllerEditorList/');
                vm.data = data;
                document.getElementById("DjangularMetaText_01").innerHTML = 'Djangular Editor ';
                /// document.getElementById("globalStatusBar").innerHTML = 'Djangular Editor ';
            });
        }

        function getMasterViewControllerDetail(id) {
            $log.debug(' ❎ LOADING MASTER VIEW CONTROLLER ! ! !');
            DjangularEditorRESTful.getDjangularMasterViewControllerDetail(id).then(function(data) {
                vm.editorContentMaster = data;
                /// vm.editorModel.clearHistory();
                $log.log('response.data');
                $log.log(data.module_js);
                vm.editorModuleJS.doc.setValue(data.module_js);
                vm.editorModel.doc.setValue(data.controller_js);
                vm.editorViewHTML.doc.setValue(data.view_html);
                vm.input.mvcId = data.id;
                vm.slaves = [];
                vm.docWasModified = false;
                vm.getSlaveViewControllers(data.id);

                vm.toolbarInfo.id = data.id;
                vm.toolbarInfo.name = data.name;
                vm.toolbarInfo.title = data.title;
                /*
                 document.getElementById("DjangularMetaText_01").innerHTML = 'Djangular Editor: "' +
                 data.name + '"';
                 document.getElementById("globalStatusBar").innerHTML = 'Editing Document:' +
                 ' "<span class="md-accent-fg">' +
                 data.name + '</span>" [<span class="md-warn-fg">' +
                 data.id + '</span>]' +
                 '&nbsp;&nbsp; - &nbsp;&nbsp;<span class="md-primary-fg md-hue-1">' +
                 data.title + '</span>';
                 */
            });
        }

        function openSlaveMenu($mdMenu, ev) {
            $mdMenu.open(ev);
        };
        ///vm.getSlaveViewControllers = getSlaveViewControllers;
        ///vm.getSlaveViewControllerDetail = getSlaveViewControllerDetail;
        ///vm.putSlaveViewControllerDetail = putSlaveViewControllerDetail;
        ///getDjangularSlaveViewControllers: getDjangularSlaveViewControllers,
        ///getDjangularSlaveViewControllerDetail: getDjangularSlaveViewControllerDetail,
        ///putDjangularSlaveViewController: putDjangularSlaveViewController,

        function getSlaveViewControllers(master_id) {
            $log.debug(' ℹ️ LOADING SLAVE VIEW CONTROLLERS ! ! !');
            DjangularEditorRESTful.getDjangularSlaveViewControllers(master_id).then(function(data) {
                $mdToast.show($mdToast.simple()
                    .textContent('Slave VCs loaded: ' + data.length));
                $log.info(data);
                vm.slaves = data;
                vm.toolbarInfo.slaveCount = data.length;
            });
        }

        function getSlaveViewControllerDetail(slave_id) {
            DjangularEditorRESTful.getDjangularSlaveViewControllerDetail(slave_id).then(function(data) {
                vm.editorContentMaster = data;
                $log.info('SLAVES LOADED!\n\n\n\n\n');
                $log.log(data.controller_js);
                $log.debug(data.view_html);
                //vm.editorModuleJS.doc.setValue(data['module_js']);
                //vm.editorModel.doc.setValue(data['controller_js']);
                //vm.editorViewHTML.doc.setValue(data.view_html);
                vm.slaveViewHTML.doc.setValue(data.view_html);
                vm.slaveCtrlJS.doc.setValue(data.controller_js);
                vm.slaveWasOpened = true;
            });
        }

        function putSlaveViewControllerDetail() {
            vm.editorContentSlave['controller_js'] = vm.slaveCtrlJS.doc.getValue();
            vm.editorContentSlave['view_html'] = vm.slaveViewHTML.doc.getValue();
            DjangularEditorRESTful.putDjangularSlaveViewController(vm.input.mvcId, vm.editorContentSlave).then(function(data) {
                vm.slaveViewHTML.doc.setValue(data.view_html);
                vm.slaveCtrlJS.doc.setValue(data.controller_js);
                $mdToast.show($mdToast.simple()
                    .textContent('Slave View & Controller Saved.'));
            });
        }

        function collectStaticGET() {
            DjangularEditorRESTful.djangoManagePyCollectStatic().then(function(data) {
                $mdToast.show($mdToast.simple()
                    .textContent('Django Finished Copying Static Files!'));
                ///document.getElementById("DjangularMetaText_01").innerHTML = 'Djangular Editor ';
                ///document.getElementById("globalStatusBar").innerHTML = 'Djangular Editor ';
            });
        }

        function putMasterViewControllerDetail() {
            vm.editorContentMaster['module_js'] = vm.editorModuleJS.doc.getValue();
            vm.editorContentMaster['controller_js'] = vm.editorModel.doc.getValue();
            vm.editorContentMaster['view_html'] = vm.editorViewHTML.doc.getValue();
            DjangularEditorRESTful.putDjangularMasterViewController(vm.input.mvcId, vm.editorContentMaster).then(function(data) {
                document.getElementById("DjangularMetaText_01").innerHTML = 'Djangular Editor ';
                ///document.getElementById("globalStatusBar").innerHTML = 'Djangular Editor ';
                vm.editorContentMaster = data;
                ///vm.editorModel.clearHistory();
                vm.editorModuleJS.doc.setValue(data['module_js']);
                vm.editorModel.doc.setValue(data['controller_js']);
                vm.editorViewHTML.doc.setValue(data.view_html);
                vm.docWasModified = false;
                $mdToast.show($mdToast.simple()
                    .textContent('Master View Controller Saved.'));
            });
        }


        function codemirrorLoaded(_editor) {
            //if (_editor && vm.editorModel.didLoadDjangular === false) {
            vm.editorModel.didLoadDjangular = true;
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.editorModel = _editor;
            $log.debug('codemirrorLoaded');
            $log.info(_editor);
            $log.log('💛');
            //}

        }

        function codemirrorLoadedModule(_editor) {
            //if (_editor && vm.editorModuleJS.didLoadDjangular === false) {
            vm.editorModuleJS.didLoadDjangular = true;
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.editorModuleJS = _editor;
            $log.debug('codemirrorLoadedModule');
            $log.info(_editor);
            $log.log('💚');
            //}
        }

        function codemirrorLoadedView(_editor) {
            //if (_editor && vm.editorViewHTML.didLoadDjangular === false) {
            vm.editorViewHTML.didLoadDjangular = true;
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.editorViewHTML = _editor;
            $log.debug('codemirrorLoadedView');
            $log.info(_editor);
            $log.log('💙');
            //}

            ///_editor.setValue("// Hello world.");
        }

        function codemirrorLoadedSlaveController(_editor) {
            //if (_editor && vm.slaveCtrlJS.didLoadDjangular === false) {
            vm.slaveCtrlJS.didLoadDjangular = true;
            var _doc = _editor.getDoc();
            $log.info(_editor);
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.slaveCtrlJS = _editor;
            $log.debug('codemirrorLoadedSlaveController');
            $log.info(_editor);
            $log.log('💜');
            //}
            ///_editor.setValue("// Hello world.");
        }

        function codemirrorLoadedSlaveView(_editor) {
            //if (_editor && vm.slaveViewHTML.didLoadDjangular === false) {
            vm.slaveViewHTML.didLoadDjangular = true;
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.slaveViewHTML = _editor;
            $log.debug('codemirrorLoadedSlaveView');
            $log.info(_editor);
            $log.log('❤️');
            $log.debug(vm.slaveViewHTML);
            //}
            ///_editor.setValue("// Hello world.");
        }

        window.onbeforeunload = documentWillClose;

        function documentWillClose() {
            if (vm.docWasModified) {
                if (vm.docWasModified === true) {
                    return "Warning\n\nYou're about to close an unsaved document.\n\nContinue?";
                }
            }
        }


        function markTest() {
            vm.editorModel.getDoc().markText({
                "line": 0,
                "ch": 3
            }, {
                "line": 0,
                "ch": 9
            }, {
                "css": "color : red"
            });
        }


        function codeChanged() {
            $log.info('codemirror : `change` called!');
            vm.docWasModified = true;
        }

        function codeWillChange() {
            $log.info('codemirror : `beforeChange` called!');
            ///vm.docWasModified = true;
        }

        function highlightVm() {
            $log.info('codemirror : `highlightVm` called!');
            var lineCount = vm.editorModel.getDoc().lineCount();
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/vm./g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    /// Highlight all: VM.VARNAME
                    var n = temp.indexOf("  vm.", step);
                    var end = temp.indexOf(" = ", step);

                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 4
                    }, {
                        "css": "color : #d31895"
                    });
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n + 4
                    }, {
                        "line": j,
                        "ch": n + 5
                    }, {
                        "css": "color : #f00"
                    });


                    if (n !== -1 && end !== -1) {
                        if (temp) {
                            if (temp.substring(n, end)) {
                                var vmName = temp.substring(n, end);
                                vm.vmVarNames.push(vmName.replace(' ', ''));
                                vm.editorModel.getDoc().markText({
                                    "line": j,
                                    "ch": n + 5
                                }, {
                                    "line": j,
                                    "ch": n + vmName.length
                                }, {
                                    "css": "color: #6666FF; font-weight:bold;"
                                });
                            }
                        }
                    }

                }
            }

            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/$mdToast/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf("$mdToast", step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 8
                    }, {
                        "css": "color : #00a0ff"
                    });
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n + 8
                    }, {
                        "line": j,
                        "ch": n + 9
                    }, {
                        "css": "color : #ccff00; font-weight:bold;"
                    });
                }
            }

        }

        function highlightKeyword(keyword) {
            $log.info('codemirror : `highlightKeyword` called!');
            var lineCount = vm.editorModel.getDoc().lineCount();
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/log./g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('$log.', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 4
                    }, {
                        "css": "color : #FF9100; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/http/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('$http(', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 5
                    }, {
                        "css": "color : #A459FF; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/mdToast/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('mdToast', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 7
                    }, {
                        "css": "color : #FF9100; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/scope/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('scope', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 5
                    }, {
                        "css": "color : #FF9100; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/Controller/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('Controller', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 10
                    }, {
                        "css": "color : #A459FF; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/.on/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('cookies', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 7
                    }, {
                        "css": "color : #D31895; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/mdDialog/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('mdDialog', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 8
                    }, {
                        "css": "color : #D31895; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/state/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('$state', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 6
                    }, {
                        "css": "color : #47DBE2; font-weight:bold;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/\);/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf(');', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 1
                    }, {
                        "css": "color : #ffc3fc;"
                    });
                }
            }
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/\(/g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('(', step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 1
                    }, {
                        "css": "color : #ffc3fc;"
                    });
                }
            }


            /*  'v.' '.' 
             for (var j = 0; j < lineCount; j++) {
             var temp = vm.editorModel.getDoc().getLine(j);
             var count = (temp.match(/ vm.|./g) || []).length;
             var step = 0;
             for (var i = 0; i < count; i++) {
             var n = temp.indexOf(' vm.', step);
             step = n;
             vm.editorModel.getDoc().markText({
             "line": j,
             "ch": n + 4
             }, {
             "line": j,
             "ch": n + temp.indexOf('.', n + 4) - 3
             }, {
             "css": "color : #23ff83;"
             });
             }
             }
             */

        }


        ////// -----------
    }
})();