import os

from django.db import models
from django.core.validators import ValidationError
from tinymce.models import HTMLField
# Create your models here.


def upload_site_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return '%s%s' % (
        filename_base,
        filename_ext.lower(),
    )


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s " % obj._meta.verbose_name)


class HomeLandingText(models.Model):
    text = HTMLField()

    def __str__(self):
        return "Landing Text"

    class Meta():
        verbose_name = "Landing Text"
        verbose_name_plural = "1 - Landing Text"

    def clean(self):
        validate_only_one_instance(self)


class HomeAboutText(models.Model):
    text = HTMLField()

    def __str__(self):
        return "About Text"

    class Meta():
        verbose_name = "2 - About Text"
        verbose_name_plural = "2 - About Text"

    def clean(self):
        validate_only_one_instance(self)

class Sponser(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to=upload_site_img)
    link = models.TextField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Sponser'
        verbose_name_plural = '3 - Sponsers'