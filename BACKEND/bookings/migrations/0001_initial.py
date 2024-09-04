# Generated by Django 5.1 on 2024-09-04 20:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attendees', '0001_initial'),
        ('events', '__first__'),
        ('tickets', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendees.attendee')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]
