# Generated by Django 4.0.6 on 2022-07-29 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemania_app', '0005_createuser_avatar_addpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addpost',
            old_name='user',
            new_name='user_uuid',
        ),
    ]