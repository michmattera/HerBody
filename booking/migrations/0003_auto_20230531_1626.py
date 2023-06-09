# Generated by Django 3.2.18 on 2023-05-31 16:26

import booking.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230523_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today, validators=[booking.models.Booking.Date_validation]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.IntegerField(choices=[(9, '9:00 - 10:00 AM'), (10, '10:00 - 11:00 AM'), (12, '12:30 PM - 13:30 PM'), (16, '16:30 PM - 17:30 PM'), (18, '18:30 PM - 19:30 PM'), (20, '20:30 PM - 21:30 PM')], default=9),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('date', 'time')},
        ),
    ]
