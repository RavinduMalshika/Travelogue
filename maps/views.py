from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Map
from .serializers import MapSerializer
from destinations.models import Destination

class MapView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        try:
            destination = request.query_params.get('destination')
            destination = Destination.objects.get(id=destination)
            
            map = Map.objects.get(destination=destination)
            serializer = MapSerializer(map, many=False, context={'request': request})
        
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print("Error when retrieving map: ", e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)