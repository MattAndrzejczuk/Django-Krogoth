(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);

    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive($interval, $window) {


        console.log('styleChangerBg');
        console.log('styleChangerBg');
        console.log('styleChangerBg');
        console.log('styleChangerBg');
        console.log('styleChangerBg');


        return {
            // scope: {
            //     offset: "@offset",
            //     scrollClass: '='
            // },
            link: function (scope, element, attr) {

                element.on('mousedown', function (event) {
                    // Prevent default dragging of selected content
                    console.log('mousedown');
                    element.css({
                        backgroundPositionY: (element.offset().top * -1) + 'px',
                        backgroundPositionX: (element.offset().left * -1) + 'px'
                    });
                });

                function updateTime() {

                    var childPos = element.offset();
                    var childHeight = element.height();
                    var parentoffset = element.parent().offset();
                    var parentHeight = element.parent().height();


                    var finalY = (childPos.top + 500) - (parentHeight);
                    element.css({
                        backgroundPositionY: (element.offset().top * -1) + 'px',
                        backgroundPositionX: (element.offset().left * -1) + 'px'
                    });

                }

                var stopTime = $interval(updateTime, 50);

                element.on('$destroy', function () {
                    console.log('$destroy  - - - - -- - - -');
                    $interval.cancel(stopTime);
                });
            }
        }
    }
})
();

