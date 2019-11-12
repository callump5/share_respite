from django.shortcuts import render
from .models import HomeLandingText, HomeAboutText, Sponser
from staff.models import Staff
from donations.models import Donation

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

    args = {
        'landing': landing,
        'about': about,
        'staff': staff,
        'sponsers':sponsers,
        'ach': ach,

    }

    return render(request, 'pages/home.html', args)