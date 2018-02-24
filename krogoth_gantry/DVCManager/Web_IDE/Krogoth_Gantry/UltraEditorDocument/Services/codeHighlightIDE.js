(function() {
    'use strict';
    angular
        .module('app.FUSE_APP_NAME')
        .factory('_DJANGULAR_SERVICE_NAME_', _DJANGULAR_SERVICE_NAME_);

    /** @ngInject */
    function _DJANGULAR_SERVICE_NAME_($log, $http, $q) {
        var service = {
            bloop: bloop
        };



        function bloop() {
            ///var deferred = $q.defer();
            var sfx = "/static/gui_sfx/click_select_units.wav";
            var audio = new Audio(sfx);
            ///try {								
            audio.play();
            ///    deferred.resolve(returnData);
            ///} catch (ex) {
            ///    deferred.reject(returnData);
            ///}
            ///return deferred.promise;
        }




        return service;
    }
})();