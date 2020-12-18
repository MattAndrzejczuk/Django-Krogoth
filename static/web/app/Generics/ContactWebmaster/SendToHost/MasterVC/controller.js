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
        vm.didGetResult = didGetResult;

		vm.formData = {};
        vm.debugResult = {};

        vm.messageUI = "";
        vm.shouldHideBtn = false;

        function onInit() {
            vm.viewDidLoad();
        }

        function onDestroy() {

        }

        function didGetResult(result) {
            if (vm.debugResult.result === "SUCCESS") {
            	vm.formData = {};
                vm.shouldHideBtn = true;
                vm.messageUI = "Thank you, we'll get back to you shortly.";
            } else {
            	vm.messageUI = "Something went wrong, please make sure you've included the suject and emaiil then try again.";
            }
        }

        function submitForm() {

            ContactRESTful.createContactForm(vm.formData)
            	.then(function(responseData) {
            		vm.debugResult = responseData;
                	vm.didGetResult(vm.debugResult);
            });
        
        }
        

        function viewDidLoad() {
            $log.log('FUSE_APP_NAME did finish loading');
        }
    }
})();