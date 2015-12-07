var app = angular.module('morado', ['ngAnimate']);


app.controller('portfolio', function($scope, $http) {

    var restUrl = 'http://192.168.59.103:32768/api/companies.json';
    console.log(restUrl);

    $http.get(restUrl).success(function(data){
        console.log(data);
        $scope.companies = data.results;



    }).error(function(data) {
        console.log(data);
    });

    $scope.getLastRound = function (company) {

        return company.rounds[0];
    }

});