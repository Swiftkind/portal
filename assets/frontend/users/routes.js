(function () {
  'use strict';

  angular
    .module('users.portal')
    .config(routes)
  ;


  function routes ($stateProvider, TEMPLATE_URL) {

    $stateProvider
      .state('users', {
        url          : '/users/dashboard/',
        templateUrl  : TEMPLATE_URL + 'dashboard.html',
        controller   : 'dashboardController',
        controllerAs : 'ctrl'
      })
    ;

  }

})();