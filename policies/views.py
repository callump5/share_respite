from django.shortcuts import render

# Create your views here.

def get_policies(request):
    return render(request, 'pages/policies.html')