(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_SLAVE_NAMEController', FUSE_APP_SLAVE_NAMEController);

    function FUSE_APP_SLAVE_NAMEController($stateParams, $http, $log, $state) {
        var vm = this;
        vm.viewName = '_SLAVE_NAME_' + $stateParams.categoryId;

        vm.$onInit = onInit;
        vm.loadMasters = loadMasters;
        vm.codemirrorLoaded = codemirrorLoaded;

        vm.nextView = 'UltraEditorDocument';

        vm.objectList = {};
        vm.selectListItem = selectListItem;

        function onInit() {
            vm.loadMasters();
        }


        function loadMasters() {
            $http({
                method: 'GET',
                url: '/krogoth_gantry/viewsets/MasterViewController/?category=' + $stateParams.categoryId
            }).then(function successCallback(response) {
                vm.objectList = response.data;

                //deferred.resolve(response.data);
            }, function errorCallback(response) {
                //deferred.reject(response);
            });
        }


        function selectListItem(id) {
            $log.log("$state.go('app."+vm.nextView+"', {'masterId': id});");
            $state.go('app.'+vm.nextView, {'masterId': id});
        }




        function codemirrorLoaded(_editor) {
            var _doc = _editor.getDoc();
            _editor.focus();
            _doc.markClean();
            _editor.setOption('firstLineNumber', 0);
            _editor.on("beforeChange", function () {
                // vm.codeWillChange();
                $log.log('beforeChange');
            });
            _editor.on("change", function () {
                // vm.codeChanged();
                $log.log('change');
            });
            vm.editorModel = _editor;
        }

        vm.editorOptions = {
            lineWrapping: true,
            lineNumbers: true,
            mode: 'javascript',
            theme: "colorforth",
            indentUnit: 4,
            indentWithTabs: true
        };


    }
})();