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
    var invId = $stateParams.id;

    if (typeof invId != 'undefined') {
      detail();
    }

    /* Get the detail of invoice by ID
     */
    function detail(){

      InvoiceService
        .getDetail(invId)
        .then(function (response) {
          self.invoice = response.data;
          self.invoice.invoice_date = new Date(self.invoice.invoice_date);
          self.invoice.due_date = new Date(self.invoice.due_date);
      });

    };

    /* Update in invoice
     */
     // TO DO: used underscore .each
    self.update = function(){
     var items = self.invoice.items; // Gets the existing items

     InvoiceService
       .update(invId, self.invoice)
       .then(function (response) {

            _.map(items, function(item){
              if (item.id) {

                InvoiceService
                  .updateItems(item.id, item)
                  .then(function (response) {

                  });

              } else {
                item.invoice = response.data.id; // Updates the invoice data in item

                InvoiceService
                 .addItems(item)
                 .then(function (response) {

               });

              }

            });

       });

    };

    /* Add row to item
     */
     self.addRow = function(){

       self.invoice.items.push({
        details  : self.invoice.items.details,
        rate     : self.invoice.items.rate,
        quantity : self.invoice.items.quantity
       })

     };

    /* Total of all items
     */
     self.total = function(){
      var total = 0;
      var inv = self.invoice.items;

      _.map(inv, function(item){
        total += item.rate * item.quantity;
        self.invoice.total_amount = total;
      });

     };

  }

})();