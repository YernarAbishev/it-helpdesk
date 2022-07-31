# Generated by Django 3.1 on 2022-07-15 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdeskApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='employee',
        ),
        migrations.AddField(
            model_name='ticket',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='helpdeskApp.department', verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='phoneNumber',
            field=models.CharField(default='', max_length=14, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Employee'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]