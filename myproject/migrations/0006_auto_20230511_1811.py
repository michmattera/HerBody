# Generated by Django 3.2.18 on 2023-05-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='client',
        ),
    ]
