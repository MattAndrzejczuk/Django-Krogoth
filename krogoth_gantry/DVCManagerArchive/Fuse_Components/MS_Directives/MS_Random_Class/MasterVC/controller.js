(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController() {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.colors = [
            'yellow',
            'red',
            'blue',
            'orange',
            'green'
        ];

        vm.colors2 = [
            'yellow',
            'red',
            'blue',
            'orange',
            'green'
        ];
    }
})();