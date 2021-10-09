from django.shortcuts import render
from .serializers import AddPicturesSerializer
from rest_framework.response import Response
from rest_framework import serializers, views, status
from .models import AddPictures
from rest_framework.parsers import MultiPartParser, FormParser

class AddPicturesView(views.APIView):
    '''
    Post pictures
    '''
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, format=None):
        print(request.data)
        serializer = AddPicturesSerializer(data=request.data)

        if serializer.is_valid():
            # serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewAddedPictures(views.APIView):
    '''
    View added images
    '''
    def get(self, request,  format=None):
        pictures = AddPictures.objects.all()
        serializer = AddPicturesSerializer(pictures, many=True)
        return Response(serializer.data)