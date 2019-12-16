(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive() {
        return {
            restrict: 'E',
            transclude: true,
            scope: {},
            template: '<div layout="row" layout-align="space-around stretch">' +
                '<div flex="10"></div>' +
                '<div flex="80" ng-transclude=""></div>' +
                '<div flex="10"></div>' +
                '</div>'
        };
    }
})
();