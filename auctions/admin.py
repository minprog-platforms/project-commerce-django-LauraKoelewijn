from django.contrib import admin

from .models import User, Categories, AuctionListing, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
