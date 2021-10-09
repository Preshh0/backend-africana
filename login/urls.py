from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import UserCreateAPIView

# router = DefaultRouter()
# router.register(r'AddPictures', views.AddPicturesView)

urlpatterns = [
    path('users/', UserCreateAPIView.as_view(), name="register"),
    
]