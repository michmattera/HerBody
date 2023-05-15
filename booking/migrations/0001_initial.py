# Generated by Django 3.2.18 on 2023-05-15 20:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('time', models.IntegerField(choices=[('9:00 - 10:00 AM', '9:00 - 10:00 AM'), ('11:00 - 12:00 AM', '11:00 - 12:00 AM'), ('16:30 PM - 17:30 PM', '16:30 PM - 17:30 PM')], max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date', 'time'],
            },
        ),
    ]
