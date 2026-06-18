from django.shortcuts import render
from rest_framework.permissions import BasePermission, IsAuthenticated
from accounts import User
from rest_framework import generics
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class IsArtist(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_artist and request.user.IsAuthenticated
    
class UploadSongView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsArtist]
    queryset = Song.objects.all()

class ViewAllSongsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        songs = Song.objects.all()
        for i in songs:
            return Response({
                'artist': i.artist,
                'title': i.title,
                'cover_image': i.cover_image,
                'audio': i.audio
            })

class SearchSongView(generics.ListAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    # filterset_fields = ['genre', 'rating']
    search_fields = ['title']

class UploadAlbumView(generics.ListCreateAPIView):    
    serializer_class = AlbumSerializer
    permission_classes = [IsArtist]
    queryset = Album.objects.all()

class CreatePlaylistView(generics.ListCreateAPIView):    
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
    queryset = Playlist.objects.all()