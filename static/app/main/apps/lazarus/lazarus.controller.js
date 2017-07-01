(function () {
    'use strict';

    angular
        .module('app.lazarus')
        .controller('LazarusController', LazarusController);

    /** @ngInject */
    function LazarusController($mdSidenav, Documents, $log, $http, $mdToast, $mdDialog) {
        var vm = this;

        // Data
        vm.accounts = {
            'creapond': 'johndoe@creapond.com',
            'withinpixels': 'johndoe@withinpixels.com'
        };
        vm.selectedAccount = 'creapond';
        vm.currentView = 'list';
        vm.showDetails = true;

        $log.log('LazarusController');
        $log.log(Documents);
        vm.path = 'just a sample path'; //Documents['arm_data'];
        vm.folders = []; // Documents.data['thumbnail'];
        vm.files = Documents['arm_data'];
        vm.selected = vm.files[0];


        // Fuse Methods
        vm.fileAdded = fileAdded;
        vm.select = select;
        vm.toggleDetails = toggleDetails;
        vm.toggleSidenav = toggleSidenav;
        vm.toggleView = toggleView;

        // ArmPrime Variables - Toast
        vm.isDlgOpen = false;

        // ArmPrime Methods - Toast
        vm.closeToast = closeToast;
        vm.openMoreInfo = openMoreInfo;
        vm.showCustomToast = showCustomToast;


        // ArmPrime Sound Effects
        vm.playSoundError = playSoundError;
        vm.playSoundClickUnit = playSoundClickUnit;

        //////////

        function playSoundError() {
            var audio = new Audio("/static/gui_sfx/alert_warn1.wav");
            audio.play();
        }

        function playSoundClickUnit() {
            var audio = new Audio("/static/gui_sfx/click_select_units.wav");
            audio.play();
        }


        function showCustomToast(msg) {
            if (msg) {
                var final_msg = msg.replace(" ", "%20");
                $mdToast.show({
                    hideDelay: 4000,
                    position: 'bottom left',
                    controller: 'ToastCtrl',
                    templateUrl: '/LazarusII/CustomToast/?msg=' + final_msg
                });
            }
        }


        function closeToast() {
            if (vm.isDlgOpen) return;

            $mdToast
                .hide()
                .then(function () {
                    vm.isDlgOpen = false;
                    $log.info('TODO: add close sound effect here.');
                });
        }


        function openMoreInfo(e) {
            if (vm.isDlgOpen) return;

            vm.isDlgOpen = true;
            $mdDialog
                .show($mdDialog
                    .alert()
                    .title('More info goes here.')
                    .textContent('Something witty.')
                    .ariaLabel('More info')
                    .ok('Got it')
                    .targetEvent(e)
                )
                .then(function () {
                    vm.isDlgOpen = false;
                })
        }


        /**
         * File added callback
         * Triggers when files added to the uploader
         *
         * @param file
         */
        function fileAdded(file) {
            // Prepare the temp file data for file list
            var uploadingFile = {
                id: file.uniqueIdentifier,
                file: file,
                type: '',
                owner: 'Emily Bennett',
                size: '',
                modified: moment().format('MMMM D, YYYY'),
                opened: '',
                created: moment().format('MMMM D, YYYY'),
                extention: '',
                location: 'My Files > Documents',
                offline: false,
                preview: '/static/assets/images/etc/sample-file-preview.jpg'
            };

            // Append it to the file list
            vm.files.push(uploadingFile);
        }


        /**
         * Select an item
         *
         * @param item
         */
        function select(item) {
            console.log(item);
            // Simple GET request example:
            $http({
                method: 'GET',
                url: item['RESTful_unit_data']
            }).then(function successCallback(response) {
                vm.playSoundClickUnit();
                vm.selected = response.data[0];
                console.log(response.data[0]);
                // this callback will be called asynchronously
                // when the response is available
            }, function errorCallback(response) {
                console.log(response.data);
                showCustomToast('Failed to load unit, we will resolve this issue soon!');
                vm.playSoundError();
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        }

        /**
         * Toggle details
         *
         * @param item
         */
        function toggleDetails(item) {
            vm.selected = item;
            toggleSidenav('details-sidenav');
        }

        /**
         * Toggle sidenav
         *
         * @param sidenavId
         */
        function toggleSidenav(sidenavId) {
            $mdSidenav(sidenavId).toggle();
        }

        /**
         * Toggle view
         */
        function toggleView() {
            vm.currentView = vm.currentView === 'list' ? 'grid' : 'list';
        }
    }
})();


(function () {
    'use strict';

    angular
        .module('app.toastCtrl',
            [
                // 3rd Party Dependencies
                'flow'
            ]
        );

})();

(function () {
    'use strict';
    angular
        .module('app.toastCtrl')
        .controller('ToastCtrl', ToastCtrl);
    /** @ngInject */
    function ToastCtrl($scope, $mdToast) {
        var vm = this;

        $scope.closeToast = function () {
            $mdToast.hide();
        };
    }
})();
