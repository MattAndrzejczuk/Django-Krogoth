/*
GET     http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/
*/
/* ~ ~ ~ ~ ~ ~ ~ ~ INDEX MODULE ~ ~ ~ ~ ~ ~ ~ ~ */
(function () {
  'use strict';

  /**
   * Main module of Krogoth app
   */
  angular
    .module('fuse', [

	  
      'app.core',
      'app.navigation',
      'app.toolbar',
      'app.quick-panel',

      /* Custom Apps Generated */
      /*|#apps#|*/

    ]);
})();