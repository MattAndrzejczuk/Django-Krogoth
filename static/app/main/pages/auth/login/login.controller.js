(function ()
{
    'use strict';

    angular
        .module('app.pages.auth.login')
        .controller('LoginController', LoginController);

    /** @ngInject */
    function LoginController($log)
    {
        // Data

        // Methods

        //////////

        $log.log('Is the static login ctrl working????');
    }
})();