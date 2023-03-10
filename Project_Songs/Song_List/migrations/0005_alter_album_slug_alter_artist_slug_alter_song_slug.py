# Generated by Django 4.1.7 on 2023-03-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Song_List', '0004_alter_album_slug_alter_artist_slug_alter_song_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100), max_length=100),
        ),
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100), max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100), max_length=100),
        ),
    ]
