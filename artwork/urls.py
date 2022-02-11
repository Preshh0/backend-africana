from django.urls import path
from .views import ArtworkList, ArtworkDetail, CategoryList


urlpatterns = [
    path('', ArtworkList.as_view(), name="artList" ),
    path('<int:pk>/', ArtworkDetail.as_view(), name="artwork"),
    path('category/', CategoryList.as_view(), name='category'),

]