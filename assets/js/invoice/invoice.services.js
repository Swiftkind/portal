var InvoiceService = function () {

  // Fetch data from backend

  var INVOICE_URL = '/api/invoices/';

  var services = {
    detail:getDetail,
  }

  function getDetail (id) {
    // Gets the invoice detail data 
    return $.get(INVOICE_URL + id);
  }

  return services;
}();