(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast, $timeout, $log, RESTfulModelVI) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.toastMsg = '';
        vm.RESTfulJSONPayload = {
            toppings: []
        };

        vm.getFKList = getFKList;
        vm.getObjectList = getObjectList;
        vm.postNewObject = postNewObject;
        vm.putModifiedObject = putModifiedObject;
        vm.deleteObject = deleteObject;

        vm.foreignKeys = [];

        vm.$onInit = onInit;
        vm.$onDestroy = onDestroy;


        function onInit() {
            vm.getObjectList();
            vm.getFKList();
        }

        function onDestroy() {
            alert('MVC did terminate.');
        }


        vm.selected = [];

        vm.selectManyToMany = selectManyToMany;
        vm.getColspan = getColspan;

        vm.didAddChip = didAddChip;
        vm.addChipToGrid = addChipToGrid;

        vm.didRemoveChip = didRemoveChip;
        vm.removeChipFromGrid = removeChipFromGrid;


        function didRemoveChip(chip, index, pizza) {
            vm.removeChipFromGrid(chip, pizza);
        }

        function removeChipFromGrid(chip, pizza) {
            for (var i = 0; i < vm.jsonResponse.length; i++) {
                if (vm.jsonResponse[i].name === pizza) {
                    vm.RESTfulJSONPayload = vm.jsonResponse[i];
                    vm.putModifiedObject(pizza);
                }
            }
        }

        function didAddChip(chip, index, pizza) {
            vm.addChipToGrid(chip, pizza);
        }

        function addChipToGrid(chip, pizza) {
            for (var i = 0; i < vm.jsonResponse.length; i++) {
                if (vm.jsonResponse[i].name === pizza) {
                    vm.RESTfulJSONPayload = vm.jsonResponse[i];
                    vm.putModifiedObject(pizza);
                }
            }
        }


        function getColspan(totalChips) {
            if (totalChips < 4) {
                return 1;
            } else {
                return Math.ceil(totalChips / 4)
            }
        }

        function selectManyToMany(item) {
            var remove = false;
            var rmindex = -1;
            if (vm.RESTfulJSONPayload.toppings) {
                for (var i = 0; i < vm.RESTfulJSONPayload.toppings.length; i++) {
                    if (vm.RESTfulJSONPayload.toppings[i] === item) {
                        $log.log(vm.RESTfulJSONPayload.toppings[i] + ' == ' + item);
                        remove = true;
                        rmindex = i;
                        break;
                    }
                }
            }

            if (remove === true) {
                $log.log('REMOVING');
                vm.RESTfulJSONPayload.toppings.splice(rmindex, 1);
            } else {
                $log.log('ADDING');
                vm.RESTfulJSONPayload.toppings.push(item);
            }
        }

        function getFKList() {
            RESTfulModelVI.getManyToManyKeys().then(function(data) {
                vm.foreignKeys = data.results;
            });
        }

        function getObjectList() {
            $log.info('GET request initiating...');
            RESTfulModelVI.getList().then(function(data) {
                $log.info('GET response from server: ');
                $log.log(data);
                vm.jsonResponse = data.results;
            });
        }

        function deleteObject(withId) {
            RESTfulModelVI.deleteObject(withId).then(function(data) {
                $log.log('DELETED THIS ONE: ');
                $log.log(withId);
                for (var i = 0; i < vm.jsonResponse.length; i++) {
                    if (withId === vm.jsonResponse[i].name) {
                        vm.jsonResponse.splice(i, 1);
                    }
                }
            });
        }

        function postNewObject() {
            RESTfulModelVI.postNewObject(vm.RESTfulJSONPayload).then(function(data) {
                $log.info('POST response from server: ');
                $log.log(data);
                vm.jsonResponse.push(data);
            });
        }



        function putModifiedObject(objId) {
            RESTfulModelVI.putEditedObject(vm.RESTfulJSONPayload, objId).then(function(data) {
                $log.info('PUT response from server: ');
                $log.log(data);
                for (var i = 0; i < vm.jsonResponse.length; i++) {
                    if (objId === vm.jsonResponse[i].name) {
                        vm.jsonResponse.splice(i, 1, data);
                        // vm.jsonResponse.push(data);
                    }
                }
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