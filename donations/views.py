from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .models import Donation
from home.models import Sponser

from .forms import DonationForm
from contact.forms import ContactRequestForm



from contact.send_mail import my_send_mail, authError
from smtplib import SMTPAuthenticationError


import requests
from share_settings.base import GOOGLE_RECAPTCHA_SECRET_KEY as GRK,STRIPE_PUBLISHABLE_KEY

from django.contrib import messages





import stripe


# Create your views here.

def get_donations(request):

    sponsers = Sponser.objects.all()

    donations = Donation.objects.all()
    ach = 0

    for donation in donations:
        ach += donation.donation

    if request.method == 'POST':

        contact_form = ContactRequestForm(request.POST)

        if contact_form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': GRK,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                contact = contact_form.save()
                contact.save()
                try:
                    my_send_mail(request, contact.name, contact.email, contact.number, contact.message)
                except SMTPAuthenticationError as e:
                    authError(request)

            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('/fundraising')

        return redirect('/fundraising')

    else:

        contact_form = ContactRequestForm()


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
        'contact_form': contact_form,

        'STRIPE_PUBLISHABLE_KEY': STRIPE_PUBLISHABLE_KEY
    }


    return render(request, 'pages/donations.html', args)
