(function () {
  'use strict'

  angular
    .module('invoices.portal')
    .service('InvoiceService', InvoiceService)
  ;

  /* INVOICE SERVICE: this wil fetch data from the backend
   */
  function InvoiceService($http, API_INVOICE_URL ,$httpParamSerializer) {

    // Local variable
    var services = {
      list       : [],
      getDetail  : getDetail,
      getList    : getList,
      terms      : [],
      getLatest  : getLatest,
      create     : create,
      update     : update,
      addItems   : addItems,
      updateItems: updateItems,
      deleteInv  : deleteInv
    }

    getList();
    getTerms();

    return services;

    /* Gets list of all invoices
     */
    function getList (params, field, order) {
      return $http.get(API_INVOICE_URL + '?' + $httpParamSerializer(params) + (field ? '&sort='+field : '') + (order ? '&order='+order : ''))
        .then(function (response) {
          services.list = response.data;
        });
    };

   /* Gets detail of the invoice by id
    */
    function getDetail (id) {
      return $http.get(API_INVOICE_URL + id + '/');
    }

   /* Gets the terms of the invoice
    */
    function getTerms () {
      return $http.get(API_INVOICE_URL + 'terms/')
        .then(function (response){
          services.terms = response.data;
        });
    }

   /* Gets the latest invoice
    */
    function getLatest () {
      return $http.get(API_INVOICE_URL + 'latest/');
    }

    /* Create new invoice
     */
    function create (data) {
      return $http.post(API_INVOICE_URL, data);
    }

    /* Update invoice
     */
    function update (id, data) {
      return $http.patch(API_INVOICE_URL + id + '/', data);
    }

    /* Delete invoice
     */
    function deleteInv (id) {
      return $http.delete(API_INVOICE_URL + id + '/');
    }

    /* Add items in invoice
     */
     function addItems (data) {
      return $http.post(API_INVOICE_URL + 'items/', data);
     }

    /* Edit items in invoice
     */
     function updateItems (id, data) {
      return $http.patch(API_INVOICE_URL + 'items/' + id + '/', data);
     }

  }

})();
