(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController(CommunityForumService) {

        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.listData = [];

        CommunityForumService.getListCategories().then(function(data) {
            vm.listData = data;
        });
    }
})();