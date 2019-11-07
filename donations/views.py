from django.shortcuts import render

# Create your views here.

def get_donations(request):
    return render(request, 'pages/donations.html')
