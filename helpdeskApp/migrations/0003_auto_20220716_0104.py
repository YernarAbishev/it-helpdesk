# Generated by Django 3.1 on 2022-07-15 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskApp', '0002_auto_20220716_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='phoneNumber',
        ),
    ]
