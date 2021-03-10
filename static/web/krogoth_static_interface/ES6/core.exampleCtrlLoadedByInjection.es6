/*
GET   http://localhost:8000/global_static_text/load_static_text_readonly/core.exampleCtrlLoadedByInjection.es6

angular.module('Foo')
.controller('Ctrl', function($scope, $rootScope, fooService) {
    $scope.msg = "It works! rootScope is " + $rootScope.$id +
        ", should be " + $('body').scope().$id;
    $scope.serviceMsg = fooService.msg;
})
.factory('fooService', function() {
    return { msg: "Some text from a service" };
})
.directive('testDirective', function() {
    return function(scope, elem) {
        $(elem).text('Directives also work');
    }
});
 */

