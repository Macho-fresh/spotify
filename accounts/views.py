from django.shortcuts import render
from .models import User
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        serializer = RegisterSerializer(data=request.data)

        try:
            user = User.objects.create_user(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )

        except user.exists():
            return Response({
                'error': 'User already exists'
            }, status=status.HTTP_401_UNAUTHORIZED)