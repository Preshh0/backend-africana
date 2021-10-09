from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import AddPicturesView, ViewAddedPictures

# router = DefaultRouter()
# router.register(r'AddPictures', views.AddPicturesView)

urlpatterns = [
    path('add-pictures/', AddPicturesView.as_view(), name="add-pictures"),
    path('view-pictures/', ViewAddedPictures.as_view(), name="view-pictures"),
]