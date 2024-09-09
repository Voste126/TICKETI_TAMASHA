from rest_framework import serializers
from bookings.models import Bookings
from events.models import Event
from tickets.models import Ticket
from accounts.models import User
from rest_framework import serializers
from .models import Bookings, Event, Ticket, User

class BookingsSerializer(serializers.ModelSerializer):
    booking_id = serializers.UUIDField(read_only=True)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Bookings
        fields = ['booking_id', 'event', 'ticket', 'user', 'quantity', 'created_at', 'updated_at']

