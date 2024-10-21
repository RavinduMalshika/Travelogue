from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Destination, DestinationImage
from .serializers import DestinationSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from reviews.models import Review
from users.models import User, UserProfile
from maps.models import Map

class DestinationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        id = request.query_params.get('id')
        location = request.query_params.get('location')
        keyword = request.query_params.get('keyword')
        rating = request.query_params.get('rating')

        print(id)

        if id:
            destination = Destination.objects.get(id=id)
            serializer = DestinationSerializer(destination, context={'request': request})
            return Response(serializer.data)
        
        destinations = Destination.objects.all()
        
        if location:
            destinations = destinations.filter(location=location)

        if keyword:
            destinations = destinations.filter(name__icontains=keyword)

        if rating:
            destinations = destinations.filter(rating__gte=rating)

        serializer = DestinationSerializer(destinations, many=True, context={'request': request})
        return Response(serializer.data)

@api_view(['POST'])
def create(request):
    try:
        user = request.data.get('user')
        name = request.data.get('name')
        country = request.data.get('country')
        map_url = request.data.get('map')
        destination_type = request.data.get('destination_type')
        description = request.data.get('description')
        cost = request.data.get('cost')
        images = request.FILES.getlist('images')
        rating = request.data.get('rating')
        review = request.data.get('review')

        start_index = map_url.find('place/') + 6
        end_index = map_url[start_index:len(map_url)].find('/') + start_index
        map_name = map_url[start_index: end_index]
 
        destination = Destination.objects.create(
            name = name,
            destination_type = destination_type,
            description = description,
            rating = rating,
            cost = cost,
            location = country,
            is_approved = False,
            is_reported = False
        )

        print("Destination created")

        destination.save()

        print("Destination saved")
        
        for image in images:
            destination_image = DestinationImage.objects.create(
                destination = destination,
                image = image
            )

            destination_image.save()

        user_review = User.objects.get(id=user)
        user_profile = UserProfile.objects.get(user=user_review)

        dest_review = Review.objects.create(
            user = user_profile,
            username = user_review.username,
            destination = destination,
            review_text = review,
            rating = rating
        )

        dest_review.save()

        print("review saved")

        print(map_url, map_name, type(map_url), type(map_name), type(destination))
        print(len(map_url))

        dest_map = Map.objects.create(
            destination = destination,
            url = map_url,
            name = map_name
        )

        print("map created")
        
        dest_map.save()

        print("map created")
        
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)