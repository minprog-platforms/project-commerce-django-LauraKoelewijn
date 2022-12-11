from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Categories, AuctionListing, Bid, Comment


def index(request):
    active_listing = AuctionListing.objects.filter(is_active=True)
    return render(request, "auctions/index.html", {
        "listings": active_listing,
        "category": Categories.objects.all()
    })

def category_sort(request):
    if request.method == "POST":
        chosen_category = request.POST['category']
        category = Categories.objects.get(category_options=chosen_category)
        active_listing = AuctionListing.objects.filter(is_active=True, category=category)
        return render(request, "auctions/index.html", {
            "listings": active_listing,
            "category": Categories.objects.all()
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

def listing(request, id):
    listingdetails = AuctionListing.objects.get(pk=id)
    all_comments = Comment.objects.filter(listing=listingdetails)
    return render(request, "auctions/listing.html", {
        "listing": listingdetails,
        "all_comments": all_comments
    })

def newbid(request, id):
    # get the new bid from form
    bid = float('%.2f' % float(request.POST["bid"]))
    # get info about page
    listingdetails = AuctionListing.objects.get(pk=id)
    # if the new bid is bigger than the previous, page has to be updated
    if bid > listingdetails.current_price.bid:
        # create a new bid object
        new_bid = Bid(
            bid=('%.2f' % bid),
            bidder=request.user
        )
        # save the new bid
        new_bid.save()
        # update the current price on the page
        listingdetails.current_price = new_bid
        # save updated version of the page
        listingdetails.save()
        return render(request, "auctions/listing.html", {
            "listing": listingdetails
        })
    else:
        messages.error(request,'The bid you placed is lower than the current bid.')
        listingdetails = AuctionListing.objects.get(pk=id)
        return render(request, "auctions/listing.html", {
            "listing": listingdetails
        })

def comment(request, id):
    # get comment from form
    comment = request.POST["comment"]
    commenter = request.user
    # get info from page
    listingdetails = AuctionListing.objects.get(pk=id)
    # create new comment object
    new_comment = Comment(
        comment=comment,
        commenter=commenter,
        listing=listingdetails
        )

    new_comment.save()

    return HttpResponseRedirect(reverse("listing",args=(id, )))

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
        # create bid as a first price
        bid = Bid(bid=float(current_price), bidder=seller)
        # and save it
        bid.save()
        # here I create a new AuctionListing object
        new_listing = AuctionListing(
            title=title,
            description=description,
            photo=photo,
            current_price=bid,
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
