# Generated by Django 2.1.3 on 2019-01-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20190109_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
