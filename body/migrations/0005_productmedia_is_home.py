# Generated by Django 5.0.4 on 2024-05-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0004_productmedia_remove_product_photos_or_videos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmedia',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]
