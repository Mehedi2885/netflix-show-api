from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from rest_framework import exceptions
from django.contrib.auth.models import update_last_login


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    password2 = serializers.CharField(style=
                                      {'input_type': 'password'},
                                      write_only=True
                                      )

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password', 'password2')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def save(self, **kwargs):
        """Create and return a new user"""
        user = UserProfile(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password1 and password2 and password2 != password1:
            raise serializers.ValidationError("Password did't match")
        user.set_password(password1)
        user.save()
        return user


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class JWTUserLoginSerializer(serializers.Serializer):
    """Serialize user login"""
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'password', )

    def validate(self, data):
        """Validate user credentials with provide data"""
        username = data.get("username", " ")
        password = data.get("password", " ")
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'username': user.username,
            'token': jwt_token
        }
