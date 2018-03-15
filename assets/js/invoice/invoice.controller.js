/* INVOICE CONTROLLER
 * @desc : This module will handle the data from the backend
 */
var InvoiceController = function () {
  // Local variable
  var controller = {
      detail         : displayDetail,
      defaultInvoice : defaultDisplay,
    }

   /* Load Invoice Default Details
   * @desc : Sets the default display of the invoice detail
   */
  function defaultDisplay () {
    var invoiceId = $('.invoice-item').first().attr('id');
    if (invoiceId) controller.detail(invoiceId);
  }

  function addItemRow () {}

   /* Load Invoice Details
   * @desc : Loads the invoice information into the template
   */
  function displayDetail (invoiceId) {
    $('#invoice-details').load(templateURL + 'invoices/invoice_detail.html');

    // Initialized the invoice service getDetail function
    var invoiceDetail = InvoiceService.detail(invoiceId);

    // Gets the detail of invoice
    invoiceDetail
      .done(function (response) {
        // Loads the data in the template
        var tmpl = _.template($('#invoiceTemplate').html());
        $('.invoice-detail').html(tmpl({invoice:response}));
        $('.invoice-detail').find('#startDate').datepicker({uiLibrary: 'bootstrap4'});
        $('.invoice-detail').find('#endDate').datepicker({uiLibrary: 'bootstrap4'});
        $('.invoice-detail').find('#dueDate').datepicker({uiLibrary: 'bootstrap4'});
        $('.invoice-detail').find('.selectpicker').selectpicker();
      });
  }

  return controller;

}();

// Calls the function that assigns the default invoice detail
InvoiceController.defaultInvoice();
