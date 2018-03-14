/* INVOICE SERVICE
 * @desc : This module will fetch the data from the backend
 */
var InvoiceService = function () {
  // URL for invoice detail API
  var INVOICE_ASCENDING_ORDER_CODE_URL = '/api/invoices/sort/?ordering=code';
  var INVOICE_ASCENDING_ORDER_DUE_DATE_URL = '/api/invoices/sort/?ordering=due_date';
  var INVOICE_ASCENDING_ORDER_STATUS_URL = '/api/invoices/sort/?ordering=status';
  var INVOICE_ASCENDING_ORDER_AMOUNT_URL = '/api/invoices/sort/?ordering=total_amount()';
  var INVOICE_DESCENDING_ORDER_DUE_DATE_URL = '/api/invoices/sort/?ordering=-due_date';
  var INVOICE_DESCENDING_ORDER_CODE_URL = '/api/invoices/sort/?ordering=-code';
  var INVOICE_DESCENDING_ORDER_STATUS_URL = '/api/invoices/sort/?ordering=-status';
  var INVOICE_DESCENDING_ORDER_AMOUNT_URL = '/api/invoices/sort/?ordering=-total_amount()';
  var INVOICE_URL = '/api/invoices/';
  // Local variable
  var services = {
    ascendingSortCode:getAscendingOrderCode,
    ascendingSortDueDate:getAscendingOrderDueDate,
    ascendingSortStatus:getAscendingOrderStatus,
    ascendingSortAmount:getAscendingOrderAmount,
    detail:getDetail,
    descendingSortCode:getDescendingOrderCode,
    descendingSortDueDate:getDescendingOrderDueDate,
    descendingSortStatus:getDescendingOrderStatus,
    descendingSortAmount:getDescendingOrderAmount,

  }

  /* Gets the Invoice Details
   * @desc : Gets the invoice details from the api invoice_detail
   */

  function getAscendingOrderCode () {
    // Get the list of ascending invoices by code
    return $.get(INVOICE_ASCENDING_ORDER_CODE_URL);
  }

  function getDescendingOrderCode () {
    // Get the list of descending invoices by code
    return $.get(INVOICE_DESCENDING_ORDER_CODE_URL);
  }

  function getAscendingOrderDueDate () {
    // Get the list of ascending invoices by due date
    return $.get(INVOICE_ASCENDING_ORDER_DUE_DATE_URL);
  }

  function getDescendingOrderDueDate () {
    // Get the list of descending invoices by due date
    return $.get(INVOICE_DESCENDING_ORDER_DUE_DATE_URL);
  }

  function getAscendingOrderStatus () {
    // Get the list of ascending invoices by status
    return $.get(INVOICE_ASCENDING_ORDER_STATUS_URL);
  }

  function getDescendingOrderStatus () {
    // Get the list of descending invoices by status
    return $.get(INVOICE_DESCENDING_ORDER_STATUS_URL);
  }

  function getAscendingOrderAmount () {
    // Get the list of ascending invoices by amount
    return $.get(INVOICE_ASCENDING_ORDER_AMOUNT_URL);
  }

  function getDescendingOrderAmount () {
    // Get the list of descending invoices by amount
    return $.get(INVOICE_DESCENDING_ORDER_AMOUNT_URL);
  }
  function getDetail (id) {
    // Gets the invoice detail data 
    return $.get(INVOICE_URL + id);
  }

  return services;
}();