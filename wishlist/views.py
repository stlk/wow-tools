import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic

from .models import Wishlist, WishlistItem


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "wishlist/index.html"
    model = Wishlist


class WishlistCreateView(LoginRequiredMixin, generic.CreateView):
    model = Wishlist
    fields = ["name"]

    def get_success_url(self):
        return reverse("wishlist:wishlist", args=(self.object.hashid,))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WishlistView(generic.CreateView):
    template_name = "wishlist/wishlist.html"
    model = WishlistItem
    fields = ["name", "item", "upgrade_level"]

    def get_success_url(self):
        return reverse("wishlist:wishlist", args=(self.object.wishlist.hashid,))

    def get(self, request, pk):
        wishlist = get_object_or_404(Wishlist, hashid=pk)

        return render(
            request,
            self.template_name,
            {"wishlist": wishlist, "items": wishlist.wishlistitem_set.all()},
        )

    def form_valid(self, form):
        wishlist = get_object_or_404(self.request.user.wishlist_set, hashid=self.kwargs["pk"])
        form.instance.wishlist_id = wishlist.id
        return super().form_valid(form)


class SearchView(generic.View):
    template_name = "wishlist/search.html"

    def get(self, request):
        query = request.GET.get("q")
        data = requests.get(f"https://classic.wowhead.com/search/suggestions-template?q={query}").json()

        return render(
            request,
            self.template_name,
            {"data": [item for item in data["results"] if item["typeName"] == "Item" and item["quality"] >= 3]},
        )
