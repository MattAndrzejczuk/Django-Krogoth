(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, ContactRESTful) {
        let vm = this;
        vm.$onInit = onInit;
        vm.$onDestroy = onDestroy;

        vm.viewName = 'FUSE_APP_NAME';
        vm.viewDidLoad = viewDidLoad;
        
        
        vm.submitForm = submitForm;
        
		vm.formData = {};
        vm.debugResult = {};

        function onInit() {
            vm.viewDidLoad();
        }

        function onDestroy() {

        }
        
        
        function submitForm() {
        
            ContactRESTful.createContactForm(vm.formData)
            	.then(function(responseData) {
            		vm.debugResult = responseData;
            });
        
        }
        

        function viewDidLoad() {
            $log.log('FUSE_APP_NAME did finish loading');
        }
    }
})();