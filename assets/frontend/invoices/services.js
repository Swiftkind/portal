(function () {
  'use strict'

  angular
    .module('invoices.portal')
    .service('InvoiceService', InvoiceService)
  ;
  /* INVOICE SERVICE: this wil fetch data from the backend
   */
  function InvoiceService($http, $httpParamSerializer, API_URL) {

    var services = {
      list: [],
      getList:getList,
      pageIndex:pageNumberLimitToIndex,
    }

    getList();
    return services;


    /* Gets all list of invoices
     */
     function getList (params) {
      return $http.get(API_URL + 'invoices/?' + $httpParamSerializer(params))
        .then(function (response) {
          services.list = response.data;
        });
    }


    /* Adjust page number between 3 pages
     */
    function pageNumberLimitToIndex (page_number) {
      switch (page_number % 3) {
        case 0:
          return page_number-3;
        case 1:
          return page_number-1;
        case 2:
           return page_number-2;
      }
    }
  }

})();