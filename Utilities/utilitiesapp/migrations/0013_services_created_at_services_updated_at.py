# Generated by Django 5.0.3 on 2024-03-19 17:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilitiesapp', '0012_remove_services_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
