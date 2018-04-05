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

    self.invoiceService = InvoiceService;

   }; // end of DashBoardController


})();
