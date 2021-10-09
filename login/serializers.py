# from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = UserProfile.objects.all()
        extra_kwargs = {
            "password":{"write_only":True}
        }
