from django.db import models
from events.models import Event
from django.core.validators import MinValueValidator
import uuid
from django.core.exceptions import ValidationError

class Ticket(models.Model):
    TICKET_CHOICES = [
        ('EARLY_BIRD', 'Early Bird'),
        ('REGULAR', 'Regular'),
        ('VIP', 'VIP'),
        ('VVIP', 'VVIP'),
        ('EXECUTIVE', 'Executive'),
    ]
    
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=100, choices=TICKET_CHOICES, default='REGULAR')
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        try:
            uuid.UUID(str(self.ticket_id))
        except ValueError:
            raise ValidationError('Invalid UUID format for ticket_id')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.ticket_type
