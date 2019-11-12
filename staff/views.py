from django.shortcuts import render
from .models import StaffRole, Staff
from home.models import Sponser

# Create your views here.

def get_staff(request):
    roles = StaffRole.objects.all().order_by('rank')
    staff = Staff.objects.all()
    sponsers = Sponser.objects.all()

    args = {
        'roles': roles,
        'sponsers':sponsers,
        'staff': staff
    }

    return render(request, 'pages/staff.html', args)