# Generated by Django 4.0.6 on 2022-07-30 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemania_app', '0007_alter_addpost_movie_trailer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('message', models.TextField()),
                ('user_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemania_app.createuser')),
            ],
        ),
    ]
