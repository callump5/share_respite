from django.contrib import admin
from .models import PolicyCategory, Policy

# Register your models here.

admin.site.register(PolicyCategory)
admin.site.register(Policy)