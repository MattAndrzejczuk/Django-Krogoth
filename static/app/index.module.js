
(function ()
{
    'use strict';

    /**
     * Main module of the Fuse
     */
    angular
        .module('fuse', [

            // Common 3rd Party Dependencies
            'uiGmapgoogle-maps',
            'textAngular',
            'xeditable',

            // Core
            'app.core',
            'app.sample',

            // Navigation
            'app.navigation',

            // Toolbar
            'app.toolbar',

            // Quick Panel
            'app.quick-panel',

            // Apps
            'app.dashboards',
            'app.calendar',
            'app.e-commerce',
            'app.mail',
            'app.chat',
            'app.file-manager',
            'app.gantt-chart',
            'app.scrumboard',
            'app.todo',
            'app.contacts',
            'app.notes',
            /// 'app.sample',
            'app.lazarus',
            'app.toastCtrl',

            // Pages
            'app.pages',
            'ui.tree',

            // User Interface
            'app.ui',

            // Components
            'app.components'



        ]);
})();

///
///  NOT USING THIS ANYMORE ! ! !
///
///  see dynamic_lazarus_page.views
///