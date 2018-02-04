# Generated by Django 2.0 on 2018-01-31 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('leagueID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('abbrev', models.CharField(blank=True, max_length=4, null=True)),
                ('bio', models.CharField(blank=True, max_length=125, null=True)),
                ('leagueStart', models.DateTimeField(blank=True, null=True)),
                ('leagueEnd', models.DateTimeField(blank=True, null=True)),
                ('playoffStart', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueStart', models.DateTimeField(blank=True, null=True)),
                ('leagueEnd', models.DateTimeField(blank=True, null=True)),
                ('champion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
                ('finalsMVP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finalsMVP', to=settings.AUTH_USER_MODEL)),
                ('leagueID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League')),
                ('leagueMVP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leagueMVP', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('leagueID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League')),
            ],
        ),
        migrations.CreateModel(
            name='LeagueOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League')),
                ('ownerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueOwnerPermissions',
            fields=[
                ('permissionID', models.AutoField(primary_key=True, serialize=False)),
                ('permission', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueTeams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leagueID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League')),
                ('teamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team')),
            ],
        ),
        migrations.AddField(
            model_name='leagueowner',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.LeagueOwnerPermissions'),
        ),
    ]
