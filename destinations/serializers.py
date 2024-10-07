from rest_framework import serializers 
from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id', 'name', 'image', 'destination_type', 'description', 'rating', 'cost', 'location']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_url(obj.image.url)
        return None