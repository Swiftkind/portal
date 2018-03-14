/* INVOICE CONTROLLER
 * @desc : This module will handle the data from the backend
 */
var InvoiceController = function () {
  // Local variable
  var controller = {
      detail:displayDetail,
      defaultInvoice:defaultDisplay,
      sort:sortInvoices,
    }

   /* Load Invoice Default Details
   * @desc : Sets the default display of the invoice detail
   */
  function defaultDisplay () {
    var invoiceId = $('.invoice-item').first().attr('id');
    if (invoiceId) controller.detail(invoiceId);
  }

  /* Load Invoice Details
   * @desc : Loads the invoice information into the template
   */
  function displayDetail (invoiceId) {
    // This will load html javacsript template
    $('#invoice-details').load(templateURL + 'invoices/invoice_detail.html');
    // Initialized the invoice service getDetail function
    var invoiceDetail = InvoiceService.detail(invoiceId);

    // Gets the detail of invoice
    invoiceDetail
      .done(function (response) {
        // Loads the data in the template
        var tmpl = _.template($('#invoiceTemplate').html());
        $('.invoice-detail').html(tmpl({invoice:response}));
      })
  }

  /* Check sort status 
   * @desc : Check sort status if ascending or descending
   */
  function checkSort (tHeadId) {
    // This will check the status
    if ($('#'+tHeadId).is('.ascending'))
      return 1;
    else
      return -1;
  }

  /* Load sorted invoices
   * @desc : Loads the sorted invoices by selected field into the template
   */
  function sortInvoices (tHeadId) {
    // This will load html javacsript template
    $('#invoices').load(templateURL + 'dashboard/dashboard_data.html');

    var sortStatus = 0
    var invNo = 'invoice-number';
    var dueDate = 'due-date';
    var status = 'payment-status';
    var amnt = 'amount';

    sortStatus = checkSort(tHeadId);

    if (sortStatus == 1 && tHeadId == invNo)
      var listDashboardData = InvoiceService.ascendingSortCode();
    if (sortStatus == -1 && tHeadId == invNo)
      var listDashboardData = InvoiceService.descendingSortCode();

    if (sortStatus == 1 && tHeadId == dueDate)
      var listDashboardData = InvoiceService.ascendingSortDueDate();
    if (sortStatus == -1 && tHeadId == dueDate)
      var listDashboardData = InvoiceService.descendingSortDueDate();

    if (sortStatus == 1 && tHeadId == status )
      var listDashboardData = InvoiceService.ascendingSortStatus();
    if (sortStatus == -1 && tHeadId == status)
      var listDashboardData = InvoiceService.descendingSortStatus();

    if (sortStatus == 1 && tHeadId == amnt )
      var listDashboardData = InvoiceService.ascendingSortAmount();
    if (sortStatus == -1 && tHeadId == amnt)
      var listDashboardData = InvoiceService.descendingSortAmount();

    listDashboardData
    .done(function (response) {
      // Loads the data in the template
      var tmpl = _.template($('#dashboardTemplate').html());
      var chevronUp = '<svg xmlns="http://www.w3.org/2000/svg"'
                      +'width="24"'
                      +'height="24"'
                      +'viewBox="0 0 24 24"'
                      +'fill="none"'
                      +'stroke="currentColor"'
                      +'stroke-width="2"'
                      +'stroke-linecap="round"'
                      +'stroke-linejoin="round"'
                      +'class="feather feather-chevron-up">'
                        +'<polyline points="18 15 12 9 6 15"></polyline>'
                      +'</svg>';
      var chevronDown = '<svg xmlns="http://www.w3.org/2000/svg"'
                        +'width="24"'
                        +'height="24"'
                        +'viewBox="0 0 24 24"'
                        +'fill="none"'
                        +'stroke="currentColor"'
                        +'stroke-width="2"'
                        +'stroke-linecap="round"'
                        +'stroke-linejoin="round"'
                        +'class="feather feather-chevron-down">'
                          +'<polyline points="6 9 12 15 18 9"></polyline>'
                        +'</svg>';
      var ascending = 'ascending';
      var descending = 'descending';
      var selAscending = 'ascending selected';
      var selDescending = 'descending selected';
      var sortMethod = 'InvoiceController.sort(this.id)';

      $('.invoices').empty();

      template = tmpl({invoices:response.results}) ;
      $('.invoices').html(template);

      $('#'+invNo).attr('onclick', sortMethod);
      $('#'+dueDate).attr('onclick', sortMethod);
      $('#'+status).attr('onclick', sortMethod);
      $('#'+amnt).attr('onclick', sortMethod);

      if ($(this)['0'].url.includes('-code')) {
        $('#'+invNo).removeClass(descending);
        $('#'+invNo).addClass(selAscending);
        $('#'+invNo+' a svg').replaceWith(chevronUp);
      } else {
        $('#'+invNo).removeClass(ascending);
        $('#'+invNo).addClass(selDescending);
        $('#'+invNo+' a svg').replaceWith(chevronDown);
      }

      if ( $(this)['0'].url.includes('-due_date') ) {
        $('#'+dueDate).removeClass(descending);
        $('#'+dueDate).addClass(selAscending);
        $('#'+dueDate+' a svg').replaceWith(chevronUp);
      } else {
        $('#'+dueDate).removeClass(ascending);
        $('#'+dueDate).addClass(selDescending);
        $('#'+dueDate+' a svg').replaceWith(chevronDown);
      }

      if ( $(this)['0'].url.includes('-status') ) {
        $('#'+status).removeClass(descending);
        $('#'+status).addClass(selAscending);
        $('#'+status+' a svg').replaceWith(chevronUp);
      } else {
        $('#'+status).removeClass(ascending);
        $('#'+status).addClass(selDescending);
        $('#'+status+' a svg').replaceWith(chevronDown);
      }

      if ( $(this)['0'].url.includes('-total_amount()') ) {
        $('#'+amnt).removeClass(descending);
        $('#'+amnt).addClass(selAscending);
        $('#'+amnt+' a svg').replaceWith(chevronUp);
      } else {
        $('#'+amnt).removeClass(ascending);
        $('#'+amnt).addClass(selDescending);
        $('#'+amnt+' a svg').replaceWith(chevronDown);
      }
    });
  }

  return controller;

}();

// Calls the function that assigns the default invoice detail
InvoiceController.defaultInvoice();