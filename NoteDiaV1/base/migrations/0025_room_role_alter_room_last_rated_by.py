# Generated by Django 4.1.5 on 2023-06-04 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_alter_room_options_room_last_rated_by_room_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='role',
            field=models.CharField(default='0', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='last_rated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_rated_room', to=settings.AUTH_USER_MODEL),
        ),
    ]
