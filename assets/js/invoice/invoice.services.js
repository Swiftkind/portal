/* INVOICE SERVICE
 * @desc : This module will fetch the data from the backend
 */
var InvoiceService = function () {
  // URL for invoice detail API
  var INVOICE_URL = '/api/invoices/';
  // Local variable
  var services = {
    detail:getDetail,
  }

  /* Gets the Invoice Details
   * @desc : Gets the invoice details from the api invoice_detail
   */
  function getDetail (id) {
    // Gets the invoice detail data 
    return $.get(INVOICE_URL + id);
  }

  return services;
}();