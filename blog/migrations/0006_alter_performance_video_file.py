# Generated by Django 5.0.3 on 2024-03-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_track_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='video_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]