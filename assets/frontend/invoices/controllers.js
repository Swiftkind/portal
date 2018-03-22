(function () {
  'use strict';

  angular
    .module('invoices.portal')
    .controller('InvoiceController', InvoiceController)
  ;

   /* INVOICE CONTROLLER: this will handle the data of the invoice lists
     from the service
    */
  function InvoiceController($scope, InvoiceService, $stateParams) {
    var self = this;
    self.invoiceService = InvoiceService;

    detail()

    /* Get the detail of invoice by ID
     */
    function detail (){
      InvoiceService
        .getDetail(invId)
        .then(function (response) {
          self.invoice = response.data;
          self.invoice.invoice_date = new Date(self.invoice.invoice_date);
          self.invoice.due_date = new Date(self.invoice.due_date);
      });
    };

  }

})();