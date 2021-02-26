/*
GET     http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/quick-panel.controller.js
*/
(function () {
  'use strict';

  angular
    .module('app.quick-panel')
    .controller('QuickPanelController', QuickPanelController);

  /** @ngInject */
  function QuickPanelController() {
    var vm = this;

    // Data
    vm.date = new Date();
    vm.settings = {
      notify: true,
      cloud: false,
      retro: true
    };



    // Methods

    //////////
  }

})();