(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);

    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive($interval, $window) {

        console.log('_DJANGULAR_DIRECTIVE_NAME_Directive');
        console.log('_DJANGULAR_DIRECTIVE_NAME_Directive');
        console.log('_DJANGULAR_DIRECTIVE_NAME_Directive');
        console.log('_DJANGULAR_DIRECTIVE_NAME_Directive');
        console.log('_DJANGULAR_DIRECTIVE_NAME_Directive');


        return {
            // scope: {
            //     offset: "@offset",
            //     scrollClass: '='
            // },
            link: function (scope, element, attr) {

                element.css({
                    'background-image': "url('/static/fancy_bgs/bg-blur-01-light.jpg')"
                });

                function updateTime() {
                    //const childPos = element.offset();
                    //const childHeight = element.height();
                    const parentoffsetLeft = element.parent().offset().left;
                    //const parentHeight = element.parent().height();

                    const y = ((element.offset().top) * -1) + 'px';
                    const x = ((element.offset().left) * -1) + 'px';

                    element.css({
                        'background-position-y': y,
                        'background-position-x': x,
                        'border-style': 'solid',
                        'border-width': '5px'
                    });

                }

                var stopTime = $interval(updateTime, 500);

                element.on('$destroy', function () {
                    console.log('akFrostedGlass $destroyed');
                    $interval.cancel(stopTime);
                });
            }
        }
    }
})
();


// .glass-test {
//     backgroundAttachment: "fixed",
//     backgroundImage: "url('/static/fancy_bgs/EPIC_Planet-3-opaque-2k.jpg')",
//     backgroundSize: "2000px 2000px",
//     backgroundRepeat: "no-repeat",
//     backgroundPositionX: "left",
//     backgroundPositionY: "top"
// }
// element.css({
//     backgroundPositionY: y,
//     backgroundPositionX: x
// });