(function () {
  'use strict'

  angular
    .module('invoices.portal')
    .service('InvoicesServices', InvoicesServices)
  ;

  function InvoicesServices($http) {
    function getLists () {
      return $http.get('api/invoices/');
    }

    function getDetail (id) {
      return $http.get('api/invoices/' + id);
    }

    var services = {
      getLists:getLists,
      getDetail:getDetail
    }

    return services;

  }

})();