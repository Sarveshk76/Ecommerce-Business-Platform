# Generated by Django 4.2.8 on 2024-01-02 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='new_arrival',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='recently_viewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='todays_offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_category', to='inventory.subcategory'),
        ),
    ]
