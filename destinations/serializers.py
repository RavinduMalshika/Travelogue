from rest_framework import serializers 
from .models import Destination, DestinationImage

class DestinationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = ['id', 'image']

    def get_images(self, obj):
        request = self.context.get('request')
        images = obj.images.all()
        return [request.build_absolute_uri(image.image.url) for image in images if image.image and request]

class DestinationSerializer(serializers.ModelSerializer):
    images = DestinationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'images', 'destination_type', 'description', 'rating', 'cost', 'location', 'is_approved', 'is_reported']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_url(obj.image.url)
        return None
    
