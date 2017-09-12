(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .directive('sticky', Sticky);

    Sticky.$inject = ['$mdSticky'];

    /** @ngInject */
    function Sticky($mdSticky, $log) {
        $log.info('sticky directive online');

        return {
            restrict: 'A',
            link: function(scope, element) {
                $log.debug('sticky directive is returning link thingy');
                $mdSticky(scope, element);
            }
        }
    }



})
();