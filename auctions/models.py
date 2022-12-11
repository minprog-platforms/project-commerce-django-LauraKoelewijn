from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category_options = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.category_options}"

class Bid(models.Model):
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, max_length=64, on_delete=models.CASCADE, related_name="bidder_user")

    def str_return_sentence(self):
        return f"Highest bid is currently €{self.bid}, placed by {self.bidder}!"

    def __str__(self):
        return f"{self.bid}"

    def winner(self):
        return f"Highest bid of €{self.bid} was placed by {self.bidder}, congratulations {self.bidder}!"


class AuctionListing(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=600)
    current_price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bid_listing")
    photo = models.URLField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    comment = models.CharField(max_length=150)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_comment")
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, blank=True, null=True, related_name="listing_comment")

    def __str__(self):
        return f'"{self.comment}" -{self.commenter}'
