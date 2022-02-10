# Generated by Django 4.0.1 on 2022-02-10 17:09

import datetime
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
            name='Artwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('art', models.URLField(blank=True, null=True)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('creator', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
