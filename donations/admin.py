from django.contrib import admin
from .models import Donation, DonationText

# Register your models here.

admin.site.register(DonationText)
admin.site.register(Donation)

