# Generated by Django 4.0.4 on 2023-02-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_movie_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('Released', 'Released'), ('Expected', 'Expected')], max_length=10, null=True),
        ),
    ]
