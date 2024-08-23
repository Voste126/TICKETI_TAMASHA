from rest_framework import serializers
from .models import Payment
from bookings.models import Bookings

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'booking_id', 'amount', 'payment_method', 'created_at', 'updated_at']
    
    payment_id = serializers.UUIDField(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(queryset=Bookings.objects.all())  # Use PrimaryKeyRelatedField
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_method = serializers.ChoiceField(choices=Payment.PAYMENT_METHOD_CHOICES)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    def create(self, validated_data):
        booking = validated_data.pop('booking_id')
        
        if Payment.objects.filter(booking_id=booking).exists():
            raise serializers.ValidationError("A payment already exists for this booking.")
        
        return Payment.objects.create(booking_id=booking, **validated_data)
