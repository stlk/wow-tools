from django.contrib.auth.models import User
from django.db import models
from django_hashids import HashidsField


class Wishlist(models.Model):
    hashid = HashidsField(real_field_name="id")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    item = models.IntegerField()

    class UpgradeLevel(models.TextChoices):
        MAJOR = "major", "Major"
        MINOR = "minor", "Minor"

    upgrade_level = models.CharField(
        max_length=50,
        choices=UpgradeLevel.choices,
    )
