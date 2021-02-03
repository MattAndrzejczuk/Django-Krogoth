/*
GET     http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/quick-panel.module.js
*/
(function () {
  'use strict';

  angular
    .module('app.quick-panel', [])
    .config(config);

  /** @ngInject */
  function config(msApiProvider) {
    // Translation

    // Api
    msApiProvider.register('quickPanel.activities', ['/static/app/data/quick-panel/activities.json']);
    msApiProvider.register('quickPanel.contacts', ['/static/app/data/quick-panel/contacts.json']);
    msApiProvider.register('quickPanel.events', ['/static/app/data/quick-panel/events.json']);
    msApiProvider.register('quickPanel.notes', ['/static/app/data/quick-panel/notes.json']);
  }
})();

/*
THIS IS BEING REMOVED
*/