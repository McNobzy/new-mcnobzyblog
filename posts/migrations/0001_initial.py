# Generated by Django 4.0.4 on 2022-07-11 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100000)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=10000)),
                ('posted_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]