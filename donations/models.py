from django.db import models
from django.conf import settings
import stripe

# Create your models here.


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
        verbose_name_plural = '1 - Donations'