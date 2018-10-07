(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive() {
        return {
            restrict: 'E',
            scope: {
                movie: '=',
                rating: '@',
                display: '&'
            },
            template: "<div>Movie title : {{movie}}</div>" +
                "Type a new movie title : <input type='text' ng-model='movie' />" +
                "<div>Movie rating : {{rating}}</div>" +
                "Rate the movie : <input type='text' ng-model='rating' />" +
                "<div><button class='kg-btn kg-btn-primary' ng-click='display(movie)'>View Movie</button></div>",

            link: function($scope, element, attrs) {
                $scope.display = function(movie) {
                    alert("Movie : " + movie);
                }
            }
        };

    }
})
();