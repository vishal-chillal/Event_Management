var app = angular.module("event_management", []);

app.controller('SignupController', ['$scope', function($scope) { 
    $scope.title = 'Sign Up'; 
    $scope.promo = 'promo';
  }]);

app.controller('SigninController', ['$scope', function($scope) { 
    $scope.title = 'Sign In'; 
    $scope.promo = 'promo';
  }]);