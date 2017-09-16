/**
 * Created by mattmbp on 8/2/17.
 */
(function() {
    'use strict';
    angular.module('fuse').config(routeConfig);

    function routeConfig($stateProvider, $urlRouterProvider, $locationProvider, $httpProvider) {
        $locationProvider.hashPrefix('!');
        $urlRouterProvider.otherwise('/LoginDjangular');
        var $cookies;
        angular.injector(['ngCookies']).invoke(['$cookies', function(_$cookies) {
            $cookies = _$cookies;
        }]);
        var layoutStyle = $cookies.get('layoutStyle') || 'LAYOUT_STYLE';
        ' + '
        var layouts = {
            LAYOUT_STYLE: {
                main: '/dynamic_lazarus_page/NgIncludedHtml/?name=htmlMainLayout',
                toolbar: '/dynamic_lazarus_page/NgIncludedHtml/?name=htmlToolbarLayout',
                navigation: '/dynamic_lazarus_page/NgIncludedHtml/?name=htmlNavLayout'
            },
            contentOnly: {
                main: '/static/app/core/layouts/content-only.html',
                toolbar: '',
                navigation: ''
            },
            contentWithToolbar: {
                main: '/static/app/core/layouts/content-with-toolbar.html',
                toolbar: '/static/app/toolbar/layouts/content-with-toolbar/toolbar.html',
                navigation: ''
            }
        };

        $stateProvider.state('app', {
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
                    templateUrl: '/static/app/quick-panel/quick-panel.html',
                    controller: 'QuickPanelController as vm'
                }
            }
        });


        // alternatively, register the interceptor via an anonymous factory
        /*
        $httpProvider.interceptors.push(function($q) {
            return {
                'request': function(config) {
                    // same as above
                    console.debug('Djangular REST Request Made 🔵 ');
                    console.debug(config);

                },
                // optional method
                'requestError': function(rejection) {
                    // do something on error
                    console.debug('Djangular REST Request Made 🔴 ');
                    console.debug(rejection);
                    return $q.reject(rejection);
                },
                'response': function(response) {
                    // same as above
                    console.debug('Djangular REST Request Made 🔵 ');
                    console.debug(response);
                },
                // optional method
                'responseError': function(rejection) {
                    // do something on error
                    console.debug('Djangular REST Request Made 🔴 ');
                    console.debug(rejection);
                    return $q.reject(rejection);
                }
            };
        });
*/
        /*
        var interceptor = ['$q', function($q) {
            function success(response) {
                return response;
            }

            function error(response) {
                if (response.status === 401) {
                    console.warn('Client Login Credentials Are Unavailable.');
                    window.location = "/LoginDjangular";
                    return $q.reject(response);
                } else {
                    console.warn('$httpProvider Interceptor has detected a server error!!!');
                    console.warn(response);
                    return $q.reject(response);
                }
            }
            return function(promise) {
                return promise.then(success, error);
            }
        }];
		*/

        /// $httpProvider.interceptors.push(interceptor);
        var tokenDefaultSetter = function($q) {
            return {

                request: function(req) {
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
                    }
                    return req;
                },
                // optional
                //                response: function(res) {
                //                   console.debug('Got Some Kind of Response ! ! !');
                //                  return res;
                //              },
                responseError: function(res) {
                    if (res.status === 401) {
                        /// Users without acess tokens will be properly redirected to login.
                        console.warn('Unauthorized Entry Detected.');
                        window.location = "#!/LoginDjangular";
                        return res;
                        ///return $q.reject(res);
                    } else {
                        console.warn('$httpProvider Interceptor has detected a server error!!!');
                        return res;
                    }
                }
            };
        }
        $httpProvider.interceptors.push(tokenDefaultSetter);






    }
})();