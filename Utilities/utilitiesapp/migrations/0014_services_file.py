# Generated by Django 5.0.3 on 2024-03-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilitiesapp', '0013_services_created_at_services_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
