(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController() {
        let vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';
        vm.viewDidLoad = viewDidLoad;
        vm.click = click;

        #KGhtml2canvas


        function onInit() {
            vm.viewDidLoad();
        }

        function click() {
            html2canvas($("#vertical-navigation"), {
                onrendered: function(canvas) {

                    $("#CANVAS_PLC").append(canvas);
                    // Clean up 
                    //document.body.removeChild(canvas);
                }
            });
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