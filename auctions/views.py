from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Categories, AuctionListing


def index(request):
    active_listing = AuctionListing.objects.filter(is_active=True)
    return render(request, "auctions/index.html", {
        "listings": active_listing
    })

def listing(request, id):
    listingdetails = AuctionListing.objects.get(pk=id)
    return render(request, "auctions/listing.html", {
        "listing": listingdetails
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createlisting(request):
    if request.method == "GET":
        return render(request, "auctions/create.html", {
            "category": Categories.objects.all()
        })
    else:
        # the data needed to save the new listing
        # extracted from the form in create.html
        title = request.POST["title"]
        description = request.POST["description"]
        current_price = request.POST["price"]
        photo = request.POST["photo"]
        category = request.POST["category"]
        seller = request.user
        category_option = Categories.objects.get(category_options=category)

        # here I create a new AuctionListing object
        new_listing = AuctionListing(
            title=title,
            description=description,
            photo=photo,
            current_price=current_price,
            seller=seller
        )
        new_listing.save()
        # Redirect to index page
        return HttpResponseRedirect(reverse(index))

def watchlist(request):
    if request.method == "GET":
        return render(request, "auctions/watchlist.html", {
            "favorites": "favorietjes"
        })
    else:
        item = request.POST["title"]
        return render(request, "auctions/watchlist.html", {
            "favorites": item
        })
