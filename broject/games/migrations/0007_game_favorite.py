# Generated by Django 2.1.3 on 2019-01-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20190111_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
