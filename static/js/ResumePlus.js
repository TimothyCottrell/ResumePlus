//What will happen when the web application loads
$(document).ready(function() {

    /* Use JQuery datepicker to let user pick date in account setting */
    $(".date-picker").datepicker();

    /* Update user profile picture */
    $("#image-upload").change(function(event) {
        var x = URL.createObjectURL(event.target.files[0]);
        $("#upload-image").attr("src",x);
    });
}); 