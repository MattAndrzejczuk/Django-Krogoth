(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdSidenav) {
        var vm = this;
        vm.$onInit = onInit;
        vm.viewName = 'FUSE_APP_NAME';
        vm.viewDidLoad = viewDidLoad;


        function onInit() {
            vm.viewDidLoad();
        }

        function viewDidLoad() {
            console.log('FUSE_APP_NAME did finish loading');
        }

        // Data
        vm.accounts = {
            'creapond': 'johndoe@creapond.com',
            'withinpixels': 'johndoe@withinpixels.com'
        };
        vm.selectedAccount = 'creapond';
        vm.currentView = 'list';
        vm.showDetails = true;

        vm.path = [
            "My Files",
            "Documents"
        ];
        vm.folders = [{
            "name": "Work Documents",
            "type": "folder",
            "owner": "me",
            "size": "",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true
        }, {
            "name": "Public Documents",
            "type": "folder",
            "owner": "public",
            "size": "",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true
        }, {
            "name": "Private Documents",
            "type": "folder",
            "owner": "me",
            "size": "",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true
        }];
        vm.files = [{
            "name": "Ongoing projects",
            "type": "document",
            "owner": "Emily Bennett",
            "size": "1.2 Mb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }, {
            "name": "Shopping list",
            "type": "document",
            "owner": "Emily Bennett",
            "size": "980 Kb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }, {
            "name": "Invoices",
            "type": "spreadsheet",
            "owner": "Emily Bennett",
            "size": "750 Kb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }, {
            "name": "Crash logs",
            "type": "document",
            "owner": "Emily Bennett",
            "size": "980 Mb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }, {
            "name": "System logs",
            "type": "document",
            "owner": "Emily Bennett",
            "size": "52 Kb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }, {
            "name": "Prices",
            "type": "spreadsheet",
            "owner": "Emily Bennett",
            "size": "27 Mb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }, {
            "name": "Anabelle Manual",
            "type": "document",
            "owner": "Emily Bennett",
            "size": "1.1 Kb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }, {
            "name": "Steam summer sale budget",
            "type": "spreadsheet",
            "owner": "Emily Bennett",
            "size": "505 Kb",
            "modified": "July 8, 2015",
            "opened": "July 8, 2015",
            "created": "July 8, 2015",
            "extention": "",
            "location": "My Files > Documents",
            "offline": true,
            "preview": "assets/images/etc/sample-file-preview.jpg"
        }];
        vm.selected = vm.files[0];

        vm.ngFlowOptions = {
            // You can configure the ngFlow from here
            target: '/api/__ExamplesBasicImageUpload/',
            chunkSize: 15 * 1024 * 1024,
            maxChunkRetries: 1,
            simultaneousUploads: 1,
            testChunks: false,
            progressCallbacksInterval: 1000
        };
        vm.ngFlow = {
            // ng-flow will be injected into here through its directive
            flow: {}
        };

        // Methods
        vm.fileAdded = fileAdded;
        vm.upload = upload;
        vm.fileSuccess = fileSuccess;

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
        function fileAdded(file) {
            // Prepare the temp file data for file list
            var uploadingFile = {
                id: file.uniqueIdentifier,
                image: file,
                type: '',
                name: "image",
                owner: 'Emily Bennett',
                size: '',
                modified: moment().format('MMMM D, YYYY'),
                opened: '',
                created: moment().format('MMMM D, YYYY'),
                extention: '',
                location: 'My Files > Documents',
                offline: false,
                preview: 'assets/images/etc/sample-file-preview.jpg'
            };

            // Append it to the file list
            vm.files.push(file);
        }

        /**
         * Upload
         * Automatically triggers when files added to the uploader
         */
        function upload() {
            // Set headers
            vm.ngFlow.flow.opts.headers = {
                'X-Requested-With': 'XMLHttpRequest',
                //'X-XSRF-TOKEN'    : $cookies.get('XSRF-TOKEN')
            };

            vm.ngFlow.flow.upload();
        }

        /**
         * File upload success callback
         * Triggers when single upload completed
         *
         * @param file
         * @param message
         */
        function fileSuccess(file, message) {
            // Iterate through the file list, find the one we
            // are added as a temp and replace its data
            // Normally you would parse the message and extract
            // the uploaded file data from it
            angular.forEach(vm.files, function(item, index) {
                if (item.id && item.id === file.uniqueIdentifier) {
                    // Normally you would update the file from
                    // database but we are cheating here!

                    // Update the file info
                    item.name = file.file.name;
                    item.type = 'document';

                    // Figure out & upddate the size
                    if (file.file.size < 1024) {
                        item.size = parseFloat(file.file.size).toFixed(2) + ' B';
                    } else if (file.file.size >= 1024 && file.file.size < 1048576) {
                        item.size = parseFloat(file.file.size / 1024).toFixed(2) + ' Kb';
                    } else if (file.file.size >= 1048576 && file.file.size < 1073741824) {
                        item.size = parseFloat(file.file.size / (1024 * 1024)).toFixed(2) + ' Mb';
                    } else {
                        item.size = parseFloat(file.file.size / (1024 * 1024 * 1024)).toFixed(2) + ' Gb';
                    }
                }
            });
        }

        /**
         * Select an item
         *
         * @param item
         */
        function select(item) {
            vm.selected = item;
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


/*
sh /Vol
*/

/*
sh /Volumes/MBP_Backup/arm-prime/docker/KILL_ALL_.sh
*/

/*
sh /Volumes/MBP_Backup/arm-prime/docker/run-docker-installed.sh
*/