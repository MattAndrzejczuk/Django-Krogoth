/* ~ ~ ~ ~ ~ ~ ~ ~ ANGULARJS 1.7.2 ~ ~ ~ ~ ~ ~ ~ ~ */
(function () {
    'use strict';
    angular
        .module('app.core')
        .directive('akFrostedGlass', akFrostedGlassDirective);

    /** @ngInject */
    function akFrostedGlassDirective($interval) {

		console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');
        console.log(' ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ akFrostedGlass ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ❄️ ');


        return {
            // scope: {
            //     offset: "@offset",
            //     scrollClass: '='
            // },
            link: function (scope, element, attr) {
                function updateTime() {
                    //const childPos = element.offset();
                    //const childHeight = element.height();
                    //const parentoffset = element.parent().offset();
                    //const parentHeight = element.parent().height();

                    const y = (element.offset().top * -1) + 'px';
                    const x = (element.offset().left * -1) + 'px';

                    element.css({
                        backgroundPositionY: y,
                        backgroundPositionX: x
                    });

                }

                var stopTime = $interval(updateTime, 100);

                element.on('$destroy', function () {
                    console.log('akFrostedGlass $destroyed');
                    $interval.cancel(stopTime);
                });
            }
        }
    }
})
();