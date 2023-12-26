# Generated by Django 4.1.7 on 2023-06-03 00:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_user_topic_alter_topic_is_selected'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='topic',
        ),
        migrations.CreateModel(
            name='UserTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='topic',
            field=models.ManyToManyField(null=True, through='base.UserTopic', to='base.topic'),
        ),
    ]
