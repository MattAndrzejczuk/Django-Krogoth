(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q, $timeout) {
        var service = {
            colorNgClick1: colorNgClick1,
            highlightCustom: highlightCustom,
            clearHighlights: clearHighlights,
            highlightedStrings: []
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
                        "css": "color : #A459FF; font-weight:bold; background-color: rgba(0, 43, 114, 0.9);"
                    });
                    step += 1;
                }
            }
            deferred.resolve(editorModel);
            return deferred.promise;
        }






        function highlightCustom(editorModel, customString) {
            service.highlightedStrings.push(customString);
            $log.log('service.highlightedStrings: ');
            $log.log(service.highlightedStrings);


            var deferred = $q.defer();
            $log.log("HIGHLIGHTING CUSTOM: " + customString);
            var sfx = "/static/gui_sfx/click_select_units.wav";
            var audio = new Audio(sfx);
            audio.play();
            var lineCount = editorModel.getDoc().lineCount();

            for (var j = 0; j < lineCount; j++) {

                var temp = editorModel.getDoc().getLine(j);

                ///$log.log('temp: ');
                ///$log.log(temp);

                var rgxp = new RegExp(customString);


                const codeLinesArray = temp.match(rgxp);
                if (codeLinesArray) {


                    ///$log.log('codeLinesArray: ');
                    ///$log.log(codeLinesArray);


                    const count = codeLinesArray.length;
                    if (count) {
                        ///$log.log('count: ');
                        ///$log.log(count);
                        var lenOfThisMatch = 0;
                        if (codeLinesArray[0]) {
                            var lenOfThisMatch = codeLinesArray[0].length;
                            ///$log.log(codeLinesArray[0] + " | " + lenOfThisMatch);
                            ///$log.log("╚════> " + count);
                        }
                        var step = 0;
                        for (var i = 0; i < count; i++) {
                            var n = temp.indexOf(customString, step);
                            step = n;
                            editorModel.getDoc().markText({
                                "line": j,
                                "ch": n
                            }, {
                                "line": j,
                                "ch": n + lenOfThisMatch
                            }, {
                                "css": "background-color: rgba(0, 255, 80, 0.99);"
                            });
                            step += 1;
                        }
                    }


                }

            }
            deferred.resolve(editorModel);
            return deferred.promise;

        }



        function clearHighlights(editorModel) {
            ///service.highlightedStrings.push(customString);
            $log.log('service.highlightedStrings: ');
            $log.log(service.highlightedStrings);

            var deferred = $q.defer();
            $log.log("HIGHLIGHTING CUSTOM: " + service.highlightedStrings);

            var lineCount = editorModel.getDoc().lineCount();

            $(service.highlightedStrings).each(function(index, element) {
                for (var j = 0; j < lineCount; j++) {

                    var temp = editorModel.getDoc().getLine(j);

                    $log.log('element: ');
                    $log.log(element);

                    var rgxp = new RegExp(element);


                    const codeLinesArray = temp.match(rgxp);
                    if (codeLinesArray) {


                        ///$log.log('codeLinesArray: ');
                        ///$log.log(codeLinesArray);


                        const count = codeLinesArray.length;
                        if (count) {
                            ///$log.log('count: ');
                            ///$log.log(count);
                            var lenOfThisMatch = 0;
                            if (codeLinesArray[0]) {
                                var lenOfThisMatch = codeLinesArray[0].length;
                                ///$log.log(codeLinesArray[0] + " | " + lenOfThisMatch);
                                ///$log.log("╚════> " + count);
                            }
                            var step = 0;
                            for (var i = 0; i < count; i++) {
                                var n = temp.indexOf(element, step);
                                step = n;
                                editorModel.getDoc().markText({
                                    "line": j,
                                    "ch": n
                                }, {
                                    "line": j,
                                    "ch": n + lenOfThisMatch
                                }, {
                                    "css": "background-color: rgba(0, 255, 80, 0.0);"
                                });

                                $timeout(function() {
                                    const sfx = "/static/gui_sfx/click_select_units.wav";
                                    const audio = new Audio(sfx);
                                    audio.play();
                                }, 50);

                                step += 1;
                            }
                        }


                    }

                }
            });

            service.highlightedStrings = [];
            deferred.resolve(editorModel);
            return deferred.promise;
        }




        return service;
    }
})();



/*

git update-index --assume-unchanged static/fancy_bgs/EPIC_Planet-3-opaque-3k.jpg
git update-index --assume-unchanged static/fancy_bgs/EPIC_Planet-3-blur-3k.jpg

*/