(function () {
  'use strict';

  angular
    .module('portal', [
    ])
    .constant('TEMPLATE_URL', '/static/frontend/templates/')
    .config(routes)
  ;

  function routes ($stateProvider, $urlRouterProvider, TEMPLATE_URL) {
    $urlRouterProvider.otherwise('/dashboard');

    $stateProvider
      .state('legacy', {
        abstract : true,
      })
    ;
  }

})();