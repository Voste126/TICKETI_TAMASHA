from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers

# Attendees model
class Attendee(models.Model):
    attendee_id =  models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField(region='KE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

