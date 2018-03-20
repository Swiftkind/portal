(function () {
  'use strict'

  angular
    .module('invoices.portal')
    .service('InvoicesServices', InvoicesServices)
  ;
  /* INVOICE SERVICE: this wil fetch data from the backend
   */
  function InvoicesServices($http) {

    // Local variable
    var services = {
      list: [],
      getDetail:getDetail
    }

    getLists();

    return services;

    /* Gets all list of invoices
     */
    function getLists () {
      return $http.get('api/invoices/')
        .then(function (resp) {
          services.list = resp.data;
        });
    }
   /* Gets detail of the invoice by id
    */
    function getDetail (id) {
      return $http.get('api/invoices/' + id + '/');
    }

  }

})();