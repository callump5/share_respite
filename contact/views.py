from django.shortcuts import render

# Create your views here.

def get_contact(request):
    return render(request, 'pages/contact.html')