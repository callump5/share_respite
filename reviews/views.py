from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

from .models import Review
from home.models import Sponser

from contact.forms import ContactRequestForm


from contact.send_mail import my_send_mail, authError
from smtplib import SMTPAuthenticationError

import requests



# Create your views here.

def get_reviews(request):
    reviews = Review.objects.all()
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
                return redirect('/reviews')

        return redirect('/reviews')

    else:

        contact_form = ContactRequestForm()


    args = {
        'sponsers':sponsers,
        'reviews':reviews,
        'contact_form': contact_form
    }
    return render(request, "pages/reviews.html", args)