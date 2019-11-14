from django.contrib import admin
from .models import OpeningDays, ContactDetail, ContactRequest

# Register your models here.

admin.site.register(OpeningDays)
admin.site.register(ContactDetail)
admin.site.register(ContactRequest)