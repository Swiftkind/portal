(function() {
    'use strict';

    angular
        .module('portal')
        .config(routes);

  function routes ($stateProvider, $urlRouterProvider,
                   $urlMatcherFactoryProvider, $locationProvider) {

    $urlRouterProvider.otherwise('/');
    $urlMatcherFactoryProvider.strictMode(false);
    $locationProvider.html5Mode(true);

    $stateProvider
        .state('legacy', {
            abstract: true,
            });
    }

})();
