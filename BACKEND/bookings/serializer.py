from rest_framework import serializers
from bookings.models import Bookings
from events.models import Event
from tickets.models import Ticket
from attendees.models import Attendee

# Serializer for the Bookings model
class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['booking_id', 'event_id', 'ticket_id', 'attendee_id', 'quantity', 'created_at', 'updated_at']
    
    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be greater than 0")
        return value

    booking_id = serializers.UUIDField(read_only=True)
    event_id = serializers.UUIDField()
    ticket_id = serializers.UUIDField()
    attendee_id = serializers.UUIDField()
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    def create(self, validated_data):
        # Convert UUIDs to actual model instances
        event = Event.objects.get(pk=validated_data.pop('event_id'))
        ticket = Ticket.objects.get(pk=validated_data.pop('ticket_id'))
        attendee = Attendee.objects.get(pk=validated_data.pop('attendee_id'))

        booking = Bookings.objects.create(
            event_id=event,
            ticket_id=ticket,
            attendee_id=attendee,
            **validated_data
        )
        return booking
    
    def update(self, instance, validated_data):
        if 'event_id' in validated_data:
            instance.event_id = Event.objects.get(pk=validated_data.get('event_id'))
        if 'ticket_id' in validated_data:
            instance.ticket_id = Ticket.objects.get(pk=validated_data.get('ticket_id'))
        if 'attendee_id' in validated_data:
            instance.attendee_id = Attendee.objects.get(pk=validated_data.get('attendee_id'))

        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
