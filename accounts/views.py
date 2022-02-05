from rest_framework import generics
from accounts.serializers import UserSerializer

# Create your views here.
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
   