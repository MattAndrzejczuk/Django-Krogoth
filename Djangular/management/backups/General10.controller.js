(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($stateParams, CommunityForumService) {
        var vm = this;

        vm.listData = [];
        CommunityForumService.getDetailCategory(1).then(function(data) {
            vm.listData = data;
        });
    }
})();