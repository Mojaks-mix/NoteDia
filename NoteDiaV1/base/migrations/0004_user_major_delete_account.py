# Generated by Django 4.1.7 on 2023-05-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('CIS', 'Computer Information System'), ('BIT', 'Bussiness Information Technology'), ('Artifical Intelligence', 'AI'), ('Data Science', 'Data Science'), ('CyberSecurity', 'CyberSecurity')], default='CS', max_length=70),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]