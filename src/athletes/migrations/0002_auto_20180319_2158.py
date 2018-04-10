# Generated by Django 2.0 on 2018-03-20 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='user_instance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_athlete', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='soccerstats',
            name='athlete_instance',
            field=models.ManyToManyField(related_name='athlete_soccer_stats', to='athletes.Athlete'),
        ),
    ]