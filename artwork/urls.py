from django.urls import path
from .views import ArtworkList, ArtworkDetail


urlpatterns = [
    path('', ArtworkList.as_view(), name="artList" ),
    path('<int:pk>/', ArtworkDetail.as_view(), name="artwork"),
]