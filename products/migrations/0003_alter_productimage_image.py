# Generated by Django 5.0.4 on 2024-04-29 12:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productimage_alt_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='product_images'),
        ),
    ]
