(function () {
  'use strict';

  angular
    .module('portal')
    .config(routes)
  ;

  function routes ($stateProvider, $urlRouterProvider,
    $urlMatcherFactoryProvider, TEMPLATE_URL) {

    $stateProvider
      .state('legacy', {
        abstract : true,
      })
    ;

    $urlRouterProvider.otherwise('/login/');
    $urlMatcherFactoryProvider.strictMode(false);
    $locationProvider.html5Mode(true);
  }

})();