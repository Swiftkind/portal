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
      list: [],
      getDetail:getDetail,
      getList: getList,
      terms: [],
      getLatest:getLatest
    }

    getList();
    getTerms();

    return services;

    /* Gets list of all invoices
     */
    function getList (params) {
      return $http.get(API_URL + 'invoices/?' + $httpParamSerializer(params))
        .then(function (response) {
          services.list = response.data;
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

  }

})();