from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createlisting, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("category_sort", views.category_sort, name="category_sort"),
    path("newbid/<int:id>", views.newbid, name="newbid"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("closed_auction/<int:id>", views.close, name="closed_auction"),
    path("remove_from_watchlist/<int:id>", views.remove_from_watchlist, name="remove_from_watchlist"),
    path("add_to_watchlist/<int:id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("watchlist", views.watchlist, name="watchlist")

]
