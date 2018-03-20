$(document).ready(function () {
	$('.selectpickerClient').selectpicker({
	  liveSearchPlaceholder: 'Search Clients'
	});

    $('.selectpickerTerms').selectpicker({
      liveSearchPlaceholder: 'Search Clients'
    });

    $('#invoiceDate').datepicker({
        uiLibrary: 'bootstrap4'
    });

    $('#dueDate').datepicker({
        uiLibrary: 'bootstrap4'
    });
});
