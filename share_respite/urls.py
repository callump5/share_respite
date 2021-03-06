"""share_respite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home_views
from info import views as info_views
from activities import views as activity_views
from staff import views as staff_views
from reviews import views as review_views
from policies import views as policy_views
from donations import views as donations_views
from contact import views as contact_views
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index),
    path('information', info_views.get_info),
    path('activites', activity_views.get_activites),
    path('staff', staff_views.get_staff),
    path('reviews', review_views.get_reviews),
    path('privacy', policy_views.get_privacy),
    path('policies', policy_views.get_policies),
    path('fundraising', donations_views.get_donations),
    path('contact', contact_views.get_contact),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
