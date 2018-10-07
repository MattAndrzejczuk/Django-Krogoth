(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast) {
        let vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';

        vm.viewDidLoad = viewDidLoad;
        //   ======
        ///    II.
        //   ======
        vm.display = display
        vm.movie = "Ice Age";
        vm.rating = 5;

        function display(movie) {
            $mdToast.show(
                $mdToast.simple()
                .textContent("Movie : " + movie)
                .position('top right')
                .hideDelay(3000)
            );
        }
        //=============================================




        //   ======
        ///   III.
        //   ======
        vm.addCustomer = addCustomer;
        vm.customers = [{
            name: "Bob"
        }, {
            name: "Steve"
        }, {
            name: "Jess"
        }, {
            name: "Kathy"
        }, {
            name: "Jim"
        }, {
            name: "Fred"
        }, {
            name: "Sarah"
        }];

        function addCustomer() {
            /*
            vm.customers.push({
                name: "Sarah"
            });
            */
        }
        //=============================================

        function onInit() {
            vm.viewDidLoad();
        }

        function viewDidLoad() {
            console.log('FUSE_APP_NAME did finish loading');
        }
    }
})();