from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

class Album(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name='songs')
    featured_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='featured_songs')
    title = models.CharField(max_length=150)
    cover_image = models.ImageField(upload_to='media/')
    audio = models.FileField(
        upload_to = 'audio/',
        validators = [FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])]
    )

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='songs',
        null=True
    )

    GENRE = [
        ('Afrobeats', 'Afrobeats'),
        ('Pop', 'Pop'),
        ('Hip-pop', 'Hip-pop'),
        ('Rap', 'Rap'),
        ('RnB', 'RnB'),
        ('Jazz', 'Jazz'),
        ('Country', 'Country'),
        ('Raggae', 'Raggae')
    ]

    genre = models.CharField(choices=GENRE, default='Pop')

    def __str__(self):
        return self.title



class Playlist(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ForeignKey(Song, on_delete=models.CASCADE)
