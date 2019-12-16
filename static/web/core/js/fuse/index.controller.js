/* ~ ~ ~ ~ ~ ~ ~ ~ ANGULARJS 1.7.2 ~ ~ ~ ~ ~ ~ ~ ~ */
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