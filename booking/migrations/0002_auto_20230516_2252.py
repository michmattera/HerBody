# Generated by Django 3.2.18 on 2023-05-16 22:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='days_of_week',
            field=models.IntegerField(choices=[(0, 'Tuesday'), (1, 'Wednesday'), (2, 'Thursday'), (3, 'Friday'), (4, 'Saturday'), (5, 'Sunday')], default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(0, 'Available'), (1, 'Unavailable')], default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.IntegerField(choices=[('9', '9:00 - 10:00 AM'), ('11', '11:00 - 12:00 AM'), ('16', '16:30 PM - 17:30 PM')], default=9),
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(0, 'Tuesday'), (1, 'Wednesday'), (2, 'Thursday'), (3, 'Friday'), (4, 'Saturday'), (5, 'Sunday')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weekday', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('time', models.IntegerField(choices=[('9', '9:00 - 10:00 AM'), ('11', '11:00 - 12:00 AM'), ('16', '16:30 PM - 17:30 PM')], default=9)),
                ('weekday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_hour', to='booking.weekday')),
            ],
        ),
    ]