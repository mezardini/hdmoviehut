# Generated by Django 4.0.4 on 2022-06-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_genre_industry_remove_movie_tag_movie_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(null=True, to='base.genre'),
        ),
    ]
