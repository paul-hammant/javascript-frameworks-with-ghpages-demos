var app= angular.module("MyApp", []);
app.controller('MyController', function($scope, $http) {
    $http.get(window.location.hash.slice(1) + "-gh-pages.txt").then(function(response) {
        $scope.repos = JSON.parse("{ \"res\": [" + response.data.trim().slice(0, -1) + "]}").res
    });
});


