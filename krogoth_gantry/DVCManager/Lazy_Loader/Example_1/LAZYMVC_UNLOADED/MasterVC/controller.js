(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($log, $state, $ocLazyLoad, $scope, $http, $q, $timeout) {
        var vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';

        vm.singleKGData = {};
        vm.createdKGDataResponse = {};

        vm.uri_1 = "/moho_extractor/GenericKGData_GetOneOrCreate/?uid=";
        vm.uri_2 = "/moho_extractor/GenericKGData_GetOneOrCreate/";

        vm.getKGDataByUID = getKGDataByUID;
        vm.postKGData = postKGData;

        function getKGDataByUID() {
            vm.GenericKGData_GetOneOrCreate_GET()
                .then(function(response) {
                    $log.log("OK");
                    $log.log(response);
                    vm.singleKGData = response;
                });
        }

        function postKGData() {
            vm.GenericKGData_GetOneOrCreate_POST()
                .then(function(response) {
                    $log.log("OK");
                    $log.log(response);
                    vm.createdKGDataResponse = response;
                });
        }



        vm.GenericKGData_GetOneOrCreate_GET = GenericKGData_GetOneOrCreate_GET;
        vm.GenericKGData_GetOneOrCreate_POST = GenericKGData_GetOneOrCreate_POST;

        function GenericKGData_GetOneOrCreate_GET() {
            var deferred = $q.defer();
            $http({
                method: 'GET',
                url: vm.uri_1 + vm.input_uid
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }


        function GenericKGData_GetOneOrCreate_POST() {

            $log.log("POST --> [" + vm.uri_2 + "]");

            const payload = {
                uid: vm.input_uid_post,
                header: vm.input_header_post,
                contents: vm.input_contents_post
            };
            $log.log(payload);

            var deferred = $q.defer();

            $http({
                method: 'POST',
                data: payload,
                url: vm.uri_2
            }).then(function successCallback(response) {
                /// Success
                deferred.resolve(response.data);
            }, function errorCallback(response) {
                /// Fail
                deferred.reject(response);
            });
            return deferred.promise;
        }
        #lazyLoadableComponents

    }
})();


// Name:
// LAZYMVC_THING

// We will load: LAZYMVC_UNLOADED

// COMPILED HTML:
////krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME

// COMPILED JAVASCRIPT:
////krogoth_gantry/DynamicJavaScriptInjector/?name=FUSE_APP_NAME