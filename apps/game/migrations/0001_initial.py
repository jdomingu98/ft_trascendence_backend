# Generated by Django 5.0.6 on 2024-06-28 19:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_streak', models.IntegerField(default=0)),
                ('invididual_win_rate', models.IntegerField(default=0)),
                ('tournament_win_rate', models.IntegerField(default=0)),
                ('time_played', models.TimeField(default=0)),
                ('punctuation', models.IntegerField(default=0)),
                ('total_match', models.IntegerField(default=0)),
                ('total_turney', models.IntegerField(default=0)),
                ('total_goals', models.IntegerField(default=0)),
                ('total_goals_against', models.IntegerField(default=0)),
                ('total_goals_stopped', models.IntegerField(default=0)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
