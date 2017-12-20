(function () {
  'use strict';

  angular
    .module('app.core')
    .factory('fuseGenerator', fuseGeneratorService);

  /** @ngInject */
  function fuseGeneratorService($cookies, $log, fuseTheming) {
    // Storage for simplified themes object
    var themes = {};

    var service = {
      generate: generate,
      rgba: rgba
    };

    return service;

    //////////

    /**
     * Generate less variables for each theme from theme's
     * palette by using material color naming conventions
     */
    function generate() {
      // Get registered themes and palettes and copy
      // them so we don't modify the original objects
      var registeredThemes = angular.copy(fuseTheming.getRegisteredThemes());
      var registeredPalettes = angular.copy(fuseTheming.getRegisteredPalettes());

      // First, create a simplified object that stores
      // all registered themes and their colors

      // Iterate through registered themes
      angular.forEach(registeredThemes, function (registeredTheme) {
        themes[registeredTheme.name] = {};

        // Iterate through color types (primary, accent, warn & background)
        angular.forEach(registeredTheme.colors, function (colorType, colorTypeName) {
          themes[registeredTheme.name][colorTypeName] = {
            'name': colorType.name,
            'levels': {
              'default': {
                'color': rgba(registeredPalettes[colorType.name][colorType.hues.default].value),
                'contrast1': rgba(registeredPalettes[colorType.name][colorType.hues.default].contrast, 1),
                'contrast2': rgba(registeredPalettes[colorType.name][colorType.hues.default].contrast, 2),
                'contrast3': rgba(registeredPalettes[colorType.name][colorType.hues.default].contrast, 3),
                'contrast4': rgba(registeredPalettes[colorType.name][colorType.hues.default].contrast, 4)
              },
              'hue1': {
                'color': rgba(registeredPalettes[colorType.name][colorType.hues['hue-1']].value),
                'contrast1': rgba(registeredPalettes[colorType.name][colorType.hues['hue-1']].contrast, 1),
                'contrast2': rgba(registeredPalettes[colorType.name][colorType.hues['hue-1']].contrast, 2),
                'contrast3': rgba(registeredPalettes[colorType.name][colorType.hues['hue-1']].contrast, 3),
                'contrast4': rgba(registeredPalettes[colorType.name][colorType.hues['hue-1']].contrast, 4)
              },
              'hue2': {
                'color': rgba(registeredPalettes[colorType.name][colorType.hues['hue-2']].value),
                'contrast1': rgba(registeredPalettes[colorType.name][colorType.hues['hue-2']].contrast, 1),
                'contrast2': rgba(registeredPalettes[colorType.name][colorType.hues['hue-2']].contrast, 2),
                'contrast3': rgba(registeredPalettes[colorType.name][colorType.hues['hue-2']].contrast, 3),
                'contrast4': rgba(registeredPalettes[colorType.name][colorType.hues['hue-2']].contrast, 4)
              },
              'hue3': {
                'color': rgba(registeredPalettes[colorType.name][colorType.hues['hue-3']].value),
                'contrast1': rgba(registeredPalettes[colorType.name][colorType.hues['hue-3']].contrast, 1),
                'contrast2': rgba(registeredPalettes[colorType.name][colorType.hues['hue-3']].contrast, 2),
                'contrast3': rgba(registeredPalettes[colorType.name][colorType.hues['hue-3']].contrast, 3),
                'contrast4': rgba(registeredPalettes[colorType.name][colorType.hues['hue-3']].contrast, 4)
              }
            }
          };
        });
      });

      // Process themes one more time and then store them in the service for external use
      processAndStoreThemes(themes);

      // Iterate through simplified themes
      // object and create style variables
      var styleVars = {};

      // Iterate through registered themes
      angular.forEach(themes, function (theme, themeName) {
        styleVars = {};
        styleVars['@themeName'] = themeName;

        // Iterate through color types (primary, accent, warn & background)
        angular.forEach(theme, function (colorTypes, colorTypeName) {
          // Iterate through color levels (default, hue1, hue2 & hue3)
          angular.forEach(colorTypes.levels, function (colors, colorLevelName) {
            // Iterate through color name (color, contrast1, contrast2, contrast3 & contrast4)
            angular.forEach(colors, function (color, colorName) {
              styleVars['@' + colorTypeName + ucfirst(colorLevelName) + ucfirst(colorName)] = color;
            });
          });
        });

        // Render styles
        render(styleVars);
      });
    }

    // ---------------------------
    //  INTERNAL HELPER FUNCTIONS
    // ---------------------------

    /**
     * Process and store themes for global use
     *
     * @param _themes
     */
    function processAndStoreThemes(_themes) {
      // Here we will go through every registered theme one more time
      // and try to simplify their objects as much as possible for
      // easier access to their properties.
      var themes = angular.copy(_themes);

      // Iterate through themes
      angular.forEach(themes, function (theme) {
        // Iterate through color types (primary, accent, warn & background)
        angular.forEach(theme, function (colorType, colorTypeName) {
          theme[colorTypeName] = colorType.levels;
          theme[colorTypeName].color = colorType.levels.default.color;
          theme[colorTypeName].contrast1 = colorType.levels.default.contrast1;
          theme[colorTypeName].contrast2 = colorType.levels.default.contrast2;
          theme[colorTypeName].contrast3 = colorType.levels.default.contrast3;
          theme[colorTypeName].contrast4 = colorType.levels.default.contrast4;
          delete theme[colorTypeName].default;
        });
      });

      // Store themes and set selected theme for the first time
      fuseTheming.setThemesList(themes);

      // Remember selected theme.
      var selectedTheme = $cookies.get('selectedTheme');

      if (selectedTheme) {
        fuseTheming.setActiveTheme(selectedTheme);
      }
      else {
        fuseTheming.setActiveTheme('default');
      }
    }


    /**
     * Render css files
     *
     * @param styleVars
     */
    function render(styleVars) {
      var cssTemplate = '/* Content hack because they wont fix */\n/* https://github.com/angular/material/pull/8067 */\n[md-theme="@themeName"] md-content.md-hue-1,\nmd-content.md-@themeName-theme.md-hue-1 {\n    color: @backgroundHue1Contrast1;\n    background-color: @backgroundHue1Color;\n}\n\n[md-theme="@themeName"] md-content.md-hue-2,\nmd-content.md-@themeName-theme.md-hue-2 {\n    color: @backgroundHue2Contrast1;\n    background-color: @backgroundHue2Color;\n}\n\n[md-theme="@themeName"] md-content.md-hue-3,\n md-content.md-@themeName-theme.md-hue-3 {\n    color: @backgroundHue3Contrast1;\n    background-color:';

      var regex = new RegExp(Object.keys(styleVars).join('|'), 'gi');
      var css = cssTemplate.replace(regex, function (matched) {
        return styleVars[matched];
      });

      var headEl = angular.element('head');
      var styleEl = angular.element('<style type="text/css"></style>');
      styleEl.html(css);
      headEl.append(styleEl);
    }

    /**
     * Convert color array to rgb/rgba
     * Also apply contrasts if needed
     *
     * @param color
     * @param _contrastLevel
     * @returns {string}
     */
    function rgba(color, _contrastLevel) {
      var contrastLevel = _contrastLevel || false;

      // Convert 255,255,255,0.XX to 255,255,255
      // According to Google's Material design specs, white primary
      // text must have opacity of 1 and we will fix that here
      // because Angular Material doesn't care about that spec
      if (color.length === 4 && color[0] === 255 && color[1] === 255 && color[2] === 255) {
        color.splice(3, 4);
      }

      // If contrast level provided, apply it to the current color
      if (contrastLevel) {
        color = applyContrast(color, contrastLevel);
      }

      // Convert color array to color string (rgb/rgba)
      if (color.length === 3) {
        return 'rgb(' + color.join(',') + ')';
      }
      else if (color.length === 4) {
        return 'rgba(' + color.join(',') + ')';
      }
      else {
        $log.error('Invalid number of arguments supplied in the color array: ' + color.length + '\n' + 'The array must have 3 or 4 colors.');
      }
    }

    /**
     * Apply given contrast level to the given color
     *
     * @param color
     * @param contrastLevel
     */
    function applyContrast(color, contrastLevel) {
      var contrastLevels = {
        'white': {
          '1': '1',
          '2': '0.7',
          '3': '0.3',
          '4': '0.12'
        },
        'black': {
          '1': '0.87',
          '2': '0.54',
          '3': '0.26',
          '4': '0.12'
        }
      };

      // If white
      if (color[0] === 255 && color[1] === 255 && color[2] === 255) {
        color[3] = contrastLevels.white[contrastLevel];
      }
      // If black
      else if (color[0] === 0 && color[1] === 0 && color[2] === 0) {
        color[3] = contrastLevels.black[contrastLevel];
      }

      return color;
    }

    /**
     * Uppercase first
     */
    function ucfirst(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }

})();
