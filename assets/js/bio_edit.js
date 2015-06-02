    var frm = $('#bio_form');
    frm.submit(function (ev) {
        $('#loader').show(); //<----here
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                $('#loader').hide();
                $('html,body').scrollTop(0);
                $('.msg').html('<p class="alert alert-success" role="alert"><strong>Success!</strong> Changes have been saved!</p>');
            }
        });

        ev.preventDefault();
    });

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
    $("#id_photo").change(function(){
        readURL(this);
    });
