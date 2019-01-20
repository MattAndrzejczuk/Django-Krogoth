(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME', ['flow']).config(config);

    function config($stateProvider,  msApiProvider, msNavigationServiceProvider) {
        $stateProvider
            .state('app.FUSE_APP_NAME', {
                url: '/FUSE_APP_NAME',
                views: {
                    'content@app': {
                        templateUrl: '/krogoth_gantry/DynamicHTMLInjector/?name=FUSE_APP_NAME',
                        controller: 'FUSE_APP_NAMEController as vm'
                    }
                }
            });


        msNavigationServiceProvider.saveItem('FUSE_APP_NAME', {
            title: 'Home',
            icon: 'entypo entypo-home',
            state: 'app.FUSE_APP_NAME',
            weight: 0
        });

        msNavigationServiceProvider.saveItem("ASSETS", {
            title: "Included Graphics",
            icon: "entypo entypo-book-open",
            weight: 8
        });


        /*
        DEFAULTS TO


        msNavigationServiceProvider.saveItem("Fuse_Components.Junk", {
        	title: "Junk",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Fuse_Components", {
        	title: "Fuse Components",
        	icon: "entypo entypo-suitcase",
        	weight: 3
        });
        msNavigationServiceProvider.saveItem("Fuse_Components.Fuse_Layout_Options", {
        	title: "Fuse Layout Options",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Fuse_Components", {
        	title: "Fuse Components",
        	icon: "entypo entypo-suitcase",
        	weight: 3
        });
        msNavigationServiceProvider.saveItem("Fuse_Components.MS_Directives", {
        	title: "MS Directives",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Fuse_Components", {
        	title: "Fuse Components",
        	icon: "entypo entypo-suitcase",
        	weight: 3
        });
        msNavigationServiceProvider.saveItem("Fuse_Components.Fuse_Apps", {
        	title: "Fuse Apps",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Third_Party_APIs", {
        	title: "Third Party APIs",
        	icon: "entypo entypo-signal",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Third_Party_APIs.Blockchain", {
        	title: "Blockchain",
        	icon: "mdi mdi-FAadjust",
        	weight: 3
        });
        msNavigationServiceProvider.saveItem("Third_Party_APIs", {
        	title: "Third Party APIs",
        	icon: "entypo entypo-signal",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Third_Party_APIs.Twitter", {
        	title: "Twitter",
        	icon: "mdi mdi-MDImdi mdi-surround-sound",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Lazy_Loader", {
        	title: "Lazy Loader",
        	icon: "entypo entypo-shareable",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Lazy_Loader.Example_1", {
        	title: "Example 1",
        	icon: "mdi mdi-FAfa fa-tasks",
        	weight: 0
        });
		

        msNavigationServiceProvider.saveItem("OS_X_Theme", {
        	title: "OS X Theme",
        	icon: "entypo entypo-palette",
        	weight: 10
        });
        msNavigationServiceProvider.saveItem("OS_X_Theme.Examples", {
        	title: "Examples",
        	icon: "mdi mdi-FAfa fa-apple",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Theme_Frameworks", {
        	title: "Theme Frameworks",
        	icon: "entypo entypo-air",
        	weight: 6
        });
        msNavigationServiceProvider.saveItem("Theme_Frameworks.Bootstrap", {
        	title: "Bootstrap",
        	icon: "mdi mdi-FAfa fa-twitter-square",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Theme_Frameworks", {
        	title: "Theme Frameworks",
        	icon: "entypo entypo-air",
        	weight: 6
        });
        msNavigationServiceProvider.saveItem("Theme_Frameworks.Material_Design", {
        	title: "Material Design",
        	icon: "mdi mdi-MDImdi mdi-google-nearby",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_IDE", {
        	title: "Web IDE",
        	icon: "entypo entypo-tools",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_IDE.Krogoth_Gantry", {
        	title: "Krogoth Gantry",
        	icon: "mdi mdi-FAfa fa-th",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_IDE", {
        	title: "Web IDE",
        	icon: "entypo entypo-tools",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_IDE.Krogoth_Core", {
        	title: "Krogoth Core",
        	icon: "mdi mdi-MDImdi mdi-chemical-weapon",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("RESTful", {
        	title: "RESTful",
        	icon: "mdi mdi-code",
        	weight: 5
        });
        msNavigationServiceProvider.saveItem("RESTful.Angular_Formly", {
        	title: "Angular Formly",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("RESTful", {
        	title: "RESTful",
        	icon: "mdi mdi-code",
        	weight: 5
        });
        msNavigationServiceProvider.saveItem("RESTful.Django_REST_Framework", {
        	title: "Django REST Framework",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("RESTful", {
        	title: "RESTful",
        	icon: "mdi mdi-code",
        	weight: 5
        });
        msNavigationServiceProvider.saveItem("RESTful.Third_Party_API", {
        	title: "Third Party API",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_Sockets", {
        	title: "Web Sockets",
        	icon: "entypo entypo-signal",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_Sockets.Advanced", {
        	title: "Advanced",
        	icon: "mdi mdi-FAadjust",
        	weight: 3
        });
        msNavigationServiceProvider.saveItem("Web_Sockets", {
        	title: "Web Sockets",
        	icon: "entypo entypo-signal",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_Sockets.Sequenced_Commands", {
        	title: "Sequenced Commands",
        	icon: "mdi mdi-MDImdi mdi-surround-sound",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_Sockets", {
        	title: "Web Sockets",
        	icon: "entypo entypo-signal",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Web_Sockets.Basics", {
        	title: "Basics",
        	icon: "mdi mdi-MDImdi mdi-surround-sound",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth", {
        	title: "Krogoth",
        	icon: "entypo entypo-network",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth.Directives", {
        	title: "Directives",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth", {
        	title: "Krogoth",
        	icon: "entypo entypo-network",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth.Async_Flow", {
        	title: "Async Flow",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth", {
        	title: "Krogoth",
        	icon: "entypo entypo-network",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth.Partials", {
        	title: "Partials",
        	icon: "mdi mdi-MDImdi mdi-webpack",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth", {
        	title: "Krogoth",
        	icon: "entypo entypo-network",
        	weight: 0
        });
        msNavigationServiceProvider.saveItem("Krogoth.Base64", {
        	title: "Base64",
        	icon: "mdi mdi-MDImdi mdi-power-socket-us",
        	weight: 0
        });
        */

    }
})();