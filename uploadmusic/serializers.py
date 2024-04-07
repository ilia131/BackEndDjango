from rest_framework import serializers
from .models import Uploadmusic , Video









class UploadmusicSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    track = serializers.FileField(use_url=True)
    

    class Meta:
        model = Uploadmusic
        fields = (
            "id",
            "title",
            "description",
            "tracks",
            "track",
            "image",
            "get_image",
            "genre",
            "key",
            "slug",
            "lyrics",
            "get_absolute_url",
            "adamid"
        )
        

class VideoSerializer(serializers.ModelSerializer):
    video = serializers.FileField(use_url=True)
    image = serializers.ImageField(use_url= True)

    class Meta:
        model = Video
        fields = (
            "video",
            'videos',
            'image',
            'images', 
        )
