(function () {
  'use strict';

  angular
    .module('dashboard.portal')
    .controller('DashboardController', DashboardController)

    /* This will handle the data of dashboard from invoice service
     */
    function DashboardController($scope, InvoiceService){
      self = this;
      self.order = 0;
      self.invoiceService = InvoiceService;
      feather.replace();

      // Request to backend
      self.sortBy = function (field, order) {
        self.invoiceService.getList('', field, order);
      }

      // Sorts the display 
      self.sort = function (field) {
        self.order = self.order == 0 ? 1 : 0;

        if (self.order === 0) {
          self.sortBy(field, 'asc');

        } else if (self.order === 1) {
          self.sortBy(field, 'desc');
          
        }
      }
    }

})();