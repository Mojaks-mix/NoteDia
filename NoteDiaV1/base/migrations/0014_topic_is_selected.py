# Generated by Django 4.2.1 on 2023-06-02 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_topic_majors'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='is_selected',
            field=models.CharField(default='0', max_length=1, null=True),
        ),
    ]