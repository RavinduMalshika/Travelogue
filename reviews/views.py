from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

class ReviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        print("called")
        try:
            destination = request.query_params.get('destination')
            print(destination)

            reviews = Review.objects.filter(destination=destination)
            print(reviews)
            serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error when retrieving reviews: ", e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)