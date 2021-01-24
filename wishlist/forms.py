from django.forms import inlineformset_factory

from .models import Wishlist, WishlistItem

WishListFormSet = inlineformset_factory(
    Wishlist,
    WishlistItem,
    fields=("name",),
)
