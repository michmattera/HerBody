# Generated by Django 3.2.18 on 2023-05-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230516_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='days_of_week',
            field=models.IntegerField(choices=[(0, 'Tuesday'), (1, 'Wednesday'), (2, 'Thursday'), (3, 'Friday'), (4, 'Saturday'), (5, 'Sunday')], default=0),
        ),
    ]
