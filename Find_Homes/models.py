from django.db import models
from django.db.models import Model
from django.utils import timezone

# from django.core import reverse

# Create your models here.


# class Rating(models.IntegerChoices):
#     POOR = 1, 'Poor'
#     FAIR = 2, 'Fair'
#     OK = 3, 'Ok'
#     GOOD = 4, 'Good'
#     EXCELLENT = 5, 'Excellent'


class Listing(Model):
    # listing_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, default=None, null=True)
    title = models.CharField(max_length=100)
    # host_id = models.ForeignKey()
    # rating = models.IntegerField(
    #     default=Rating.EXCELLENT, choices=Rating.choices)
    price_per_night = models.DecimalField(decimal_places=2, max_digits=10000)
    description = models.CharField(max_length=300)
    images = models.ImageField(
        upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Location(Model):
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.address1
