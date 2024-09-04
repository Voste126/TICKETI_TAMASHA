from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from .models import Attendee

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ["email", "username", "password"]

    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50, write_only=True)

    def validate(self, attrs):
        email_exists = Attendee.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)

def create(self, validated_data):
    attendee = Attendee.objects.create_user(
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password']
    )
    attendee.set_password(validated_data['password'])
    attendee.save()
    
    token = Token.objects.create(user=attendee)
    return attendee
