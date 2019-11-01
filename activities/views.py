from django.shortcuts import render

# Create your views here.

def get_activites(request):
    return render(request, 'pages/activities.html')