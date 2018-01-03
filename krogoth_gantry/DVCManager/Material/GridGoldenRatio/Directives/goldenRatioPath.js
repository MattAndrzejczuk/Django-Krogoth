(function () {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('_DJANGULAR_DIRECTIVE_NAME_', _DJANGULAR_DIRECTIVE_NAME_Directive);

    /** @ngInject */
    function _DJANGULAR_DIRECTIVE_NAME_Directive($timeout, $interval) {
        const timeoutLen = 800;
        return {
            // scope: {
            //     offset: "@offset",
            //     scrollClass: '='
            // },
            link: function (scope, element, attr) {
                scope.width = 50;
                scope.height = 50;

                function updateTime() {
                    switch (attr.goldenRatioPath) {
                        case '0':
                            $timeout(function () {
                                    /// md grid tiles not good for canvases,
                                    /// so we'll call a timeout hack just for this demo.
                                    const parent = element[0].parentNode.getBoundingClientRect().height;
                                    attr.height = parent;
                                    const halfHeight = parent / 2;

                                    scope.width = parent;
                                    scope.height = parent;
                                    $timeout(function () {
                                            var ctx = element[0].getContext("2d");
                                            ctx.beginPath();
                                            ctx.moveTo(0, parent);
                                            ctx.bezierCurveTo(0, halfHeight, halfHeight, 0, parent, 0);
                                            ctx.stroke();
                                        },
                                        timeoutLen + 100);
                                },
                                timeoutLen + 200);
                            break;
                        case '1':
                            $timeout(function () {
                                    /// md grid tiles not good for canvases,
                                    /// so we'll call a timeout hack just for this demo.
                                    const parent = element[0].parentNode.getBoundingClientRect().height;
                                    attr.height = parent;
                                    const halfHeight = parent / 2;

                                    scope.width = parent;
                                    scope.height = parent;
                                    $timeout(function () {
                                            var ctx = element[0].getContext("2d");
                                            ctx.beginPath();
                                            ctx.moveTo(parent, parent);
                                            ctx.bezierCurveTo(parent, halfHeight, halfHeight, 0, 0, 0);
                                            ctx.stroke();
                                        },
                                        timeoutLen + 300);
                                },
                                timeoutLen + 400);
                            // it.title = '5X5';
                            break;
                        case '4':
                            $timeout(function () {
                                    /// md grid tiles not good for canvases,
                                    /// so we'll call a timeout hack just for this demo.
                                    const parent = element[0].parentNode.getBoundingClientRect().height;
                                    attr.height = parent;
                                    const halfHeight = parent / 2;

                                    scope.width = parent;
                                    scope.height = parent;
                                    $timeout(function () {
                                            var ctx = element[0].getContext("2d");
                                            ctx.beginPath();
                                            ctx.moveTo(0, parent);
                                            ctx.bezierCurveTo(0, parent, parent, parent, parent, 0);
                                            ctx.stroke();
                                        },
                                        timeoutLen + 500);
                                },
                                timeoutLen + 600);
                            // it.title = '1X1';
                            break;
                        case '5':
                            $timeout(function () {
                                    /// md grid tiles not good for canvases,
                                    /// so we'll call a timeout hack just for this demo.
                                    const parent = element[0].parentNode.getBoundingClientRect().height;
                                    attr.height = parent;
                                    const halfHeight = parent / 2;

                                    scope.width = parent;
                                    scope.height = parent;
                                    $timeout(function () {
                                            var ctx = element[0].getContext("2d");
                                            ctx.beginPath();
                                            ctx.moveTo(0, 0);
                                            ctx.bezierCurveTo(0, parent, parent, parent, parent, parent);
                                            ctx.stroke();
                                        },
                                        timeoutLen + 700);
                                },
                                timeoutLen + 800);
                            // it.title = '1X1';
                            break;
                        case '2':
                            $timeout(function () {
                                    /// md grid tiles not good for canvases,
                                    /// so we'll call a timeout hack just for this demo.
                                    const parent = element[0].parentNode.getBoundingClientRect().height;
                                    attr.height = parent;
                                    const halfHeight = parent / 2;

                                    scope.width = parent;
                                    scope.height = parent;
                                    $timeout(function () {
                                            var ctx = element[0].getContext("2d");
                                            ctx.beginPath();
                                            ctx.moveTo(0, parent);
                                            ctx.bezierCurveTo(0, halfHeight, halfHeight, 0, parent, 0);
                                            ctx.stroke();
                                        },
                                        timeoutLen + 900);
                                },
                                timeoutLen + 950);
                            break;
                        case '3':
                            $timeout(function () {
                                    /// md grid tiles not good for canvases,
                                    /// so we'll call a timeout hack just for this demo.
                                    const parent = element[0].parentNode.getBoundingClientRect().height;
                                    attr.height = parent;
                                    const halfHeight = parent / 2;

                                    scope.width = parent;
                                    scope.height = parent;
                                    $timeout(function () {
                                            var ctx = element[0].getContext("2d");
                                            ctx.beginPath();
                                            ctx.moveTo(parent, parent);
                                            ctx.bezierCurveTo(parent, halfHeight, halfHeight, 0, 0, 0);
                                            ctx.stroke();
                                        },
                                        timeoutLen + 970);
                                },
                                timeoutLen + 990);
                            break;
                    }


                }

                var stopTime = $interval(updateTime, 6000);

                element.on('$destroy', function () {
                    console.log('akFrostedGlass $destroyed');
                    $interval.cancel(stopTime);
                });

                updateTime();
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