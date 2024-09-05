from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import User

# Serializer for the User model
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)

    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)
        return user