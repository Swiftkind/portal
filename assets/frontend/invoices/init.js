(function () {
  'use strict';

  angular
    .module('invoices.portal', [])
    .constant('TEMPLATE_URL', '/static/frontend/templates/invoices/')
    .constant('API_INVOICE_URL', '/api/invoices/')
  ;

})();