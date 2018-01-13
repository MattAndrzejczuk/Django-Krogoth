(function () {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($mdToast, $timeout, $log, $q) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';


        $mdToast.show(
            $mdToast.simple()
                .textContent('Toast Supported')
                .position('bottom right')
                .hideDelay(2000)
        );


        vm.tiles = buildGridModel({
            icon: "avatar:svg-",
            title: "Svg-",
            background: ""
        });


        function buildGridModel(tileTmpl) {
            var it, results = [];

            for (var j = 0; j < 6; j++) {

                it = angular.extend({}, tileTmpl);
                it.icon = it.icon + (j + 1);
                it.title = it.title + (j + 1);
                it.span = {row: 1, col: 1};
                it.index = j;

                switch (j + 1) {
                    // case 1:
                    //     it.background = "red";
                    //     it.span.row = 3;
                    //     it.span.col = 3;
                    //     it.title = '3X3';
                    //     break;
                    // case 2:
                    //     it.background = "green";
                    //     it.span.row = 2;
                    //     it.span.col = 2;
                    //     it.title = '2X2';
                    //     break;
                    // case 3:
                    //     it.background = "darkBlue";
                    //     it.span.row = 8;
                    //     it.span.col = 8;
                    //     it.title = '8X8';
                    //     break;
                    // case 4:
                    //     it.background = "blue";
                    //     it.span.row = 1;
                    //     it.span.col = 1;
                    //     it.title = '1X1';
                    //     break;
                    // case 5:
                    //     it.background = "yellow";
                    //     it.span.row = 1;
                    //     it.span.col = 1;
                    //     it.title = '1X1';
                    //     break;

                    // case 6:
                    //     it.background = "pink";
                    //     it.span.row = 5;
                    //     it.span.col = 5;
                    //     it.title = '5X5';
                    //     break;


                    case 1:
                        it.background = "darkBlue";
                        it.span.row = 8;
                        it.span.col = 8;
                        it.title = '8X8';
                        break;
                    case 2:
                        it.background = "pink";
                        it.span.row = 5;
                        it.span.col = 5;
                        it.title = '5X5';
                        break;
                    case 3:
                        it.background = "blue";
                        it.span.row = 1;
                        it.span.col = 1;
                        it.title = '1X1';
                        break;
                    case 4:
                        it.background = "yellow";
                        it.span.row = 1;
                        it.span.col = 1;
                        it.title = '1X1';
                        break;
                    case 5:
                        it.background = "blue";
                        it.span.row = 3;
                        it.span.col = 3;
                        it.title = '3X3';
                        break;
                    case 6:
                        it.background = "pink";
                        it.span.row = 2;
                        it.span.col = 2;
                        it.title = '2X2';
                        break;

                    // case 13:
                    //     it.background = "yellow";
                    //     break;
                    // case 14:
                    //     it.background = "yellow";
                    //     break;
                    // case 15:
                    //     it.background = "yellow";
                    //     break;
                    // case 16:
                    //     it.background = "yellow";
                    //     break;
                }

                results.push(it);
            }
            return results;
        }


    }
})();



