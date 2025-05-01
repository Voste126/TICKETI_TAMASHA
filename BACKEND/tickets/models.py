# This file defines the Ticket model, which includes fields for event, user, price paid, and payment status.

from django.db import models
from django.conf import settings
from events.models import Event
import uuid

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    purchase_timestamp = models.DateTimeField(auto_now_add=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    payment_method = models.CharField(max_length=20, choices=[('stripe', 'Stripe'), ('mpesa', 'MPESA')], blank=True, null=True)

    def __str__(self):
        return f'Ticket {self.id} for {self.event.title}'
