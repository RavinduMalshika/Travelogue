from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    contact_num = models.IntegerField(default=None)
    visited_places = models.ManyToManyField(Destination)