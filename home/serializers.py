from rest_framework import serializers
from .models import AddPictures


class AddPicturesSerializer(serializers.Serializer):

    class Meta:
        model = AddPictures
        fields = AddPictures.objects.all()

