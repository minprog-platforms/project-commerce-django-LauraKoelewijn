from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=600)
    current_price = models.FloatField()
    photo = models.URLField()
    category = models.CharField(max_length=20)
