# Generated by Django 2.1.3 on 2019-02-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_game_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='games',
            field=models.ManyToManyField(to='games.Game'),
        ),
    ]
