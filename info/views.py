from django.shortcuts import render

# Create your views here.

def get_info(request):
    return render(request, 'pages/info.html')