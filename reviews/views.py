from django.shortcuts import render
from .models import Review
from home.models import Sponser

# Create your views here.

def get_reviews(request):
    reviews = Review.objects.all()
    sponsers = Sponser.objects.all()

    args = {
        'sponsers':sponsers,
        'reviews':reviews
    }
    return render(request, "pages/reviews.html", args)