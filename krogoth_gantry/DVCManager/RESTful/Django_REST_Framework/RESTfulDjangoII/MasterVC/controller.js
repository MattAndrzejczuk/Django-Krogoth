(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast, $timeout, $log, RESTfulModelII) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.toastMsg = '';
        vm.RESTfulJSONPayload = {};

        vm.getObjectList = getObjectList;
        vm.postNewObject = postNewObject;
        vm.deleteObject = deleteObject;

        vm.$onInit = onInit;
        vm.$onDestroy = onDestroy;


        function onInit() {
            vm.getObjectList();
        }

        function onDestroy() {
            alert('MVC did terminate.');
        }



        // vm.jsonResponse = Blog.results;

        function getObjectList() {
            $log.info('GET request initiating...');
            RESTfulModelII.getList().then(function(data) {
                $log.info('GET response from server: ');
                $log.log(data);
                vm.jsonResponse = data.results;
            });
        }

        function deleteObject(withId) {
            RESTfulModelII.deleteObject(withId).then(function(data) {
                vm.jsonResponse.pop(data);
            });
        }

        function postNewObject() {
            RESTfulModelII.postNewObject(vm.RESTfulJSONPayload).then(function(data) {
                $log.info('POST response from server: ');
                $log.log(data);
                vm.jsonResponse.push(data);
            });
        }


    }
})();


/* avoid */
/*
function OrderController($http, $q, config, userInfo) {
    var vm = this;
    vm.checkCredit = checkCredit;
    vm.isCreditOk;
    vm.total = 0;

    function checkCredit() {
        var settings = {};
        // Get the credit service base URL from config
        // Set credit service required headers
        // Prepare URL query string or data object with request data
        // Add user-identifying info so service gets the right credit limit for this user.
        // Use JSONP for this browser if it doesn't support CORS
        return $http.get(settings)
            .then(function (data) {
                // Unpack JSON data in the response object
                // to find maxRemainingAmount
                vm.isCreditOk = vm.total <= maxRemainingAmount
            })
            .catch(function (error) {
                // Interpret error
                // Cope w/ timeout? retry? try alternate service?
                // Re-reject with appropriate error for a user to see
            });
    };
}
*/

/* recommended */
/*
function OrderController(creditService) {
    var vm = this;
    vm.checkCredit = checkCredit;
    vm.isCreditOk;
    vm.total = 0;

    function checkCredit() {
        return creditService.isOrderTotalOk(vm.total)
            .then(function (isOk) {
                vm.isCreditOk = isOk;
            })
            .catch(showError);
    };
}
*/