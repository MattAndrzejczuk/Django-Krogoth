/*
GET   http://localhost:8000/global_static_text/load_static_text_readonly/ms-splash-screen.directive.es6
 */
(function () {
  'use strict';

  angular
    .module('app.core')
    .directive('msSplashScreen', msSplashScreenDirective);

  /** @ngInject */
  function msSplashScreenDirective($animate) {
    return {
      restrict: 'E',
      link: function (scope, iElement) {
        var splashScreenRemoveEvent = scope.$on('msSplashScreen::remove', function () {
          $animate.leave(iElement).then(function () {
            // De-register scope event
            splashScreenRemoveEvent();

            // Null-ify everything else
            scope = iElement = null;
          });
        });
      }
    };
  }
})();