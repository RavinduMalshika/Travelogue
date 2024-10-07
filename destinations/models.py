from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    destination_type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)
    cost = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

