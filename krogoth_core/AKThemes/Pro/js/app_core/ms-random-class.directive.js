/* ~ ~ ~ ~ ~ ~ ~ ~ ANGULARJS 1.7.2 ~ ~ ~ ~ ~ ~ ~ ~ */
(function () {
  'use strict';

  angular
    .module('app.core')
    .directive('msRandomClass', msRandomClassDirective);

  /** @ngInject */
  function msRandomClassDirective() {
    return {
      restrict: 'A',
      scope: {
        msRandomClass: '='
      },
      link: function (scope, iElement) {
        var randomClass = scope.msRandomClass[Math.floor(Math.random() * (scope.msRandomClass.length))];
        iElement.addClass(randomClass);
      }
    };
  }
})();