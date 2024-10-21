from rest_framework import serializers
from .models import Review, UserProfile, Destination
from users.serializers import UserProfileSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()
    destination = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all())

    class Meta:
        model = Review
        fields = ['user_profile', 'destination', 'review_text', 'rating']