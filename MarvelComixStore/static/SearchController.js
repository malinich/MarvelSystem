var SearchModel = angular.module("SearchModel",[])

SearchModel.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

SearchModel.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});

SearchModel.controller('SearchCtrl',function ($scope, $http) {
    $scope.formModel = new FormData();

    $scope.items = [{name:"------",id:"0"}];
    $scope.tags = [];

    $scope.selectedItem=$scope.items[0];

    $scope.Comixes=[];

    $scope.keywords="";

    $scope.tags=[];

    var jsons;

    $http({
        method: 'GET',
        url: '/get_years/'
    }).then(function (response) {
        console.log(response.data);
        var entries=response.data.split('\n');
        for(i=0;i<response.data.split('\n').length-1;i++){
            $scope.items.push({name:entries[i],id:entries[i]});
        }
    });


    $http({
        method: 'GET',
        url: '/get_tags/'
    }).then(function (response) {
        console.log(response.data);
        var entries=response.data.split('\n');
        for(i=0;i<response.data.split('\n').length-1;i++){
            $scope.tags.push({name:entries[i],id:entries[i]});
        }
    });

    $scope.Reset=function () {
        $scope.keywords="";
        $scope.selectedItem=$scope.items[0];
    }

    $scope.OnTagsClick=function (tag) {
        $scope.keywords=$scope.tags[tag-1].name;
        $scope.OnSubmit();
    };

    $scope.OnSubmit=function () {
        $scope.Comixes=[];

        $scope.formModel.append('keywords',$scope.keywords);
        $scope.formModel.append('year',$scope.selectedItem['id']);
        $http({
            method: 'POST',
            url: '/marvel/',
            headers: {
               'Content-Type': undefined
            },
            data:$scope.formModel,
            transformRequest: angular.identity
        }).then(function (response) {
            jsons=response.data.split("\\|/");
            for(i=0;i<jsons.length-1;i++){
                var comix = angular.fromJson(jsons[i])
                comix.description=comix.description.toString().slice(0,350)+"...";
                $scope.Comixes.push(comix);
                console.log($scope.Comixes);
            }

        });
        $scope.formModel=new FormData();
    }

});