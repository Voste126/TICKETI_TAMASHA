from rest_framework import serializers
from events.models import Event

#serializer for the event model

class EventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    date = serializers.DateTimeField()
    location = serializers.CharField(max_length=100)
    tickets_available = serializers.IntegerField()
    organizer = serializers.CharField(max_length=100)
    image_url = serializers.URLField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Event
        fields = ['event_id', 'title', 'description', 'date', 'location', 'image_url', 'created_at', 'updated_at', 'tickets_available', 'organizer']




