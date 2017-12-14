(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController() {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';
        vm.documentation = [];


        vm.documentation.push({
            "name": "LazarusII Data Model",
            "root": "/LazarusII/serialized",
            "description": "Where all Total Annihilation data is stored.",
            "endpoint": "/"
        });

        vm.documentation.push({
            "name": "LazarusII",
            "root": "/LazarusII/serialized",
            "description": "Unit FBI Data",
            "endpoint": "/FBISerialized"
        });

        vm.documentation.push({
            "name": "LazarusII",
            "root": "/LazarusII/serialized",
            "description": "Weapons live here.",
            "endpoint": "/WeaponTDF"
        });

        vm.documentation.push({
            "name": "LazarusII",
            "root": "/LazarusII/serialized",
            "description": "The corpse data for units and structures.",
            "endpoint": "/FeatureTDF"
        });

        vm.documentation.push({
            "name": "LazarusII",
            "root": "/LazarusII/serialized",
            "description": "Unit command card for building units and structures.",
            "endpoint": "/DownloadTDF"
        });

        vm.documentation.push({
            "name": "LazarusII",
            "root": "/LazarusII/serialized",
            "description": "TA Sound Data, gives url to WAV files.",
            "endpoint": "/SoundTDF"
        });

    }
})();