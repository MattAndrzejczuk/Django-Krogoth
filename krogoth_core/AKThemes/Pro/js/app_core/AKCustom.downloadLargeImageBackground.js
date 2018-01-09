(function () {
    'use strict';
    angular
        .module('app.core')
        .directive('largeImageDownloadBackground', largeImageDownloadBackground);

    /** @ngInject */
    function largeImageDownloadBackground($interval) {


		console.log('largeImageDownloadBackground');
        console.log('largeImageDownloadBackground');
        console.log('largeImageDownloadBackground');
        console.log('largeImageDownloadBackground');
        console.log('largeImageDownloadBackground');
        alert('Global Directive has been loaded successfully.');


        return {
            // scope: {
            //     offset: "@offset",
            //     scrollClass: '='
            // },
            link: function (scope, element, attr) {
                element.css({
                         'background-color': 'green'
                     });
                // function updateTime() {
                //     const y = (element.offset().top * -1) + 'px';
                //     const x = (element.offset().left * -1) + 'px';
                //     element.css({
                //         backgroundPositionY: y,
                //         backgroundPositionX: x
                //     });
                // }
                // var stopTime = $interval(updateTime, 1000);
                // element.on('$destroy', function () {
                //     console.log('akFrostedGlass $destroyed');
                //     $interval.cancel(stopTime);
                // });
            }
        }
    }
})
();