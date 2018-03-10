(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            colorNgClick1: colorNgClick1
        };



        function colorNgClick1(editorModel) {
            var deferred = $q.defer();

            var sfx = "/static/gui_sfx/click_select_units.wav";
            var audio = new Audio(sfx);
            audio.play();


            var lineCount = editorModel.getDoc().lineCount();
            for (var j = 0; j < lineCount; j++) {
                var temp = editorModel.getDoc().getLine(j);

                const codeLinesArray = (temp.match(/(ng-click)(=)(")?([^"^>^]+?|\/\?)([^"^>^]+)?(\3|#| |>)/g) || []);
                const count = codeLinesArray.length;

                var lenOfThisMatch = 0;
                if (codeLinesArray[0]) {
                    var lenOfThisMatch = codeLinesArray[0].length;
                    $log.log(codeLinesArray[0] + " | " + lenOfThisMatch);
                    $log.log("╚════> " + count);
                }


                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('ng-click', step);
                    step = n;
                    editorModel.getDoc().markText({
                        "line": j,
                        "ch": n
                    }, {
                        "line": j,
                        "ch": n + lenOfThisMatch
                    }, {
                        "css": "color : #A459FF; font-weight:bold;"
                    });
                    step += 1;
                }
            }
            deferred.resolve(editorModel);
            return deferred.promise;
        }




        return service;
    }
})();