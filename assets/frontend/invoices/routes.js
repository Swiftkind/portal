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
        templateUrl  : TEMPLATE_URL + 'invoice_add.html',
        controller   : 'InvoicesAddController',
        controllerAs : 'ctrl'
      })
      .state('invoiceDetail', {
        url          : '/invoices/:id/',
        templateUrl : TEMPLATE_URL + 'invoice_update.html',
        controller   : 'InvoiceUpdateController',
        controllerAs : 'ctrl'
      })
    ;
  }

})();