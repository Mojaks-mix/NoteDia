# Generated by Django 4.2.1 on 2023-05-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_room_media_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='media_file',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
