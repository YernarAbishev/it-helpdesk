# Generated by Django 3.1 on 2022-07-15 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=255, verbose_name='Department name')),
                ('cabinetNumber', models.IntegerField(max_length=4, verbose_name='Cabinet number')),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50, verbose_name='First name')),
                ('lastName', models.CharField(max_length=50, verbose_name='Last name')),
                ('phoneNumber', models.CharField(max_length=14, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdeskApp.department', verbose_name='Department')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemDescription', models.TextField(verbose_name='Problem description')),
                ('ticketDate', models.DateTimeField(default=datetime.datetime.now)),
                ('photo', models.ImageField(upload_to='problems', verbose_name='Photo')),
                ('isActive', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdeskApp.employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
