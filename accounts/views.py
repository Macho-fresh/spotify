from django.shortcuts import render
from .models import User
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        serializer = RegisterSerializer(data=request.data)

        try:
            user = User.objects.create_user(
                username = serializer.validated_data['username'],
                email = serializer.validated_data['email'],
                password = serializer.validated_data['password']
            )

        except user.exists():
            return Response({
                'error': 'User already exists'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        serializer = LoginSerializer(data=request.data)
        
        username = serializer.validated_data['username'],
        password = serializer.validated_data['password']

        try:
            user = authenticate(request, username=username, password=password)
        except user is None:
            return Response({
                'error': 'user does not exist'
            })
        
        login(request, user)

        
            