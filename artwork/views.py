from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Artwork, Category
from .serializers import ArtworkSerializer, CategorySerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ArtworkList(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self, request, format=None):
        artwork = Artwork.objects.all()
        serializer = ArtworkSerializer(artwork, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArtworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["creator"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
class ArtworkDetail(APIView):

    def get_object(self, pk):
        try:
            return Artwork.objects.get(pk=pk)
        except Artwork.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        artwork = self.get_object(pk)
        serializer = ArtworkSerializer(artwork)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        artwork = self.get_object(pk)
        serializer = ArtworkSerializer(artwork, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        artwork = self.get_object(pk)
        artwork.delete()
        message = "This art doesn't exist anymore."
        return Response(status={status.HTTP_204_NO_CONTENT, message})

class CategoryList(APIView):

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["name"] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
