# Generated by Django 5.0.1 on 2024-01-06 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0002_delete_municipal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['id']},
        ),
    ]