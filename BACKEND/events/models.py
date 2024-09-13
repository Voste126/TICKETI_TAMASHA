import uuid
from django.db import models

# events model
class Event(models.Model):
    event_id =  models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True,max_length=1000)
    tickets_available = models.IntegerField()
    organizer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title