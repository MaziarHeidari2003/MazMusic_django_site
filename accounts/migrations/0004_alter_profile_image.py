# Generated by Django 5.0.3 on 2024-03-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_bio_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default_profile', null=True, upload_to=''),
        ),
    ]
