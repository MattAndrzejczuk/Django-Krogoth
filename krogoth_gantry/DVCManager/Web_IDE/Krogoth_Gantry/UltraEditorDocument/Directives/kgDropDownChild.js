/* TESTED AND VERIFIED WITH LATEST VERSION */
(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive() {
        console.log(" 🎞  _DJANGULAR_DIRECTIVE_NAME_Directive SPAWNED");
        return {
            require: '^^kgDropDownParent',
            restrict: 'E',
            transclude: true,
            scope: {
                title: '=title'
            },
            link: function(scope, element, attrs, tabsCtrl) {
                console.log(" 🎞  tabsCtrl.addPane");
                tabsCtrl.addPane(scope);
            },
            templateUrl: '/moho_extractor/NgIncludedHtml/?name=backgroundPickerItem'
        };

    }
})
();