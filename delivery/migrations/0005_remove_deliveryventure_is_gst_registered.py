# Generated by Django 4.2.5 on 2023-09-27 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_deliveryventure_user_delete_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryventure',
            name='is_gst_registered',
        ),
    ]
