(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $http, $mdToast, $cookies, $state) {
        var vm = this;
        vm.name = 'krogoth_gantry';
        vm.form = {};

        var defaultTabName = document.getElementById("krogoth_gantryMetaText_01").innerHTML;
        document.getElementById("krogoth_gantryMetaText_01").innerHTML = 'ArmPrime: Login - (' + defaultTabName.replace('krogoth_gantry', '') + ')';

        vm.clickLogin = clickLogin;
        vm.didPressEnter = didPressEnter;

        function clickLogin(isNotValid) {
            if (isNotValid === false) {

                $http({
                    method: 'POST',
                    url: '/rest-auth/login/',
                    data: {
                        username: vm.form.username,
                        password: vm.form.password
                    }
                }).then(function successCallback(response) {
                    /// Success
                    $log.info('Login Successful');
                    $log.debug(response.data);
                    $log.log(response.data.key);

                    if (response.status === 200) {
                        $mdToast.show($mdToast.simple().textContent('Login Successful.'));
                        $cookies.put('token', response.data.key);
                        $state.go('app.home');
                    } else if (response.status === 400) {
                        $mdToast.show($mdToast.simple().textContent('Invalid Username or Password.'));
                    } else {
                        $mdToast.show($mdToast.simple().textContent('Server Error, our fast assist repair KBOTs will be dispatched to look into the situation.'));
                    }

                }, function errorCallback(response) {
                    /// Fail
                    $mdToast.show($mdToast.simple().textContent('Server Error - Login'));
                });

            }
        }


        function didPressEnter(e, isNotValid) {
            $log.info(e);
            //See notes about 'which' and 'key'
            if (e.originalEvent.keyCode === 13) {
                vm.clickLogin(isNotValid);
            }
        }


        /*----------------------------------*/
    }
})();