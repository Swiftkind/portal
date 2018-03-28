(function () {
  'use strict'

  angular
    .module('invoices.portal')
    .service('InvoiceService', InvoiceService)
  ;

  /* INVOICE SERVICE: this wil fetch data from the backend
   */
  function InvoiceService($http, $httpParamSerializer, API_URL) {

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
      deleteInv     : deleteInv
    }

    getList();
    getTerms();

    return services;

    /* Gets list of all invoices
     */
    function getList (params) {
      return $http.get(API_URL + 'invoices/' + $httpParamSerializer(params))
        .then(function (response) {
          services.list = response.data.result;
        });
    }

   /* Gets detail of the invoice by id
    */
    function getDetail (id) {
      return $http.get(API_URL + 'invoices/' + id + '/');
    }

   /* Gets the terms of the invoice
    */
    function getTerms () {
      return $http.get(API_URL + 'invoices/terms/')
        .then(function (response){
          services.terms = response.data;
        });
    }

   /* Gets the latest invoice
    */
    function getLatest () {
      return $http.get(API_URL + 'invoices/latest/');
    }

    /* Create new invoice
     */
    function create (data) {
      return $http.post(API_URL + 'invoices/', data);
    }

    /* Update invoice
     */
    function update (id, data) {
      return $http.patch(API_URL + 'invoices/' + id + '/', data);
    }

    /* Delete invoice
     */
    function deleteInv (id) {
      return $http.delete(API_URL + 'invoices/' + id + '/');
    }

    /* Add items in invoice
     */
     function addItems (data) {
      return $http.post(API_URL + 'invoices/items/', data);
     }

    /* Edit items in invoice
     */
     function updateItems (id, data) {
      return $http.patch(API_URL + 'invoices/items/' + id + '/', data);
     }

  }

})();