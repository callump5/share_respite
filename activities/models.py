import os

from django.db import models
from django.core.validators import ValidationError

# Create your models here.


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s " % obj._meta.verbose_name)


def upload_site_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return '%s%s' % (
        filename_base,
        filename_ext.lower(),
    )

class ActivityBlurb(models.Model):
    text = models.TextField()

    def __str__(self):
        return 'Activity Page Text'


    def clean(self):
        validate_only_one_instance(self)


    class Meta():
        verbose_name = 'Activity Page Text'
        verbose_name_plural = '1 - Activity Page Text'


class Activity(models.Model):
    week = models.DateField()
    file = models.FileField(upload_to=upload_site_img)

    def __str__(self):
        return str(self.week)

    class Meta():
        verbose_name = 'Activity'
        verbose_name_plural = '2 - Activities'

