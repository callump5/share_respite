
function showInput() {
    document.getElementById('id_donation').value =
                document.getElementById("user_input").value;
    document.getElementById('donation_fee').innerHTML =
                document.getElementById("user_input").value;
    $('#donation-form').css('display', 'block')
}

$('.donations__form--close').on('click', function () {
    $('#donation-form').css('display', 'none');
});

$('#donation-form').find('label').addClass('donations__form--label');
$('#donation-form').find('input').addClass('donations__form--input');
$('#validate_card_btn').removeClass('donations__form--input');
$('#form-submit').removeClass('donations__form--input')
    .attr("disabled", true)
    .on('click', function () {
        $('.loader').css('display', 'block');
    });



$('#validate_card_btn').on('click', function () {

    $('.loader').css('display', 'block');

    // This identifies your website in the createToken call below
    Stripe.setPublishableKey('pk_test_caLAMi5hXVyU8cYdjeN0J2Bo');

    var card = {
        number:   $("#id_credit_card_number").val(),
        expMonth: $("#id_expiry_month").val(),
        expYear:  $("#id_expiry_year").val(),
        cvc:      $("#id_cvv").val()
    };

    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#stripe-error-message").css('display', 'none');
            console.log(status, response);
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);
            $("#form-submit").attr("disabled", false);

            $('.loader').css('display', 'none');

        } else {
            $('.loader').css('display', 'none');
            $("#stripe-error-message").text(response.error.message).css('display', 'block');
            $("#credit-card-errors").show().css('display', 'block');
        }
    });

    return false;

});

