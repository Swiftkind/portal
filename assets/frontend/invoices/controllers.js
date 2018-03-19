(function() {
    'use strict';

    angular
        .module('invoices.portal')
        .controller('InvoicesController', InvoicesController);

  /* INVOICE CONTROLLER
   */
  function InvoicesController($scope, InvoicesServices) {
    var self = this;

    InvoicesServices
      .getLists()
      .then(function (response) {
        $scope.invoices =response.data;
      })
    ;

  $scope.detail = function (id) {
    InvoicesServices
      .getDetail(id)
      .then(function (response) {
        $scope.invoice_date = new Date(response.data.invoice_date);
        $scope.due_date = new Date(response.data.due_date);
        $scope.invoice = response.data;
        console.log(response.data);
      })
    ;
  }

  }

})();