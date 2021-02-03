/*
GET     http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/
*/
(function () {
  'use strict';

  angular
    .module('fuse')
    .controller('IndexController', IndexController);

  /** @ngInject */
  function IndexController(fuseTheming) {
    var vm = this;

    // Data
    vm.themes = fuseTheming.themes;

    //////////
  }
})();