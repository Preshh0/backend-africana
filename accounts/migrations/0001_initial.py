# Generated by Django 3.2.6 on 2022-02-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('username', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]