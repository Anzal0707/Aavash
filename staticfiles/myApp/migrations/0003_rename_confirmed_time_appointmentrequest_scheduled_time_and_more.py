# Generated by Django 5.1 on 2025-01-16 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_appointmentrequest_remove_appointment_slot_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentrequest',
            old_name='confirmed_time',
            new_name='scheduled_time',
        ),
        migrations.RemoveField(
            model_name='appointmentrequest',
            name='doctor',
        ),
    ]