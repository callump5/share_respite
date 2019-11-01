from django.shortcuts import render

# Create your views here.

def get_staff(request):
    return render(request, 'pages/staff.html')