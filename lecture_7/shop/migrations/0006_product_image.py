# Generated by Django 5.1.5 on 2025-02-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_category_options_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
