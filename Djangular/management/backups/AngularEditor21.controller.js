(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $scope, $http, $mdToast, $cookies, $state) {
        var vm = this;
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
            theme: "dracula",
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

        var body = document.body,
            html = document.documentElement;
        var height = Math.max(body.scrollHeight, body.offsetHeight,
            html.clientHeight, html.scrollHeight, html.offsetHeight);
        vm.heightFromButtons = height;

        vm.getMasterViewControllerDetail = getMasterViewControllerDetail;
        vm.codemirrorLoaded = codemirrorLoaded;
        vm.codemirrorLoadedModule = codemirrorLoadedModule;
        vm.codemirrorLoadedView = codemirrorLoadedView;
        vm.collectStaticGET = collectStaticGET;
        vm.editorModel = {};
        vm.editorModuleJS = {};
        vm.editorViewHTML = {};

        vm.docWasModified = false;
        vm.markTest = markTest;
        vm.data = [];
        vm.mvcCtrl = {};

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

        function codemirrorLoaded(_editor) {
            // Editor part
            var _doc = _editor.getDoc();
            _editor.focus();
            // Options
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            // Events
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.editorModel = _editor;
            _editor.setValue("// Hello world.");
            ///_editor.setSize('100%', '1000px');
        }

        function codemirrorLoadedModule(_editor) {
            // Editor part
            var _doc = _editor.getDoc();
            _editor.focus();
            // Options
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            // Events
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.editorModuleJS = _editor;
            _editor.setValue("// Hello world.");
            ///_editor.setSize('100%', '1000px');
        }

        function codemirrorLoadedView(_editor) {
            // Editor part
            var _doc = _editor.getDoc();
            _editor.focus();
            // Options
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            // Events
            _editor.on("beforeChange", function() {
                vm.codeWillChange();
            });
            _editor.on("change", function() {
                vm.codeChanged();
            });
            vm.editorViewHTML = _editor;
            _editor.setValue("// Hello world.");
        }
        vm.getMasterViewControllers = getMasterViewControllers;
        vm.codeChanged = codeChanged;
        vm.codeWillChange = codeWillChange;
        vm.highlightVm = highlightVm;
        vm.highlightKeyword = highlightKeyword;
        vm.putMasterViewControllerDetail = putMasterViewControllerDetail;
        vm.editorContent = {};
        vm.input = {};

        function codeChanged() {
            $log.info('codemirror : `change` called!');
            vm.docWasModified = true;
        }

        function codeWillChange() {
            $log.info('codemirror : `beforeChange` called!');
            vm.docWasModified = true;
        }

        function highlightVm() {
            $log.info('codemirror : `highlightVm` called!');
            var lineCount = vm.editorModel.getDoc().lineCount();
            for (var j = 0; j < lineCount; j++) {
                var temp = vm.editorModel.getDoc().getLine(j);
                var count = (temp.match(/vm./g) || []).length;
                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf("vm.", step);
                    step = n;
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + 2
                    }, {
                        "css": "color : #23FF83"
                    });
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n + 2
                    }, {
                        "line": j,
                        "ch": n + 3
                    }, {
                        "css": "color : #00A0FF"
                    });
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
                        "css": "color : #23FF83"
                    });
                    vm.editorModel.getDoc().markText({
                        "line": j,
                        "ch": n + 8
                    }, {
                        "line": j,
                        "ch": n + 9
                    }, {
                        "css": "color : #00A0FF"
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
                        "css": "color : #FF9100"
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
                        "css": "color : #A459FF"
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
                        "css": "color : #FF9100"
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
                        "css": "color : #FF9100"
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
                        "css": "color : #A459FF"
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
                        "css": "color : #D31895"
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
                        "css": "color : #D31895"
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
                        "css": "color : #47DBE2"
                    });
                }
            }
        }


        function getMasterViewControllers() {
            $http({
                method: 'GET',
                url: '/Djangular/MasterViewControllerEditorList/'
            }).then(function successCallback(response) {
                /// Success
                $log.info('/Djangular/MasterViewControllerEditorList/');
                vm.data = response.data;
                document.getElementById("DjangularMetaText_01").innerHTML = 'Djangular Editor ';
                document.getElementById("globalStatusBar").innerHTML = 'Djangular Editor ';
            }, function errorCallback(response) {
                /// Fail
                $mdToast.show($mdToast.simple().textContent('Server Error - Login'));
            });
        }

        function getMasterViewControllerDetail(id) {
            $log.info('/Djangular/MasterViewControllerEditorDetail/?id=' + id);
            $http({
                method: 'GET',
                url: '/Djangular/MasterViewControllerEditorDetail/?id=' + id
            }).then(function successCallback(response) {
                /// Success

                vm.editorContent = response.data;

                /// vm.editorModel.clearHistory();
                $log.log('response.data');
                $log.log(response.data);
                vm.editorModuleJS.doc.setValue(response.data['module_js']);
                vm.editorModel.doc.setValue(response.data['controller_js']);
                vm.editorViewHTML.doc.setValue(response.data.view_html);
                vm.input.mvcId = response.data.id;

                document.getElementById("DjangularMetaText_01").innerHTML = 'Djangular Editor: "' + response.data.name + '"';
                document.getElementById("globalStatusBar").innerHTML = 'Editing Document: "<span class="md-accent-fg">' +
                    response.data.name + '</span>" [<span class="md-warn-fg">' + response.data.id + '</span>]' +
                    '&nbsp;&nbsp; - &nbsp;&nbsp;<span class="md-primary-fg md-hue-1">' + response.data.title + '</span>';
            }, function errorCallback(response) {
                /// Fail
                $mdToast.show($mdToast.simple().textContent('Server Error - Login'));
            });
        }


        function collectStaticGET() {
            $log.info('/LazarusII/AutoCollectStatic/');
            $http({
                method: 'GET',
                url: '/LazarusII/AutoCollectStatic/'
            }).then(function successCallback(response) {
                /// Success

                $mdToast.show($mdToast.simple().textContent('Django Finished Copying Static Files!'));
            }, function errorCallback(response) {
                /// Fail
                $mdToast.show($mdToast.simple().textContent('Server Error - Collect Static'));
            });
        }

        function putMasterViewControllerDetail() {
            vm.editorContent['module_js'] = vm.editorModuleJS.doc.getValue();
            vm.editorContent['controller_js'] = vm.editorModel.doc.getValue();
            vm.editorContent['view_html'] = vm.editorViewHTML.doc.getValue();
            $http({
                method: 'PUT',
                data: vm.editorContent,
                url: '/Djangular/MasterViewControllerEditorDetail/?id=' + vm.input.mvcId
            }).then(function successCallback(response) {
                /// Success
                $log.info('/Djangular/MasterViewControllerEditorDetail/?id=' + vm.input.mvcId);
                vm.editorContent = response.data;

                /// vm.editorModel.clearHistory();
                vm.editorModuleJS.doc.setValue(response.data['module_js']);
                vm.editorModel.doc.setValue(response.data['controller_js']);
                vm.editorViewHTML.doc.setValue(response.data.view_html);
                $mdToast.show($mdToast.simple().textContent('Saved ' + vm.editorContent['title']));
                vm.docWasModified = false;
            }, function errorCallback(response) {
                /// Fail
                $mdToast.show($mdToast.simple().textContent('Failed To Save Master View Controller.'));
            });
        }


        window.onbeforeunload = documentWillClose;

        function documentWillClose() {
            if (vm.docWasModified) {
                if (vm.docWasModified === true) {
                    return "Warning\n\nYou're about to close an unsaved document.\n\nContinue?";
                }
            }
        }

        ////// -----------
    }
})();