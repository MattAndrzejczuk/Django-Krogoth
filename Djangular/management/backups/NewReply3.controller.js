(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('_SLAVE_NAME_Controller', _SLAVE_NAME_Controller);

    function _SLAVE_NAME_Controller($stateParams, $log) {
        var vm = this;
        vm.viewName = '_SLAVE_NAME_' + $stateParams.id;
        vm.threadId = $stateParams.id;
    }
})();