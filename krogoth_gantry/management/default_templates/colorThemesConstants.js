/**
 * Created by mattmbp on 8/2/17.
 */
(function() {
    'use strict';

    var fuseThemes = {
        default: {
            "primary": {
                "name": "blue",
                "hues": {
                    "default": "900",
                    "hue-1": "A700",
                    "hue-2": "600",
                    "hue-3": "A200"
                }
            },
            "accent": {
                "name": "amber",
                "hues": {
                    "default": "A700",
                    "hue-1": "A400",
                    "hue-2": "A200",
                    "hue-3": "A100"
                }
            },
            "warn": {
                "name": "deep-purple",
                "hues": {
                    "default": "A400",
                    "hue-1": "A700",
                    "hue-2": "A200",
                    "hue-3": "900"
                }
            },
            "background": {
                "name": "fuse-paleblue",
                "hues": {
                    "default": "900",
                    "hue-1": "800",
                    "hue-2": "A700",
                    "hue-3": "50"
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