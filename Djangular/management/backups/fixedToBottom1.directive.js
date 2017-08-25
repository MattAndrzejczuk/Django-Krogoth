(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);
    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive($window, $log, $interval) {

        return {
            restrict: 'AE',
            link: link
        };

        function link(scope, element, attrs) {
            $log.info('_DJANGULAR_DIRECTIVE_NAME_Directive');

            function tick() {
                $log.info('tick');
            }
            var promise = $interval(tick, 1000);
            scope.$on('$destroy', function() {
                $log.debug('timer destroyed');
                $interval.cancel(promise);
            });
            element.css({
                'background-color': 'blue'
            });
            var offsetTop = element.offset().top;
            angular.element($window).bind('wheel', function() {
                console.log('scrolling...');
                console.log($window.scrollTop());
                console.log($window.scrollBottom());
                element.css({
                    'top': offsetTop + 'px'
                });
            });

            element.bind("wheel", function() {
                console.log('Scrolled below header.');
            });


            //var topClass = attrs.setClassWhenAtTop; // get CSS class from directive's attribute value
            // get element's offset top relative to document

            $window.on('scroll', function(e) {
                console.log('Scrolled below header.');
                //if ($win.scrollTop() >= offsetTop) {
                //    element.addClass(topClass);
                //} else {
                //    element.removeClass(topClass);
                //}
            });
        }

    }
})
();