from django.contrib import admin
from .models import StaffRole, Staff, Trustee, TrusteeSection

# Register your models here.

admin.site.register(StaffRole)
admin.site.register(Staff)
admin.site.register(Trustee)
admin.site.register(TrusteeSection)