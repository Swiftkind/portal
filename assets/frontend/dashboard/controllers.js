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
    var order = 0;

    self.invoiceService = InvoiceService;

    // request to the backend
    self.sortBy = function(field, order) {
      self.invoiceService.getList('', field, order);
    };

    // Sort the display
    self.sort = function (field) {
      self.order = self.order == 0 ? 1 : 0;

      if(self.order === 0) {
        self.sortBy(field, 'asc');
      } else if (self.order === 1) {
        self.sortBy(field, 'desc');
      };
    };

   }; // end of DashBoardController


})();
