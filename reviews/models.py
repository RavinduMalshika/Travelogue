from django.db import models
from users.models import UserProfile
from destinations.models import Destination

class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()