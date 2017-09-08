(function() {
    'use strict';
    angular.module('app.FUSE_APP_NAME').controller('FUSE_APP_NAMEController', FUSE_APP_NAMEController);

    function FUSE_APP_NAMEController($http) {
        var vm = this;
        vm.viewName = 'FUSE_APP_NAME';

        document.getElementById("DjangularMetaText_01").innerHTML = 'Lazarus Mod Editor';


        vm.panel_ModArt = buildGridModel_ModArt({
            icon: "avatar:svg-",
            img: "/static/lazarus_TA_menus/",
            title: "Svg-",
            background: "md-amber-bg"
        }, 4);
        vm.panel_LazarusApps = buildGridModel_LazarusApps({
            icon: "avatar:svg-",
            title: "Svg-",
            title: "Svg-",
            background: "md-amber-bg"
        }, 3);

        /// buildGridModel_PublishedMods
        vm.widgetUnitCount = {
            title: 'UNITS',
            value: 154
        };
        vm.widgetWeaponCount = {
            title: 'WEAPONS',
            value: 244
        };

        vm.publish = {
            revision: '1.1',
            info: "Release"
        };



        /// 
        vm.totalUnits = 0;
        vm.modName = 'X';
        $http({
            method: 'GET',
            url: '/LazarusDatabase/UnitFBIFromSQLView/'
        }).then(function successCallback(response) {
            vm.totalUnits = response.data['list_response'].length;
            vm.modName = response.data['mod'];
        }, function errorCallback(response) {

        });
        /// 



        function buildGridModel_ModArt(tileTmpl, totalTiles) {
            var it = [];
            var results = [];
            for (var j = 0; j < totalTiles; j++) {
                it = angular.extend({}, tileTmpl);
                it.icon = 'icon-hexagon' ///it.icon + (j + 1);
                it.title = it.title + (j + 1);
                it.span = {
                    row: 3,
                    col: 3
                };
                switch (j + 1) {
                    // Mod Art
                    case 1:
                        it.background = "md-primary-bg md-hue-3";
                        it.title = 'MAIN SCREEN';
                        it.img = "/static/lazarus_TA_menus/FrontendX.png";
                        break;
                    case 2:
                        it.background = "md-primary-bg md-hue-3";
                        it.title = 'SINGLE PLAYER SCREEN';
                        it.img = "/static/lazarus_TA_menus/SINGLEBG.png";
                        break;
                    case 3:
                        it.background = "md-primary-bg md-hue-3";
                        it.title = 'MULTIPLAYER LOBBY';
                        it.img = "/static/lazarus_TA_menus/battleroom2.png";
                        break;
                    case 4:
                        it.background = "md-primary-bg md-hue-3";
                        it.title = 'SKIRMISH SETUP';
                        it.img = "/static/lazarus_TA_menus/Skirmsetup4x.png";
                        break;

                }
                results.push(it);
            }
            return results;
        }


        function buildGridModel_LazarusApps(tileTmpl, totalTiles) {
            var it = [];
            var results = [];
            for (var j = 0; j < totalTiles; j++) {
                it = angular.extend({}, tileTmpl);
                it.icon = 'icon-hexagon' ///it.icon + (j + 1);
                it.title = it.title + (j + 1);
                it.span = {
                    row: 2,
                    col: 5
                };
                switch (j + 1) {
                    // Mod Art
                    case 1:
                        it.background = "md-accent-bg md-hue-3 editor-units";
                        it.title = 'UNIT EDITOR';
                        it.description = "Customize unit hitpoints, resource cost, and many other properties.";
                        break;
                    case 2:
                        it.background = "md-accent-bg md-hue-3 editor-weapons";
                        it.title = 'WEAPON EDITOR';
                        it.description = "Modify unit damage, units can carry up to three weapons. " +
                            "(Mods with more than 255 weapons will require Unofficial Patch v3.9.02)";
                        break;
                    case 3:
                        it.background = "md-accent-bg md-hue-3 editor-techtree";
                        it.title = 'TECH TREE EDITOR';
                        it.description = "Create your own tech levels here! Customize what all units are able to build here.";
                        break;

                }
                results.push(it);
            }
            return results;
        }

        function buildGridModel_PublishedMods(tileTmpl, totalTiles) {
            var it = [];
            var results = [];
            for (var j = 0; j < totalTiles; j++) {
                it = angular.extend({}, tileTmpl);
                it.icon = 'icon-cloud-download' ///it.icon + (j + 1);
                it.title = vm.publishedMods[j].build + ' ' + vm.publishedMods[j].info;
                it.universalCompatibility = (vm.publishedMods[j].compatibility === 'v3.9.02');
                it.background = "md-background-bg md-hue-3";
                it.span = {
                    row: 1,
                    col: 1
                };
                /*
                switch (j + 1) {
                    // Mod Art
                    case 1:
                        it.background = "md-accent-bg md-hue-1";
                        it.title = 'Initial Build';
                        break;
                        
                    case 2:
                        it.background = "md-accent-bg md-hue-1";
                        it.title = 'WEAPON EDITOR';
                        break;
                    case 3:
                        it.background = "md-accent-bg md-hue-1";
                        it.title = 'TECH TREE EDITOR';
                        break;
                }
				*/
                results.push(it);
            }
            return results;
        }

        vm.publishedMods = [{
            info: "Alpha",
            build: '0.1',
            compatibility: 'v3.1'
        }, {
            info: "Alpha",
            build: '0.2',
            compatibility: 'v3.1'
        }, {
            info: "Alpha",
            build: '0.3',
            compatibility: 'v3.1'
        }, {
            info: "Public Beta",
            build: '0.4',
            compatibility: 'v3.9.02'
        }, {
            info: "Release Candidate",
            build: '1.0',
            compatibility: 'v3.9.02'
        }];
        vm.panel_PublishedMods = buildGridModel_PublishedMods({
            icon: "avatar:svg-",
            title: "Svg-",
            title: "Svg-",
            background: "md-amber-bg"
        }, 5);









    }
})();