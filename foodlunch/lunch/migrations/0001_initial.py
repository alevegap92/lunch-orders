# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 15:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('to_update', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(blank=True, upload_to='foodtype')),
                ('price', models.IntegerField(default=0)),
                ('foodselect', models.CharField(choices=[('m', 'MainDich'), ('s', 'Salad'), ('d', 'Desert')], default='m', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('menutime', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('to_update', models.DateTimeField(auto_now=True)),
                ('menu', models.ManyToManyField(to='lunch.FoodType')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('delivery', models.BooleanField(default=True)),
                ('ordertime', models.TimeField()),
                ('orderdate', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch.Menu')),
            ],
        ),
    ]
