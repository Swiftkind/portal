(function () {
  'use strict';

  angular
    .module('portal', [
      'ui.router',
      'invoices.portal'
    ])
    .constant('TEMPLATE_URL', '/static/frontend/templates/')
  ;

})();