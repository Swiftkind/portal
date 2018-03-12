var InvoiceController = function () {

  // Manipulate data from invoice service

  var controller = {
      detail:displayDetail,
    }

  $('#invoice-detail').load('/static/js/invoice/templates/invoice_detail.html');
  function displayDetail (inv_id) {
    // Handle the invoice detail
    var invoiceDetail = InvoiceService.detail(inv_id);

    invoiceDetail
      .done(function (response) {
        var context = {
          code: response.code,
          items: response.items,
          notes: response.notes,
          total_amount: response.total_amount
        };
        var tmpl = _.template($('#invoiceTemplate').html());
        $('.invoice-view-details').html(tmpl(context));
      })
  }

  return controller;

}

var invoiceCtrl = InvoiceController();

// Sets the default display of the invoice detail
$(function () {
  var inv_id = $('.invoice-item').first().attr('id');
  if (inv_id) invoiceCtrl.detail(inv_id);
});