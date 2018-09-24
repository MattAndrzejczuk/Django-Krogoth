(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $state, $ocLazyLoad, $scope, $http, $q, $timeout) {
        var vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';

        vm.REST_GenericKGData_GetOneOrCreate = "/moho_extractor/GenericKGData_GetOneOrCreate/?uid=";



        function getDjangularMasterViewControllers() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: vm.REST_GenericKGData_GetOneOrCreate + vm.input_uid
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }

        # lazyLoadableComponents

    }
})();


// Name:
// LAZYMVC_THING

// We will load: LAZYMVC_UNLOADED

// COMPILED HTML:
////krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME

// COMPILED JAVASCRIPT:
////krogoth_gantry/DynamicJavaScriptInjector/?name=FUSE_APP_NAME