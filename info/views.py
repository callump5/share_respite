from django.shortcuts import render
from .models import InformationText, StickyNote
from home.models import Sponser

# Create your views here.

def get_info(request):
    sponsers = Sponser.objects.all()
    info = InformationText.objects.all()
    stickys = StickyNote.objects.all()

    args = {
        'info': info,
        'sponsers':sponsers,
        'stickys': stickys
    }

    return render(request, 'pages/info.html', args)