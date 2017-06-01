(function ()
{
    'use strict';

    angular
        .module('app.lazarus')
        .controller('LazarusController', LazarusController);

    /** @ngInject */
    function LazarusController($mdSidenav, Documents, $log)
    {
        var vm = this;

        // Data
        vm.accounts = {
            'creapond'    : 'johndoe@creapond.com',
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


        // Methods
        vm.fileAdded = fileAdded;
        vm.select = select;
        vm.toggleDetails = toggleDetails;
        vm.toggleSidenav = toggleSidenav;
        vm.toggleView = toggleView;

        //////////

        /**
         * File added callback
         * Triggers when files added to the uploader
         *
         * @param file
         */
        function fileAdded(file)
        {
            // Prepare the temp file data for file list
            var uploadingFile = {
                id       : file.uniqueIdentifier,
                file     : file,
                type     : '',
                owner    : 'Emily Bennett',
                size     : '',
                modified : moment().format('MMMM D, YYYY'),
                opened   : '',
                created  : moment().format('MMMM D, YYYY'),
                extention: '',
                location : 'My Files > Documents',
                offline  : false,
                preview  : '/static/assets/images/etc/sample-file-preview.jpg'
            };

            // Append it to the file list
            vm.files.push(uploadingFile);
        }



        /**
         * Select an item
         *
         * @param item
         */
        function select(item)
        {
            vm.selected = item;
        }

        /**
         * Toggle details
         *
         * @param item
         */
        function toggleDetails(item)
        {
            vm.selected = item;
            toggleSidenav('details-sidenav');
        }

        /**
         * Toggle sidenav
         *
         * @param sidenavId
         */
        function toggleSidenav(sidenavId)
        {
            $mdSidenav(sidenavId).toggle();
        }

        /**
         * Toggle view
         */
        function toggleView()
        {
            vm.currentView = vm.currentView === 'list' ? 'grid' : 'list';
        }
    }
})();