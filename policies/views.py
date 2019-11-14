from django.shortcuts import render,redirect
from django.contrib import messages

from .models import PolicyCategory, Policy
from home.models import Sponser

from contact.forms import ContactRequestForm

from contact.send_mail import my_send_mail, authError
from smtplib import SMTPAuthenticationError

import requests
from share_respite.settings import GOOGLE_RECAPTCHA_SECRET_KEY as GRK



# Create your views here.

def get_policies(request):
    categories = PolicyCategory.objects.all()
    policies = Policy.objects.all()
    sponsers = Sponser.objects.all()

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
                return redirect('/policies')

        return redirect('/policies')

    else:

        contact_form = ContactRequestForm()


    args = {
        'categories': categories,
        'policies': policies,
        'sponsers': sponsers,
        'contact_form': contact_form
    }
    return render(request, 'pages/policies.html', args)