# Generated by Django 5.1 on 2025-01-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]
