from django.shortcuts import render
from .models import ContactDetail, OpeningDays
from home.models import Sponser

# Create your views here.

def get_contact(request):
    contacts = ContactDetail.objects.all()
    openings = OpeningDays.objects.all().order_by('rank')
    sponsers = Sponser.objects.all()

    args = {
        'contacts': contacts,
        'sponsers':sponsers,
        'openings': openings
    }

    return render(request, 'pages/contact.html', args)