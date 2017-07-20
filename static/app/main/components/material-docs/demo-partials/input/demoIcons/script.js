angular
  .module('inputIconDemo', ['ngMaterial', 'ngMessages'])
  .controller('DemoCtrl', function($scope) {
    $scope.user = {
      name: '345345',
      email: '',
      phone: '',
      address: 'Mountain View, CA',
      donation: 19.99
    };
  });
