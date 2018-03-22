(function () {
  'use-strict';

  angular
    .module('invoices.portal')
    .directive('invoiceDetail', invoiceDetail)

    /* INVOICE CONTROLLER: holds the form for invoice
    */
    function invoiceDetail(TEMPLATE_URL) {
      var directive = {
        restrict: 'EA',
        templateUrl: TEMPLATE_URL + '/invoices/invoice_form.html',
        controller: 'InvoiceController',
        controllerAs: 'ctrl',
        bindToController: true
      };
      return directive;
    }

})();