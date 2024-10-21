from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    destination_type = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.FloatField(default=0.0)
    cost = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)

class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='destinations')