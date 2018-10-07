(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive($interval) {





        return function(scope, element, attrs) {
            var format, // date format
                stopTime; // so that we can cancel the time updates

            // used to update the UI
            function updateTime() {
                //$log.log("updateTime " + Date().toString());
                ///const x = window.innerWidth;
                const y = window.innerHeight - 125;
                ///const display = `Width: ${x} Height: ${y}`;
                ///element.text(display);
                element.css('height', (y + 'px'));
            }

            // watch the expression, and update the UI on change.
            /*
            scope.$watch(attrs.myCurrentTime, function(value) {
                format = value;
                updateTime();
            });
			*/

            stopTime = $interval(updateTime, 3000);

            // listen on DOM destroy (removal) event, and cancel the next UI update
            // to prevent updating time after the DOM element was removed.
            element.on('$destroy', function() {
                $interval.cancel(stopTime);
            });
        }







    }
})
();