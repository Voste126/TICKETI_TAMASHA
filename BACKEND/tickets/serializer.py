from rest_framework import serializers
from tickets.models import Ticket

#serializer for the ticket model

class TicketSerializer(serializers.ModelSerializer):
    ticket_type = serializers.CharField(max_length=100)
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Ticket
        fields = ['ticket_id', 'event_id', 'ticket_type', 'price', 'quantity', 'created_at', 'updated_at']