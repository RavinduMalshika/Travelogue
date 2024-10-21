from django.db import models
from destinations.models import Destination

class Map(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    url = models.TextField()
    name = models.CharField(max_length=200)
