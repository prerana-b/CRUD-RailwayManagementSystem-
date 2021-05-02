from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Ticketinfo(models.Model):
    pass_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True, unique=True)
    pass_address = models.TextField(null=True)
    aadhar = models.ImageField(null=True, blank=True, upload_to='images/')
    gender = models.CharField(max_length=20)
    # CHECKBOX FIELDS
    foodreqd = models.BooleanField('Food required', default=False)
    railwaypasscon = models.BooleanField(
        'Railway Pass Concession', default=False)
    # DROP-DOWN FIELD
    carr = (
        ('ec', "Exec. Chair Car"),
        ('2a', "AC 2 Tier"),
        ('fc', "First Class"),
        ('3a', "AC 3 Tier"),
        ('3e', "AC 3 Economy"),
        ('cc', "Chair Car"),
        ('sl', "Sleeper"),
        ('2s', "Second Sitting")

    )
    carr = models.CharField(max_length=20, choices=carr, default='All Classes')
    bag_weight = models.FloatField()
    dateofdeparture = models.DateField()  # DATE OF REGISTRATION

    class Meta:
        db_table = 'Bookings'
