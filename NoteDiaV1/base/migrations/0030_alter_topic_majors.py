# Generated by Django 4.1.5 on 2023-06-06 01:56

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_user_major_alter_user_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='majors',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Computer Science', 'Computer Science'), ('Computer Information Systems', 'Computer Information Systems'), ('Bussiness Information Technology', 'Bussiness Information Technology'), ('Artifical Intelligence', 'Artifical Intelligence'), ('Data Science', 'Data Science'), ('CyberSecurity', 'CyberSecurity'), ('Computer Engineering', 'Computer Engineering'), ('Software Engineering', 'Software Engineering')], max_length=200, null=True),
        ),
    ]