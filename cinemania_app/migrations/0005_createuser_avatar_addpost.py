# Generated by Django 4.0.6 on 2022-07-26 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemania_app', '0004_remove_createuser_avatar_remove_createuser_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='createuser',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='profiles'),
        ),
        migrations.CreateModel(
            name='AddPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('release_date', models.DateField()),
                ('main_actors', models.TextField()),
                ('genre', models.TextField()),
                ('description', models.TextField()),
                ('poster', models.ImageField(default='poster.png', upload_to='posters')),
                ('movie_trailer', models.CharField(max_length=250)),
                ('posted_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemania_app.createuser')),
            ],
        ),
    ]