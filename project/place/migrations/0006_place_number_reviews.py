# Generated by Django 5.0.1 on 2024-01-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_alter_image_id_place_alter_place_id_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='number_reviews',
            field=models.IntegerField(default=0),
        ),
    ]
