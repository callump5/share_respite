from django.db import models
from django.core.validators import ValidationError
from tinymce.models import HTMLField

# Create your models here.


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s " % obj._meta.verbose_name)


class InformationText(models.Model):
    text = HTMLField()

    def __str__(self):
        return "Information Text"

    class Meta():
        verbose_name = 'Information Text'
        verbose_name_plural = '1 - Information Text'

    def clean(self):
        validate_only_one_instance(self)

class StickyNote(models.Model):
    title = models.CharField(max_length=300, help_text='This will not be displayed, this is for your reference')
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Sticky Note'
        verbose_name_plural = '2 - Sticky Notes'

