(function ()
{
    'use strict';
    var fuseThemes = {
        default : {"primary":{"name":"fuse-blue","hues":{"default":"900","hue-1":"A700","hue-2":"A100","hue-3":"200"}},
            "accent":{"name":"lime","hues":{"default":"900","hue-1":"A700","hue-2":"A400","hue-3":"300"}},
            "warn":{"name":"red","hues":{"default":"A700","hue-1":"900","hue-2":"500","hue-3":"A100"}},
            "background":{"name":"fuse-paleblue","hues":{"default":"900","hue-1":"A700","hue-2":"800","hue-3":"700"}}},
        }
    };
    angular
        .module('app.core')
        .constant('fuseThemes', fuseThemes);
})();
