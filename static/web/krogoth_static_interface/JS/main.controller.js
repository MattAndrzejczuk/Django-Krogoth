/*
GET     http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/
*/
(function () {
  'use strict';

  angular
    .module('fuse')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController($scope, $rootScope) {
    // Data

    //////////

    // Remove the splash screen
    $scope.$on('$viewContentAnimationEnded', function (event) {
      if (event.targetScope.$id === $scope.$id) {
        $rootScope.$broadcast('msSplashScreen::remove');
      }
    });
  }
})();