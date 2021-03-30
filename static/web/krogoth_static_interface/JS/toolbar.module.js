/*


curl --location --request GET 'http://localhost:8000/global_static_text/save_sqldb_to_filesystem_text/navigation.module'

curl --location --request GET 'http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/navigation.module'

curl --location --request PATCH 'http://localhost:8000/global_static_text/admin_editor_text/navigation.module/' \
--form 'doc_name="FirstJavaScriptDoc"' \
--form 'content="console.log(\"Hello world!\");\\n// COOL ITS GOOD. "'




GET     http://localhost:8000/global_static_text/save_filesystem_to_sqldb_text/navigation.module.js
*/
/* ~ ~ ~ ~ ~ ~ ~ ~ TOOLBAR MODULE ~ ~ ~ ~ ~ ~ ~ ~ */
(function ()
{
    'use strict';

    angular
        .module('app.toolbar', [])
        .config(config);

    /** @ngInject */
    function config()
    {

		
    }
})();
