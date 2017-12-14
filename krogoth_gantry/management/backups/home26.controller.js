(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http, CommunityForumService, $stateParams, $log, $timeout) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.lazarusVersion = document.getElementById("krogoth_gantryVersion").innerHTML.replace('krogoth_gantry ', '');

        vm.formatThreadBody = formatThreadBody;
        document.getElementById("krogoth_gantryMetaText_01").innerHTML = 'ArmPrime News';

        vm.listData = [];
        CommunityForumService.getDetailCategory(4).then(function(data) {
            vm.listData = data;
            $log.info('PREPARING TO FORMAT ALL THREADS!');
            $log.log('vm.listData.length: ')
            $log.debug(vm.listData.posts.length);
            $log.debug(vm.listData.posts);
            var formatHtml = function() {
                for (var i = 0; i < vm.listData.posts.length; i++) {
                    vm.formatThreadBody(vm.listData.posts[i]['body'], vm.listData.posts[i]['id']);
                }
            }
            $timeout(formatHtml, 500);
        });


        function formatThreadBody(text, threadId) {
            $log.info('Will now format the thread: ');
            $log.debug("threadBody" + threadId);
            document.getElementById("threadBody" + threadId).innerHTML = text;
        }
    }
})();