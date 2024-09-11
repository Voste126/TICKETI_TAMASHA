from django.db import models
from bookings.models import Bookings
import uuid

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('CC', 'CREDIT CARD'),
        ('DC', 'DEBIT CARD'),
        ('MP', 'MPESA'),
        ('MC', 'MASTERCARD'),
    ]

    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking_id = models.OneToOneField(Bookings, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, default='MP')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.payment_id)  # Correctly convert UUID to string
  # Convert the UUID to a string

