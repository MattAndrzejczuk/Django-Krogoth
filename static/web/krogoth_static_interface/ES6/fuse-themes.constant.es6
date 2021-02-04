/*
GET   http://localhost:8000/global_static_text/load_static_text_readonly/fuse-themes.constant.es6
 */
(function () {
    'use strict';

    var fuseThemes = {
        default: {
            primary: {
                name: 'blue',
                hues: {
                    'default': '800',
                    'hue-1': '600',
                    'hue-2': '400',
                    'hue-3': 'A100'
                }
            },
            accent: {
                name: 'green',
                hues: {
                    'default': '400',
                    'hue-1': '300',
                    'hue-2': '600',
                    'hue-3': 'A100'
                }
            },
            warn: {
                name: 'pink'
            },
            background: {
                name: 'grey',
                hues: {
                    'default': 'A100',
                    'hue-1': 'A100',
                    'hue-2': '100',
                    'hue-3': '300'
                }
            }
        },
        'pinkTheme': {
            primary: {
                name: 'blue-grey',
                hues: {
                    'default': '800',
                    'hue-1': '600',
                    'hue-2': '400',
                    'hue-3': 'A100'
                }
            },
            accent: {
                name: 'pink',
                hues: {
                    'default': '400',
                    'hue-1': '300',
                    'hue-2': '600',
                    'hue-3': 'A100'
                }
            },
            warn: {
                name: 'blue'
            },
            background: {
                name: 'grey',
                hues: {
                    'default': 'A100',
                    'hue-1': 'A100',
                    'hue-2': '100',
                    'hue-3': '300'
                }
            }
        },
        'tealTheme': {
            primary: {
                name: 'fuse-blue',
                hues: {
                    'default': '900',
                    'hue-1': '600',
                    'hue-2': '500',
                    'hue-3': 'A100'
                }
            },
            accent: {
                name: 'teal',
                hues: {
                    'default': '500',
                    'hue-1': '400',
                    'hue-2': '600',
                    'hue-3': 'A100'
                }
            },
            warn: {
                name: 'deep-orange'
            },
            background: {
                name: 'grey',
                hues: {
                    'default': 'A100',
                    'hue-1': 'A100',
                    'hue-2': '100',
                    'hue-3': '300'
                }
            }
        }
    };

    angular
        .module('app.core')
        .constant('fuseThemes', fuseThemes);
})();