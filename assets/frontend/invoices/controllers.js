(function () {
  'use strict';

  angular
    .module('invoices.portal')
    .controller('InvoicesController', InvoicesController)
  ;


  /* INVOICE CONTROLLER
   */
  function InvoicesController($scope) {
    var self = this;

    console.log('invoice controller has been loaded successfully!');


  }

})();