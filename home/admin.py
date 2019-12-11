from django.contrib import admin

from .models import HomeLandingText, HomeAboutText, Sponser, HomeImages

# Register your models here.

admin.site.register(HomeLandingText)
admin.site.register(HomeAboutText)
admin.site.register(HomeImages)
admin.site.register(Sponser)
