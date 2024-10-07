from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.permissions import AllowAny

class DestinationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True, context={'request': request})
        return Response(serializer.data)

def home(request):
    return render(request, 'index.html')