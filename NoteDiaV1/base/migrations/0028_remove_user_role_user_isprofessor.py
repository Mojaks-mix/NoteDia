# Generated by Django 4.1.5 on 2023-06-06 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_delete_defaulttopics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='isProfessor',
            field=models.BooleanField(default=False),
        ),
    ]
