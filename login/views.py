from django.shortcuts import render
from .serializers import UserCreateSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, views, status
# from django.contrib.auth import get_user_model
from .models import UserProfile
from rest_framework import filters
# Create your views here.


class UserCreateAPIView(views.APIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
    def post(self, request, format=None):
        print(request.data)
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            # serializers.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        