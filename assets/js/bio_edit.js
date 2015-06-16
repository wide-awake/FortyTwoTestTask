// handling form
var bioForm = $('#bio_form');

var options = {
    beforeSubmit: function(){
        $('#bio_form :input').prop("disabled", true);
        //$('#loader').show();
    },
    success: function(){
        $('#bio_form :input').prop("disabled", false);
        $('html,body').scrollTop(0);
        $('#loader').hide();
        $('.msg').html('<p class="alert alert-success" role="alert"><strong>Success!</strong> Changes have been saved!</p>');
    }
};

bioForm.ajaxForm(options);


// image preview from input
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
            reader.onload = function (e) {
                $('#photo-preview').attr('src', e.target.result);
            }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#id_photo").change(function(){readURL(this);});


// datepicker
$(function() {
    $( ".datepicker" ).datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: "1915:2015",
        dateFormat: "yy-mm-dd"
	    });
});
