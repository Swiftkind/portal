(function () {
  'use strict';

  angular
    .module('invoices.portal')
    .controller('InvoicesAddController', InvoicesAddController)
    .controller('InvoiceUpdateController', InvoiceUpdateController)
  ;

  /* INVOICE CONTROLLER: displays the data of invoice from the service
   */
  function InvoicesAddController($scope, InvoicesServices) {
    var self = this;

    self.InvoicesServices = InvoicesServices;

    console.log(InvoicesServices.list);
  }

  /* INVOICE CONTROLLER: displays the detail of the invoice
   */
  function InvoiceUpdateController($scope, InvoicesServices, $stateParams) {
    var self = this;
    self.InvoicesServices = InvoicesServices;

      detail();

      function detail (){
        InvoicesServices
          .getDetail($stateParams['id'])
          .then(function (response) {
            self.invoice_date = new Date(response.data.invoice_date);
            self.due_date = new Date(response.data.due_date);
            self.invoice = response.data;
        });
      };

  }

})();