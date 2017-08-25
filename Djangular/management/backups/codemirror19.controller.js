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

        vm.getMasterViewControllerDetail = getMasterViewControllerDetail;
        vm.codemirrorLoaded = codemirrorLoaded;
        vm.codemirrorLoadedModule = codemirrorLoadedModule;
        vm.codemirrorLoadedView = codemirrorLoadedView;
        vm.editorModel = {};
        vm.editorModuleJS = {};
        vm.editorViewHTML = {};

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
                $log.info('codemirror : `beforeChange` called!');
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
                $log.info('codemirror : `beforeChange` called!');
            });
            _editor.on("change", function() {
                /// vm.codeChanged();
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
                $log.info('codemirror : `beforeChange` called!');
            });
            _editor.on("change", function() {
                /// vm.codeChanged();
            });
            vm.editorViewHTML = _editor;
            _editor.setValue("// Hello world.");
            ///_editor.setSize('100%', '1000px');
        }
        vm.getMasterViewControllers = getMasterViewControllers;
        vm.codeChanged = codeChanged;
        vm.highlightVm = highlightVm;
        vm.highlightKeyword = highlightKeyword;
        vm.putMasterViewControllerDetail = putMasterViewControllerDetail;
        vm.editorContent = {};
        vm.input = {};

        function codeChanged() {
            $log.info('codemirror : `change` called!');
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
        }

        function getMasterViewControllers() {
            $http({
                method: 'GET',
                url: '/Djangular/MasterViewControllerEditorList/'
            }).then(function successCallback(response) {
                /// Success
                $log.info('/Djangular/MasterViewControllerEditorList/');
                vm.data = response.data;
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
            }, function errorCallback(response) {
                /// Fail
                $mdToast.show($mdToast.simple().textContent('Server Error - Login'));
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
            }, function errorCallback(response) {
                /// Fail
                $mdToast.show($mdToast.simple().textContent('Server Error - Login'));
            });
        }

        ////// -----------
    }
})();