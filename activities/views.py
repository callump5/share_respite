from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Activity, ActivityBlurb
from home.models import Sponser

from contact.forms import ContactRequestForm

from contact.send_mail import my_send_mail, authError
from smtplib import SMTPAuthenticationError

import requests
from django.conf import settings




# Create your views here.

def get_activites(request):
    activities = Activity.objects.all()
    blurb = ActivityBlurb.objects.all()
    sponsers = Sponser.objects.all()

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
                return redirect('/activities')

        return redirect('/activities')

    else:

        contact_form = ContactRequestForm()


    args = {
        'activities': activities,
        'sponsers': sponsers,
        'contact_form': contact_form,
        'blurb': blurb
    }
    return render(request, 'pages/activities.html', args)