from django.shortcuts import render
from .models import Activity
from home.models import Sponser
# Create your views here.

def get_activites(request):
    activities = Activity.objects.all()
    sponsers = Sponser.objects.all()
    args = {
        'activities': activities,
        'sponsers': sponsers
    }
    return render(request, 'pages/activities.html', args)