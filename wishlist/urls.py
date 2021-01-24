from django.urls import path

import wishlist.views as views

app_name = "wishlist"

urlpatterns = [
    path("", views.IndexView.as_view(), name="dashboard"),
    path("api/search", views.SearchView.as_view(), name="search"),
    path("new-wishlist", views.WishlistCreateView.as_view(), name="new-wishlist"),
    path("wishlist/<str:pk>/", views.WishlistView.as_view(), name="wishlist"),
]
