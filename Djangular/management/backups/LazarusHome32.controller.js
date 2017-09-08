(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController() {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.lazarusVersion = document.getElementById("DjangularVersion").innerHTML.replace('Djangular ', '');
        document.getElementById("DjangularMetaText_01").innerHTML = 'Lazarus Unit Editor';
    }
})();