# Generated by Django 3.2.19 on 2023-07-14 17:05

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
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('date', 'time')},
        ),
    ]
