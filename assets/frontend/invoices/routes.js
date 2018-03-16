(function () {
  'use strict';

  angular
    .module('invoices.portal')
    .config(routes)
  ;


  function routes ($stateProvider, TEMPLATE_URL) {

    $stateProvider
      .state('invoices', {
        url          : '/invoices/',
        templateUrl  : TEMPLATE_URL + 'invoices.html',
        controller   : 'InvoicesController',
        controllerAs : 'ctrl'
      })
    ;

  }

})();