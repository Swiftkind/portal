var InvoiceController = function () {

  // Manipulate data from invoice service

  var controller = {
      detail:displayDetail,
    }

  function displayDetail (id) {
    // Handle the invoice detail
    var inv_id = id;
    var invoiceDetail = InvoiceService.detail(inv_id);
    var itemTbody = $("items-tbody");

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
