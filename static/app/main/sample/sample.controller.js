(function ()
{
    'use strict';

    angular
        .module('app.sample')
        .controller('SampleController', SampleController);

    /** @ngInject */
    function SampleController()
    {
        var vm = this;

        // Data
        vm.helloText = 'This one was created manually instead of using the database. ';

        vm.helloText = 'This file can be used as a nice little scaffold.';
        // Methods

        //////////
        
    }
})();
