
        "CoreTheme1" : {"primary":{"name":"deep-purple","hues":{"default":"900","hue-1":"A700","hue-2":"300","hue-3":"A100"}},"accent":{"name":"red","hues":{"default":"900","hue-1":"A700","hue-2":"300","hue-3":"A100"}},"warn":{"name":"amber","hues":{"default":"A700","hue-1":"900","hue-2":"300","hue-3":"A100"}},"background":{"name":"fuse-paleblue","hues":{"default":"900","hue-1":"600","hue-2":"800","hue-3":"A700"}}},
        'tealTheme': {
            primary   : {
                name: 'fuse-blue',
                hues: {
                    'default': '900',
                    'hue-1'  : '600',
                    'hue-2'  : '500',
                    'hue-3'  : 'A100'
                }
            },
            accent    : {
                name: 'teal',
                hues: {
                    'default': '500',
                    'hue-1'  : '400',
                    'hue-2'  : '600',
                    'hue-3'  : 'A100'
                }
            },
            warn      : {
                name: 'deep-orange'
            },
            background: {
                name: 'grey',
                hues: {
                    'default': 'A100',
                    'hue-1'  : 'A100',
                    'hue-2'  : '100',
                    'hue-3'  : '300'
                }
            }
        }
    };

    angular
        .module('app.core')
        .constant('fuseThemes', fuseThemes);
})();
