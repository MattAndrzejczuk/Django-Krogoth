(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast, $timeout, $log, Blog, $q) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.toastsPoped = 1;
        vm.addToastToQueue = addToastToQueue;
        vm.forItem = forItem;
        vm.errorToast = errorToast;
        vm.toastMsg = '';


        $log.log(' [ ❤️ ] Blog : ');
        $log.log(Blog);


        vm.toastMsg = Blog.results.toString();

        vm.addToastToQueue();
        vm.data = Blog.results;

        function forItem(inObj, doAction) {
            return function () {
                var deferred = $q.defer();
                try {
                    for (var i = 0; i < withLen; i++) {

                    }
                    deferred.resolve();
                }
                catch (err) {

                    deferred.reject();
                }
                return deferred.promise;
            };
        }

        function addToastToQueue() {
            vm.toastsPoped += 1;
            $log.log(' [ 💙 ] ');
            $mdToast.show(
                $mdToast.simple()
                    .textContent(' [' + vm.toastsPoped + ' 🍞 ] : ' + vm.toastMsg)
                    .position('bottom right')
                    .hideDelay(2000)
            );
        }

        function errorToast(err) {
            vm.toastsPoped += 1;
            $mdToast.show(
                $mdToast.simple()
                    .textContent(' [' + vm.toastsPoped + ' 🍞 ] : ' + err)
                    .position('top left')
                    .hideDelay(2500)
            );
        }


        vm.tiles = buildGridModel({
            icon: "avatar:svg-",
            title: "Svg-",
            background: ""
        });

        function buildGridModel(tileTmpl) {
            var it, results = [];

            for (var j = 0; j < 11; j++) {

                it = angular.extend({}, tileTmpl);

                it.title = vm.data[j];
                it.span = {row: 1, col: 1};

                switch (j + 1) {
                    case 1:
                        it.background = "red";
                        it.span.row = 2;
                        it.span.col = 3;
                        it.icon = '';
                        break;

                    case 2:
                        it.background = "green";
                        break;
                    case 3:
                        it.background = "darkBlue";
                        break;
                    case 4:
                        it.background = "blue";
                        it.span.col = 2;
                        break;

                    case 5:
                        it.background = "yellow";
                        it.span.row = it.span.col = 2;
                        break;

                    case 6:
                        it.background = "pink";
                        break;
                    case 7:
                        it.background = "darkBlue";
                        break;
                    case 8:
                        it.background = "purple";
                        break;
                    case 9:
                        it.background = "deepBlue";
                        break;
                    case 10:
                        it.background = "lightPurple";
                        break;
                    case 11:
                        it.background = "yellow";
                        break;
                }

                results.push(it);
            }
            return results;
        }






        vm.posts = [{
            "user": {
                "name": "Andrew Green",
                "avatar": "/static/assets/images/avatars/andrew.jpg"
            },
            "message": "Hey, man! Check this, it’s pretty awesome!",
            "time": "June 12, 2015",
            "type": "article",
            "like": 98,
            "share": 6,
            "article": {
                "title": "The Fallout 4 Pip-Boy Edition Is Back In Stock Now",
                "subtitle": "Kotaku",
                "excerpt": "The Fallout 4 Pip-Boy edition is back in stock at Gamestop, for all 3 platforms. Additionally, Walmart also has it in stock for the PS4 and Xbox One as of this writing, as does Best Buy.",
                "media": {
                    "type": "image",
                    "preview": "/static/assets/images/etc/fallout.jpg"
                }
            },
            "comments": [
                {
                    "user": {
                        "name": "Alice Freeman",
                        "avatar": "/static/assets/images/avatars/alice.jpg"
                    },
                    "time": "June 10, 2015",
                    "message": "That’s a wonderful place. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et eleifend ligula. Fusce posuere in sapien ac facilisis. Etiam sit amet justo non felis ornare feugiat."
                }
            ]
        }];
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
            .then(function(data) {
             // Unpack JSON data in the response object
               // to find maxRemainingAmount
               vm.isCreditOk = vm.total <= maxRemainingAmount
            })
            .catch(function(error) {
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
          .then(function(isOk) { vm.isCreditOk = isOk; })
          .catch(showError);
    };
}
*/
