from rest_framework import serializers
from .models import *
from accounts.models import User

class SongSerializer(serializers.ModelSerializer):
    featured_artist = serializers.SlugRelatedField(
        queryset=User.objects.filter(is_artist=True),
        slug_field='username',
        required=False,
        allow_null=True
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            self.fields['album'].queryset = Album.objects.filter(artist=request.user)

    
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['artist']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'   
        read_only_fields = ['artist']   

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'  
        read_only_fields = ['user']   
