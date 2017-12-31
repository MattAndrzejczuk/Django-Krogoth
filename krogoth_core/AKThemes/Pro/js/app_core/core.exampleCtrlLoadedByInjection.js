// Load javascript file with controllers/directives/services
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