from django.urls import path
from .views import *

urlpatterns = [
    path('upload-song/', UploadSongView.as_view()),
    path('view-all-songs/', ViewAllSongsView.as_view()),
    path('search-songs/', SearchSongView.as_view()),
    path('upload-album/', UploadAlbumView.as_view()),
    path('create-playlist/', CreatePlaylistView.as_view()),
    path('add-to-playlist/', AddSongToPlaylistView.as_view()),
]
