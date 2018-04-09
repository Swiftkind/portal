(function() {
  'use strict';

  angular
    .module('dashboard.portal')
    .controller('DashBoardController', DashBoardController)
  ;

  /* DashBoardController
   * @ desc: This will displat the list of user invoices
   */
   function DashBoardController($scope, InvoiceService) {
    feather.replace();
    var self = this;
    var order = 'asc';

    self.invoiceService = InvoiceService;

    self.sorting = {
      'customer': false,
      'code': false,
      'due_date': false,
      'status': false,
    };

    //request to the backend
    self.sortBy = function(field, order) {
      var page_number = {"page": self.invoiceService.list.page.number}
      self.invoiceService.getList(page_number, field, order);
    };

    // Sort the display
    self.sort = function (field) {
      feather.replace();
      self.sorting[field] = !self.sorting[field];
      self.order = self.order == 'asc' ? 'desc' : 'asc';

      if(self.order === 'asc') {
        self.sortBy(field, 'asc');
      } else if (self.order === 'desc') {
        self.sortBy(field, 'desc');
      };
    };

   }; // end of DashBoardController


})();
