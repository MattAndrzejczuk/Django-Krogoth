/* syntaxAnalyzePropertiesVM */

/*

Grabs all unique properties for the controller i.e.

/// vm.firstProperty = foo
/// vm.anotherProp = bar


To give us the result:

/// ["firstProperty", "anotherProp"]

*/





(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            getAllVms: getAllVms,
            detectedVmProperties: [],
            highlightCurrentDocument: highlightCurrentDocument
        };



        function getAllVms(editorModel) {
            var deferred = $q.defer();
            var sfx = "/static/gui_sfx/click_select_units.wav";
            var audio = new Audio(sfx);
            audio.play();

            var lineCount = editorModel.getDoc().lineCount();
            for (var j = 0; j < lineCount; j++) {
                var temp = editorModel.getDoc().getLine(j);

                const codeLinesArray = (temp.match(/(vm.)(.+)(?==|\[)()/g) || []);
                const count = codeLinesArray.length;

                var lenOfThisMatch = 0;
                if (codeLinesArray[0]) {
                    var lenOfThisMatch = codeLinesArray[0].length;
                    $log.log(codeLinesArray[0] + " | " + lenOfThisMatch);
                    $log.log("╚════> " + count);
                }


                var step = 0;
                for (var i = 0; i < count; i++) {
                    var n = temp.indexOf('vm.', step);
                    step = n;

                    $log.log("codeLinesArray[i]: ");
                    $log.debug(codeLinesArray[i]);

                    service.detectedVmProperties.push(codeLinesArray[i]);

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

            $log.log("service.detectedVmProperties: ");
            $log.log(service.detectedVmProperties);
            $log.log(" - - - - - - - - - - - ");
            deferred.resolve(service.detectedVmProperties);
            return deferred.promise;
        }


        function highlightCurrentDocument(editorModel) {
            /*
            for (var x = 0; x < service.detectedVmProperties.length; x++) {

                var lineCount = editorModel.getDoc().lineCount();



                var regx = new RegExp("\\b(" + service.detectedVmProperties[x] + ")\\b");
                for (var j = 0; j < lineCount; j++) {
                    var temp = editorModel.getDoc().getLine(j);
                    const codeLinesArray = (temp.match(/( vm.(.*?))(\[|=|+|-)/g) || []);
                    const count = codeLinesArray.length;
                    var lenOfThisMatch = 0;
                    if (codeLinesArray[0]) {
                        var lenOfThisMatch =
                            codeLinesArray[0].replace("=", "").replace("[", "").replace(" ", "").length;
                        $log.log(codeLinesArray[0] + " | " + lenOfThisMatch);
                        $log.log("╚════> " + count);
                    }
                    var step = 0;
                    for (var i = 0; i < count; i++) {
                        var n = temp.indexOf('vm.', step);
                        step = n;
                        $log.log("highlightCurrentDocument[i]: ");
                        $log.debug(codeLinesArray[i]);
                        const el = codeLinesArray[i].replace("=", "").replace("[", "").replace(" ", "");
                        uniqueValues.add(
                            codeLinesArray[i].replace("=", "").replace("[", "").replace(" ", "")
                        );
                        editorModel.getDoc().markText({
                            "line": j,
                            "ch": n
                        }, {
                            "line": j,
                            "ch": n + lenOfThisMatch
                        }, {
                            "css": "color : #A459FF; font-weight:bold; background-color: rgba(255, 243, 154, 0.9);"
                        });
                        step += 1;
                    }
                }
            }
			*/
        }

        return service;
    }
})();