# Generated by Django 5.1 on 2024-09-08 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='ticket_id',
            new_name='ticket',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='user_id',
            new_name='user',
        ),
    ]
