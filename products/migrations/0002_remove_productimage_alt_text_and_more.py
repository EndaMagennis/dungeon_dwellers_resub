# Generated by Django 5.0.4 on 2024-04-17 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='alt_text',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='image_url',
        ),
    ]
