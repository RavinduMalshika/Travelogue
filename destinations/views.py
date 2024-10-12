from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import AllowAny

class DestinationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        location = request.query_params.get('location')
        keyword = request.query_params.get('keyword')
        rating = request.query_params.get('rating')

        destinations = Destination.objects.all()

        if location:
            destinations = destinations.filter(location=location)

        if keyword:
            destinations = destinations.filter(name__icontains=keyword)

        if rating:
            destinations = destinations.filter(rating__gte=rating)

        serializer = DestinationSerializer(destinations, many=True, context={'request': request})
        return Response(serializer.data)

def home(request):
    return render(request, 'index.html')