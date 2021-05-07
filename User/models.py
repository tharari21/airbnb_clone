from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    user = models.ForeignKey('auth.User')
#     # User - id, name, date_of_birth, rating, phone number, email, ssn, credit_card_number, isHost - Maybe reserve certain ids for hosts.
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False)
    last_name = models.CharField(null=False)
    dob = models.DateField(null=False)
    rating = models.RatingField()
    phone_number = models.PhoneNumberField()
    email = models.EmailField()
    ssn = models.CharField()


    def __str__(self):
        return self.first_name + self.last_name