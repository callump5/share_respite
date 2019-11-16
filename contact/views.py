from django.shortcuts import render,redirect
from django.contrib import messages

from .models import ContactDetail, OpeningDays
from home.models import Sponser


from contact.send_mail import my_send_mail, authError
from smtplib import SMTPAuthenticationError


import requests
from django.conf import settings

from django.contrib import messages
from django.conf import settings

from .forms import ContactRequestForm

# Create your views here.

def get_contact(request):
    contacts = ContactDetail.objects.all()
    openings = OpeningDays.objects.all().order_by('rank')
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
                return redirect('/contact')

        return redirect('/contact')

    else:

        contact_form = ContactRequestForm()

    args = {
        'contacts': contacts,
        'sponsers':sponsers,
        'openings': openings,
        'contact_form': contact_form
    }

    return render(request, 'pages/contact.html', args)