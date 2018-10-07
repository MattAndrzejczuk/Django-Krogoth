(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive() {
        return {
            restrict: 'A',
            link: function($scope, element, attrs) {
                element.on('click', function() {
                    element.html('You clicked me!');
                });
                element.on('mouseenter', function() {
                    element.css('background-color', 'yellow');
                });
                element.on('mouseleave', function() {
                    element.css('background-color', 'white');
                });
            }
        };

    }
})
();