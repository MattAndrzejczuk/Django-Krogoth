(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $http, $mdToast, $cookies, $state, $mdDialog) {
        var vm = this;
        vm.name = 'Arm Prime';
        vm.form = {};

        var defaultTabName = document.getElementById("DjangularMetaText_01").innerHTML;
        document.getElementById("DjangularMetaText_01").innerHTML = 'ArmPrime Registration - (' + defaultTabName.replace('Djangular', '') + ')';

        var eulaText = "http://slipsum.com/ The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy My brothers. And you will know My name is the Lord when I lay My vengeance upon thee. Your bones don't break, mine do. That's clear. Your cells react to bacteria and viruses differently than mine. You don't get sick, I do. That's also clear. But for some reason, you and I react the exact same way to water. We swallow it too fast, we choke. We get some in our lungs, we drown. However unreal it may seem, we are connected, you and I. We're on the same curve, just on opposite ends. Normally, both your asses would be dead as fucking fried chicken, but you happen to pull this shit while I'm in a transitional period so I don't wanna kill you, I wanna help you. But I can't give you this case, it don't belong to me. Besides, I've already been through too much shit this morning over this case to hand it over to your dumb ass. ";

        vm.clickRegister = clickRegister;

        function clickRegister(isNotValid) {
            if (isNotValid === false) {
                $http({
                    method: 'POST',
                    url: '/rest-auth/register-basic/',
                    data: {
                        username: vm.form.username,
                        email: vm.form.email,
                        password: vm.form.password,
                        faction: 'core'
                    }
                }).then(function successCallback(response) {
                    /// Success
                    $log.info('Login Successful');
                    $log.debug(response.data);
                    $log.log(response.data.key);
                    $mdToast.show($mdToast.simple().textContent('Registration Successful!'));
                    $cookies.put('token', response.data.key);
                    $state.go('app.LoginDjangular');
                }, function errorCallback(response) {
                    /// Fail
                    $mdToast.show($mdToast.simple().textContent('Server Error - Failed To Register.'));
                });
            }
        }


        vm.showEula = showEula;

        function showEula($event) {
            $mdDialog.show({
                targetEvent: $event,
                template: '<md-dialog>' +
                    '  <md-dialog-content> <h1>{{ titleFromOutside }}</h1> ' +
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
                    termsAndConditions: eulaText
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


        /* UPLOAD CONTROLLER */


        /*----------------------------------*/
    }
})();