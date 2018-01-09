(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($ocLazyLoad, $state, $log) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        vm.didClickLoadScript = didClickLoadScript;
        vm.didClickLoadModule = didClickLoadModule;
        vm.triggerButton = triggerButton;
        vm.loadView = loadView;

        vm.providers = {};
        vm.queueLen = 0;


        $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=lazyMVC');


        function didClickLoadScript() {
            // var script = document.createElement("script");
            // script.type = "text/javascript";
            // script.src = "/moho_extractor/NgIncludedJs/?name=FOO";
            // document.getElementsByTagName("head")[0].appendChild(script);
            // return false;
            $ocLazyLoad.load('/krogoth_gantry/DynamicJavaScriptInjector/?name=lazyMVC&ov=file.js');

        }

        function didClickLoadModule() {
            $state.go('app.lazyMVC');
        }

        function loadView() {
            $('<div id="ctrl" ng-controller="Ctrl">' +
                '<div ng-bind="msg"/>' +
                '<div ng-bind="serviceMsg"/>' +
                '<div test-directive/>' +
                '</div>').appendTo('ak-foo');
        }



        function triggerButton(event) {
            switch (event) {
                case 'examplePage':
                    $state.go('app.FUSE_APP_NAME.slave', {sampleObject: 'SomeObject'});
                    break;
            }
        }


        vm.stateObjectViewName = $state.params.sampleObject;

        /*
                // Make module Foo and store providers for later use
                var providers = {};
                angular.module('Foo', [], function ($controllerProvider, $compileProvider, $provide) {
                    providers = {
                        $controllerProvider: $controllerProvider,
                        $compileProvider: $compileProvider,
                        $provide: $provide
                    };
                });
        // Bootstrap Foo
                angular.bootstrap($('ak-foo'), ['Foo']);

        // .. time passes ..

        // Store our _invokeQueue length before loading our controllers/directives/services
        // This is just so we don't re-register anything
                var queueLen = angular.module('Foo')._invokeQueue.length;

        // Load javascript file with controllers/directives/services
                angular.module('Foo')
                    .controller('Ctrl', function ($scope, $rootScope, fooService) {
                        $scope.msg = "It works! rootScope is " + $rootScope.$id +
                            ", should be " + $('body').scope().$id;
                        $scope.serviceMsg = fooService.msg;
                    })
                    .factory('fooService', function () {
                        return {msg: "Some text from a service"};
                    })
                    .directive('testDirective', function () {
                        return function (scope, elem) {
                            $(elem).text('Directives also work');
                        }
                    });


        // Load html file with content which uses above content
                $('<div id="ctrl" ng-controller="Ctrl">' +
                    '<div ng-bind="msg"/>' +
                    '<div ng-bind="serviceMsg"/>' +
                    '<div test-directive/>' +
                    '</div>').appendTo('body');


        // Register the controls/directives/services we just loaded
                var queue = angular.module('Foo')._invokeQueue;
                for (var i = queueLen; i < queue.length; i++) {
                    var call = queue[i];
                    // call is in the form [providerName, providerFunc, providerArguments]
                    var provider = providers[call[0]];
                    if (provider) {
                        // e.g. $controllerProvider.register("Ctrl", function() { ... })
                        provider[call[1]].apply(provider, call[2]);
                    }
                }


        // compile the new element
                $('body').injector().invoke(function ($compile, $rootScope) {
                    $compile($('#ctrl'))($rootScope);
                    $rootScope.$apply();
                });
        */

    }
})();