/*
GET   http://localhost:8000/global_static_text/load_static_text_readonly/ms-responsive-table.directive.es6
 */
(function () {
  'use strict';

  angular
    .module('app.core')
    .directive('msResponsiveTable', msResponsiveTableDirective);

  /** @ngInject */
  function msResponsiveTableDirective() {
    return {
      restrict: 'A',
      link: function (scope, iElement) {
        // Wrap the table
        var wrapper = angular.element('<div class="ms-responsive-table-wrapper"></div>');
        iElement.after(wrapper);
        wrapper.append(iElement);

        //////////
      }
    };
  }
})();