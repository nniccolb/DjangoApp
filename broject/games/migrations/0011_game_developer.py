# Generated by Django 2.1.3 on 2019-02-01 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_auto_20190123_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='games.UserProfile'),
            preserve_default=False,
        ),
    ]
