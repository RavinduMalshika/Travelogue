from django.db import models
from django.contrib.auth.models import User
from destinations.models import Destination

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics', blank=True, null=True)
    location = models.CharField(max_length=100)
    visited_places = models.ManyToManyField(Destination, related_name='visited_by')
    wishlist = models.ManyToManyField(Destination, related_name='wished_by')