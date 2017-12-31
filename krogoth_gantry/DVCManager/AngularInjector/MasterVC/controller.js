(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController() {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        vm.url_to_ctrl = '/moho_extractor/KrogothFoundation/?unique_name=coreExampleCtrlLoadedByInjection';

        vm.providers = {};
        vm.queueLen = angular.module('fuse')._invokeQueue.length;

        // 2.)
        vm.loadAdditionalJavaScript = loadAdditionalJavaScript;

        // 3.)
        vm.loadHTMLFile = loadHTMLFile;

        // 4.)
        vm.registerNewMasterViewController = registerNewMasterViewController;

        // 5.)
        vm.compileNewMasterViewController = compileNewMasterViewController;








        /// 2.) An entire master view controller as a single .js file will be loaded by:
        function loadAdditionalJavaScript(url) {
            var script = document.createElement("script");
            // This script has a callback function that will run when the script has
            // finished loading.
            script.src = url;
            script.type = "text/javascript";
            document.getElementsByTagName("head")[0].appendChild(script);
        }

        // LOAD NEW CTRL FROM THIS URL:
        ///http://localhost/moho_extractor/KrogothFoundation/?unique_name=coreExampleCtrlLoadedByInjection

            /// angular.module('Foo')
            /// .controller('Ctrl', function($scope, $rootScope, fooService) {
            ///     $scope.msg = "It works! rootScope is " + $rootScope.$id +
            ///         ", should be " + $('body').scope().$id;
            ///     $scope.serviceMsg = fooService.msg;
            /// })
            /// .factory('fooService', function() {
            ///     return { msg: "Some text from a service" };
            /// })
            /// .directive('testDirective', function() {
            ///     return function(scope, elem) {
            ///         $(elem).text('Directives also work');
            ///     }
            /// });




    }
})();