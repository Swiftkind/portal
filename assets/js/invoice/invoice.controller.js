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
          total_item: response.total_items
        };
        var tmpl = _.template($('#invoiceTemplate').html());
        $('.invoice-view-details').html(tmpl(context));
      })
  }

  return controller;

}

var invoiceCtrl = InvoiceController();
