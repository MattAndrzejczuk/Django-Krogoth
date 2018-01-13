(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($cookies, $mdToast) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.currentLayout = $cookies.get('layoutStyle') || 'verticalNavigation';
        vm.selectLayout = selectLayout;

        function selectLayout(sel) {
            $mdToast.show({
                template: '<md-toast>Selected ' + sel + '</md-toast>',
                hideDelay: 2000,
                position: 'bottom right'
            });
            $cookies.put('layoutStyle', sel);
        }

        vm.layoutOptions = [
            'verticalNavigation',
            'verticalNavigationFullwidthToolbar',
            'verticalNavigationFullwidthToolbar2',
            'horizontalNavigation',
            'contentOnly',
            'contentWithToolbar'
        ]


    }
})();