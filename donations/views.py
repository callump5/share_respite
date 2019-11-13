from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .forms import DonationForm
from .models import Donation
from home.models import Sponser




import stripe


# Create your views here.

def get_donations(request):

    sponsers = Sponser.objects.all()

    donations = Donation.objects.all()
    ach = 0

    for donation in donations:
        ach += donation.donation

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount= int(form.cleaned_data['donation'] * 100),
                    currency="GBP",
                    description= 'Share',
                    card= form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    new_form = form.save(False)
                    new_form.save()
                    messages.success(request, 'Thank you, your donation of £' + str(form.cleaned_data['donation']) + ' is greatly appreciated!')
                else:
                    messages.error(request, "Sorry, we were unable to take a payment with that card!")
            except stripe.error.CardError:
                messages.error(request, "Unfortunately, your card was declined!")

            return redirect('/fundraising')
    else:
        form = DonationForm()


    args = {
        'sponsers':sponsers,
        'ach':ach,
        'form':form,

        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
    }


    return render(request, 'pages/donations.html', args)
