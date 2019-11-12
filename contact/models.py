from django.db import models

# Create your models here.

class OpeningDays(models.Model):
    day = models.CharField(max_length=255)
    opening = models.TimeField()
    closing = models.TimeField()
    rank = models.IntegerField()

    def __str__(self):
        return self.day

    class Meta():
        verbose_name = 'Opening Day'
        verbose_name_plural = '1 - Opening Days'

class ContactDetail(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Contact Detail'
        verbose_name_plural = '2 - Contact Details'