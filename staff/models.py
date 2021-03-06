import os
from django.db import models
from tinymce.models import HTMLField


def upload_site_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return '%s%s' % (
        filename_base,
        filename_ext.lower(),
    )

# Create your models here.

class StaffRole(models.Model):
    role = models.CharField(max_length=300)
    rank = models.IntegerField()

    def __str__(self):
        return self.role

    class Meta():
        verbose_name = 'Staff Role'
        verbose_name_plural = '1 - Staff Roles'

class Staff(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    role = models.ForeignKey(StaffRole, on_delete=models.CASCADE)
    rank = models.IntegerField()
    bio = HTMLField()
    img = models.ImageField(upload_to=upload_site_img)
    def __str__(self):
        return self.last_name

    class Meta():
        verbose_name = 'Staff Profile'
        verbose_name_plural = '2 - Staff Profiles'


class TrusteeSection(models.Model):
    role = models.CharField(max_length=300)
    rank = models.IntegerField()

    def __str__(self):
        return self.role

    class Meta():
        verbose_name = 'Trustee Role'
        verbose_name_plural = '4 - Trustee Roles'


class Trustee(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    link = models.CharField(max_length=500)
    role = models.ForeignKey(TrusteeSection, on_delete=models.CASCADE)
    rank = models.IntegerField()
    bio = HTMLField()
    img = models.ImageField(upload_to=upload_site_img)

    def __str__(self):
        return self.last_name

    class Meta():
        verbose_name = 'Trustee Profile'
        verbose_name_plural = '3 - Trustee Profiles'
