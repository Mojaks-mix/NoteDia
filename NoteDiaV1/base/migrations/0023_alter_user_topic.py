# Generated by Django 4.2.1 on 2023-06-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_remove_topic_is_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='topic',
            field=models.ManyToManyField(limit_choices_to={'majors': models.CharField(choices=[('Computer Science', 'CS'), ('Computer Information System', 'CIS'), ('Bussiness Information Technology', 'BIT'), ('Artifical Intelligence', 'AI'), ('Data Science', 'Data Science'), ('CyberSecurity', 'CyberSecurity')], max_length=70, null=True)}, through='base.UserTopic', to='base.topic'),
        ),
    ]
