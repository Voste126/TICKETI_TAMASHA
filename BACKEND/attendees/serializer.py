from rest_framework import serializers
from attendees.models import Attendee

# Serializer for the Attendee model
class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['attendee_id', 'name', 'email', 'phone', 'created_at', 'updated_at']

    
    def validate_email(self, value):
        # Ensure the email is in the correct format (though this is already handled by EmailField)
        if '@' not in value:
            raise serializers.ValidationError("Email must be in the correct format")
        return value

    
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=12)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)


