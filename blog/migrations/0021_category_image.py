# Generated by Django 5.0.3 on 2024-03-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_performance_performer_remove_post_musician_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='Chick_Corea.jpg', upload_to=''),
        ),
    ]