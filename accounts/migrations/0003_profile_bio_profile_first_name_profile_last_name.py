# Generated by Django 5.0.3 on 2024-03-26 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_profile_picture_profile_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='someone', max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='someone', max_length=120),
        ),
    ]
