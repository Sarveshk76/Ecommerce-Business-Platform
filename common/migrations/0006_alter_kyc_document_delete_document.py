# Generated by Django 4.2.5 on 2023-09-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_remove_document_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='document',
            field=models.FileField(upload_to='documents/'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
