(function () {
  'use strict';

  angular
    .module('dashboard.portal')
    .controller('DashboardController', DashboardController)

    /* This will handle the data of dashboard from invoice service
     */
    function DashboardController($scope, InvoiceService){
      self = this;
      self.invoiceService = InvoiceService;
      feather.replace();

      self.sortBy = function (field, order) {
        self.invoiceService.getList('', field, order);
      }
    }

})();