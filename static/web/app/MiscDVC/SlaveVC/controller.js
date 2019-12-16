(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('_SLAVE_NAME_Controller', _SLAVE_NAME_Controller);

    function _SLAVE_NAME_Controller($stateParams) {
        var vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';
        vm.viewDidLoad = viewDidLoad;
        vm.itemId = '';

        function onInit() {
            console.log('_SLAVE_NAME_ did finish loading');
            vm.viewDidLoad();
        }

        function viewDidLoad() {
            // vm.itemId = $stateParams.theUniqueStateId;
        }
    }
})();


/// APPEND THIS TO THE MASTER STATE PROVIDER:
/*
*             .state('app.FUSE_APP_NAME.slave', {
*                url: '/FUSE_APP_NAME/:theUniqueStateId',
*                views: {
*                    'main@': {
*                        templateUrl: '/moho_extractor/NgIncludedHtml/?name=content-only.html',
*                        controller: 'MainController as vm'
*                    },
*                    'content@app.FUSE_APP_NAME.slave': {
*                        templateUrl: '/krogoth_gantry/DynamicHTMLSlaveInjector/?name=FUSE_APP_SLAVE_NAME',
*                        controller: 'FUSE_APP_SLAVE_NAMEController as vm'
*                    }
*
*                }
*            })
*
* */