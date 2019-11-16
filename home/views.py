from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .models import HomeLandingText, HomeAboutText, Sponser
from contact.forms import ContactRequestForm

from staff.models import Staff
from donations.models import Donation


from contact.send_mail import my_send_mail, authError
from smtplib import SMTPAuthenticationError

import requests





# Create your views here.


def index(request):
    landing = HomeLandingText.objects.all()
    about = HomeAboutText.objects.all()
    staff = Staff.objects.all()
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
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
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
                return redirect('/')

        return redirect('/')

    else:

        contact_form = ContactRequestForm()

    args = {
        'landing': landing,
        'about': about,
        'staff': staff,
        'sponsers':sponsers,
        'ach': ach,
        'contact_form': contact_form

    }

    return render(request, 'pages/home.html', args)