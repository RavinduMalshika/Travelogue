from rest_framework import serializers 
from .models import Map, Destination

class MapSerializer(serializers.ModelSerializer):
    destination = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all())

    class Meta:
        model = Map
        fields = ['id', 'destination', 'url', 'name']

    