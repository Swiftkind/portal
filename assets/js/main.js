$(document).ready(function () {
	$('.selectpicker').selectpicker({
	  liveSearchPlaceholder: 'Search Clients'
	});

	$('.datepicker').datepicker({
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
