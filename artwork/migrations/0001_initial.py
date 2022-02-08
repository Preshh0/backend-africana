# Generated by Django 4.0.1 on 2022-02-08 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
                ('creator', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
