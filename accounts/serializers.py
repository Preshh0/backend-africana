from .models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    
    email_address = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only = True, validators=[validate_password],)
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name', 
            'username', 
            'email_address', 
            'password', 
            'password2'
        )

        extra_kwargs = {
            'password':{'write_only': True}
        }

    def validate(self, attrs):
        if attrs ['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email_address = validated_data['email_address'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username","email_address"]