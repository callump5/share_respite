from django.db import models
from django.core.validators import ValidationError

# Create your models here.

class Review(models.Model):
    author = models.CharField(max_length=300, default='anonymous')
    review = models.TextField()

    def __str__(self):
        return str(self.id) + ' - ' + self.author


    def check_max(self, taken_slots):

        full = False

        if taken_slots >= 4:
            full = True

        return full


    def clean(self):

        reviews = Review.objects.all().count()

        if reviews:
            if self.check_max(reviews):
                raise ValidationError('Max of 4 Reviews. If probablems still persist, delete the 4th review and recreate correctly')

    class Meta():
        verbose_name = 'Review'
        verbose_name_plural = '1 - Reviews'