# Generated by Django 5.1 on 2024-08-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.AddField(
            model_name='event',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
