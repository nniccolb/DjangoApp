# Generated by Django 2.1.3 on 2019-02-18 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_userprofile_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='highscore',
        ),
        migrations.AddField(
            model_name='score',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AddField(
            model_name='score',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.UserProfile'),
        ),
    ]
