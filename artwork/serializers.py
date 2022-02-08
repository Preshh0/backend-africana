from turtle import title
from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artwork
        fields = ['id', 'title', 'description', 'creator', 'created_at']

