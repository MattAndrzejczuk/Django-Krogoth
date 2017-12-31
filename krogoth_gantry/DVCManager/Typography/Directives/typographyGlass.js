(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);

    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive($interval) {


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
                console.log('link');
                console.log('link');



                element.on('mousedown', function (event) {
                    // Prevent default dragging of selected content
                    console.log('mousedown');
                    element.css({
                        backgroundPositionY: (element.offset().top * -1) + 'px',
                        backgroundPositionX: (element.offset().left * -1) + 'px'
                    });
                });

                function updateTime() {
                    // console.log('updateTime');
                    // console.log($window.scrollY);

                    var childPos = element.offset();
                    var childHeight = element.height();
                    var parentoffset = element.parent().offset();
                    var parentHeight = element.parent().height();

                    // console.log('childPos');
                    // console.log(childPos);
                    // console.log('element');
                    // console.log(element);
                    // console.log('parentHeight');
                    // console.log(parentHeight);
                    // console.log('parentoffset');
                    // console.log(parentoffset);
                    // console.log('childHeight');
                    // console.log(childHeight);
                    // console.log(element.parent());
                    // var finalY = (childPos.top + 500) - (parentHeight);

                    const y = 'translateY(' + (element.offset().top * -1) + 'px)';
                    const x = 'translateX(' + (element.offset().top * -1) + 'px)';

                    element.css({
                        WebkitTransform: 'translate('+x+','+y+')'
                        // backgroundPositionY: y,
                        // backgroundPositionX: x
                    });

                }

                var stopTime = $interval(updateTime, 100);

                element.on('$destroy', function () {
                    console.log('$destroy  - - - - - - - - -');
                    $interval.cancel(stopTime);
                });
            }
        }
    }
})
();

