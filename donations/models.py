from django.db import models
from django.conf import settings
from django.core.validators import ValidationError

from tinymce.models import HTMLField
import stripe


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s " % obj._meta.verbose_name)


# Create your models here.
class DonationText(models.Model):
    text = HTMLField()

    def __str__(self):
        return "Donations Text"

    class Meta():
        verbose_name = "Donations Text"
        verbose_name_plural = "1 - Donations Text"

    def clean(self):
        validate_only_one_instance(self)

class Donation(models.Model):
    donation = models.DecimalField(max_digits=6, decimal_places=2, default=2.50)
    email = models.EmailField()

    stripe_id = models.CharField(max_length=40, default='')

    def charge(self, request, email, fee):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create a Customer
        stripe_customer = stripe.Customer.create(
            card=token,
            description=email
        )

        # Save the Stripe ID to the customer's profile
        self.stripe_id = stripe_customer.id
        self.save()

        # Charge the Customer instead of the card
        stripe.Charge.create(
            amount=fee, # in cents
            currency="gbp",
            customer=stripe_customer.id
        )

        return stripe_customer


    def __str__(self):
        return 'Donation - ' + str(self.id)

    class Meta():
        verbose_name = 'Donations'
        verbose_name_plural = '2 - Donations'