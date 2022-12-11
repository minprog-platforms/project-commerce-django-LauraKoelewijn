from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createlisting, name="create"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("category_sort", views.category_sort, name="category_sort"),
    path("newbid/<int:id>", views.newbid, name="newbid"),
    path("comment/<int:id>", views.comment, name="comment"),

]
