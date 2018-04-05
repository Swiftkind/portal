(function () {
  'use strict';

  angular
    .module('dashboard.portal')
    .config(routes)
  ;

  function routes($stateProvider, TEMPLATE_URL) {
    $stateProvider
      .state('dashboard', {
          url: '/dashboard/',
          templateUrl: TEMPLATE_URL + '/dashboard.html/',
          controller: 'DashBoardController',
          controllerAs: 'ctrl',
      });
  }; // end of routes

})();
