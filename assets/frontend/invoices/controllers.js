(function () {
  'use strict';

  angular
    .module('invoices.portal')
    .controller('InvoiceController', InvoiceController)
  ;

   /* INVOICE CONTROLLER: this will handle the data of the invoice lists
     from the service
    */
  function InvoiceController($scope, InvoiceService, $stateParams, 
        $q, $state) {

    var self = this;
    self.invoiceService = InvoiceService;
    var invId = $stateParams.id;
    self.success = true;
    self.errorItems = true;
    self.form = {};

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
          self.form = angular.copy(self.invoice);
      });

    };

    /* Update in invoice
     */
    self.update = function(){
     var items = self.invoice.items; // Gets the existing items
     self.invoice = angular.copy(self.form);

     InvoiceService
       .update(invId, self.invoice)
       .then(function (response) {
          self.success = false;

          _.map(items, function(item){
            if (item.id) {

              InvoiceService
                .updateItems(item.id, item)
                .then(function (response) {
                  self.success = false;
                }).catch(function(error){
                  self.errorItems = false;
                });

            } else {
              item.invoice = response.data.id; // Updates the invoice data in item

              InvoiceService
               .addItems(item)
               .then(function (response) {
                  self.success = false;
               }).catch(function(error){
                    self.errorItems = false;
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
     self.getTotal = function(){
      var total = 0;

      _.map(self.invoice.items, function(item){
        total += item.rate * item.quantity;
        self.invoice.total_amount = total || 0;
      });

     };

    /* Delete invoice
     */
     self.delete = function(){

      InvoiceService
        .deleteInv(invId)
        .then(function(response){
          InvoiceService.list = _.filter(InvoiceService.list, function(item) {
           return item.id != invId; });
          var last = InvoiceService.list[InvoiceService.list.length-1].id;
          $state.go('invoiceDetail', {id: last});
        });

     };

  }

})();