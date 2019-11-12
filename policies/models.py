from django.db import models

# Create your models here.

class PolicyCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta():
        verbose_name = 'Policy Category'
        verbose_name_plural = '1 - Policy Categories'

class Policy(models.Model):

    title = models.CharField(max_length=255)
    category = models.ForeignKey(PolicyCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Policy'
        verbose_name_plural = '2 - Policies'