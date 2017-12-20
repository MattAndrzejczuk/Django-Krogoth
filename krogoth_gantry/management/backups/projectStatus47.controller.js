(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdDialog, $scope, $http) {
        var vm = this;

        vm.img1IsVisible = false;
        vm.img2IsVisible = false;
        vm.img3IsVisible = false;
        vm.img4IsVisible = false;
        vm.img5IsVisible = false;
        vm.img6IsVisible = false;

        vm.picInfo = {
            0: '',
            /// DownloadTDF Screenshots:
            1: 'In this mod, we can see which menu and buttons my Arm Fart and Arachnids currently occupy.',
            2: '',
            3: '',
            /// WeaponTDF Screenshots:
            4: 'As you can see, the weapon TDF editor GUI is still in it\'s very early stages.',
            5: 'You can notice the green text below, which is a raw dump of the Weapon TDF data that lives in the ArmPrime database.',
            6: 'In this example, under "Select Weapon Property" we picked "lavaexplosiongaf"'
        };

        vm.previewFullSizeImage = previewFullSizeImage;

        function previewFullSizeImage($event, imgSrc, info) {
            $mdDialog.show({
                targetEvent: $event,
                template: '<md-dialog>' +
                    '<md-dialog-content class="md-background-fg md-hue-3">' +
                    '<br>' +
                    '<img src="{{ imgSrc }}">' +
                    '</img>' +
                    '<p class="md-background-fg md-hue-3"> {{ info }} </p>' +
                    '<br>' +
                    '<div id="responseLog" style="background-color: black"></div> <br>' +
                    '</md-dialog-content>' +
                    '  <md-dialog-actions>' +
                    '    <md-button ng-click="closeDialog()" class="md-warn">' +
                    '      close' +
                    '    </md-button>' +
                    '  </md-dialog-actions>' +
                    '</md-dialog>',
                controller: PreviewFullImageController,
                onComplete: afterShowAnimation,
                locals: {
                    imageInfo: vm.picInfo[info],
                    imageUrl: imgSrc
                }
            });

            function afterShowAnimation(scope, element, options) {}
        }

        function PreviewFullImageController($scope, $mdDialog, $http, imageInfo, imageUrl) {
            $scope.imgSrc = imageUrl;
            $scope.info = imageInfo;
            $scope.closeDialog = function() {
                $mdDialog.hide();
            };
        }



    }
})();