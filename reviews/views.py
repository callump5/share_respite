from django.shortcuts import render

# Create your views here.

def get_reviews(request):
    return render(request, "pages/reviews.html")