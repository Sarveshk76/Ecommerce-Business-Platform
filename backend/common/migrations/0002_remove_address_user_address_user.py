# Generated by Django 4.2.7 on 2023-11-24 16:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ManyToManyField(related_name='address', to=settings.AUTH_USER_MODEL),
        ),
    ]
