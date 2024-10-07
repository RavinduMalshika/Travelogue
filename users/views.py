import re
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User, auth
from .models import UserProfile
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer

class UserProfileView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(UserProfile.objects.filter(user=user).first(), context={'request': request})
        print(serializer.data['visited_places'])
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'image': serializer.data['image'],
            'visited_places': serializer.data['visited_places'],
        }
        return Response(user_data, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')
    image = request.FILES.get('image')

    print(username, first_name, last_name, email, password, confirm_password, image)

    if validate_password(password):
        return Response({"error": "password"}, status=status.HTTP_401_UNAUTHORIZED)
    
    elif password != confirm_password: 
        return Response({"error": "confirmPassword"}, status=status.HTTP_401_UNAUTHORIZED)
    
    elif User.objects.filter(email=email).exists():
        return Response({"error": "email"}, status=status.HTTP_401_UNAUTHORIZED)
    
    elif User.objects.filter(username=username).exists():
        return Response({"error": "username"}, status=status.HTTP_401_UNAUTHORIZED)
   
    else:
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password, 
            first_name=first_name, 
            last_name=last_name, 
            is_staff=False
            )
        
        try:
        
            user_profile = UserProfile.objects.create(
                user = user,
                image=image,
            )

            user_profile.save()

            refresh = RefreshToken.for_user(user)

        except:
            print("Error creating user")
            user.delete()

        return Response({
                "message": "Registration Successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
    
#Password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, one number, and one special character.

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        # Check what data is being received
        print("Request Data: ", request.data)

        username = request.data.get('username')
        password = request.data.get('password')

        print("Username: ", username)
        print("Password: ", password)

        # Authenticate the user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            #Generate JWT token for the user
            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Login Successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Login Failed"}, status=status.HTTP_400_BAD_REQUEST)

        
    else:
        print("Not POST")
        return Response({"message": "Login Failed"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data.get('refresh_token')
        print(refresh_token)

        # Create a RefreshToken instance using the provided refresh token
        token = RefreshToken(refresh_token)
        print(token)

        # Blacklist the token, making it invalid for future use
        token.blacklist()

        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
def validate_password(password):
    pattern = r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$'

    if not re.match(pattern, password):
        return True
    else:
        return False

