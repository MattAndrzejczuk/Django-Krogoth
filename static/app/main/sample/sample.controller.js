(function ()
{
    'use strict';

    angular
        .module('app.sample') // MUST BE 'app.sample' OR IT WILL CRASH !
        .controller('SampleController', SampleController);

    /** @ngInject */
    function SampleController()
    {
        var vm = this;

        vm.helloText = 'This one was created manually instead of using the database. ';

        vm.helloText = 'This file can be used as a nice little scaffold.';

        
    }
})();
