(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive() {

        let controller = ['$scope', function($scope) {

            function init() {
                $scope.items = angular.copy($scope.datasource);
            }

            init();

            $scope.addItem = function() {
                $scope.add();

                //Add new customer to directive scope
                $scope.items.push({
                    name: 'New Directive Controller Item'
                });
            };
        }];

        let template;
        template =
            '<button class="kg-btn kg-btn-primary" ng-click="addItem()">Add Item</button><ul>' +
            '<li ng-repeat="item in items">{{ ::item.name }}</li></ul>';

        return {
            restrict: 'E',
            scope: {
                datasource: '=',
                add: '&'
            },
            controller: controller,
            template: template
        };
    }
})
();