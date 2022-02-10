from django.urls import path
from .views import UserCreate
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import ( #this line works despite the yellow squiggly lines
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('register/', UserCreate.as_view(), name='user_create'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]