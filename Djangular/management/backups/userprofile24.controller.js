(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController(Timeline, About, PhotosVideos, $http) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        vm.user = {};

        vm.posts = Timeline.posts;
        vm.activities = Timeline.activities;
        vm.about = About.data;
        vm.photosVideos = PhotosVideos.data;

        vm.loadUser = loadUser;

        function loadUser() {
            $http({
                url: '/rest-auth/user/'
            }).then(function successCallback(response) {
                vm.user = response.data;
            }, function errorCallback(response) {
                $mdToast.show($mdToast.simple().textContent('Login is required.'));
            });
        }

        vm.loadUser();
    }
})();