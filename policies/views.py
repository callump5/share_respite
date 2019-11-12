from django.shortcuts import render
from .models import PolicyCategory, Policy
from home.models import Sponser

# Create your views here.

def get_policies(request):
    categories = PolicyCategory.objects.all()
    policies = Policy.objects.all()
    sponsers = Sponser.objects.all()

    args = {
        'categories': categories,
        'policies': policies,
        'sponsers': sponsers
    }
    return render(request, 'pages/policies.html', args)