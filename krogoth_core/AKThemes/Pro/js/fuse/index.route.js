(function () {
    'use strict';

    angular
        .module('fuse')
        .config(routeConfig);

    /** @ngInject */
    function routeConfig($stateProvider, $urlRouterProvider, $locationProvider, $httpProvider) {

        /* Django doesn't like HTML5 mode. */

        /* $locationProvider.html5Mode(true); */


		const krogoth_injected={};



        $locationProvider.hashPrefix('!');
        $urlRouterProvider.otherwise('/home');

        /**
         * Layout Style Switcher
         *
         * This code is here for demonstration purposes.
         * If you don't need to switch between the layout
         * styles like in the demo, you can set one manually by
         * typing the template urls into the `State definitions`
         * area and remove this code
         */
            // Inject $cookies
        var $cookies;

        angular.injector(['ngCookies']).invoke([
            '$cookies', function (_$cookies) {
                $cookies = _$cookies;
            }
        ]);


        // Get active layout
        var layoutStyle = $cookies.get('layoutStyle') || 'verticalNavigation';

        var layouts = {
            verticalNavigation: {
                main: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation.html',
                toolbar: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation_toolbar.html',
                navigation: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation_navigation.html'
            },
            verticalNavigationFullwidthToolbar: {
                main: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation-fullwidth-toolbar.html',
                toolbar: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation-fullwidth-toolbar_toolbar.html',
                navigation: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation_navigation.html'
            },
            verticalNavigationFullwidthToolbar2: {
                main: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation-fullwidth-toolbar-2.html',
                toolbar: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation-fullwidth-toolbar-2_toolbar.html',
                navigation: '/moho_extractor/NgIncludedHtml/?name=vertical-navigation-fullwidth-toolbar-2_navigation.html'
            },
            horizontalNavigation: {
                main: '/moho_extractor/NgIncludedHtml/?name=horizontal-navigation.html',
                toolbar: '/moho_extractor/NgIncludedHtml/?name=horizontal-navigation_toolbar.html',
                navigation: '/moho_extractor/NgIncludedHtml/?name=horizontal-navigation_navigation.html'
            },
            contentOnly: {
                main: '/moho_extractor/NgIncludedHtml/?name=content-only.html',
                toolbar: '',
                navigation: ''
            },
            contentWithToolbar: {
                main: '/moho_extractor/NgIncludedHtml/?name=content-with-toolbar.html',
                toolbar: '/moho_extractor/NgIncludedHtml/?name=content-with-toolbar_toolbar.html',
                navigation: ''
            }
        };
        // END - Layout Style Switcher

        // State definitions
        $stateProvider
            .state('app', {
                abstract: true,
                views: {
                    'main@': {
                        templateUrl: layouts[layoutStyle].main,
                        controller: 'MainController as vm'
                    },
                    'toolbar@app': {
                        templateUrl: layouts[layoutStyle].toolbar,
                        controller: 'ToolbarController as vm'
                    },
                    'navigation@app': {
                        templateUrl: layouts[layoutStyle].navigation,
                        controller: 'NavigationController as vm'
                    },
                    'quickPanel@app': {
                        templateUrl: '/moho_extractor/NgIncludedHtml/?name=quick-panel.html',
                        controller: 'QuickPanelController as vm'
                    }
                }
            });


        /// $httpProvider.interceptors.push(interceptor);
        var tokenDefaultSetter = function ($q) {
            return {

                request: function (req) {
                    if ($cookies.get('token')) {
                        /// Using Access Token From Cookie
                        console.debug('Using Cookie Token: ' + $cookies.get('token'));
                        req.headers.Authorization = 'Token ' + $cookies.get('token');
                    } else if (sessionStorage.getItem('token')) {
                        /// Using Access Token From Session
                        console.debug('Using Session Token: ' + sessionStorage.getItem('token'));
                        req.headers.Authorization = 'Token ' + sessionStorage.getItem('token');
                    } else {
                        /// No access tokens! 'responseError' below will resolve this issue.
                        console.warn('Client Login Credentials Are Unavailable.');
						req.headers.Authorization = 'Token ' + krogoth_injected['guest_token'];
                    }
                    return req;
                },
                // optional
                //                response: function(res) {
                //                   console.debug('Got Some Kind of Response ! ! !');
                //                  return res;
                //              },
                responseError: function (res) {
                    if (res.status === 401) {
                        /// Users without acess tokens will be properly redirected to login.
                        console.warn('Unauthorized Entry Detected.');
                        window.location = "#!/Login_akdvc";
						if ($cookies.get('token')) {
							$cookies.remove('token');
						}
						$cookies.put('token', krogoth_injected['guest_token']);
                        return res;
                        ///return $q.reject(res);
                    } else if (res.status === 401) {
                        alert('You have been throttled for making too many requests, try again later.');
                    } else {
                        console.warn('$httpProvider Interceptor has detected a server error!!!');
                        return res;
                    }
                }
            };
        }
        $httpProvider.interceptors.push(tokenDefaultSetter);


        /* - - - - - - - - - - - */
    }

})();