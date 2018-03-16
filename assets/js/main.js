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

    $('#profile').on('click', function(e) {
        e.preventDefault();
        $('#profile-side-bar').toggleClass('active');
    });

    $('.side-bar-toggle').on('click', function() {
        $('#profile-side-bar').removeClass('active');
    });
});
