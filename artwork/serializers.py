from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):

    # creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'art', 'description', 'creator', 'created_at']

