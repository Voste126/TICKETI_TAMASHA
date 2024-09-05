from django.db import models
from events.models import Event
from accounts.models import User
from tickets.models import Ticket
import uuid
# Create your models here.
# Boookings model 

class Bookings(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.booking_id