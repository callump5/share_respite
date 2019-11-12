from django.db import models

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    activity = models.TextField()
    items = models.TextField()
    meeting = models.TextField()
    slots = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Activity'
        verbose_name_plural = '1 - Activities'

