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
                    $mdToast.show($mdToast.simple().textContent('Login Successful'));
                    $cookies.put('token', response.data.key);
                    $state.go('app.home');
                }, function errorCallback(response) {
                    /// Fail
                    $mdToast.show($mdToast.simple().textContent('Server Error - Login'));
                });

            }
        }




        /*----------------------------------*/
    }
})();