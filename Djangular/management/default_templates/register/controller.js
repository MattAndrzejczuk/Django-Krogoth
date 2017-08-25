(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $http, $mdToast, $cookies, $state) {
        var vm = this;
        vm.name = 'Arm Prime';
        vm.form = {};



        vm.clickLogin = clickLogin;

        function clickLogin(isNotValid) {
            if (isNotValid === false) {
                $http({
                    method: 'POST',
                    url: '/rest-auth/register-basic/',
                    data: {
                        username: vm.form.username,
                        password: vm.form.password
                    }
                }).then(function successCallback(response) {
                    /// Success
                    $log.info('Login Successful');
                    $log.debug(response.data);
                    $log.log(response.data.key);
                    $mdToast.show($mdToast.simple().textContent('Login Successful'));
                    $cookies.put('token', response.data.key);
                    $state.go('app.home');
                }, function errorCallback(response) {
                    /// Fail
                    $mdToast.show($mdToast.simple().textContent('Server Error - Login'));
                });
            }
        }

        /*
        vm.showEula = showEula;
        function showEula($event) {
            $mdDialog.show({
                targetEvent: $event,
                template: '<md-dialog>' +
                    '  <md-dialog-content> {{ titleFromOutside }} '
                '<br>' +
                '<p>{{ termsAndConditions }}</p>' +
                '</md-dialog-content>' +
                '  <md-dialog-actions>' +
                '    <md-button ng-click="closeDialog()" class="md-primary">' +
                '      close' +
                '    </md-button>' +
                '  </md-dialog-actions>' +
                '</md-dialog>',
                controller: EULAController,
                onComplete: afterShowAnimation,
                locals: {
                    eulaTitle: 'Terms and Conditions',
                    termsAndConditions: 'blah blah blah blah. just agree to this already.'
                }
            });

            function afterShowAnimation(scope, element, options) {
                /// Dialog finished appearing, do something here...
            }
        }

        function EULAController($scope, $mdDialog, eulaTitle, termsAndConditions) {
            $scope.titleFromOutside = eulaTitle;
            $scope.termsAndConditions = termsAndConditions;
            $scope.closeDialog = function() {
                $mdDialog.hide();
            };
        }
		*/

        /* UPLOAD CONTROLLER */


        /*----------------------------------*/
    }
})();