(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive() {
        return {
            restrict: 'AE',
            transclude: true,
            scope: {},
            controller: ['$scope', function MyTabsController($scope) {
                var panes = $scope.panes = [];
                console.log(" 🎞  MyTabsController SPAWNED");
                $scope.select = function(pane) {
                    console.log(" 🎞  SELECTED SOMETHING... ");
                    angular.forEach(panes, function(pane) {
                        pane.selected = false;
                    });
                    pane.selected = true;
                };

                this.addPane = function(pane) {
                    if (panes.length === 0) {
                        $scope.select(pane);
                    }
                    panes.push(pane);
                };
            }],
            templateUrl: '/moho_extractor/NgIncludedHtml/?name=backgroundPickerDropDown'
        };

    }
})
();