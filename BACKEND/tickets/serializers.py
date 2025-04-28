from .models import Ticket
from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'event',
            'user',
            'purchase_timestamp',
            'price_paid',
            'qr_code',
            'payment_status',
            'payment_method'
        ]

class TicketPurchasePayloadSerializer(serializers.Serializer):
    event_id = serializers.IntegerField(help_text="The ID of the event to purchase a ticket for.")

class TicketPurchaseResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'qr_code']

class StripePaymentPayloadSerializer(serializers.Serializer):
    event_id = serializers.IntegerField(help_text="The ID of the event for which the Stripe payment is being simulated.")

class StripePaymentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'qr_code']

class MPESAPaymentPayloadSerializer(serializers.Serializer):
    event_id = serializers.IntegerField(help_text="The ID of the event for which the MPESA payment is being simulated.")

class MPESAPaymentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'qr_code']