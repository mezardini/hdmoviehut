# Generated by Django 4.1.5 on 2023-03-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_movie_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_year',
            field=models.CharField(max_length=200),
        ),
    ]
