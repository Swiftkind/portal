$(document).ready(function () {
	$('.selectpicker').selectpicker({
	  liveSearchPlaceholder: 'Search Clients'
	});

    $('#startDate').datepicker({
        uiLibrary: 'bootstrap4'
    });

    $('#endDate').datepicker({
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
