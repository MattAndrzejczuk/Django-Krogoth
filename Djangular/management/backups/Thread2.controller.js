(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('_SLAVE_NAME_Controller', _SLAVE_NAME_Controller);

    function _SLAVE_NAME_Controller($stateParams, $log, CommunityForumService) {
        var vm = this;

        vm.createThreadMode = false;
        vm.createReplyMode = false;
        vm.form = {};
        vm.currentState = $stateParams;
        vm.addReply = addReply;
        vm.newThreadHttpPOSTRequest = newThreadHttpPOSTRequest;
        vm.newReplyHttpPOSTRequest = newReplyHttpPOSTRequest;

        if ($stateParams.id) {
            vm.viewName = '_SLAVE_NAME_ ' + $stateParams.id;
            vm.listData = {};
            CommunityForumService.getDetailThread($stateParams.id).then(function(data) {
                vm.listData = data;
            });
        } else {
            vm.viewName = 'Create New _SLAVE_NAME_';
            vm.createThreadMode = true;
        }

        function addReply() {
            vm.createReplyMode = !vm.createReplyMode;
        }

        function newThreadHttpPOSTRequest() {
            $log.log('newThreadHttpPOSTRequest');
            var jsonData = {
                "title": vm.form.title,
                "body": vm.form.body,
                "category": 1
            };
            $log.log(jsonData);
            vm.viewName = 'Posting New Thread . . . ';
            CommunityForumService.postNewThread(jsonData).then(function(data) {
                vm.createThreadMode = false;
                var newThreadToLoad = data['id'];
                vm.viewName = 'Loading Newly Created Thread . . . ';
                vm.form = {};
                CommunityForumService.getDetailThread(newThreadToLoad).then(function(data) {
                    vm.viewName = '';
                    vm.listData = data;
                });
            });
        }

        function newReplyHttpPOSTRequest() {
            $log.log('newReplyHttpPOSTRequest');
            var jsonData = {
                "body": vm.form.body,
                "post": $stateParams.id
            };
            $log.log(jsonData);
            vm.viewName = 'Posting Reply . . . ';
            CommunityForumService.postNewReply(jsonData).then(function(data) {
                vm.createReplyMode = false;
                vm.viewName = 'Reloading Thread . . . ';
                vm.form = {};
                CommunityForumService.getDetailThread($stateParams.id).then(function(data) {
                    vm.listData = data;
                    vm.viewName = '';
                });
            });
        }


    }
})();