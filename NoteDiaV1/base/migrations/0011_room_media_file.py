# Generated by Django 4.1.7 on 2023-05-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_room_media_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='media_file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
