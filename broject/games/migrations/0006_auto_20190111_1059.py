# Generated by Django 2.1.3 on 2019-01-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
