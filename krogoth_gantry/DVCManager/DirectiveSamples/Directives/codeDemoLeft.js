(function () {
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
            template:
            /* ~~ */'<div flex layout-padding ng-transclude></div>'
        };
    }
})
();