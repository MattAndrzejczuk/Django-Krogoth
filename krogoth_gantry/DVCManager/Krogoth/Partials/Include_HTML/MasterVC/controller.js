(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController() {
        var vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';
        vm.viewDidLoad = viewDidLoad;


        function onInit() {
            vm.viewDidLoad();
        }

        function viewDidLoad() {
            console.log('FUSE_APP_NAME did finish loading');
        }
    }
})();


/*
sh /Vol
*/

/*
sh /Volumes/MBP_Backup/arm-prime/docker/KILL_ALL_.sh
*/

/*
sh /Volumes/MBP_Backup/arm-prime/docker/run-docker-installed.sh
*/