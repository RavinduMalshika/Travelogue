from rest_framework import serializers
from .models import UserProfile, Destination
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    visited_places = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all(), many=True)
    wishlist = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all(), many=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'image', 'location', 'visited_places', 'wishlist']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_url(obj.image.url)
        return None