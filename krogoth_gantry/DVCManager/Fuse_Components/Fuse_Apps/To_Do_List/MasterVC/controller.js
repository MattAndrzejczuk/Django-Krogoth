(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($document, $mdDialog, $mdSidenav) {
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
        vm.tasks = [{
            "id": "561551bd7fe2ff461101c192",
            "title": "Proident tempor est nulla irure ad est",
            "notes": "Id nulla nulla proident deserunt deserunt proident in quis. Cillum reprehenderit labore id anim laborum.",
            "startDate": "Wednesday, January 29, 2014 3:17 PM",
            "dueDate": null,
            "completed": false,
            "starred": false,
            "important": false,
            "deleted": false,
            "tags": [
                {
                    "id": 1,
                    "name": "frontend",
                    "label": "Frontend",
                    "color": "#388E3C"
                }
            ]
        },
            {
                "id": "561551bd4ac1e7eb77a3a750",
                "title": "Magna quis irure quis ea pariatur laborum",
                "notes": "",
                "startDate": "Sunday, February 1, 2015 1:30 PM",
                "dueDate": "Friday, December 30, 2016 10:07 AM",
                "completed": false,
                "starred": false,
                "important": true,
                "deleted": false,
                "tags": [
                    {
                        "id": 1,
                        "name": "frontend",
                        "label": "Frontend",
                        "color": "#388E3C"
                    },
                    {
                        "id": 4,
                        "name": "issue",
                        "label": "Issue",
                        "color": "#0091EA"
                    }
                ]
            },
            {
                "id": "561551bd917bfec2ddef2d49",
                "title": "Ullamco duis commodo sint ad aliqua aute",
                "notes": "Sunt laborum enim nostrud ea fugiat cillum mollit aliqua exercitation ad elit.",
                "startDate": "Friday, April 11, 2014 3:43 AM",
                "dueDate": "Wednesday, July 26, 2017 11:14 AM",
                "completed": false,
                "starred": true,
                "important": true,
                "deleted": false,
                "tags": [
                    {
                        "id": 3,
                        "name": "API",
                        "label": "API",
                        "color": "#FF9800"
                    }
                ]
            },
            {
                "id": "561551bdeeb2fd6877e18c29",
                "title": "Eiusmod non occaecat pariatur Lorem in ex",
                "notes": "Nostrud anim mollit incididunt qui qui sit commodo duis. Anim amet irure aliquip duis nostrud sit quis fugiat ullamco non dolor labore. Lorem sunt voluptate laboris culpa proident. Aute eiusmod aliqua exercitation irure exercitation qui laboris mollit occaecat eu occaecat fugiat.",
                "startDate": "Wednesday, May 7, 2014 4:14 AM",
                "dueDate": "Friday, December 15, 2017 4:01 AM",
                "completed": true,
                "starred": true,
                "important": false,
                "deleted": false,
                "tags": [
                    {
                        "id": 2,
                        "name": "backend",
                        "label": "Backend",
                        "color": "#F44336"
                    }
                ]
            }];
        vm.tags = [
            {
                "id": 1,
                "name": "frontend",
                "label": "Frontend",
                "color": "#388E3C"
            },
            {
                "id": 2,
                "name": "backend",
                "label": "Backend",
                "color": "#F44336"
            },
            {
                "id": 3,
                "name": "API",
                "label": "API",
                "color": "#FF9800"
            },
            {
                "id": 4,
                "name": "issue",
                "label": "Issue",
                "color": "#0091EA"
            },
            {
                "id": 5,
                "name": "mobile",
                "label": "Mobile",
                "color": "#9C27B0"
            }
        ];
        vm.completed = [];
        vm.colors = ['blue', 'blue-grey', 'orange', 'pink', 'purple'];
        vm.projects = {
            'creapond': 'Project Creapond',
            'withinpixels': 'Project Withinpixels'
        };
        vm.selectedFilter = {
            filter: 'Start Date',
            dueDate: 'Next 3 days'
        };
        vm.selectedProject = 'creapond';

        // Tasks will be filtered against these models
        vm.taskFilters = {
            search: '',
            tags: [],
            completed: '',
            deleted: false,
            important: '',
            starred: '',
            startDate: '',
            dueDate: ''
        };
        vm.taskFiltersDefaults = angular.copy(vm.taskFilters);
        vm.showAllTasks = true;

        vm.taskOrder = '';
        vm.taskOrderDescending = false;

        vm.sortableOptions = {
            handle: '.handle',
            forceFallback: true,
            ghostClass: 'todo-item-placeholder',
            fallbackClass: 'todo-item-ghost',
            fallbackOnBody: true,
            sort: true
        };
        vm.msScrollOptions = {
            suppressScrollX: true
        };

        // Methods
        vm.preventDefault = preventDefault;
        vm.openTaskDialog = openTaskDialog;
        vm.toggleCompleted = toggleCompleted;
        vm.toggleSidenav = toggleSidenav;
        vm.toggleFilter = toggleFilter;
        vm.toggleFilterWithEmpty = toggleFilterWithEmpty;
        vm.filterByStartDate = filterByStartDate;
        vm.filterByDueDate = filterByDueDate;
        vm.resetFilters = resetFilters;
        vm.toggleTagFilter = toggleTagFilter;
        vm.isTagFilterExists = isTagFilterExists;

        init();

        //////////

        /**
         * Initialize the controller
         */
        function init() {
            angular.forEach(vm.tasks, function (task) {
                if (task.startDate) {
                    task.startDate = new Date(task.startDate);
                    task.startDateTimestamp = task.startDate.getTime();
                }

                if (task.dueDate) {
                    task.dueDate = new Date(task.dueDate);
                    task.dueDateTimestamp = task.dueDate.getTime();
                }
            });
        }

        /**
         * Prevent default
         *
         * @param e
         */
        function preventDefault(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        /**
         * Open new task dialog
         *
         * @param ev
         * @param task
         */
        function openTaskDialog(ev, task) {
            $mdDialog.show({
                controller: 'To_Do_ListSlaveController',
                controllerAs: 'vm',
                templateUrl: '/krogoth_gantry/DynamicHTMLSlaveInjector/?name=To_Do_ListSlave',
                parent: angular.element($document.body),
                targetEvent: ev,
                clickOutsideToClose: true,
                locals: {
                    Task: task,
                    Tasks: vm.tasks,
                    event: ev
                }
            });
        }

        /**
         * Toggle completed status of the task
         *
         * @param task
         * @param event
         */
        function toggleCompleted(task, event) {
            event.stopPropagation();
            task.completed = !task.completed;
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
         * Toggles filter with true or false
         *
         * @param filter
         */
        function toggleFilter(filter) {
            vm.taskFilters[filter] = !vm.taskFilters[filter];

            checkFilters();
        }

        /**
         * Toggles filter with true or empty string
         * @param filter
         */
        function toggleFilterWithEmpty(filter) {
            if (vm.taskFilters[filter] === '') {
                vm.taskFilters[filter] = true;
            }
            else {
                vm.taskFilters[filter] = '';
            }

            checkFilters();
        }

        /**
         * Reset filters
         */
        function resetFilters() {
            vm.showAllTasks = true;
            vm.taskFilters = angular.copy(vm.taskFiltersDefaults);
        }

        /**
         * Check filters and mark showAllTasks
         * as true if no filters selected
         */
        function checkFilters() {
            vm.showAllTasks = !!angular.equals(vm.taskFiltersDefaults, vm.taskFilters);
        }

        /**
         * Filter by startDate
         *
         * @param item
         * @returns {boolean}
         */
        function filterByStartDate(item) {
            if (vm.taskFilters.startDate === true) {
                return item.startDate === new Date();
            }

            return true;
        }

        /**
         * Filter Due Date
         *
         * @param item
         * @returns {boolean}
         */
        function filterByDueDate(item) {
            if (vm.taskFilters.dueDate === true) {
                return !(item.dueDate === null || item.dueDate.length === 0);
            }

            return true;
        }

        /**
         * Toggles tag filter
         *
         * @param tag
         */
        function toggleTagFilter(tag) {
            var i = vm.taskFilters.tags.indexOf(tag);

            if (i > -1) {
                vm.taskFilters.tags.splice(i, 1);
            }
            else {
                vm.taskFilters.tags.push(tag);
            }

            checkFilters();
        }

        /**
         * Returns if tag exists in the tagsFilter
         *
         * @param tag
         * @returns {boolean}
         */
        function isTagFilterExists(tag) {
            return vm.taskFilters.tags.indexOf(tag) > -1;
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