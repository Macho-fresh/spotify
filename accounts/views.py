from django.shortcuts import render
from .models import User
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        if User.objects.filter(username=username).exists():
            return Response({
                'error': 'User already exists'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password
        )

        return Response ({
            'message': f'Welcome {user.username}'
        })

        

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return Response(
                {'error': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        login(request, user)
        return Response ({
            'message': 'login successful'
        }, status=status.HTTP_200_OK)
       