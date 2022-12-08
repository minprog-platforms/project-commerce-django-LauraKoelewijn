from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category_options = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.category_options}"

class AuctionListing(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=600)
    current_price = models.FloatField()
    photo = models.URLField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    

    def __str__(self):
        return f"{self.title}"
