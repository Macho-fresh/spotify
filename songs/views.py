from django.shortcuts import render
from rest_framework.permissions import BasePermission, IsAuthenticated
from accounts.models import User
from rest_framework import generics, status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class IsArtist(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
class UploadSongView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsArtist]
    queryset = Song.objects.all()

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)

class ViewAllSongsView(generics.ListAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    queryset=Song.objects.all()

    # def get(self, request):
    #     songs = Song.objects.all()
    #     # return Response({
    #     #     'songs': songs
    #     # })
    #     for i in songs:
    #         return Response({
    #             'artist': i.artist,
    #             'title': i.title,
    #             'cover_image': i.cover_image,
    #             'audio': i.audio
    #         })

class SearchSongView(generics.ListAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    queryset=Song.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]

    # filterset_fields = ['genre', 'rating']
    search_fields = ['title', 'genre']

class UploadAlbumView(generics.ListCreateAPIView):    
    serializer_class = AlbumSerializer
    permission_classes = [IsArtist]
    queryset = Album.objects.all()

    def perform_create(self, serializer):
        serializer.save(artist=self.request.user)

class CreatePlaylistView(generics.ListCreateAPIView):    
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
    queryset = Playlist.objects.all()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AddSongToPlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        song_id = int(request.query_params.get('song_id'))
        playlist_id = int(request.query_params.get('playlist_id'))

        playlist = Playlist.objects.get(id=playlist_id)
        song = Song.objects.get(id=song_id)
        playlist.objects.create(
            title = playlist.title,
            user = request.user,
            songs = song
        )

        return Response({
            'message': f'{song} added to {playlist}'
        }, status=status.HTTP_201_CREATED)